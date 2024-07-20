def divi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: No se puede dividir entre 0")


if __name__ == "__main__":
    print(divi(4, 2))
