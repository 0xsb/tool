#-*- coding:utf-8 -*-
import hashlib
import base64
import string
import os
import sys
from module import argparse
from module import random
from module import printc
presentAdd = os.getcwd()
sys.path.append(presentAdd+"\\module\\urllib")
sys.path.append(presentAdd+"\\module\\zxing")
from module import zxing
import urllib
from urllib import parse



#将一些常用的公用的函数封装起来为一个工具类
class tool:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self):
        self.name=1

   #以下是一些常用的工具函数

   # 将字母转化为对应的ASCII
    def lettToASCII(self,s):
        result = ''
        for i in s:
            result = result + str(ord(i)) + ' '
        return result

    # 将ASCII转化为对应的字母以及字符
    def asciiToLett(self,s):
        list = s.split(' ')
        result = ''
        for i in list:
            i = int(i)
            result = result + chr(i)
        return result

    # 将十六进制转化为十进制
    def hexToDec(self,s):
        original = s
        s = s.split(" ")
        if s[len(s)-1] =="":
            del s[len(s)-1]
        result = ''
        for i in s:
            result = result + " " + str(int(i, 16))
        return result

    # 将十进制转化为十六进制
    def decToHex(self,s):
        original = s
        s=s.split(" ")
        if s[len(s)-1] =="":
            del s[len(s)-1]
        result = ''
        for i in s:
            i = int(i)
            result = result + " " + hex(i)
        return result

#定义全局变量以供使用
tool=tool()

visibleCharacter={
    ' ': '%08','    ': '%09',
    '!': '%21', "\"": '%22', '#': '%23', '$': '%24', '%': '%25', '&': '%26','\'':'%27' ,'(': '%28',')': '%29',
    '*':'%2a','+':'%2b',',':'%2c','-':'%2d','.':'%2e','/':'%2f',
    '0': '%30', '1': '%31', '2': '%32', '3': '%33', '4': '%34', '5': '%35', '6': '%36', '7': '%37', '8': '%38', '9': '%39',
    ':':'%3a',';':'%3b','<':'%3c','=':'%3d','>':'%3e','?':'%3f','@':'%40',
    'A':'%41','B':'%42','C':'%43','D':'%44','E':'%45','F':'%46','G':'%47','H':'%48','I':'%49','J':'%4a','K':'%4b','L':'%4c','M':'%4d','N':'%4e','O':'%4f','P':'%50','Q':'%51','R':'%52','S':'%53','T':'%54','U':'%55','V':'%56','W':'%57','X':'%58','Y':'%59','Z':'%5a',
    '[':'%5b','\\':'%5c',']':'%5d','^':'%5e','_':'%5f','\`':'%60',
    'a':'%61','b':'%62','c':'%63','d':'%64','e':'%65','f':'%66','g':'%67','h':'%68','i':'%69','j':'%6a','k':'%6b','l':'%6c','m':'%6d','n':'%6e','o':'%6f','p':'%70','q':'%71','r':'%72','s':'%73','t':'%74','u':'%75','v':'%76','w':'%77','x':'%78','y':'%79','z':'%7a',
    '{':'%7b','|':'%7c','}':'%7d','~':'%7e',
    ',':'%82','\"':'%84',
}

"""
        
        名字：CTF之常用工具汇总
        
        作者：白猫
        
        时间：2018-3-22
        
        QQ ：1058763824
        

"""

