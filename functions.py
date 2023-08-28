def newContact(person):
    data = open('Dict.txt', 'a', encoding="utf-8")
    data.writelines(person +"\n")
    print("успешно добавлено")
    data.close()

def printAll():
    data = open ('Dict.txt', 'r', encoding="utf-8")
    for line in data:
        print(line)
    data.close()

def searchPerson(surname):
    data = open ('Dict.txt', 'r', encoding="utf-8")
    found = True
    for line in data:
        if surname in line.split():
            print(line)
        else:
            found = False
    if found == False:
        print("-такого нету")
    data.close()

def deletePerson(val):
    data = open('Dict.txt', 'r', encoding="utf-8")
    Lines = data.readlines()
    data = open('Dict.txt', 'w', encoding="utf-8")
    for line in Lines:
        if val not in line.split():
            data.write(line)
    data.close()
    print("контакт удален")

def changePerson(val, val2):
    data = open ('Dict.txt', 'r+', encoding="utf-8")
    Lines = data.readlines()
    existPerson = False
    for x in range(len(Lines)):
        if val in Lines[x].split():
            Lines[x] = val2 +"\n"
            existPerson = True
    data = open('Dict.txt', 'w', encoding="utf-8")
    for line in Lines:
        data.write(line)    
    if existPerson == False:
        print("не удалось, контакт не найден")
    else:
        print("успешно изменено")
    data.close()