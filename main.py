import time, rotatescreen as rotate
import random

screen_display = rotate.get_primary_display()
angels = [90, 180, 270, 0]


def rotating():
    for i in range(2):
        for x in angels:
            screen_display.rotate_to(x)
            time.sleep(0.5)


def input_random_number():
    x = random.randint(1, 5)
    tries = 0

    while True:
        tries += 1
        input_random = int(input('Input random number:'))

        if input_random == x:
            print(f'number of tries: {tries}')
            rotating()
            break
        else:
            print('Input again')


if __name__ == '__main__':
    input_random_number()
