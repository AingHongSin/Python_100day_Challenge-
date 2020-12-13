from art import logo

# Add
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operator = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}
def Calculation():
    print(logo)
    nextCalc = False

    n1 = float(input("What is the first number? "))
    for keys in operator:
        print(keys)

    while not nextCalc:

        operation_symbole = input("Pick a operation symbole above: ")
        n2 = float(input("What is the next number? "))

        answer = operator[operation_symbole](n1, n2)

        print(f"{n1} {operation_symbole} {n2} = {answer}")

        next = input(f"Type 'y' to continue with {answer}, type 'n' for exit: ")
        

        if next == 'y':
            n1 = answer
        else:
            nextCalc = True
            Calculation()
Calculation()
