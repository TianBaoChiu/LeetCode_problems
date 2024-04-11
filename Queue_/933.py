# Problem Description
# 933. Number of Recent Calls

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

# Constraints:

# 1 <= t <= 109
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.

#########################################################################################
from typing import List
from collections import deque


class Solution:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue

        start_time = t - 3000
        queue.append(t)

        while queue and queue[0] < start_time:
            queue.popleft()

        return len(queue)


if __name__ == "__main__":
    solution = Solution()

    inputs = ["RecentCounter", "ping", "ping", "ping", "ping"]
    params = [[], [1], [100], [3001], [3002]]
    expected_output = [None, 1, 2, 3, 3]

    for i in range(len(inputs)):
        input_func = inputs[i]
        param = params[i]

        if input_func == "RecentCounter":
            solution = Solution()
            output = None
        else:
            output = getattr(solution, input_func)(*param)

        expected = expected_output[i]
        if output == expected:
            print(
                f"Input: {input_func}({', '.join(map(str, param))}), Output: {output}"
            )
        else:
            print(
                f"Input: {input_func}({', '.join(map(str, param))}), Expected: {expected}, Got: {output}"
            )
