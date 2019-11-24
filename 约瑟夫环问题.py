persons = [True] * 30
index,num,conter = 0,0,0
while conter < 15 :
    if persons[index]:
        num +=1
        if num == 9:
            persons[index] = False
            conter += 1
            num = 0
    index +=1
    index %= len(persons)

for person in persons:
    print("基" if person else "非",end='')
print()