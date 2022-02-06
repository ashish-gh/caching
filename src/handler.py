from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import List
from urllib.request import Request

# from flask import Request


class AbstractHandler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self.handle(*args, **kwargs)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.__dict__)

    @property
    def __classname__(self) -> str:
        return str(f"{self.__class__.__name__}")


class FileHandler(AbstractHandler):
    def __init__(self, valid_extensions: List[str] = []) -> None:
        self.valid_extensions = valid_extensions

    @staticmethod
    def is_valid_file(file_name: str):
        """
        Is valid file
        """
        ...

    @classmethod
    def is_valid_extension(cls: classmethod, ext: str = "") -> bool:
        """
        Is valid extension
        """
        if ext not in cls.valid_extensions:
            raise ValueError(f"Not valid extension type")
        return True

    def handle(self, request: Request, **kwargs):
        ...

