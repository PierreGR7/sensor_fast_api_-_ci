from ast import Store
import unittest
from datetime import date

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from sensor_data_app.store import StoreSensor

class TestStore(unittest.TestCase):
    def test_get_traffic_by_store(self):
        strasbourg_store = StoreSensor("Strasbourg", 1000, 100)
        traffic_Strasbourg = strasbourg_store.get_traffic_by_store(date(2026, 2, 2))
        self.assertEqual(traffic_Strasbourg,905)

    def test_get_traffic_by_sensor(self):
        strasbourg_store = StoreSensor("Strasbourg", 1000, 100)
        traffic_Strasbourg = strasbourg_store.get_traffic_by_sensor(1,date(2026, 2, 2))
        self.assertEqual(traffic_Strasbourg,90)

    def test_sunday_closed(self):
        strasbourg_store = StoreSensor("Lille", 1000, 100)
        visits = strasbourg_store.get_traffic_by_sensor(1,date(2026, 2, 8))
        self.assertEqual(visits, -1)

if __name__ == "__main__":
    unittest.main()