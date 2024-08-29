# File write 

# 1.Write to an existing file
# to write to an existing file, you must add a parameter to the open() function:
# "a"(append) will append to the end of the file 
# "w"(write) will overwirte any existing content 

#open the file and append content to the file:
f1 = open("demofile2.txt", "a")
f1.write("now the file has more content!\n")
f1.close()

#open and read the file after the appending:
f2 = open("demofile2.txt", "r")
print(f2.read())
f2.close()

# 3.open the file and overwrite the content:
f3 = open("demofile3.txt", "w")
f3.write("I have deleted the content")
f3.close()

# open and read the file after the overwriting
f4 = open("demofile3.txt", "r")
print(f4.read())
f4.close()

