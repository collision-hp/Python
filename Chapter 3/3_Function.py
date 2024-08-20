str="manifestation"
print(len(str))
print(str.endswith("ion")) #like comparison returns boolean values
print(str.startswith("Manif")) #case sensitive
print(str.capitalize()) #Capitalizes the first letter only
print(str.upper())

updated_string = str.replace('a' , 'z')
print(updated_string)