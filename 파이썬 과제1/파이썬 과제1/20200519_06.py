
my_dict = {"최정호":"010-6722-xxxx","송민선":"010-5029-xxxx","이종훈":"010-6335-xxxx","정재환":"010-8589-xxxx"}

name = input("찾고자 하는 사람을 입력하시오.")

if my_dict.get(name) != None :
    print("%s의 전화번호는 %s입니다." %(name,my_dict.get(name)))
else :
    print("%s의 번호를 찾을 수 없습니다." %name)

