import numpy as np
from datetime import date

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from sensor_data_app.sensor import SensorVisitCount

class storeSensor:
    def __init__(self, name:str, avg_visit:int, std_visit:int, perc_break : float = 0.0, perc_malfunction : float = 0.0) -> None:
        self.name = name
        self.sensors = list()

        