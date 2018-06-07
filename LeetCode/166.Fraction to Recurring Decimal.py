class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        is_neg = (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0)
        integer = str(abs(int(float(numerator) / denominator)))
        if is_neg:
            integer = '-' + integer
        fractional = []
        numerator %= denominator
        if is_neg and abs(denominator) != 1:
            numerator = denominator - numerator
        if numerator == 0:
            return integer
        record = {}
        i = 0
        while numerator not in record:
            record[numerator] = i
            numerator *= 10
            fractional.append(str(numerator / denominator))
            numerator %= denominator
            if numerator == 0:
                return integer + '.' + ''.join(fractional)
            i += 1
        i = record[numerator]
        return integer + '.' + ''.join(fractional[:i]) + '(' + ''.join(fractional[i:]) + ')'
