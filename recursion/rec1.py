#вызвал числа от 1 до 992
# def rec(x):
#     print(x)
#     rec(x+1)
# rec(1)    

def rec(x):
  if x < 4:
     print(x)
     rec(x+1)
     print(x)
rec(1)
#Ответ:    если rec(2) то Ответ:
# 1                          2  
# 2                          3
# 3                          3  
# 3                          2 
# 2
# 1