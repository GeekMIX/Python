# filename = file open.py

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# 1.open a file 
# To open the file , use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:
f1 = open("demofile.txt","r")
print("f1.printing content of file:\n" + f1.read())

'''
2.Return the 5 first characters of the file:
By default the read() method returns the whole text, 
but you can also specify how many characters you want to return:
'''

f2 = open("demofile.txt", "r")
print("\nf2.print 5 character:\n" + f2.read(5))

'''
3.Read Lines 
You can return one line by using the readline() function:
'''



f3 = open("demofile.txt", "r")
print("\nf3.print one line of the file:\n" + f3.readline())

# 4.read two lines of the file:
# By calling readline() two times, you can read the two first lines:

f4 = open("demofile.txt", "r")
print("f4.print one line of the file:\n" + f4.readline())
print("f4.print one line of the file:\n" + f4.readline())

# 5.Loop through the file line by line 
# By looping through the lines of the file, you can read the whole file, line By line:

f5 = open("demofile.txt", "r")
for x in f5:
    print(x)

# 6.Close the file when you are finish with it:
# It is a good habit to close the file when you are done with it.

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
print("all file are closed")

# Note: You should always close your file, In some cases,
# due to buffering,changes made to a file may not show until you close the file.