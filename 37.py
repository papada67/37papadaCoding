print("โปรแกรมคำนวณคะแนนรวม\n")

point_math = int(input("คะแนนวิชาคณิตศาสตร์ "))
point_chemistry = int(input("คะแนนวิชาเคมี "))
point_science = int(input("คะแนนวิชาวิทยาศาสตร์ "))

total_point = (point_science + point_chemistry + point_math)
average_point = total_point / 3

print("\nคะแนนรวม:" , total_point)
print("คะแนนเฉลี่ย : ", average_point)

if average_point >= 60:
    print("ระดับคะแนน : ควรปรับปรุง ")
elif average_point >= 70:
    print("ระดับคะแนน : ผ่าน ")
else:
    print("ระดับคะแนน : ยอดเยี่ยม ")  

print("Programmer : papada rungarunchai ")    