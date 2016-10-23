class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cur_gas = start = i = 0
        is_finish = False
        while i < len(gas):
            cur_gas += gas[i] - cost[i]
            i += 1
            if cur_gas < 0:
                if is_finish:
                    return -1
                cur_gas, start = 0, i
            if i == len(gas) and not is_finish:
                is_finish, i = True, 0
        return start
