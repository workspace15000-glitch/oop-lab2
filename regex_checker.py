import re


class FloatValidator:
    def __init__(self) -> None:
        # Число содержит точку или показатель степени e/E.
        number = (
            r"[+-]?(?:(?:[0-9]+\.[0-9]*|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
            r"|[0-9]+[eE][+-]?[0-9]+)"
        )
        self.pattern = re.compile(number)

    def is_valid(self, value: str) -> bool:
        return self.pattern.fullmatch(value) is not None
