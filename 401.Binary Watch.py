class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0: return ["0:00"]
        selects = [[i] for i in range(10)]
        for i in range(num - 1):
            for _ in range(len(selects)):
                ary = selects.pop(0)
                if ary[-1] < 9:
                    for j in range(ary[-1] + 1, 10):
                        new = ary[:]
                        new.append(j)
                        selects.append(new)
        return self.convert(selects)
                    
    def convert(self, selects):
        result = []
        for select in selects:
            hour = minute = 0
            for num in select:
                if num < 4:
                    hour += 1 << num
                else:
                    minute += 1 << (num - 4)
            if hour <= 11 and minute <= 59:
                m = str(minute)
                if minute <= 9:
                    m = '0' + m
                result.append(str(hour) + ':' + m)
        return result

def readBinaryWatch2(self, num):
    return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]
