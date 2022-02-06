from dataclasses import dataclass, field

from .enum import StatusCode


@dataclass
class ResponseDTO:
    message: str = ""
    status_code: int = StatusCode.SUCCESS.value
    data: dict = field(default_factory=lambda: {})
    # metadata: dict = field(default_factory=lambda: {})
