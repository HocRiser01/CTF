# CTF Writeup合集

## Misc

[**BugKu  这是一张单纯的图片**](https://ctf.bugku.com/challenges/detail/id/2.html)

strings file.jpg

&#为Unicode，解码即可

*key{you are right}*

[**BugKu 隐写**](https://ctf.bugku.com/challenges/detail/id/3.html)

png图片头IHDR后三四位为宽，七八位为高，一般会有一个出错。

可以[爆破](https://wiki.x10sec.org/misc/picture/png-zh/)验证CRC，这里是将高改为和宽一样。

*BUGKU{a1e5aSA}*

[**BugKu 眼见非实**](https://ctf.bugku.com/challenges/detail/id/5.html)

docx改为zip，得到document.xml

*flag{F1@g}*

[**BugKu 啊哒**](https://ctf.bugku.com/challenges/detail/id/6.html)

binwalk得到加密35695.zip，查看图片详细信息（mac下为工具-检查器-型号）可以看到base16编码，解码得到sdnisc_2018，从而打开压缩包得到flag.txt

*flag{3XiF_iNf0rM@ti0n}*

[**BugKu 又一张图片，还单纯吗**](https://ctf.bugku.com/challenges/detail/id/7.html)

foremost -i file.jpg

*falg{NSCTF_e6532a34928a3d1dadd0b049d5a3cc57}*

```fcrackzip -b -c aA1 -l 6-6 -p -u a.zip```

若密码在密码本文件里，则`fcrackzip -D -p passwd a.zip`

[**BugKu 多种方法解决**](https://ctf.bugku.com/challenges/detail/id/11.html)

文本编辑器打开，直接复制到浏览器就能打开。

或者base64转图片，扫描二维码。

*KEY{dca57f966e4e4e31fd5b15417da63269}*

[**BugKu 白哥的鸽子**](https://ctf.bugku.com/challenges/detail/id/14.html)

Hex打开发现fg2ivyo}l{2s3_o@aw__rcl@，栅栏数3解密即可。

*flag{w22_is_v3ry_cool}*

[**BugKu linux**](https://ctf.bugku.com/challenges/detail/id/15.html)

strings flag

*key{feb81d3834e2423c9903f4755464060b}*

[**BugKu 富强民主**](https://ctf.bugku.com/challenges/detail/id/61.html)

社会主义核心价值观编码 http://mix.bid/a/decoder/

*flag{90025f7fb1959936}*

[**BugKu 隐写3**](https://ctf.bugku.com/challenges/detail/id/16.html)

高度改为01DF即可

*flag{He1l0_d4_ba1}*

[**BugKu zip伪加密**](https://ctf.bugku.com/challenges/detail/id/57.html)

`50 4B 03 04 ** ** 00 00`（头文件标记）以及`50 4B 01 02 ** ** ** ** 00 00`（目录中文件文件头标记，中间分别表示压缩使用的软件和使用的版本）

*flag{Adm1N-B2G-kU-SZIP}*

[**BugKu Linux2**](https://ctf.bugku.com/challenges/detail/id/19.html)

strings搜索KEY

*KEY{24f3627a86fc740a7f36ee2c7a1c124a}*

[**BUU 金三胖**](https://buuoj.cn/challenges#%E9%87%91%E4%B8%89%E8%83%96)

gif逐帧查找flag

*flag{he11ohongke}*

[**BUU 二维码**](https://buuoj.cn/challenges#%E4%BA%8C%E7%BB%B4%E7%A0%81)

`binwalk -e` `fcrackzip -b -c1 -l 4 -u`得到密码7639

*flag{vjpw_wnoei}*

[**BUU N种方法解决**](https://buuoj.cn/challenges#N%E7%A7%8D%E6%96%B9%E6%B3%95%E8%A7%A3%E5%86%B3)

base64转图片

*KEY{dca57f966e4e4e31fd5b15417da63269}*

[**BUU 大白**](https://buuoj.cn/challenges#%E5%A4%A7%E7%99%BD)

png高度错误

```python
import os
import binascii
import struct


misc = open("dabai.png","rb").read()

for i in range(1024):
    data = misc[12:20] +struct.pack('>i',i)+ misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0x6d7c7135:
        print i
```

正确高度479

*flag{He1l0_d4_ba1}*

[**BUU 文件中的秘密**](https://buuoj.cn/challenges)

Hex Friend

*flag{870c5a72806115cb5439345d8b014396}*

[**BUU zip伪加密**](https://buuoj.cn/challenges#zip%E4%BC%AA%E5%8A%A0%E5%AF%86)

两处09 00改为00 00即可

*flag{Adm1N-B2G-kU-SZIP}*

[**BUUCTF ningen**](https://buuoj.cn/challenges#ningen)

4位密码fcrackzip得到密码8368

*flag{b025fc9ca797a67d2103bfbc407a6d5f}*

## Crypto

[**BugKu /.-**](https://ctf.bugku.com/challenges/detail/id/46.html)

[摩斯电码](https://www.atool99.com/morse.php)

`%u7b`即`&#123;`Unicode前128就是ASCII，对应`{`。`%u7d`同理。

*flag{d3fcbf17f9399504}*

[**BugKu 聪明的小羊**](https://ctf.bugku.com/challenges/detail/id/47.html)

栅栏数为2

*flag{6fde4163df05d900}*

[**BugKu ok**](https://ctf.bugku.com/challenges/detail/id/48.html)

[ook编码](https://www.splitbrain.org/services/ook)

*flag{0a394df55312c51a}*

[**BugKu [+-<>]**](https://ctf.bugku.com/challenges/detail/id/49.html)

Brainfuck编码，可以用上一题的网址解码

*flag{0d86208ac54fbf12}*

[**BugKu 把猪困在猪圈里**](https://ctf.bugku.com/challenges/detail/id/159.html)

[base64转图片](http://tool.chinaz.com/tools/imgtobase/)或文本内容最前面加上`data:image/jpg;base64,`

得到图片，猪圈密码

![image-20210129095049333](/Users/cloudsky/Library/Application Support/typora-user-images/image-20210129095049333.png)

*flag{thisispigpassword}*

[**BugKu easy_crypto**](https://ctf.bugku.com/challenges/detail/id/50.html)

[01摩斯电码解密](http://ctf.ssleye.com/morse.html)

**flag{m0rse_code_1s_interest1n9!}**

[**BugKu 简单加密**](https://ctf.bugku.com/challenges/detail/id/51.html)

```python
s = "e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA"
ss = list(s)
for i in range(len(s)):ss[i]=chr(ord(s[i])-4)
s = ''.join(ss)
```

base64转ASCII

*key{68743000650173230e4a58ee153c68e8}*

[**BugKu 散乱的密文**](https://ctf.bugku.com/challenges/detail/id/52.html)

215634重排

*flag{52048c453d794df1}*

[**BugKu .!?**](https://ctf.bugku.com/challenges/detail/id/54.html)

变形Ook

*flag{bugku_jiami}*

[**BugKu 一段base64**](https://ctf.bugku.com/challenges/detail/id/53.html)

Base64->Escape->Hex->Escape->ASCII(DEC)->Unicode->Unicode->url

*flag{ctf_tfc201717qwe}*

[**BugKu 奇怪的密码**](https://ctf.bugku.com/challenges/detail/id/55.html)

变形凯撒，第一位-1，第二位-2，...

```python
s = input()
ss = list(s)
for i in range(len(ss)):ss[i]=chr(ord(ss[i])-i-1)
s = ''.join(ss)
print(s)
```

*flag{lei_ci_jiami}*

[**BugKu 告诉你个秘密**](https://ctf.bugku.com/challenges/detail/id/58.html)

Hex转ASCII再base64解码得到`r5yG lp9I BjM tFhBT6uh y7iJ QsZ bhM`

键盘密码：键盘上每个字母的上下左右。

*flag{TONGYUAN}*

[**BugKu 这不是md5**](https://ctf.bugku.com/challenges/detail/id/59.html)

十六进制转ASCII

*flag{ae73587ba56baef5}*

[**BugKu 贝斯家族**]()

[base91](http://www.atoolbox.net/Category.php?Id=27)

*flag{554a5058c9021c76}*

[**BugKu 进制转换**](https://ctf.bugku.com/challenges/detail/id/63.html)

```python
s=["d87","x65","x6c","x63","o157","d109","o145","b100000","d116","b1101111","o40","x6b","b1100101","b1101100","o141","d105","x62","d101","b1101001","d46","o40","d71","x69","d118","x65","x20","b1111001","o157","b1110101","d32","o141","d32","d102","o154","x61","x67","b100000","o141","d115","b100000","b1100001","d32","x67","o151","x66","d116","b101110","b100000","d32","d102","d108","d97","o147","d123","x31","b1100101","b110100","d98","d102","b111000","d49","b1100001","d54","b110011","x39","o64","o144","o145","d53","x61","b1100010","b1100011","o60","d48","o65","b1100001","x63","b110110","d101","o63","b111001","d97","d51","o70","d55","b1100010","d125","x20","b101110","x20","b1001000","d97","d118","o145","x20","d97","o40","d103","d111","d111","x64","d32","o164","b1101001","x6d","o145","x7e"]
s1=''; t=''
for s1 in s:
	if s1[0:1]=='d': t=t+chr(int(s1[1:]))
	if s1[0:1]=='x': t=t+chr(int(s1[1:],16))
	if s1[0:1]=='o': t=t+chr(int(s1[1:],8))
	if s1[0:1]=='b': t=t+chr(int(s1[1:],2))
print(t)
```

*flag{1e4bf81a6394de5abc005ac6e39a387b}*

[**BugKu affine**](https://ctf.bugku.com/challenges/detail/id/64.html)

```python
s = "szzyfimhyzd"
l = []
for i in s: l.append(ord(i)-97)
flag = ''
for i in l:
    for j in range(0,26):
        c = (17 * j - 8) % 26
        if(c == i): flag += chr(j+97)
print(flag)
```

*flag{affineshift}*

[**BugKu rsa**](https://ctf.bugku.com/challenges/detail/id/66.html)

Wiener攻击即可

*flag{Wien3r_4tt@ck_1s_3AsY}*

[**BugKu 来自宇宙的信号**](https://ctf.bugku.com/challenges/detail/id/67.html)

[标准银河字母](https://baike.baidu.com/item/%E6%A0%87%E5%87%86%E9%93%B6%E6%B2%B3%E5%AD%97%E6%AF%8D/2691355?fr=aladdin)

*flag{nopqrst}*

[**BUU MD5**](https://buuoj.cn/challenges#MD5)

https://www.cmd5.com/ 

*flag{admin1}*

[**BUU Url编码**](https://buuoj.cn/challenges#Url%E7%BC%96%E7%A0%81)

*flag{and 1=1}*

[**BUU 一眼就解密**](https://buuoj.cn/challenges#%E4%B8%80%E7%9C%BC%E5%B0%B1%E8%A7%A3%E5%AF%86)

base64

*flag{THE_FLAG_OF_THIS_STRING}*

[**BUU 看我回旋踢**](https://buuoj.cn/challenges#%E7%9C%8B%E6%88%91%E5%9B%9E%E6%97%8B%E8%B8%A2)

[ROT13](https://www.qqxiuzi.cn/bianma/rot5-13-18-47.php)

加密和解密都是位移13位，flag加密为synt

*flag{5cd1004d-86a5-46d8-b720-beb5ba0417e1}*

[**BUU 摩丝**](https://buuoj.cn/challenges#%E6%91%A9%E4%B8%9D)

摩斯电码

*flag{ILOVEYOU}*

[**BUU password**](https://buuoj.cn/challenges#password)

*flag{zs19900315}*

[**BUU 变异凯撒**](https://buuoj.cn/challenges#%E5%8F%98%E5%BC%82%E5%87%AF%E6%92%92)

```python
m='afZ_r9VYfScOeO_UL^RWUc'
for i in range(0,len(m)):
    print(chr(ord(m[i])+i+5))
```

*flag{Caesar_variation}*

[**BUU Quoted-printable**](https://buuoj.cn/challenges#Quoted-printable)

就是Hex编码

[**BUU 篱笆墙的影子**](https://buuoj.cn/challenges#%E7%AF%B1%E7%AC%86%E5%A2%99%E7%9A%84%E5%BD%B1%E5%AD%90)

栅栏编码

*flag{wethinkwehavetheflag}*

[**BUU rsarsa**](https://buuoj.cn/challenges#rsarsa)

```python
import gmpy2
gmpy2.mpz(x)#初始化一个大整数x
gmpy2.mpfr(x)#初始化一个高精度浮点数x
C = gmpy2.powmod(M,e,n)#幂取模，结果是 C = (M^e) mod n
d = gmpy2.invert(e,phi)#求逆元，de = 1 mod (p-1)*(q-1)
gmpy2.is_prime(n)#判断n是不是素数
gmpy2.gcd(a,b)#欧几里得算法
gmpy2.gcdext(a,b)#扩展欧几里得算法
gmpy2.iroot(x,n)#x开n次根
```

```python
from Crypto.Util import number
s='this is a demo'
#字节转换为long型整数
ls=number.bytes_to_long(s)
bits=8*len(s)
#生成长度为bits的素数
gp=number.getPrime(bits)
#生成强的素数（gsp-1，gsp+1均至少具有一个大的素因子）
gsp=number.getStrongPrime(1024)
#计算gri在模grn下的逆
iin=number.inverse(gri,grn)
#判断iin是否为素数
ip=number.isPrime(iin)
#long型整数转换为字节
tb=number.long_to_bytes(ls)
```

*flag{5577446633554466577768879988}*

[**BUU 大帝的密码武器**](https://buuoj.cn/challenges#%E5%A4%A7%E5%B8%9D%E7%9A%84%E5%AF%86%E7%A0%81%E6%AD%A6%E5%99%A8)

试出ROT13时对应原文为SECURITY，同样位移ComeChina即可。

*flag{PbzrPuvan}*

[**BUU [BJDCTF 2nd]cat_flag**](https://buuoj.cn/challenges#[BJDCTF%202nd]cat_flag)

二进制转文本

*BJD{M!a0~}*

[**BUU [BJDCTF 2nd]燕言燕语-y1ng**](https://buuoj.cn/challenges#[BJDCTF%202nd]%E7%87%95%E8%A8%80%E7%87%95%E8%AF%AD-y1ng)

十六进制转字符得到yanzi，[维吉尼亚解密](https://www.qqxiuzi.cn/bianma/weijiniyamima.php)，密钥为yanzi

*BJD{yanzi_jiushige_shabi}*

[**BUU [GKCTF2020]小学生的密码学**](https://buuoj.cn/challenges#[GKCTF2020]%E5%B0%8F%E5%AD%A6%E7%94%9F%E7%9A%84%E5%AF%86%E7%A0%81%E5%AD%A6)

仿射加密，解密得到sorcery，base64编码

*flag{c29yY2VyeQ==}*

[**BUU 信息化时代的步伐**](https://buuoj.cn/challenges#%E4%BF%A1%E6%81%AF%E5%8C%96%E6%97%B6%E4%BB%A3%E7%9A%84%E6%AD%A5%E4%BC%90)

[中文电码](http://code.mcdvisa.com/)：4位数字表示一个汉字

*flag{计算机要从娃娃抓起}*

[**BUU RSA1**](https://buuoj.cn/challenges#RSA1)

https://lazzzaro.github.io/2020/05/06/crypto-RSA/

RSA问题集合

[**BUU 凯撒？替换？呵呵!**](https://buuoj.cn/challenges#%E5%87%AF%E6%92%92%EF%BC%9F%E6%9B%BF%E6%8D%A2%EF%BC%9F%E5%91%B5%E5%91%B5!)

不知替换规则的凯撒

https://quipqiup.com/

各种模式都试一下

[**BUU old-fashion**](https://buuoj.cn/challenges#old-fashion)

同上

*flag{n1_2hen-d3_hu1-mi-ma_a}*

[**BUU RSA3**](https://buuoj.cn/challenges#RSA3)

RSA共模攻击

*flag{49d91077a1abcb14f1a9d546c80be9ef}*

[**BUU RSA2**](https://buuoj.cn/challenges#RSA2)

RSA dp泄漏攻击

*flag{wow_leaking_dp_breaks_rsa?_98924743502}*

[**BUU 异性相吸**](https://buuoj.cn/challenges#%E5%BC%82%E6%80%A7%E7%9B%B8%E5%90%B8s)

异或即可，文件输入

```python
with open('miwen.txt' )as a:
    a=a.read()
with open('key.txt' )as b:
    b=b.read()
d=''
for i in range(0,len(b)):
    d+=chr(ord(a[i])^ord(b[i]))
print(d)
```

*flag{ea1bc0988992276b7f95b54a7435e89e}*

[**BUU 还原大师**](https://buuoj.cn/challenges#%E8%BF%98%E5%8E%9F%E5%A4%A7%E5%B8%88)

MD5爆破

```python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import hashlib

#print hashlib.md5(s).hexdigest().upper()
k = 'TASC?O3RJMV?WDJKX?ZM'
for i in range(26):
	temp1 = k.replace('?',str(chr(65+i)),1)
	for j in range(26):
		temp2 = temp1.replace('?',chr(65+j),1)
		for n in range(26):
			temp3 = temp2.replace('?',chr(65+n),1)
			s = hashlib.md5(temp3.encode('utf8')).hexdigest().upper()
			if s[:4] == 'E903':
				print (s)
```

*flag{E9032994DABAC08080091151380478A2}*

[**BUU Unencode**](https://buuoj.cn/challenges#Unencode)

[UUencode](http://ctf.ssleye.com/uu.html)

*flag{dsdasdsa99877LLLKK}*

[**BUU [AFCTF2018]Morse**](https://buuoj.cn/challenges#[AFCTF2018]Morse)

摩斯电码，HEX解码

```python
flag='61666374667b317327745f73305f333435797d'
print(flag.decode('hex'))
```

[**BUU Dangerous RSA**](https://buuoj.cn/challenges#Dangerous%20RSA)

先strings得到题面

低加密指数攻击

*flag{25df8caf006ee5db94d48144c33b2c3b}*

[**BUU [GUET-CTF2019]BabyRSA**](https://buuoj.cn/challenges#[GUET-CTF2019]BabyRSA)

```python
libnum.n2s(int(m))#数字转字符串(ASCII)
```

直接算出基本参数即可

*flag{cc7490e-78ab-11e9-b422-8ba97e5da1fd}*

[**BUU RSA5**](https://buuoj.cn/challenges#RSA5)

e固定，多组n和c。可能能找出某对n的gcd，即为p。

```python
n=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20]
c=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20]
for i in range(len(n)):
	for j in range(len(n)):
		if(i!=j):
			if(gcd(n[i],n[j])!=1):
				print(i+1,j+1)
#(5, 18)
p=mpz(gcd(n[i],n[j]))
q=n5/p
phi=(p-1)*(q-1)
e=65537
d=invert(e,phi)
m=pow(c5,d,n5)
print(hex(m)[2:].decode('hex'))
```

[**BUU 传感器**](https://buuoj.cn/challenges#%E4%BC%A0%E6%84%9F%E5%99%A8)

曼彻斯特编码

```python
cipher='5555555595555A65556AA696AA6666666955'
def iee(cipher):
    tmp=''
    for i in range(len(cipher)):
        a=bin(eval('0x'+cipher[i]))[2:].zfill(4)
        tmp=tmp+a[1]+a[3]
    plain=[hex(int(tmp[i:i+8][::-1],2))[2:] for i in range(0,len(tmp),8)]
    print(''.join(plain).upper())

iee(cipher)
```

*flag{FFFFFED31F645055F9}*

[**BUU 密码学的心声**](https://buuoj.cn/challenges#%E5%AF%86%E7%A0%81%E5%AD%A6%E7%9A%84%E5%BF%83%E5%A3%B0)

八进制，每三位一组转ASCII.

```python
s = '111 114 157 166 145 123 145 143 165 162 151 164 171 126 145 162 171 115 165 143 150'
tmp = [s.split(' ')[i] for i in range(len(s.split(' ')))]
cipher = ''
for i in tmp:
    cipher += chr(int(i,8))
flag = "flag{"+cipher+"}"
print(flag)
```

*flag{ILoveSecurityVeryMuch}*

[**BUU [BJDCTF2020]这是base??**](https://buuoj.cn/challenges#[BJDCTF2020]%E8%BF%99%E6%98%AFbase??)

题面给了一个新编码表，替换编码。

base64库也可以做32位编码和解码。

```python
import base64
dict={0: 'J', 1: 'K', 2: 'L', 3: 'M', 4: 'N', 5: 'O', 6: 'x', 7: 'y', 8: 'U', 9: 'V', 10: 'z', 11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: '7', 20: '8', 21: '9', 22: 'P', 23: 'Q', 24: 'I', 25: 'a', 26: 'b', 27: 'c', 28: 'd', 29: 'e', 30: 'f', 31: 'g', 32: 'h',33: 'i', 34: 'j', 35: 'k', 36: 'l', 37: 'm', 38: 'W', 39: 'X', 40: 'Y', 41: 'Z', 42: '0', 43: '1', 44: '2', 45: '3', 46: '4', 47: '5', 48: '6', 49: 'R', 50: 'S', 51: 'T', 52: 'n', 53: 'o', 54: 'p', 55: 'q', 56: 'r', 57: 's', 58: 't', 59: 'u', 60: 'v', 61: 'w', 62: '+', 63: '/', 64: '='}
base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
cipher='FlZNfnF6Qol6e9w17WwQQoGYBQCgIkGTa9w3IQKw'
res=''
for i in range(len(cipher)):
    for j in range(64):
        if(dict[j]==cipher[i]):
            res+=base64_list[j]
flag=base64.b64decode(res)
print(flag)
```

*flag{D0_Y0u_kNoW_Th1s_b4se_map}*

[**[MRCTF2020]vigenere**](https://buuoj.cn/challenges#[MRCTF2020]vigenere)

未知密钥的vigenere密码爆破：https://www.guballa.de/vigenere-solver

*



## Web

[**BugKu web1**](https://ctf.bugku.com/challenges/detail/id/68.html)

查看源代码即可

[**BugKu web2**](https://ctf.bugku.com/challenges/detail/id/69.html)

审查元素，修改maxlength="2"即可。

[**BugKu web3**](https://ctf.bugku.com/challenges/detail/id/70.html)

index.php?what=flag

[**BugKu web5**](https://ctf.bugku.com/challenges/detail/id/72.html)

php中`==`为弱相等（值相等即可），`===`为强相等（类型与值均一样），故"1a"与"1"比较时会将"1a"截取前面尽量多位的纯数字，故"1a"=="1"。

[**BugKu web6**](https://ctf.bugku.com/challenges/detail/id/73.html)

源码中&#形式编码为Unicode，解码即可。

[**BugKu web7**](https://ctf.bugku.com/challenges/detail/id/74.html)

Burp suite中repeater功能逐步查看，获得flag

