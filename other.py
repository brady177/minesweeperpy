from howmany import howmany
from makemine import *
import language as l
def show(a,h,table):#显示布局
    print()
    i=0
    while i<h:
        x,line=0,""
        while x<a:
            if table[a*i+x]=="" or table[a*i+x]=="!" or table[a*i+x]=="A":
                line=line+"[ ]"
            elif table[a*i+x]==0:
                line=line+"   "
            else:
                line=line+" "+str(table[a*i+x])+" "
            x=x+1
        print(line)
        i=i+1
def showend(a,h,table):#显示结束时布局
    print()
    i=0
    while i<h:
        x,line=0,""
        while x<a:
            if table[a*i+x]=="" or table[a*i+x]=="A":
                line=line+"[ ]"
            elif table[a*i+x]=="!":
                line=line+"[!]"
            elif table[a*i+x]==0:
                line=line+"   "
            else:
                line=line+" "+str(table[a*i+x])+" "
            x=x+1
        print(line)
        i=i+1
def main(a,h,m,lan):#主体
    i,table=0,[]
    while i<a*h:
        table=table+[""]
        i=i+1
    show(a,h,table)
    level="?"
    while level == "?":
        where_a=input(l.words(lan,"main",0))
        where_h=input(l.words(lan,"main",1))
        if where_a=="exit" or where_h=="exit":
            level="exit"
        else:
            where_a=int(where_a)-1
            where_h=int(where_h)-1
            if where_a<0 or where_a+1>a or where_h<0 or where_h+1>h:
                print(l.words(lan,"main",2))
            else:
                table=makemine(a,h,m,where_a,where_h)
                table[a*where_h+where_a]=howmany(a,h,table,where_a,where_h)
                level=""
    i=0
    while i<a*h-m and level=="":
        show(a,h,table)
        where_a=input(l.words(lan,"main",0))
        where_h=input(l.words(lan,"main",1))
        if where_a=="exit" or where_h=="exit":
            level="exit"
            break
        else:
            where_a=int(where_a)-1
            where_h=int(where_h)-1
            if where_a<0 or where_a+1>a or where_h<0 or where_h+1>h:
                print(l.words(lan,"main",2))
            elif table[a*where_h+where_a]=="!":
                level="died"
                break
            elif table[a*where_h+where_a]=="" or table[a*where_h+where_a]=="A":
                table[a*where_h+where_a]=howmany(a,h,table,where_a,where_h)
                i=i+1
            else:
                print(l.words(lan,"main",3))
    if level=="":
        level="won"
    showend(a,h,table)
    return level
def end(level,lan):
    if level=="won":
        print(l.words(lan,"end",0))
    elif level=="died":
        print(l.words(lan,"end",1))
    input(l.words(lan,"end",2))
