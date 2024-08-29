# create a new file

# 1.to create a new file in python, use the open() method, 
# with one of the following parameters:
# "x" (create) will create a file , returns an error if the file exist
# "a" (append) will create a file if the specified file dose not exist
# "w" (write) will create a file if the specified file does not exist


# 2.check if file exist ,then delete it
# to delete a file , you must import the os module , and run its os.remove() function:
# to avoid getting an error , you might want to check if the file exists before you try to delete it:




# 删除指定文件
import os
def remove_file(filename):
    """
    删除给定文件名的文件。

    如果文件存在，则将其删除，并打印删除成功的消息。
    如果文件不存在，则打印文件不存在的消息。

    参数:
    filename (str): 要删除的文件的名称。
    """
    # 检查文件是否存在
    if os.path.exists(filename):
        # 如果文件存在，则删除它
        os.remove(filename)
        print("delete file succeeded")
    else:
        # 如果文件不存在，则打印相应消息
        print("the file does not exist")
        raise FileNotFoundError