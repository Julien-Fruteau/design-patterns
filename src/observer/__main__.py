from src.observer.observer_dashboard_current_kpis import DashboardCurrentKPIs
from src.observer.subject_kpis import KPIs


with KPIs() as kpis:
    curr_kpis = DashboardCurrentKPIs(kpis)  # attach itself to kpis
    kpis.set_kpis(25, 10, 5)
    curr_kpis.display()
    kpis.deattach(curr_kpis)

# kpis._observers
# kpis.attach(curr_kpis)