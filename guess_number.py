import random

n = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')


def is_valid(arg):
    if not arg.isdigit():
        return False
    else:
        return True if 1 <= int(arg) <= 100 else False


def enter_number():
    while True:
        guess_number = input('введите целое число от 1 до 100: ')
        if not is_valid(guess_number):
            print('А может быть все-таки введем целое число от 1 до 100?')
        else:
            return int(guess_number)


def hint():
    guess_number = enter_number()
    if guess_number < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif guess_number > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        return 1


def game():
    count_tries = 1

    while hint() != 1:
        count_tries += 1
        hint()

    print('Потрачено попыток: ', count_tries)


game()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
