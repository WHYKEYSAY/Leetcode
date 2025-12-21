import string

class Codec:
    def __init__(self):
        self.url_to_id = {}
        self.id_to_url = {}
        self.counter = 1
        # Base62 characters: 0-9, a-z, A-Z
        self.chars = string.digits + string.ascii_letters
        self.base = len(self.chars)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        Args:
            longUrl (str): The original URL.
            
        Returns:
            str: The shortened URL (e.g., "http://tinyurl.com/5aB").
        """
        if longUrl in self.url_to_id:
            id_val = self.url_to_id[longUrl]
        else:
            id_val = self.counter
            self.url_to_id[longUrl] = id_val
            self.id_to_url[id_val] = longUrl
            self.counter += 1
            
        # Convert ID to Base62 string
        short_key = self._id_to_base62(id_val)
        return "http://tinyurl.com/" + short_key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        Args:
            shortUrl (str): The shortened URL.
            
        Returns:
            str: The original URL.
        """
        short_key = shortUrl.replace("http://tinyurl.com/", "")
        id_val = self._base62_to_id(short_key)
        return self.id_to_url.get(id_val, "")
        
    def _id_to_base62(self, id_val):
        if id_val == 0:
            return self.chars[0]
        
        result = []
        while id_val > 0:
            val = id_val % self.base
            result.append(self.chars[val])
            id_val //= self.base
            
        return "".join(reversed(result))
    
    def _base62_to_id(self, base62_str):
        id_val = 0
        for char in base62_str:
            val = self.chars.find(char)
            id_val = id_val * self.base + val
        return id_val

if __name__ == "__main__":
    # Example usage
    codec = Codec()
    url = "https://www.google.com/search?q=design+tinyurl"
    print(f"Original: {url}")
    
    short_url = codec.encode(url)
    print(f"Shortened: {short_url}")
    
    decoded_url = codec.decode(short_url)
    print(f"Decoded:  {decoded_url}")
    
    assert url == decoded_url
