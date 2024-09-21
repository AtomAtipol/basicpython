# fullname = input("Enter your name:")
# age = int(input("Enter your age:"))
# print(fullname)
# print(age+5)

user = input("Enter username:")
pwd = input("Enter password:")

set_user = "admin"
set_pass = "1234"

if user == set_user and pwd == set_pass:
    print("Yah! login success")
else:
    print("Opp! login fail!!")