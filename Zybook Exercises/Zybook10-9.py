class Car:

    def __init__(self, model_year=0, price=0, current_year=0, current_value=0):
        self.model_year = model_year
        self.price = price
        self.current_year = current_year
        self.current_value = current_value

    def calc_current_value(self):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = self.current_year - self.model_year
        self.current_value = round(self.price * (1 - depreciation_rate) ** car_age)
        return self.current_value

    def __str__(self):
        return (
            f"Car's information:\n"
            f"  Model year: {self.model_year}\n"
            f"  Purchase price: ${self.price}\n"
            f"  Current value: ${self.calc_current_value()}"
        )


if __name__ == "__main__":
    car_year = int(input())
    purchase_price = int(input())
    current_year = int(input())

    user_car = Car(car_year, purchase_price, current_year)
    print(user_car)