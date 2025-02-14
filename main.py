class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotADirectoryError("Subclass must implement method.")


class Dog(Animals):
    def speak(self):
        return f"{self.name} говорит ГАВ!"


class Cat(Animals):
    def speak(self):
        return f"{self.name} говорит МЯУ!"


Dog = Dog("Бобик")
Cat = Cat("Мурзик")

print(Dog.speak())
print(Cat.speak())
