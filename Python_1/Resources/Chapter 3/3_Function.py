str='MasAla Chai'
print(str.lower())
print(str.upper())
print(str.capitalize())
print(len(str))
str1="     Lemon Chai        "
print(str1.strip())
print(str1.replace("Lemon","Ginger"))
print(str1)#string is immutable

str2="Lemon, Ginger, Masala, Mint"
print(str2.split())
print(str2.split(", "))

str3="Masala Chai"
print(str3.find("Chai"))

str4="Masala Chai Chai Chai Chai"
print(str4.count("Chai"))

type="Masala Chai"
quantity=2
order="I ordered {} cups of {}"
print(order.format(quantity,type))
order1="I ordered {} cups of {} chai".format("4","Lemon")
print(order1)

#list to string
variety=['Lemon',"Masala","Ginger"]
print(", ".join(variety))

chai="Masala Chai"
for i in chai:
    print(i,end="")
    



