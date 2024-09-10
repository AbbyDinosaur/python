def add():
    x, y = float(input("Enter x: ")),float(input("Enter y:"))
    print (f" {x} + {y} = {x+y} ")


def sub():
    x, y = int(input("Enter x:")), int(input("Enter y:"))
    print(f"{x} - {y} = {x-y}")
    
def mul():
    x, y = float(input("Enter x:")), float(input("Enter y:"))
    print(f"{x} * {y} = {x*y}")
    
def div():
    a, b = int(input("Enter a:")), int(input("Enter b:"))
    print(f"{a} / {b} = {a/b}")
    
def floor():
    a, b = int(input("Enter a:")), int(input("Enter b:"))
    print(f"{a} // {b} = {a//b}")
    
def expo():
    a, b = int(input("Enter a:")), int(input("Enter b:"))
    print(f"{a} ** {b} = {a**b}")

def moduless():
    a, b = int(input("Enter a:")), int(input("Enter b:"))
    print(f"{a} % {b} = {a%b}")
    
def calculator():
    print("""
          ====================
           |  [+]. Add      |
           |  [-]. Sub      |
           |  [*]. Mul      |
           |  [/]. Div      |
           |  [//]. FLoor   |
           |  [%]. Modul    |
           |  [**]. Expo    |
          ====================
          """)
    
    choice = input("Select one choice [ + , - , * , / , // , % , ** ] : ")
    
    if choice == '+':
        add()
    elif choice == '-':
        sub()
    elif choice == '*':
        mul()
    elif choice == '/':
        div()
    elif choice == '//':
        floor()
    elif choice == '%':
        moduless()
    elif choice == '**':
        expo()
    else:
        print("Invalid Choice")


calculator()