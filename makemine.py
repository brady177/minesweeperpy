import random as rd
def makemine(a,h,m,wa,wh):#安排布局
    i,table=0,[]
    while i<a*h:
        table=table+[""]
        i=i+1
    i=0
    if wa==0:
        table[wh*a+wa+1]="A"
        if wh==0:
            table[(wh+1)*a+wa],table[(wh+1)*a+wa+1]="A","A"
        elif wh==h-1:
            table[(wh-1)*a+wa],table[(wh-1)*a+wa+1]="A","A"
        else:
            table[(wh+1)*a+wa],table[(wh+1)*a+wa+1]="A","A"
            table[(wh-1)*a+wa],table[(wh-1)*a+wa+1]="A","A"
    if wa==a-1:
        table[wh*a+wa-1]="A"
        if wh==0:
            table[(wh+1)*a+wa],table[(wh+1)*a+wa-1]="A","A"
        elif wh==h-1:
            table[(wh-1)*a+wa],table[(wh-1)*a+wa-1]="A","A"
        else:
            table[(wh+1)*a+wa],table[(wh+1)*a+wa-1]="A","A"
            table[(wh-1)*a+wa],table[(wh-1)*a+wa-1]="A","A"
    else:
        table[wh*a+wa-1],table[wh*a+wa+1]="A","A"
        if wh==0:
            table[(wh+1)*a+wa],table[(wh+1)*a+wa+1]="A","A"
            table[(wh+1)*a+wa],table[(wh+1)*a+wa-1]="A","A"
        elif wh==h-1:
            table[(wh-1)*a+wa],table[(wh-1)*a+wa+1]="A","A"
            table[(wh-1)*a+wa],table[(wh-1)*a+wa-1]="A","A"
        else:
            table[(wh+1)*a+wa],table[(wh+1)*a+wa+1]="A","A"
            table[(wh-1)*a+wa],table[(wh-1)*a+wa+1]="A","A"
            table[(wh+1)*a+wa],table[(wh+1)*a+wa-1]="A","A"
            table[(wh-1)*a+wa],table[(wh-1)*a+wa-1]="A","A"
    y=9
    while m>0:
        if table[i]=="A":
            y=y-1
        else:
            x=rd.random()
            if x<m/(a*h-i-y):
                table[i]="!"
                m=m-1
        i=i+1
    return table
