
import os

systemLog = "Amula->:"

def sysLog(filename:str, log:str):
    print("Amula->:"+filename+log)
    

def mk (filename, type):
    '''
    Make a file or directory 
    '''
    if os.path.exists(filename):
        if os.path.isdir(filename) and type=="f":
            f = open(filename, "a")
            f.close()
           
            sysLog(filename,"is created")
        else:
            print(systemLog + f"{filename} is exist, can't create it")
    else:
        # create a file
        if type == "f":
            f = open(filename, "x")
            f.close()
            print(filename + " is created")
        # create a directory
        elif type == "d":
            os.mkdir(filename)
            print(filename + " is created")
        else:
            print("the second argument only is \"f\" or \"d\" ")
            

def rm (filename):
    '''
    Delete a file or directory
    '''
    if os.path.exists(filename):
        if os.path.isfile(filename):
            os.remove(filename)
            print(filename + " is deleted")
        else:
            os.rmdir(filename)
            print(filename + " is deleted")
    else:
        print(f"{filename} isn't exist, can't delete it")
    


