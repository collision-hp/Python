def shift(str):
    for i in str:
        asci=ord(i)
        c=chr(asci+1)
        print(c,end='')
        
str="python"
shift(str)
