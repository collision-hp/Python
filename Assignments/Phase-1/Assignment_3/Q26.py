def rep(str):
    for i in str:
        if (i=="a" or i=="e" or i=="i" or i=="0" or i=="u"):
            str=str.replace(i,"*")   
    return str

str="utit"
print(rep(str))
            