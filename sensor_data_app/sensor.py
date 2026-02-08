import sys
from datetime import date, timedelta

import numpy as np


class SensorVisitCount:
    '''Class that simulates the number of visits detected by a sensor'''

    def __init__(self, avg_visit:int, std_visit:int, perc_break : float = 0.02, perc_malfunction : float = 0.04) -> None:
        '''Initialize the sensor with average visits, standard deviation,
        and probabilities of break or malfunction'''
 
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_break = perc_break
        self.perc_malfunction = perc_malfunction

    def simulate_visit_count(self, business_date: date) -> int:
        '''Simulate the theoretical visit count for a given business date'''

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

    def get_visit_count(self,  business_date:date) -> int:
        '''Return the final visit count, taking into account
        possible sensor break or malfunction'''

        np.random.seed(seed=business_date.toordinal())
        proba_malfunction = np.random.random()

        if proba_malfunction < self.perc_break:
            '''Sensor completely broken: returns zero visits'''
            return 0

        visit = self.simulate_visit_count(business_date)

        if proba_malfunction < self.perc_malfunction:
            '''Sensor malfunction: only 20% of visits detected'''
            visit = np.floor(visit*0.2)

        return visit


if __name__ == "__main__":
    '''Entry point of the script: reads a date from command line
    or uses a default one'''
    if len(sys.argv) >1: # beacause self is already the first argv
        year, month, day = [int(v) for v in sys.argv[1].split("-")]
    else : 
        year, month, day = 2026, 4, 2
    
    queried_date= date(year,month,day)

    capteur = SensorVisitCount(1000, 100)
    print(capteur.get_visit_count(queried_date))