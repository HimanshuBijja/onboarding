def main():
    try:
        a, b = int(input('number1: ')), int(input('number2: '))
    except ValueError:
        print('Invalid input')
        return

    if a == 0 or b == 0:
        print('Zero division')
        return
    else:
        x = min(a, b)
        for i in range(x, 0, -1):
            if a % i == 0 and b % i == 0:
                print(f"GCD of {a} and {b}: {i}")
                break

main()
