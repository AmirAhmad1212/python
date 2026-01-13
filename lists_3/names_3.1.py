# 3.1-3.4 printing eachpersons name from a name and greeting them one at a time

names = ['zeeshan','azlan','ibrar','ali','qaiser']

print(f"good morning    {names[0].title()}\n")
print(f"good morning    {names[1].capitalize()}\n")
print(f"good morning    {names[2].upper()}\n")
print(f"good morning    {names[3].title()}\n")
print(f"good morning    {names[4].lower()}\n")

massage = f"Hello {names[0]} im happily inviting you to dinner"
massage = massage.capitalize()
print(massage)

# 3.5 altering person who isnt able to make it to dinner

altered_person = names[0]
new_person = names[-1]
print(altered_person)
print(f"\t wasnt able to join dinner so now {new_person} will join us")

#removing item from list
names.remove(names[-2])

# adding new values to list
names.append('aqsa')
names.insert(2, 'musa')
names.insert(1, 'yassassa')

print(names)