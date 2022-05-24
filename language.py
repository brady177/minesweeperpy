def zh_cn(which,num):
    index=["Minesweeper 回车开始","帮助文档","长：","高：","地雷数:","配置无效,请重新输入！"]
    o_main=["点击第几列？","点击第几行？","位置无效。","该位置已被点击。"]
    o_end=["你赢了！","你输了，再接再厉！","游戏结束，回车退出。"]
    if which=="index":
        return index[num]
    elif which=="main":
        return o_main[num]
    elif which=="end":
        return o_end[num]
    else:
        return "故障！找不到相应文字。"
def en(which,num):
    index=["I am a middle school student from China，and my English isn't good.Please help me if you can!\nMinesweeper.Enter to start.","The Helping File","Width:","Height:","Number of mines:","The number was too big or small,try to answer again!"]
    o_main=["Where do you want to open?\n  The column:","  The line:","It isn't on the screen.","It was opened."]
    o_end=["You won!","You died.Try again!","Game over,Enter to exit."]
    if which=="index":
        return index[num]
    elif which=="main":
        return o_main[num]
    elif which=="end":
        return o_end[num]
    else:
        return "Error!Cannot find the word."
def words(lan,which,num):
    if lan==1:
        return zh_cn(which,num)
    elif lan==2:
        return en(which,num)
    else:
        return "Error!"
