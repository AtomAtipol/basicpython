#สร้างฟังก์ชันแล้วไม่มีการ return value
def hello(name):
    print(f"hello{name}")

#สร้างฟังก์ชันแบบมีการ Return Value
def area (width, height):
    total = width * height
    return total


#เรียกใช้งานฟังก์ชัน hello()
hello("Atipol")


#เรียกใช้งานฟังก์ชัน area()
print(area(5, 8))
print("พื้นที่ทั้งหมด",area(15, 8))


#ฟังก์ชันแบบมีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print (f"Name: {name}")
    print (f"Salary: {salary}")
    print (f"Language: {lang}")

#เรียกใช้งานฟังก์ชัน show_info() ต้องติดอยู่ฝั่งซ้าย
show_info()
show_info('Atom', 1000000, 'Python')