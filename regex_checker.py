import re


class FloatValidator:
    def __init__(self) -> None:
        # Число содержит точку или показатель степени e/E.
        number = (
            r"[+-]?(?:(?:[0-9]+\.[0-9]*|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
            r"|[0-9]+[eE][+-]?[0-9]+)"
        )
        self.pattern = re.compile(number)
        # Не ищем часть слова или записи вроде 1.2.3.
        self.search_pattern = re.compile(
            r"(?<![\w.+-])" + number + r"(?!\w|\.[0-9])"
        )

    def is_valid(self, value: str) -> bool:
        return self.pattern.fullmatch(value) is not None

    def validate_text(self, text: str) -> list[str]:
        return self.search_pattern.findall(text)
