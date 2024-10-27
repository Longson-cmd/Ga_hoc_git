# return model and car_value

class Car():
    tax = 1
    car_number = 0
    def __init__(self, brand, model, founded_year, price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price
        Car.car_number += 1
    def car_value(self):
        return (self.price * self.tax)
    @classmethod
    def from_string(cls, car_string):
        brand, model, founded_year, price = car_string.split('-')
        founded_year = int(founded_year)
        price = int(price)
        return cls(brand, model, founded_year, price)
    @staticmethod
    def check_price(price):
        if price <= 800:
            return 'xe rẻ'
        else:
            return 'xe đắt'
     
car_temp = 'Matit-Xelau-1977-500'
car_1 = Car('Toyota', 'Camry', 1970, 1000)
car_2 = Car('BMV', 'Lixux', 1980, 900) 
car_3 = Car.from_string(car_temp)
print(car_1.check_price(car_1.price))
print(Car.check_price(car_3.price))
 



    










