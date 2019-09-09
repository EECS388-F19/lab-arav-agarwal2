import random


def main():
    print("Arav Agarwal")
    randA = random.randint(0,101)
    randB = random.randint(0,101)
    print(randA)
    print(randB)
    print("Sum = " + str(randA + randB))
    print("Average = " + str((randA + randB)/2))

if __name__ == "__main__":
    main()
