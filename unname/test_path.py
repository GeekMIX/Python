from pathlib import Path

current_dir = Path.cwd()
print(str(current_dir))
print(current_dir.parent)

for i in current_dir.iterdir():
    pass

new_dir = current_dir / 'new_dir'
# This function is used to create a new directory. 
# new_dir is the path of the directory to be created.
# The parameter exist_ok=True indicates that if the directory already exists, 
# no exception will be raised, but rather it will return quietly.
new_dir.mkdir(exist_ok=True)     


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function

# 调用outer_function并获取返回的inner_function
add_five = outer_function(5)

# 使用返回的函数
result = add_five(10)
print(result)  # 输出: 15