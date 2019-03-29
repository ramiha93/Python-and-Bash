#!/usr/bin/env python3

def repeat_bad(s):
    name= 9001
    iterr =""
    for f in range(0, len(s)):
        if((name-1)>(9000)):iterr+="-"
        name=name+1
        iterr +=s[f]*((name%9000)-1)
    iterr = iterr.title()
    print(iterr)
    return iterr


def repeat_good(s):
    pos = 0     #position
    new_s = ""  #string to return

    for i in range(0, len(s)):
        #if not first character, apply "-"
        if(pos>0):
            new_s+="-"
        pos+=1
        new_s += s[i]*pos
    new_s = new_s.title()

    print(new_s)
    return new_s


repeat_good("testing")
repeat_bad("testing")
