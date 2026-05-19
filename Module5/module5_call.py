#Importing class then running the same logic

from module5_mod import NumberStorage #import class from other file


def main():
    n = int(input("Enter N: "))

    storage = NumberStorage()

    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        storage.insert(number)

    x = int(input("Enter X: "))

    print(storage.search(x))


if __name__ == "__main__":
    main()