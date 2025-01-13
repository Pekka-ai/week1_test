class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def __str__(self):
        return f"{self.name}, age {self.age} "

    # Getter name:lle
    @property
    def name(self):
        return self._name

    # Setter name:lle
    @name.setter
    def name(self, value):
        self._name = value

    # Getter age:lle
    @property
    def age(self):
        return self._age

    # Setter age:lle
    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    pekka = Person("Pekka", 10)
    print(pekka)