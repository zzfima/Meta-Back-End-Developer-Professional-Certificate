try:
    v = 0
    c = 33
    l = c / v
except ZeroDivisionError:
    print("can not divide by zero")
except Exception as e:
    print("Get exception: ", e)
finally:
    print("finally")
