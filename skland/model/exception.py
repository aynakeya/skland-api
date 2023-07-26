import json
from typing import Union


class SklandException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)


class SklandApiException(SklandException):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __str__(self):
        return f"SklandApiException {self.code}: {self.message}"
