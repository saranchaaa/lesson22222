import random as r
import time as t

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    def turnon(self):
        print("Engine is turned on!")
    def turnoff(self):
        print("Engine is turned off!")
    def print_info(self):
        print(f"Car name = {car.name}. "
              f"Car max speed = {car.max_speed}km/per hour.")

namee = input("What's your car name? - ")
opnamee = r.choice("Mercedes BMW Volkswagen Lada Ferrari Lamborghini Ford Mustang Mitsubishi Honda Peugeot".split())

car = Car(namee, r.randint(160, 360))
op = Car(opnamee, r.randint(100, 400))

print("\n")
car.print_info()
print("\n")

wgd1 = input("""What  do you want to do?
1 - race
2 - stop the game - """)

if wgd1 == '2':
    print("Bye!")
    print("\n")

elif wgd1 == '1':
    print(f"Your opponent's car name = {op.name}. "
          f"Your opponent's car max speed = {op.max_speed}km/per hour."
          f"Your car max speed = {car.max_speed}km/per hour.")
    print("\n")
    car.turnon()
    print("Race is on...")
    print()
    t.sleep(1.5)

    if op.max_speed > car.max_speed:
        print("You lose!")
        car.turnoff()

        print("\n")

    if op.max_speed < car.max_speed:
        print(f"You win!")
        car.turnoff()

        print("\n")

    if op.max_speed == car.max_speed:
        print("Your car's max speed are equal!")

else:
    print("Something is wrong. Please, try again!")
