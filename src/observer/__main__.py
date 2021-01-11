from src.observer.Observer import CurrentKPIs
from src.observer.Subject import KPIs


with KPIs() as kpis:                # kpis is the subject
    curr_kpis = CurrentKPIs(kpis)   # observer curr_kpis, attach itself to kpis
    kpis.set_kpis(25, 10, 5)        # initialise subject with values
    curr_kpis.display()             # use obeserver that has been updated
    kpis.deattach(curr_kpis)        # detach observer

# kpis._observers
# kpis.attach(curr_kpis)