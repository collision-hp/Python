n=[45,56,877,5454,4,5]
 
def is_odd(x):
    return x%2!=0
v=list(filter(is_odd,n))
print(v)

v1=list(filter(lambda x:x%2!=0,n))
print(v1)

v2=list(ele for ele in n if is_odd(ele))
print(v2)

n1=list(map(lambda x:x**2 ,n))
print(n1)

n2=list(item**2 for item in n)
print(n2)

vn=list(map(lambda x:x**2 , filter(is_odd,n)))
print(vn)

vn1=list(ele**2 for ele in n if is_odd(ele))
print(vn1)