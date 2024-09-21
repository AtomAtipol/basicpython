scores = {'John': 1200,
          'Bobby' : 500,
          'Bam' : 1700,
          'Ball' : 2700}

print(scores)
print(scores['Ball'])

#เพิ่มสมาชิกเข้าไปใน Dictionary
scores['roger'] = 3200
print(scores)

#การสร้าง dictionary ว่าง
point = {}

#เพิ่มค่าเข้าไปใน dictionary ว่าง
point['mr_a'] = 3.2
point['mr_b'] = 2.7
point['mr_c'] = 5.3
point['mr_d'] = 6.8

print(point)

#การ Loop อ่านสมาชิกทั้งหมดของ Dictionary ออกมา
for k, v in scores.items():
    print(k, v)