import abc
from typing import Union

class AObserver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, value: Union[int, None] = None):
        pass

    # turn the class into a context manager (with ...)
    def __enter__(self):
        return self

    # turn the class into a context manager (with ...)
    @abc.abstractmethod
    def __exit__(self, exception_type, exception_value, traceback):     # type: ignore
        pass
