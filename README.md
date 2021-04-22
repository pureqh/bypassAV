# bypassAV
条件触发式远控 VT 6/70 免杀国内杀软及defender、卡巴斯基等主流杀软
## 原理
https://pureqh.top/?p=5412
## use
1. 将shellcode填至go_shellcode_encode.py生成混淆后的base64 payload<br>
2. 然后将生成的payload填至main.go build("b64shellcode")<br>
3. 将main.go中的url替换为你vbs的某个网页或文本（局域网网页同样可以，但是需要程序可以正常使用时此网页需要可以访问）<br>
4. 编译：go build -trimpath -ldflags="-w -s -H=windowsgui"<br>

## 更新日志 2021/4/22

鉴于可能被标记特征，更新了随机生成go脚本的生成器，另外更改了编译命令，可以在exe中去除部分编译机器的信息<br>
