import random

secret_number = random.randint(1, 100)
count = 0

print("สุ่มทายเลข")

while True:
    guess = int(input("กรอกตัวเลข: "))
    count +=1

    if guess > secret_number :
        print("มากไป!")
    elif guess < secret_number :
        print("น้อยไป!")
    else :
        print("ถูกต้อง! เลขคือ :" , secret_number)
        print("ทายไปทั้งหมด ", count, "ครั้ง")
        break