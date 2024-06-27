# write a program that will serve as an interpreter for math in python language.
# the program will accept x y z, whereas x is an integer, y is a basic math operator and z is an integer.
# for e.g., x y z => 1 + 1. x = 1, y = + and z = 1.
# the output should be 2.0

print("Follow the rule: x y z => 1 + 1")
val = input("Expression: ").strip().lower()

x, y, z = val.split()

x, z = float(x), float(z)

match y:
    case "+":
        num = x + z
        print(num)
    case "-":
        num = x - z
        print(num)
    case "*":
        num = x * z
        print(num)
    case "/":
        num = x / z
        print(num)
    case _:
        print("Error!")
