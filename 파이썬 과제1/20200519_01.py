id_front = 970329
id_back = 1611111

# id_front를 0으로 시작되면 SyntaxError 발생함.

if str(id_back)[0:1] == "1" :
    gender = "남자"
    age = 2020 - 1900 - int(str(id_front)[0:2]) + 1
elif str(id_back)[0:1] == "3" :
    gender = "남자"
    age = 2020 - 2000 - int(str(id_front)[0:2]) + 1
elif str(id_back)[0:1] == "2" :
    gender = "여자"
    age = 2020 - 1900 - int(str(id_front)[0:2]) + 1
elif str(id_back)[0:1] == "4":
    gender = "여자"
    age = 2020 - 2000 - int(str(id_front)[0:2]) + 1
else :
    gender = "오류"

month = str(id_front)[2:4]
days = str(id_front)[4:6]

print("나이 : %d\n생일 : %d월 %d일\n성별 : %s" %(age,int(month),int(days),gender))