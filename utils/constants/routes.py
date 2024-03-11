from enum import Enum


class APIRoutes(str, Enum):
    QUESTIONS = '/questions'

    def __str__(self) -> str:
        return self.value
