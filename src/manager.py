from __future__ import annotations

from abc import abstractmethod
from typing import Type

from flask import Flask, Request
from loguru import logger

from .handler import FileHandler


class ContextManager:
    ...


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
    def __init__(self, app: Flask, request: Request) -> None:
        app = app
        request = request
        logger.info(f"Request : {request}")

    def __enter__(self) -> Type[RequestManager]:
        logger.info(f"Entered : {self.__classsname__}")
        return self

    def __exit__(self, *args, **kwargs):
        logger.debug(f"Exited : {self.__classname__}")

    def after(self, response: dict) -> dict:
        ...

