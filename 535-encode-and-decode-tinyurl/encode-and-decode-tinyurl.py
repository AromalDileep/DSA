import re
class Codec:

    def __init__(self):
        self.mp = {} #longUrl, shortUrl

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        st = "".join(chr(random.randint(48,122)) for _ in range(6))
        short_url = 'https://tin.e/'  + st
        self.mp[short_url] = longUrl
        return short_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mp[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))