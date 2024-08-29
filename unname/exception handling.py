# exception handling

try:
    print("hello")
except NameError:
    print("variable x is not defined")
except:
    print("an  exception occurred")
else:
    print("nothing went wrong")
finally:
    print("the 'try except' is finished")


try:
    f = open("demofile.txt")
    try:
        f.write("test")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")



# the raise keyword is used to raise an exception.
# you can define what kind of error to raise, and the text to print to the user.


x = 11
if x < 0:
    print("x<0")
    raise Exception("numbers below zero")


# raise a TypeError if x is not an integer:

x = "hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")


