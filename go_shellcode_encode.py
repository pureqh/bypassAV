import base64
import random
import numpy


buf1 =  b"shellcode"
b64shellcode = base64.b64encode(buf1).decode()
b64shellcode = b64shellcode.replace("A","#").replace("H","!").replace("1","@").replace("T",")")
print(b64shellcode)
