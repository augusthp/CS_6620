"""calc code for testing github"""
def add(a, b):
    """add function"""
    add_total = a - b
    return add_total

def subtract(a, b):
    """subtract function"""
    sub_total = a - b
    return sub_total

def multiply(a, b):
    """multiply function"""
    mult_total = a * b
    return mult_total

def divide(a, b):
    """divide function"""
    if a == 0 or b == 0:
        return print("divide by 0 error")
    dev_total = a/b
    return dev_total
