from src.observer.ASubject import ASubject


class KPIs(ASubject):
    _open_tickets:int = -1
    _closed_tickets:int = -1
    _new_tickets:int = -1

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_tickets: int, closed_tickets:int , new_tickets:int):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()
