print("A tool for writing a number in the binary system")
while True:
    try:
        n = int(input("Enter the number: "))
        bin_n=bin(n)
        print(f"Number {n} in binary system: {bin_n}")
    except ValueError:
        print("This is not an integer! Please, enter the int number.")
