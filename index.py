from other import *
import language as l
print("Choose your language:[1]简体中文,[2]English")
lan=int(input("Select [1/2]:"))
level=input(l.words(lan,"index",0))
if level=="help" or level=="Help"or level=="HELP":
    print(l.words(lan,"index",1))
    f=open("help.txt")
    print(f.read())
    end(level,lan)
elif level=="license" or level=="License" or level=="LICENSE":
    f=open("LICENSE.txt")
    print(f.read())
    f.close()
    end(level,lan)
elif level=="exit":
    end(level,lan)
else:
    a,h,m=50,50,50
    while a>30 or h>24 or m>a*h*0.5 or a<4 or h<4 or m<2:
        a=int(input(l.words(lan,"index",2)))
        h=int(input(l.words(lan,"index",3)))
        m=int(input(l.words(lan,"index",4)))
        if a>30 or h>24 or m>a*h*0.5 or a<4 or h<4 or m<2:
            print(l.words(lan,"index",5))
    level=main(a,h,m,lan)#主体
    end(level,lan)
