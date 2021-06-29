from typing import ClassVar


class MyClass :
    classVar = 0
    def __init__ (self, initValue):
        print("MyClass 생성자가 호출되었습니다.")
        self.r = initValue

    def foo():
        print("MyClass에 오신 것을 환영합니다.")

    def foo1(self):
        print("MyClass 객체를 이용해야만 호출됩니다.")

    def printClass (self, mesg):
        print("%s : r = %d"%(mesg, self.r))

a = MyClass(10)
MyClass.foo()               
a.foo1()
MyClass.foo1(a)
a.printClass("멤버변수 출력")

b = MyClass(20)
print(a.classVar)
print(b.classVar)
MyClass.classVar = 10
print(a.classVar)
print(b.classVar)
