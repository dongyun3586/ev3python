from calculator import Calculator, Calculator2

calc1 = Calculator()
print(calc1.add(3,4))

calc2 = Calculator2(30, 40)
print(calc2.add())
print(calc2.subtract())

calc3 = Calculator2(num2=30, num1=40)
print(calc3.add())
print(calc3.subtract())