from loguru import logger


class ErrorHandler(Exception):
    """
    Generic error class
    """

    def __init__(
        self, message: str = "", code: int = None, error_response: str = ""
    ) -> None:
        if not isinstance(message, str):
            raise TypeError(
                f"Expected type of error message to be str. Got {type(message)}"
            )

        self.code = code
        self.error_message = error_response
        super(ErrorHandler, self).__init__(message)

    @property
    def message(self):
        return self.args[0]


class ErrorHandler(Exception):
    def __init__(
        self, status_code: int = 500, error: str = "", message: str = "Error"
    ) -> None:
        self.error = str(error) or ""
        self.message = str(message) or "Error"
        super().__init__(message)


class FileHandlerError(ErrorHandler):
    def __init__(
        self, status_code: int = 500, error: str = "", message: str = "Error"
    ) -> None:
        super().__init__(status_code, error, message)


class FileMissingError(FileHandlerError):
    """
    Raise if no file is passed
    """

    pass


class FileParsingError(FileHandlerError):
    """
    Raise when the parser is not able to parse file
    """

    pass
