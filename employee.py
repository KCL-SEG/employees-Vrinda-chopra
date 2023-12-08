"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hourly_rate=0, hours_worked=0, bonus=0, contracts=0, commission_per_contract=0):
        self.name = name
        self.salary = salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract
    
    def calculate_monthly_pay(self):
        return self.salary

    def calculate_hourly_pay(self):
        return self.hourly_rate * self.hours_worked

    def calculate_bonus(self):
        return self.bonus

    def calculate_commission(self):
        return self.contracts * self.commission_per_contract
    
    def get_pay(self):
        get_pay = 0
        get_pay += self.calculate_monthly_pay() if self.salary else 0
        get_pay += self.calculate_hourly_pay() if self.hourly_rate else 0
        get_pay += self.calculate_bonus() if self.bonus else 0
        get_pay += self.calculate_commission() if self.contracts and self.commission_per_contract else 0
        return get_pay

    def generate_explanation(self):
        explanation = f"{self.name} "
        if self.salary:
            explanation += f"works on a monthly salary of {self.salary}"
        elif self.hourly_rate:
            explanation += f"works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour"

        if self.bonus:
            explanation += f" and receives a bonus commission of {self.bonus}"

        elif self.contracts and self.commission_per_contract:
            explanation += f" and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract"

        explanation += f". Their total pay is {self.get_pay()}."
        return explanation


    def __str__(self):
        return self.generate_explanation()


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)
print(str(billie))


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourly_rate=25, hours_worked=100)
print(str(charlie))



# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, contracts=4, commission_per_contract=200)
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hourly_rate=25, hours_worked=150, contracts=3, commission_per_contract=220)
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hourly_rate=30, hours_worked=120, bonus=600)
print(str(ariel))
