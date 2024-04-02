def collatz(number):
    if number % 2:
        return 3 * number + 1
    else:
        return number // 2

try:
    number = int(input("Enter a number: "))
    while (collatz(number) != 1):
        number = collatz(number)
        print(f"{number}")
        
except ValueError:
    print("You must enter an integer")
