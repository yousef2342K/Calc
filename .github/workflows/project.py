class calc:
    def __init__(self,num1,num2):
       self.num1=num1
       self.num2=num2

    def add(self):
        return self.num1+self.num2

    def multiply(self):
        return self.num1*self.num2

    def subs(self):
        return self.num1-self.num2

    def div(self):
        return self.num1/self.num2

    def mod(self):
        return self.num1%self.num2
x = int(input("Enter the first number plz :  "))
y = int(input("Enter the second number plz : "))

calc1=calc(x,y)

print (f"the sum of the two number is {calc1.add()}")
print (f"the product of the two number is {calc1.multiply()}")
print (f"the difference of the two number is {calc1.subs()}")
print (f"the quotient of the two number is {calc1.div()}")
print (f"the modulus of the two number is {calc1.mod()}")
