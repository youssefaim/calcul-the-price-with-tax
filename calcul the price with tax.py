P = float(input("Enter the price of the product: "))
category = input("Enter TAX of the product (A, B, or C): ")

match category:
    case "A":
        FP = P * (1 + 7/100)
    case "B":
        FP = P * (1 + 20/100)
    case "C":
        FP = P * (1 + 25/100)
    case _:
        print("Invalid category entered.")
        FP = None

if FP is not None:
    print("The price with TAX included is:", FP)