def menu():
    usage = """-m MD5 encryption
       -s      SH1 encryption
       --h     Show help information
       -b64    Base64 encode
       -b32    Base32 encode
       -b16    Base16 encode
       -db64   Base64 decode
       -db32   Base32 decode
       -db16   Base16 decode
       -urlen  URL encode
       -urlde  URL decode
       -unien  Unicode Encode                 Example:  -unien    "A"        Result: \\u0061
       -unide  Unicode Decode                 Example:  -unide    "\\u0061"  Result: A
       -hten   HTML Encode                    Example:  -hten    "A"         Result: &#97;
       -htde   HTML Decode                    Example:  -htde    "&#97"      Result: A
       -bin    Binary To Decimal
       -octal  Octal Decimal to Decimal
       -hex    Hexadecimal to Decimal
       -dbin   Decimal To Binary 
       -doctal Decimal to Octal 
       -dhex   Decimal to Hexadecimal
       -ord    Letter To ASCII  attention      Example:  -ord asdfasfa      -ord="dfafs afasfa  asfasf"
       -chr    ASCII  To Letters               Example:  -chr 105           -chr = "102 258 654"
       -roten  Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode
       -rotde  Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode
       -offset Rot Encode or Decode Offset  
       -gqr    Generate QRcode images          Example:  -gqr = "I love you"
       -pqr    Parse QRcode  images            Example:  -pqr = "C:\QR.png"   
      """

    #在使用ord 和chr命令的时候要注意如果输入的字符和数字不包含空格则直接实用例子前面的命令如果包含空格则使用后面的命令

    parser = argparse.ArgumentParser()

    parser.add_argument('-m',dest='md',help='MD5 encryption')
    parser.add_argument('-s', dest='sh', help='SH1 encryption')
    parser.add_argument('--h',action="store_true",help='Show help information')
    parser.add_argument('-b64', dest='b64', help='Base64 encode')
    parser.add_argument('-b32', dest='b32', help='Base32 encode')
    parser.add_argument('-b16', dest='b16', help='Base16 encode')
    parser.add_argument('-db64', dest='db64', help='Base64 decode')
    parser.add_argument('-db32', dest='db32', help='Base32 decode')
    parser.add_argument('-db16', dest='db16', help='Base16 decode')
    parser.add_argument('-urlen', dest='urlen', help='URL encode')
    parser.add_argument('-urlde', dest='urlde', help='URL decode')
    parser.add_argument('-unien', dest='unien', help='Unicode Encode')
    parser.add_argument('-unide', dest='unide', help='Unicode Decode ')
    parser.add_argument('-hten', dest='hten', help='HTML Encode')
    parser.add_argument('-htde', dest='htde', help='HTML Decode ')
    parser.add_argument('-bin', dest='bin', help='Binary To Decimal')
    parser.add_argument('-octal', dest='octal', help='Octal  to Decimal')
    parser.add_argument('-hex', dest='hex', help='Hexadecimal to Decimal')
    parser.add_argument('-dbin', dest='dbin', help='Decimal To Binary ')
    parser.add_argument('-doctal', dest='doctal', help='Decimal to Octal ')
    parser.add_argument('-dhex', dest='dhex', help='Decimal to Hexadecimal')
    parser.add_argument('-ord', dest='ord', help="Letter To ASCII               Example:  -ord aaaaaa  , -ord=\"aaa aaa\"")
    parser.add_argument('-chr', dest='chr', help="ASCII  To Letter              Example:  -chr 105     ,  -chr = \"101 101\" ")
    parser.add_argument('-roten',dest='roten', help='Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode')
    parser.add_argument('-rotde', dest='rotde', help='Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode')
    parser.add_argument('-gqr', dest='gqr', help='Generate QRcode images          Example:  -gqr = "I love you"')
    parser.add_argument('-pqr', dest='pqr', help='Parse QRcode  images            Example:  -pqr = "C:\QR.png"')
    parser.add_argument('-offset', dest='offset', type=int,help=' ')



    options = parser.parse_args()

    if options.md :
        s = options.md
        md5(s)
    elif options.sh:
        s = options.sh
        sh1(s)
    elif options.b64:
        s = options.b64.encode()
        stringToB64(s)
    elif options.b32:
        s = options.b32.encode()
        stringToB32(s)
    elif options.b16:
        s = options.b16.encode()
        stringToB16(s)
    elif options.db64:
        s = options.db64.encode()
        b64ToString(s)
    elif options.db32:
        s = options.db32.encode()
        b32ToString(s)
    elif options.db16:
        s = options.db16.encode()
        b16ToString(s)
    elif options.urlen:
        s = options.urlen
        urlEncode(s)
    elif options.urlde:
        s = options.urlde
        urlDecode(s)
    elif options.bin:
        s = options.bin
        binToDec(s)
    elif options.octal:
        s = options.octal
        octToDec(s)
    elif options.hex:
        s = options.hex
        hexToDec(s)
    elif options.dbin:
        s = options.dbin
        decToBin(s)
    elif options.doctal:
        s = options.doctal
        decToOct(s)
    elif options.dhex:
        s = options.dhex
        decToHex(s)
    elif options.doctal:
        s = options.doctal
        decToOct(s)
    elif options.dhex:
        s = options.dhex
        decToHex(s)
    elif options.ord:
        s = options.ord
        lettToASCII(s)
    elif options.chr:
        s = options.chr
        asciiToLett(s)
    elif options.roten and options.offset:
        s = options.roten
        offset = options.offset
        print("Origina      :"+s)
        print("Rot{offset} Encode:".format(offset=offset)+rotEncode(s,offset))
    elif options.rotde and options.offset:
        s = options.rotde
        offset = options.offset
        print("Rot_{offset} Encode:".format(offset=offset) + s)
        print("Rot_{offset} Decode:".format(offset=offset)+ str(rotDecode(s, offset)))
    elif options.gqr:
        print()
        s = options.gqr
        generateQR(s)
    elif options.pqr:
        print()
        s = options.pqr
        parseQR(s)
    elif options.unien:
        print()
        s = options.unien
        uniencode(s)
    elif options.unide:
        print()
        s = options.unide
        unidecode(s)
    elif options.hten:
        print()
        s = options.hten
        htmlencode(s)
    elif options.htde:
        print()
        s = options.htde
        htmldecode(s)
    else:
        helpInfo()


