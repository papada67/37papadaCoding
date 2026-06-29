print("คำนวณผลBMI")

bmi_weight = float(input("น้ำหนักของคุณ : "))
bmi_height = float(input("ส่วนสูงของคุณ : "))

totei_bmi =  bmi_weight / ((bmi_height / 100) ** 2)

print("คำนวณผลbmi : " , totei_bmi)
print("ผลbmi : " , totei_bmi)

if totei_bmi < 18.5 :
    print("ผลของคุณ : น้ำหนักน้อย ")
elif totei_bmi <= 22.9 :
    print("ผลของคุณ : ปกติ ")
else :
    print("ผลของคุณ : อ้วน ")
