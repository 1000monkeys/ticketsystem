import sys


def get_price(age: int) -> int:
    """Returns the price for a given age"""
    try:
        age = int(age)
    except ValueError:
        print("Please input a integer!")
        return ValueError

    if age < 4:
        return 0
    elif 3 < age < 19:
        return 5
    elif 18 < age < 65:
        return 10
    elif 64 < age:
        return 8


def get_total(ages):
    """Calculates the total amount due with discounts"""
    total = 0
    discount = False
    if len(ages) > 4:
        discount = True

    for age in ages:
        total += get_price(age)

    return total, discount


if __name__ == '__main__':
    while True:
        amount_persons = int(input("How many people? "))

        total = 0
        ages = []
        discount = False
        for i in range(amount_persons):
            age = input("Age: ")
            if age == 999 or age == 'q':
                sys.exit()

            print("Price:     €" + str(get_price(int(age))))
            ages.append(int(age))

            total, discount = get_total(ages)
            print("Total:     €" + str(total))

        print("###################")
        if discount:
            total -= 5
            print("Discount:  €5")
        print("Total:     €" + str(total))
        print("###################")
