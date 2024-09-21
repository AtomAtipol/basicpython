print ("------------------")
print ("#Summatioon Program")
print ("# Type 'exit' to end the program")
print ("------------------")

# #ตัวแปรไว้เก็บผลรวม
sumdata = 0
count = 1

while True:
    data = input (f"Enter Number{count}:")
    # ตรวจว่าผู้ใช้ป้อน 'exit'
    if data == "exit":
        break
    #การหาผลรวม
    sumdata += int(data)
    count = count + 1

print (f"Sumvalue is {sumdata}:")