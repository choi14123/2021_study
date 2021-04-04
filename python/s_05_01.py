name = ""
year = 0
q = ['python']
salary = 0
salary_d = 0

class Employ :


    def __init__(self,name,year):
        self.name = name
        self.year = year
        print(name, "의 연차는", year, "년 입니다.")



    def salary(self):
        if self.year <= 5:
            self.salary = 3000 + self.year * 100
        elif self.year <= 10:
            self.salary = 3500 + self.year * 110
        elif self.year <= 15:
            self.salary = 4000 + self.year * 130
        print(self.name, "의 연봉", self.salary,"만원 입니다.")



    def degree(self):
        if self.name in q:
            self.salary_d = self.salary + 1200
        print(self.name, "님의 연봉은 학위 소지로 인하여", self.salary_d, "만원 입니다.")


    def __getattr__(self, anything) :
        print("잘못된 값 입니다.")


a = Employ ("python", 7)
a.salary()
a.degree()
a.money
print(
    a.name, a.salary_d)




