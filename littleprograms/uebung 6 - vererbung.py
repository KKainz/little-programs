class Customer:

    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addresses = []

    def add_address(self, a: 'Address'):
        self.addresses.append(a)

    def __str__(self):
        return f'Customer(Name: {self.name}, Phone Number: {self.phone_number}, EMail: {self.email}, Address: {self.addresses})'

class Address:

    def __init__(self, street: str, city: str, postal_code: str, country: str):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country

    def __str__(self):
        return f'{self.street}, {self.postal_code}, {self.city}, {self.country}'

if __name__ == '__main__':
    c = Customer("Max Kauffrog", "0664 23 943 22", "maxi@kauffrog.at")
    c.add_address(Address("Teststraße 1", "graz", "8010", "AT"))
    c.add_address(Address("Teststraße 2", "Graz", "8010", "AT"))
    print(c)

