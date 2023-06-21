# Python Exception Hierarchy. - 

# Example - 

def python_exception_hierarchy(digit):
    try:
        a = int(digit)
        print(a)
    except Exception as e:
        print(e)
    finally:
        print("Exception has been finished")

python_exception_hierarchy('gkire')