def print_goroda(goroda):
    for gorod in goroda:
        print (gorod,end=" | ")
goroda=["Tallinn", "Tartu", "Parnu", "Valga","Lunia","Elva"]
#print_goroda(goroda)
goroda.append("Tapa")
#print_goroda(goroda)
goroda.append("Narva")
#print_goroda(goroda)
goroda.insert(0,"Voru")
print_goroda(goroda)
goroda.insert(4,"Hapsalu")
#print_goroda(goroda)
#goroda.sort()
#print_goroda(goroda)
#goroda.reverse()
#print_goroda(goroda)
#print (len(goroda))
#goroda.append("Narva")
#print_goroda(goroda)
##############################
users={"Tom","Bob","Aice","Tom"}
print(users)
users.add("Tom")
print(users)
users.add("Petja")
print(users)

users2 = users.copy()
users2.add("Vasja")
users2.add("Katja")
users2.difference(users)
x = users2.difference(users)
print(x)
#33333333333333333333333333333333333333333333333
def clear():
    for i in range(20):
        print(" ")
clear()
"""
dictionary = {"Au": "Золото", "Fe": "Железо", "H": "Водород", "O": "Кислород","Li":"Litii","Be":"Berilum","B":"Boron", "C":"Carbon"}
print(dictionary)
list_dict = dict(dictionary)
print(list_dict)
dictionary[C]="Carbon"
print(dictionary)
for element in dictionary:
    if element =="Litium":
        print("Founded!")
    else:
        print("Not Founded!")"""
clear()
######################################
user = ("Tom", 2010, "Net")
user2 = ("Viktor", 1860, "Net")
user3 = ("Tomas-Hendrik", 2100, "Net")
name, age, isMarried = user
name, age, isMarried = user2
name, age, isMarried = user3
#print(name)             # Tom
#print(age)              # 22
#print(isMarried)        # False
#print(name)
#print(age)
#print(isMarried)
#print(name, age, isMarried)
#print(user2)
for i in range(len(user)):
    print(user[i],end=" ")
list_users=list()
list_users.append(user)
list_users.append(user2)
list_users.append(user3)
print("Name,Age,IsNotMarryed")
for users in list_users:
    for i in range (len(user)):
        print(user[i], end=" ")
print()