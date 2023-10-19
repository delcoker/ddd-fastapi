from typing import Any, Optional, Union


class ApiResult:
    def __init__(self, response_data: Any = None, error: Optional[Exception] = None):
        self.response_data = response_data
        self.error = error

    @property
    def is_successful(self) -> bool:
        return not self.error and 200 <= self.response_data.status_code < 300
