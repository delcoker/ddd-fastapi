class ProjectException(Exception):
    """Exception raised for errors in the project.

    Attributes:
        message (str): Explanation of the error.
        errors: Additional details or list of errors leading to this exception.
    """

    def __init__(self, message="project error", errors=None):
        self._message = message
        super().__init__(self._message)
        self.errors = errors

    @property
    def message(self):
        return self._message

    def __str__(self):
        return f"{self.message}. Errors: {self.errors}"
