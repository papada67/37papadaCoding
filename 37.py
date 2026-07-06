start = int(input("เริ่มต้น : "))
ead = int(input("สิ้นสุด : "))

for row in range(start , ead + 1) :
    print("แม่" , row)

    for multiplier in range(1,13) :
        ans = row * multiplier
        print(row, "x",multiplier, "=", ans)