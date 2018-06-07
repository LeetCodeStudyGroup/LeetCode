class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT= 2147483647
        if divisor == 0:
            return MAX_INT

        is_negative = False
        if dividend < 0:
            dividend = 0 - dividend
            is_negative = not is_negative
        if divisor < 0:
            divisor = 0 - divisor
            is_negative = not is_negative

        if divisor == 1 and not is_negative and dividend > MAX_INT:
            return MAX_INT
        
        divs = [divisor]
        cnts = [1]
        i = 0
        while divs[i] + divs[i] <= dividend:
            divs.append(divs[i] + divs[i])
            cnts.append(cnts[i] + cnts[i])
            i += 1

        count = 0
        i = len(cnts) - 1
        while dividend > 0 and i >= 0:
            if dividend - divs[i] >= 0:
                dividend -= divs[i]
                count += cnts[i]
            i -= 1

        if is_negative:
            return 0 - count
        return MAX_INT if count > MAX_INT else count
