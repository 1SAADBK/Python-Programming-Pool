def ft_harvest_total():
    i = 1
    total = 0
    while i <= 3:
        total += int(input(f"Day {i} harvest: "))
        i += 1
    print(f"Total harvest: {total}")
