# Задача
# Является ли строка ПАЛИНДРОМОМ 
# шалаш = шалаш 
# asddsa 
# '' and 'a'

def palindrom(s): #s = это строка, принимает одну строку в данном случае
    if len(s) <= 1: # если длина строки меньше или равна единице
        return True # Значит это палиндром
    if s[0] != s[-1]: #если первый символ не равен последнему 
        return False
    return palindrom(s[1: -1]) #проверяем оставшуюся строку

print(palindrom('шалаш')) #Ответ: True
print(palindrom('шала')) #Ответ: False
print(palindrom('')) #Ответ: True
