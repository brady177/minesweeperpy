def ul(a,t,wa,wh):#左上
    if t[(wh-1)*a+wa-1]=="!":
        return 1
    else:
        return 0
def um(a,t,wa,wh):#中上
    if t[(wh-1)*a+wa]=="!":
        return 1
    else:
        return 0
def ur(a,t,wa,wh):#右上
    if t[(wh-1)*a+wa+1]=="!":
        return 1
    else:
        return 0
def ml(a,t,wa,wh):#左中
    if t[wh*a+wa-1]=="!":
        return 1
    else:
        return 0
def mr(a,t,wa,wh):#右中
    if t[wh*a+wa+1]=="!":
        return 1
    else:
        return 0
def dl(a,t,wa,wh):#左下
    if t[(wh+1)*a+wa-1]=="!":
        return 1
    else:
        return 0
def dm(a,t,wa,wh):#中下
    if t[(wh+1)*a+wa]=="!":
        return 1
    else:
        return 0
def dr(a,t,wa,wh):#右下
    if t[(wh+1)*a+wa+1]=="!":
        return 1
    else:
        return 0
#以下是软件引用部分
def howmany(a,h,t,wa,wh):
    if wa==0:
        if wh==0:
            return mr(a,t,wa,wh)+dm(a,t,wa,wh)+dr(a,t,wa,wh)
        elif wh==h-1:
            return um(a,t,wa,wh)+ur(a,t,wa,wh)+mr(a,t,wa,wh)
        else:
            return um(a,t,wa,wh)+ur(a,t,wa,wh)+mr(a,t,wa,wh)+dm(a,t,wa,wh)+dr(a,t,wa,wh)
    elif wa==a-1:
        if wh==0:
            return ml(a,t,wa,wh)+dm(a,t,wa,wh)+dl(a,t,wa,wh)
        elif wh==h-1:
            return ul(a,t,wa,wh)+ur(a,t,wa,wh)+ml(a,t,wa,wh)
        else:
            return ul(a,t,wa,wh)+um(a,t,wa,wh)+ml(a,t,wa,wh)+dl(a,t,wa,wh)+dm(a,t,wa,wh)
    else:
        if wh==0:
            return ml(a,t,wa,wh)+mr(a,t,wa,wh)+dl(a,t,wa,wh)+dm(a,t,wa,wh)+dr(a,t,wa,wh)
        elif wh==h-1:
            return ul(a,t,wa,wh)+um(a,t,wa,wh)+ur(a,t,wa,wh)+ml(a,t,wa,wh)+mr(a,t,wa,wh)
        else:
            return ul(a,t,wa,wh)+um(a,t,wa,wh)+ur(a,t,wa,wh)+ml(a,t,wa,wh)+mr(a,t,wa,wh)+dl(a,t,wa,wh)+dm(a,t,wa,wh)+dr(a,t,wa,wh)
