# Compount Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than or equal to zero")
    else:
        break



while True:
    time = float(input("Enter the time of investment: "))
    if time < 0:
        print("Time cannot be less than or equal to zero")
    else:
        break


while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate cannot be less than or equal to 0")
    else:
        break


total = principle * pow((1 + rate / 100), time)

print (f"The total investment over {time} year/s is ${total:.2f}")