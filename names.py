from name_function import get_formatted_name

print("Enter q to quit")
while True:
    first = input("\nPlease give me your first name: ")
    if first == "q":
        break

    last = input("Please give me your last name: ")
    if last == "q":
        break

    middle = input("Please give me your middle name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"\tNeatly formatted name: {formatted_name}")
