class ClassA:
    def __init__(self):
        self.weight = 41
        print("Середня вага дітей з класу А=")
        print(self.weight)

class ClassB(ClassA):
    def __init__(self):
        super().__init__()
        self.age = 13
        print("Середній вік дітей з класу Б=")
        print(self.age)

class ClassC(ClassB):
    def __init__(self):
        super().__init__()
        self.height = 165
        print("Середній зріст дітей з класу В=")
        print(self.height)

Bogdan_from_classC = ClassC()

print("Вага Богдана з 8B=", Bogdan_from_classC.weight)
print("Вік Богдана з 8B=", Bogdan_from_classC.age)
print("Зріст Богдана з 8B=", Bogdan_from_classC.height)