def helpInfo():

    printc.printf("""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       -m      MD5 encryption
       -s      SH1 encryption
       --h     Show help information
       -b64    Base64 encode
       -b32    Base32 encode
       -b16    Base16 encode
       -db64   Base64 decode
       -db32   Base32 decode
       -db16   Base16 decode
       -urlen  URL encode
       -urlde  URL decode
       -unien  Unicode Encode                 Example:  -unien    "A"        Result: \\u0061
       -unide  Unicode Decode                 Example:  -unide    "\\u0061"  Result: A
       -hten   HTML Encode                    Example:  -hten     "A"        Result: &#97;
       -htde   HTML Decode                    Example:  -htde     "&#97"     Result: A
       -bin    Binary To Decimal
       -octal  Octal Decimal to Decimal
       -hex    Hexadecimal to Decimal
       -dbin   Decimal To Binary 
       -doctal Decimal to Octal 
       -dhex   Decimal to Hexadecimal
       -ord    Letter To ASCII  attention      Example:  -ord asdfasfa      -ord="dfafs afasfa  asfasf"
       -chr    ASCII  To Letters               Example:  -chr 105           -chr = "102 258 654"
       -roten  Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode
       -rotde  Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode
       -offset Rot Encode or Decode Offset  
       -gqr    Generate QRcode images          Example:  -gqr = "I love you"
       -pqr    Parse QRcode  images            Example:  -pqr = "C:\QR.png"   
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""","skyblue")

# 进行MD5加密

def md5(s):
    original = s
    md  = hashlib.md5()
    s = s.encode(encoding = 'utf-8')
    md.update(s)
    info1='Original:'+original
    info2='Md5 Encryption:'+md.hexdigest()
    printc.printf(info1,'blue')
    printc.printf(info2,'green')

#进行sh1加密

def sh1(s):
    original = s
    sh = hashlib.sha1()
    s = s.encode(encoding='utf-8')
    info1='Original:' + original
    info2='SH1 Encryption:' + sh.hexdigest()
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

#将字符串转换为base64编码格式

