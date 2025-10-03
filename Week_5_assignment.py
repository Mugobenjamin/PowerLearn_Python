# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"


# Subclass (Inheritance + Polymorphism)
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, android_version):
        # Call parent constructor
        super().__init__(brand, model, storage)
        self.android_version = android_version

    # Polymorphism: Overriding the info() method
    def info(self):
        return f"{self.brand} {self.model} running Android {self.android_version}, {self.storage}GB storage"


# Subclass (Encapsulation)
class SuperSmartphone(Smartphone):
    def __init__(self, brand, model, storage, security_code):
        super().__init__(brand, model, storage)
        self.__security_code = security_code  

    def unlock(self, code):
        if code == self.__security_code:
            print("Phone unlocked!")
        else:
            print("Wrong code, access denied.")


# ----------- Usage ------------
# Create objects
iphone = Smartphone("Apple", "iPhone 15", 256)
samsung = AndroidPhone("Samsung", "Galaxy S24", 512, "14")
secure_phone = SuperSmartphone("OnePlus", "11 Pro", 128, "1234")

# Demonstrate methods
print(iphone.info())
iphone.power_on()

print(samsung.info())  # Polymorphism (overridden info)

secure_phone.unlock("1111")  # Wrong code
secure_phone.unlock("1234")  # Correct code
