# bypassAV
条件触发式远控 VT 6/70 免杀国内杀软及defender、卡巴斯基等主流杀软
## 原理
https://pureqh.top/?p=5412
## use
将shellcode填至go_shellcode_encode.py生成混淆后的base64 payload
然后将生成的payload填至main.go build("b64shellcode")
将main.go中的url替换为你vbs的某个网页或文本（局域网网页同样可以，但是需要程序可以正常使用时此网页需要可以访问）
编译：go build -ldflags="-w -s -H=windowsgui"
