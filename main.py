def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def split_entry(entry):
    for operator in ['+', '-', '*' ,'/']:
        if operator in entry:
            return entry.split(operator), operator

def calculate(entry):
    entry = split_entry(entry=entry)
    a, b = map(float, entry[0])
    operator = entry[1]


    if operator == "+":
        return addition(a, b)
    elif operator == "-":
        return subtraction(a, b)

    elif operator == "*":
        return multiplication(a, b)

    elif operator == "/":
        return division(a, b)

def main():
    while True:
        try:
            entry = input()
            print(entry, entry.split())
            print(calculate(entry=entry))

        except Exception as e:
            print(e)
            continue



if __name__ == "__main__":
    main()