from __future__ import annotations

from abc import abstractmethod
from typing import Type
from urllib.request import Request

from loguru import logger

from .handler import FileHandler


class RequestManager:
    @abstractmethod
    def __enter__(self) -> Type[RequestManager]:
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def after(self, response: dict) -> dict:
        raise NotImplementedError


class FileManager(RequestManager, FileHandler):
    def __enter__(self) -> Type[RequestManager]:
        logger.info(f"Entered : {self.__classsname__}")