def stringToB64(s):
    res = base64.b64encode(s)
    info1 = 'Original:' + str(s)[2:-1]
    info2 = 'Base64 encode:' + str(res)[2:-1]
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


#将base64编码格式转化为正常的字符类型

def b64ToString(s):
    decode = base64.b64decode(s)
    info1 = 'Base64:' + str(s)[2:-1]
    info2 = 'Base64 decode:' + str(decode)[2:-1]
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

#将字符串转为b32编码格式

def stringToB32(s):
    encode = base64.b32encode(s)
    info1 = 'Original:' + str(s)[2:-1]
    info2 = 'Base32 encode:' + str(encode)[2:-1]
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

    
#将base32编码格式转化为正常的字符类型

def b32ToString(s):
    decode = base64.b32decode(s)
    info1 = 'Base32:' + str(s)[2:-1]
    info2 = 'Base32 decode:' + str(decode)[2:-1]
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将字符串转为base16编码格式

def stringToB16(s):
    encode = base64.b16encode(s)
    info1 = 'Original:' + str(s)[2:-1]
    info2 = 'Base16 encode:' + str(encode)[2:-1]
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将base16编码格式转化为正常的字符类型

def b16ToString(s):
    decode = base64.b16decode(s)
    info1 = 'Base16:' + str(s)[2:-1]
    info2 = 'Base16 decode:' + str(decode)[2:-1]
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

def isVisibleCharacter(s):
    try:
        for i in string.printable:
            if (s==i):
                return True
                break
    except:
        return False


#进行url编码

def urlEncode(s):
    encodeString=''
    for i in s:
        if (isVisibleCharacter(i)):
            encodeString=encodeString+visibleCharacter[i]
        else:
            encodeString=encodeString+urllib.parse.quote(i)

    info1 = 'Original:' + s
    info2 = 'URL encode:' + encodeString
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')



#进行url编码

def urlDecode(s):
    decode = urllib.parse.unquote(s)
    info1 = 'URL encode:' + s
    info2 = 'URL decode:' + decode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


#将二进制转化为十进制

def binToDec(s):
    original = s
    s = s.split(" ")
    result = ''
    for i in s:
        result = result+" "+str(int(i,2))

    info1 = 'Binary :'+str(original)
    info2 = 'Decimal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将八进制转化为十进制

def octToDec(s):
    original = s
    s = s.split(" ")
    result = ''
    for i in s:
        result = result+" "+str(int(i, 8))

    info1 = 'Octal :' + str(original)
    info2 = 'Decimal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将十六进制转化为十进制

def hexToDec(s):
    original = s
    s = s.split(" ")
    result = ''
    for i in s:
        result = result+" "+str(int(i, 16))

    info1 = 'Hex :' + str(original)
    info2 = 'Decimal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将十进制转化为二进制

def decToBin(s):
    original=s
    s =s.split(" ")
    result=''
    for i in s:
        i = int(i)
        result =result+ " "+bin(i)

    info1 = 'Decimal:' + str(original)
    info2 = 'Binary:' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

# 测试

def test(s):
    print("Successful:"+str(s))



# 将十进制转化为八进制

def decToOct(s):
    original = s
    s = s.split(" ")
    result = ''
    for i in s:
        i = int(i)
        result = result+" "+oct(i)

    info1 = 'Decimal :' + str(original)
    info2 = 'Octal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将十进制转化为十六进制

def decToHex(s):
    original = s
    s = s.split(" ")
    result = ''
    for i in s:
        i = int(i)
        result = result+" "+hex(i)

    info1 = 'Decimal :' + str(original)
    info2 = 'Hex :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


#将字母转化为对应的ASCII

def lettToASCII(s):
   result = ''

   for i in s:
       result = result+str(ord(i)) + ' '

   info1 = 'Letters:'+s
   info2 = 'ASCII  :'+result
   printc.printf(info1, 'blue')
   printc.printf(info2, 'green')


#将ASCII转化为对应的字母以及字符


