# While Creating a Custom Exception we use the Exception class because we need to add the all the method of Exception Class so that we can overite as per our requirements.

#Example -

class test(Exception):
    "Raise Exception has been Ocured"
    pass

try:
    a = 5
    if a>4:
        raise test
except test:
    print("Custom Exception has been raised")