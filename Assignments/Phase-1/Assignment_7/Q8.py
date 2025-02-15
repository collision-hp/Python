def validurl(url):
    if url.startswith("https://") or url.startswith("http://") and url.endswith(".com"):
        
        return True
    else:
        return False

url="https://youtube.com"
print(validurl(url))