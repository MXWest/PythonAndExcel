bar_count = 0


def bars() -> None:
    global bar_count
    bar_count += 1
    print(f"\n>> -----{bar_count}----- <<\n")
