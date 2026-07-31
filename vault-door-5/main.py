
str_encoded = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"+ "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"+"JTM0JTVmJTM0JTMyJTYzJTM2JTM0JTMwJTM5JTYy"
import base64
dec = base64.b64decode(str_encoded)
url_str = dec.decode("utf-8")

from urllib.parse import unquote

ans = unquote(url_str)
print("picoCTF{" + ans + "}")

