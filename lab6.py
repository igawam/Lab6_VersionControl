# Manato Igawa

def encode(data):
    pw_list = [int(digit) for digit in data]
    encoded_list = [(digit + 3) % 10 for digit in pw_list]
    encoded_pw = ''.join(map(str, encoded_list))
    return encoded_pw


# Nathan King
def decode(encoded_pw):
    empty_string=''
    for i in encoded_pw:
        empty_string += str((int(i)+7) % 10)
    return empty_string

def main():
    menu = ['Encode',
            'Decode',
            'Quit']

    contn = True

    while contn:
        print('Menu')
        print('-------------')

        for i in range(len(menu)):
            print(f'{i + 1}.', menu[i])
        print()
        opt = int(input('Please enter an option: '))

        if opt == 1:
            pw = input('Please enter your password to encode: ')
            encoded_pw = encode(pw)
            print('Your password has been encoded and stored!')
            print()

        elif opt == 2:
            print(f'The encoded password is {encode(pw)}, and the original password is {decode(encoded_pw)}.')
            print()

        elif opt == 3:
            contn = False


if __name__ == '__main__':
    main()
