import numpy as np
from datetime import date

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from sensor_data_app.sensor import SensorVisitCount

class StoreSensor:
    '''Class representing a store composed of multiple traffic sensors'''
    def __init__(self, name:str, avg_visit:int, std_visit:int, perc_break : float = 0.0, perc_malfunction : float = 0.0) -> None:
        '''Initialize a store with a name and create its sensors'''
        self.name = name
        self.sensors = list()

        # reproducibility of measurements (same result when we take the same store)
        '''Generate a deterministic seed based on the store name'''
        seed = np.sum(list(self.name.encode("ascii")))
        np.random.seed(seed=seed)

        # traffic per sensor (let's say there are 8 sensors in each store)
        '''Traffic distribution across the 8 sensors'''
        traffic_percentage = [0.50,0.20,0.10,0.05,0.03,0.01,0.01,0.10]
        np.random.shuffle(traffic_percentage)

        # We initialize the 8 sensors of each store
        '''Creation of the 8 sensors with their respective traffic share'''
        for i in range(8):
            sensor = SensorVisitCount(
                avg_visit * traffic_percentage[i],
                std_visit * traffic_percentage[i],
                perc_break,
                perc_malfunction
            )
            self.sensors.append(sensor)

    def get_traffic_by_sensor(self, sensor_id : int, business_date : date) -> int:
        '''Return the visit count for a specific sensor'''
        return self.sensors[sensor_id].get_visit_count(business_date)

    def get_traffic_by_store(self, business_date : date) -> int:
        '''Return the total visit count for the whole store'''
        visit = 0
        for i in range(8):
            visit += self.sensors[i].get_visit_count(business_date)
        return visit

if __name__ == "__main__":
    strasbourg_store = StoreSensor("Strasbourg", 1000, 100)
    print(strasbourg_store.get_traffic_by_store(date(2026, 2, 2)))
    print(strasbourg_store.get_traffic_by_sensor(1,date(2026, 2, 2)))