def asciiToLett(s):
   list=s.split(' ')
   result = ''
   for i in list:
       i = int(i)
       result =result + chr(i)

   info1 = 'ASCII    :'+s
   info2 = 'Letters  :'+result
   printc.printf(info1, 'blue')
   printc.printf(info2, 'green')


#Rot类型的加密：就是将字母在字母表中向前移动n位

def rotEncode(st,offset):
    def rot(ch):
        f = lambda x : chr((ord(ch)-x+offset)%26+x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(rot(c) for c in st)



#Rot类型的解密：rot加密的逆向过程

def rotDecode(st,offset):
    def rot(ch):
        f = lambda x : chr((ord(ch)-x-offset)%26+x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(rot(c) for c in st)

#生成二维码图片
def generateQR(data):
    QRImagePath =os.getcwd()+"/qrcode.png"
    imageInfo="照片存储在:"+QRImagePath
    messageInfo="信息:"+data
    printc.printf(messageInfo,"blue")
    printc.printf(imageInfo,"green")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    #data = input("请输入信息:")
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('qrcode.png')
    if sys.platform.find('darwin') >= 0:
        os.system('open %s' % QRImagePath)
    elif sys.platform.find('linux') >= 0:
        os.system('xdg-open %s' % QRImagePath)
    else:
        os.system('call %s' % QRImagePath)
    time.sleep(1)

#解析二维码图片
def parseQR(filename):
    #filename=input("请输入二维码照片路径:")
    img=Image.open(filename)
    ran=int(random.random()*100000)
    img.save('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))
    zx=zxing.BarCodeReader()
    data=''
    zxdata = zx.decode('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))
    info1="二维码路径:"+filename
    info2="二维码详情:"+str(zxdata)
    printc.printf(info1,"blue")
    printc.printf(info2,"green")

#这里要使用上面的函数,在不破坏前面的前提下重新修改一下函数


#将字符串进行unicode编码
def uniencode(s):
    original=s
    s=tool.lettToASCII(s)
    s=tool.decToHex(s)
    s=" "+s
    s=s.replace(" 0x","\\u00")
    info1="String       : "+original
    info2="UnicodeEncode: "+s

    printc.printf(info1, "blue")
    printc.printf(info2, "green")

#将unicode编码格式的字符串解码为正常的字符串
def unidecode(s):
    original = s
    temp=''
    s=s.replace("\\u00"," 0x")
    s=s.split(" ")
    del s[0]
    for i in range(len(s)):
        if i<len(s)-1:
            temp = temp + str(s[i]) + " "
        else:
            temp=temp+str(s[i])
    s=temp
    s=tool.hexToDec(s)
    s=s.split(" ")
    temp=''
    del s[0]
    for i in range(len(s)):
        if i < len(s) - 1:
            temp = temp + str(s[i]) + " "
        else:
            temp = temp + str(s[i])
    s=temp
    s=tool.asciiToLett(s)

    info1 = "String:      " + original
    info2 = "UnicodeDecode:  " + s
    printc.printf(info1, "blue")
    printc.printf(info2, "green")

def htmlencode(s):
    original=s
    temp=""
    s=tool.lettToASCII(s)
    s=s.split()
    for i in range(len(s)):
        temp = temp +"&#"+ str(s[i]) + ";"
    s=temp

    info1="Original String: "+original
    info2="HTML   Encoding: "+s
    printc.printf(info1, "blue")
    printc.printf(info2, "green")

def htmldecode(s):
    original=s
    temp=''
    s = s.replace(";", "")
    s = s.replace("&#", " ")
    s = s.split()
    for i in range(len(s)):
        if i < len(s) - 1:
            temp = temp + str(s[i]) + " "
        else:
            temp = temp + str(s[i])
    s=temp
    s=tool.asciiToLett(s)
    info1="HTML Encode:"+original
    info2="HTML Decode:"+s
    printc.printf(info1, "blue")
    printc.printf(info2, "green")








if __name__=='__main__':

    menu()




