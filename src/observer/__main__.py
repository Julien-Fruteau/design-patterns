from src.observer.Observer import CurrentKPIs
from src.observer.Subject import KPIs


with KPIs() as kpis:                        # kpis is the subject, (with) benefit context manager implementation of Subject class
    with CurrentKPIs(kpis) as curr_kpis:    # benefit Observer Context Manager implementation
        # curr_kpis = CurrentKPIs(kpis)     # observer curr_kpis, attach itself to kpis
        kpis.set_kpis(25, 10, 5)            # initialise subject with values, NOTE that it update Observer attached at the same time
        curr_kpis.display()                 # use obeserver that has been updated
        # kpis.deattach(curr_kpis)          # detach observer. NOTE that curr_kpis automatically detach itself with __exit__ method
