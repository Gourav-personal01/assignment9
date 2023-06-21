# Arithmetic Error are the error which is generated due to mathematic calculations.

# 1. Zero dividion error
#Example - 

try:
    a = 5/0
    print(a)
except ArithmeticError:
    print("Arithmetic error has been occured")

#2. Float Point Error
#Example - 

try:
    a = 5/0.0
    print(a)
except ArithmeticError:
    print("Arithmetic Error has been Ocured.")