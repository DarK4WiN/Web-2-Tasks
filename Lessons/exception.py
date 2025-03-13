a = 5

try:
    print('a is: ' + str(a))
except TypeError as e:
    print(e, 'error')
except ZeroDivisionError as e:
    print('We cannot divide by zero')
else:
    print('No error')
finally:
    print('Close the program')