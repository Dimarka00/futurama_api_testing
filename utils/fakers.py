from random import choice, randint
from string import ascii_letters, digits


def random_number(start: int = 100, end: int = 1000) -> int:
    return randint(start, end)


def random_number_from_1_to_100(start: int = 1, end: int = 100) -> int:
    return randint(start, end)


def random_string(start: int = 5, end: int = 15) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_list_of_strings(start: int = 5, end: int = 15) -> list[str]:
    return [random_string() for _ in range(randint(start, end))]
