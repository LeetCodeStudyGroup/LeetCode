class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        folder = path.split("/")
        i = 0
        while i < len(folder):
            if folder[i] == "." or folder[i] == "":
                folder.pop(i)
                i -= 1
            elif folder[i] == "..":
                folder.pop(i)
                i -= 1
                if i >= 0:
                    folder.pop(i)
                    i -= 1
            i += 1
        if len(folder) == 0:
            return '/'
        result = ""
        for f in folder:
            result += "/" + f
        return result
