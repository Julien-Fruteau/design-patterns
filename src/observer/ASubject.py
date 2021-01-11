import abc
from typing import Union
from src.observer.AObserver import AObserver

class ASubject(metaclass=abc.ABCMeta):

    _observers = set()

    def attach(self, observer: AObserver):
        self._observers |= {observer}

    def deattach(self, observer: AObserver):
        self._observers -= {observer}

    def notify(self, value: Union[int, None] = None) -> None:
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):     # type: ignore
        self._observers.clear()
