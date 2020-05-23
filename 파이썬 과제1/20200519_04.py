grade_list = [60,40,30,50,25]
avg = 0
length = len(grade_list)
for num in range(0,length) :
    avg = avg + grade_list[num]

for num in range(0,length) :
    if grade_list[num] > avg/length :
        print("%d번째 학생 합격!" %num)
    else : print("%d번째 학생 불합격!" %num)