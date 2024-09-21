number = [5, 8, 13, 24, 7, 12]
name = ['atom','alex','axe','ant']
mixed = [10, 10.75, True, 'atipol']

# การเข้าถึงสมาชิกใน list
print(number[1])
print(name[3])
print(mixed[2],mixed[3])
print(number)

# การนับจำนวนสมาชิกใน list
print("สมาชิกทั้งหมดของ number =", len(number))

#การสร้าง list แบบว่าง (emty list)
data = []

#การเพิ่มสมาชิกเข้าไปใน List ว่าง
data.append(10)
data.append(15)
data.append(20)
print(data)


#อัพเดทสมาชิกใน List
data[1] = 12

print(data)

#ฟังก์ชันวนลูปอ่านสมาชิกทั้งหมด
for n in number:
    print (n)


#Loop เพื่อหาผลรวม
sum = 0
for num in number:
    sum += num
print(sum)