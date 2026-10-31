def days_recursive(days):
    if days > 0:
        days_recursive(days - 1)
        print(f"Day {days}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    days_recursive(days)
    print("Harvest time!")
