def vorep(str):
    vow_map={"a":"e","e":"i","i":"o","o":"u","u":"a"}
    for i in str:
        if (i in vow_map):
            j=vow_map[i]
            str=str.replace(i,j)
    print(str)
    
vorep("sequence")