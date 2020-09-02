from src.observer.observer_abc import AbsObserver


class DashboardCurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self, value=None):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

    def display(self):
        print(f"Current open tickets : {self.open_tickets}")
        print(f"New tickets : {self.closed_tickets}")
        print(f"Tickets closed : {self.new_tickets}")

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)
