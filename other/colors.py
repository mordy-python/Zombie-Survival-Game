# Created by Jordan Leich on 7/27/2020

from colored import fg, attr
from time import sleep
from classes import Difficulty


GREEN = fg('green')
RED = fg('red')
YELLOW = fg('yellow')
BLUE = fg('blue')
RESET = attr('reset')


def print_green(message_text, sleep_duration=0):
    print(f'{GREEN}{message_text}{RESET}')
    sleep(sleep_duration)


def print_red(message_text, sleep_duration=0):
    print(f'{RED}{message_text}{RESET}')
    sleep(sleep_duration)


def print_yellow(message_text, sleep_duration=0):
    print(f'{YELLOW}{message_text}{RESET}')
    sleep(sleep_duration)


def print_blue(message_text, sleep_duration=0):
    print(f'{BLUE}{message_text}{RESET}')
    sleep(sleep_duration)


def user_error(message_text, sleep_duration=0):
    print_red(message_text, sleep_duration)


# print and sleep
def print_s(message_text, sleep_duration=0):
    print(message_text)
    sleep(sleep_duration)


def print_health(player_difficulty, message, sleep_duration=0):
    if player_difficulty == Difficulty(1):
        print_green(message, sleep_duration)
    elif player_difficulty == Difficulty(2):
        print_yellow(message, sleep_duration)
    elif player_difficulty == Difficulty(3):
        print_red(message, sleep_duration)
