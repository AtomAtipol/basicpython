#Import ทั้งหมดทุกฟังก์ชันใน Module (numbers)
import numberx

#import มาบางฟัก์ชัน
# from numbery import factorial, fibonacci
#import ทุกฟังก์ชัน ระบุ module เมื่อไหร่ก็ได้
# from numbery import *

# import และเปลี่ยนชื่อฟังก์ชัน
from numberx import factorial as fa, fibonacci as fi

# #เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

print(fa(5))
print(fi(100))