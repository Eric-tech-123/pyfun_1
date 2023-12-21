name=str(input("enter your names: "))
age=int(input("enter your age: "))
print(f"hello,{name} you are {age} years old")
txt="hello again,{} you are {} years old"
print(txt.format(name,age))