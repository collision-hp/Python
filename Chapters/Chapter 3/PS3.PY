#Q1
a=input("Enter your Name-")
print("Good Afternoon" ,a)

#Q2
letter='''
Dear <|Name|>,
You are Selected!
<|Date|>'''
print(letter.replace("<|Name|>" , 'King').replace("<|Date|>" , "24 Nov 2024"))

#Q3
a='How  are you Butcher, I just wanted you to know you have done a magnificant job by putting the videos online'
print(a.find("  ")) #detect double space
#Q4
print(a.replace("  " , " "))
print(a) #remains the same as the original string because strings are immuttable

#Q5
letter = "How are you Butcher,\n\tI just wanted you to know you have done a \"magnificant job\" by uploading video online. \n\t\t\tThanks for the help"
print(letter)
