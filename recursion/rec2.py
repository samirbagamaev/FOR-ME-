#Задача на нахождение факториала 
#типо 5! = 120 5! = 1*2*3*4*5 = 120

def fact(x):
    if x == 1:
        return x
    return fact(x-1) * x    #n! = (n-1)! * n

print(fact(5)) #Ответ : 120
print(fact(9)) #Ответ : 362880