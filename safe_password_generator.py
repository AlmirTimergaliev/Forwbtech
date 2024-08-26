from random import shuffle, randint, choice
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception = 'il1Lo0O'
chars = ''

def generate_password(length):
    passwords = []
    for _ in range(number):
        shuffle(list(chars))
        password = ''.join(chars)
        border = password.index(choice(password[:len(password) // 2]))
        password = password[border:border + length]
        passwords.append(password)
    return passwords

number = int(input('Количество паролей: '))
length = int(input('Длина пароля: '))
is_number = input('Включать ли цифры?(да/нет): ')
is_capital_letters = input('Включать ли прописные буквы?(да/нет): ')
is_lowercase_letters = input('Включать ли строчные буквы?(да/нет): ')
is_special_letters = input('Включать специальные символы !#$%&*+-=?@^_ ?(да/нет): ')
is_exception_letters = input('Исключать ли символы il1Lo0O ?(да/нет): ')

if is_number == 'да':
    chars += digits
if is_capital_letters == 'да':
    chars += uppercase_letters
if is_lowercase_letters == 'да':
    chars += lowercase_letters
if is_special_letters == 'да':
    chars += punctuation
if is_exception_letters == 'да':
    for c in exception:
        chars = chars.replace(c, '')

print(generate_password(length))
