score1 = int(input("คะแนนวิชาที่1 "))
score2 = int(input("คะแนนวิชาที่2 "))
score3 = int(input("คะแนนวิชาที่3 "))

totei_score = (score1 + score2 + score3)

if totei_score < 60:
    print("ระดับคะแนน  ควรปรับปรุง")
elif totei_score <= 79:
    print("ระดับคะแนน = ผ่าน")
else :
    print("ระดับคะแนน = ดีเยี่ยม") 

    print("คะแนนรวมของคุณ = ", totei_score)
    print("คะแนนเฉลี่ย 3 วิชา = ", totei_score / 3)