class Dog :
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name


my_dog = Dog("jindo")
my_dog1 = Dog("뽀삐")
print(my_dog)
print(my_dog1)
