import sys
from datetime import date, timedelta

import numpy as np


class SensorVisitCount:

    def __init__(self, avg_visit:int, std_visit:int,) -> None:
 
        self.avg_visit = avg_visit
        self.std_visit = std_visit

    def simulate_visit_count(self, business_date: date) -> int:

        # reproducibility of measurements
        np.random.seed(seed=business_date.toordinal())

        # Find out which day corresponds from Monday = 0 to Sunday = 6
        week_day = business_date.weekday()

        visit = np.random.normal(self.avg_visit, self.std_visit)
        # More traffic wednesday, friday and saturday
        if week_day == 2:
            visit *= 1.2
        if week_day == 4:
            visit *= 1.3
        if week_day == 5:
            visit *= 1.4

        # on sunday the store is closed
        if week_day == 6:
            visit = -1

        # Return an integer
        return np.floor(visit)

if __name__ == "__main__":
    capteur = SensorVisitCount(1000, 100)
    print(capteur.simulate_visit_count(date(2026,2,4)))