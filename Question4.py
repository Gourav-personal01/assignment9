#Lookup Error are the Errors which is generated due to fetching the non-exist file from the dictionary file.

#Example - Index Error 

try:
    a = [1,2]
    print(a[3])
except LookupError:
    print("lookup error has been Ocuured")

#Example - Key Error

try:
    employees = {1: "John", 2: "Darren", 3: "Paul"}
    print(employees[4])
except LookupError:
    print("Lookup Error has been Ocured")