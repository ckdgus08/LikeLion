# 클래스 

class Dog(object):
    def __init__(self, name, gender) :
        self.name = name
        self.gender = gender
    def __str__(self):
        return f'이름은 {self.name}이고 성별은 {self.gender}입니다.'
    def bark(self, tf):
        if tf == True :
            print("멍멍")
a = Dog("reo","남")
b = Dog("mini","여")
print(a)
a.bark(True)
print(b)
b.bark(False)

