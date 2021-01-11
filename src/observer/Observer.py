from src.observer.Subject import KPIs
from typing import Union
from src.observer.AObserver import AObserver


class CurrentKPIs(AObserver):
    open_tickets: int = -1
    closed_tickets: int = -1
    new_tickets: int = -1

    def __init__(self, kpis: KPIs):
        self._kpis = kpis
        kpis.attach(self)

    def update(self, value: Union[int, None] = None):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

    def display(self):
        print(f"Current open tickets : {self.open_tickets}")
        print(f"New tickets : {self.closed_tickets}")
        print(f"Tickets closed : {self.new_tickets}")

    def __exit__(self, exception_type, exception_value, traceback):     # type: ignore
        self._kpis.deattach(self)
