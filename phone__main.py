from functions import *

def initPy():
    a = int(input())
    if a == 1:
        user = input("Введите имя, фамилию, отчество и номер телефона: ")
        newContact(user)
    elif a == 2:
        printAll()
    elif a== 3:
        nick = input("Введите фамилию нужного человека: ")
        searchPerson(nick)
    elif a== 4:
        nick = input("Введите фамилию для удаления: ")
        deletePerson(nick)
    elif a== 5:
        oldContact = input("Введите фамилию для изменения: ")
        newContact = input("Введите новые имя, фамилию, отчество и номер телефона:")
        changePerson(oldContact, newContact)