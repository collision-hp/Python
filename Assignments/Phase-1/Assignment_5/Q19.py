def unque_pair(words):
    s=set()
    for i in words:
        k=1
        flag=0
        for k in words:
            for j in i:
                for l in k:
                    if j==k:
                        flag=1
                        break
                if flag==0:
                    ts=list[j,k]
    print(ts)
    
words = ["apple", "dogs", "cats", "bird", "fish", "zebra", "lion"]
unque_pair(words)