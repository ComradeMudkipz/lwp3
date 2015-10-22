# compoundInterestCalculator.py
# A compound interest calculator.

P = int(10000)
n = int(12)
r = float(0.8)
t = int(input("How many years? "))
print(P * (1 + r / n) ** n * t)
