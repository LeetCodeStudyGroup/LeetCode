class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = []
        star = []
        i =  0
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == '*':
                match.append(p[i])
                star.append(True)
                i += 1
            else:
                match.append(p[i])
                star.append(False)
            i += 1

        i = len(match) - 1
        while i > 0:
            if star[i] and star[i - 1] and match[i] == match[i - 1]:
                match.pop(i)
                star.pop(i)
            elif not star[i] and star[i - 1] and match[i] == match[i - 1]:
                star[i] = True
                star[i - 1] = False
            i -= 1

        if s == '':
            return self.check_match(s, match, star, 0, 0)
        return self.find_possible_match(s, match, star, 0, 0)

    def check_match(self, s, match, star, i, j):
        is_new = False
        while i < len(s) and j < len(match):
            if is_new and star[j]:
                return self.find_possible_match(s, match, star, i, j)
            elif not self.is_same(s[i], match[j]) and star[j]:
                j += 1
                is_new = True
                continue
            elif self.is_same(s[i], match[j]):
                if star[j]:
                    return self.check_match(s, match, star, i + 1, j) or \
                        self.check_match( s, match, star, i + 1, j + 1)
                else:
                    j += 1
                    is_new = True
            else:
                return False
            i += 1
        if i < len(s):
            return False
        while j < len(match):
            if not star[j]:
                return False
            j += 1
        return True

    def find_possible_match(self, s, match, star, i, j):
        possible = self.get_star_pos(s, match, star, i, j)
        if possible == None or len(possible) == 0:
            return False
        for p_j in possible:
            if self.check_match(s, match, star, i, p_j):
                return True
        return False
        
    def get_star_pos(self, s, match, star, i, j):
        cs = s[i] if i < len(s) else ''
        if j >= len(match):
            return None
        possible = []
        inx = j
        while inx < len(match):
            if self.is_same(cs, match[inx]):
                possible.append(inx)
            if not star[inx]:
                    break
            inx += 1
        return possible

    def is_same(self, s, p):
        return True if p == '.' or s == p else False
