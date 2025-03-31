print("Russia-Ukranian War\n")
print("Mission-1(Clearing the field)\n")

cities=["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
cleaned_cities=[]
for i in cities:
    if i not in cleaned_cities:
        cleaned_cities.append(i)

cleaned_cities.sort()
print(cleaned_cities)

print("X---------X----------X----------X\n")

print("Mission-2(High Alert Identification)\n")

cleaned_cities = {"Dnipro", "Kharkiv", "Kyiv", "Lviv", "Odessa"}
previous_intel = {"Kyiv", "Mariupol", "Lviv", "Donetsk"}

common=set()
commoncit=cleaned_cities.intersection(previous_intel)
common.update(commoncit)
print(common)

all=set()
allcit=cleaned_cities.union(previous_intel)
all.update(allcit)
print(all)

unique=set()
uniquecit=all-common
unique.update(uniquecit)
print(unique)

print("X---------X----------X----------X\n")

print("Mission-3(Detailed City Intel)\n")

high_alert_cities = ("Kyiv", "Lviv") 
city_data = [("Kyiv", 2800000, 250), ("Kharkiv", 1431000, 180), ("Lviv",721301, 90), ("Odessa", 1029049, 120)]
high_alert_cities_info={}
population=0
aid=0
for i in high_alert_cities:
    for j in city_data:
        if i==j[0]:
            high_alert_cities_info.update({i:j})
            population+=j[1]
            aid+=j[2]
print(high_alert_cities_info)
print("Total population is ",population)
print("Total number of aids required ",aid)

print("X---------X----------X----------X\n")

print("Mission-4 (Tracking Supply Distribution\n")

supplies = [("Kyiv", "Food", 500), ("Moscow", "Medicines", 200), ("Lviv", "Water", 300), ("Saint Peters-burg", "Blankets", 100), ("Kharkiv", "Food", 150)]
subdict={}
for i,j,h in supplies:
    subdict[i]={j:h}  
print(subdict)



