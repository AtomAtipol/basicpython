a = 5
b = 9.55
c = "atomatipol"

print(a)
print(b)
print(c)
print(a,b,c)

#การสร้างตัวแปรหลายในบรรทัดเดียวกัน
x = y = z = 10
j,k = 5, 15
print(x,y,z)
print(j,k)

#Boolean
status = True
msg = False

print(status, msg)

#ตัวแปรแสดงผลร่วมกับข้อความ
#วิธีที่ 1 concat string > ต่อท้าย
print("ราคาขายต่อชิ้น",b,"บาท มีจำนวน",a,"ชิ้น")

#วิธีที่ 2 string interpolation > คำนวณ
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น"% (b,a))

#วิธีที่ 3 format string > นิยม
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")