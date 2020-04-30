#input module


def read_text(prompt):
    while True:
        text = input(prompt)
        break
    return text


def read_int(prompt):
    while True:
        try:
            value = int(read_text(prompt))
            break
        except ValueError:
            print('Integer values only!')
    return value

def read_float(prompt):
    while True:
        try:
            value = float(read_text(prompt))
            break
        except ValueError:
            print('Decimal values only!')
    return value


def menu_selector(prompt, min_value, max_value):
    while True:
        option = read_float(prompt)
        if option < min_value:
            print(f'least vales: {min_value}')
            continue
        elif option > max_value:
            print(f'Highest value: {max_value}')
            continue
        else:
            break
    return option
