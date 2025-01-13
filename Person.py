class Person:
    def __init__(self, name, age, city, address, phone_number):
        self._name = name
        self._age = age
        self._city = city
        self._address = address
        self._phone_number = phone_number

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


    @property
    def city(self, _default = None):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self, _default=None):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        return f"{self.name}, age {self.age}, {self.address} {self.city}, phone: {self.phone_number}"

if __name__ == "__main__":
    pekka = Person("Pekka", 10, "Lahti", "Testitie 12", "044123456")
    print(pekka)

