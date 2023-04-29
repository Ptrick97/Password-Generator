import random


def generate_password(num_characters):
    alphabet_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabet_lower = list('abcdefghijklmnopqrstuvwxyz')
    especial_characters = list('!@#$%<>/?')
    numeric_characters = list('0123456789')
    generating_password = alphabet_lower + alphabet_upper + especial_characters + numeric_characters

    while True:
        num_characters = int(input('How many characters do you want in your password (8 to 20): '))
        if num_characters < 8 or num_characters > 20:
            print('Valor inválido, escolha um número entre 8 e 20')
        else:
            break
    result = ''
    for i in range(num_characters):
        result += random.choice(generating_password)

    return result


password = generate_password(num_characters=int)
print(password)

