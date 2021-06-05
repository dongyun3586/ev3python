class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

# 매개 변수가 있는 생성자
class Calculator2:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2






