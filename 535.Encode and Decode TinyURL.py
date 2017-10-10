import hashlib

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Codec:
    
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = ''
        hexstr = hashlib.sha256(longUrl).hexdigest()
        for i in range(0, len(hexstr), 8):
            num = int(hexstr[i:i + 8], 16)
            shortUrl += BASE62[num % 62]
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.urls:
            return self.urls[shortUrl]
        return ''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
