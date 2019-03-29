from attr import dataclass


@dataclass(frozen=True, cmp=True)
class BaseError(Exception):
    message: str


class InvalidInput(BaseError):
    """
    Raised when the input file cannot be parsed.
    """

    pass


class DeserializeError(BaseError):
    """
    Raised when the parse result cannot be deserialized to file structure models.
    """

    pass


@dataclass(frozen=True, cmp=True)
class BaseWarning(Warning):
    message: str


class MissingExamplesWarning(BaseWarning):
    """
    Raised when examples are missing in ScenarioOutline
    """

    pass


class EmptyExamplesWarning(BaseWarning):
    """
    Raised when an examples table is empty
    """

    pass


class NothingChanged(BaseWarning):
    """Raised when reformatted code is the same as source."""

    pass
