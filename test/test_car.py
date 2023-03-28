import unittest
from datetime import datetime, timedelta
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        self.current_date = datetime(2023, 3, 28)
        self.last_service_date = datetime(2019, 3, 28)
        self.battery = NubbinBattery(self.last_service_date, self.current_date)

    def test_needs_service_true(self):
        self.battery.last_service_date = self.current_date - timedelta(days=5*365)
        self.assertTrue(self.battery.needs_service())

    def test_needs_service_false(self):
        self.battery.last_service_date = self.current_date - timedelta(days=3*365)
        self.assertFalse(self.battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        self.current_date = datetime(2023, 3, 28)
        self.last_service_date = datetime(2019, 3, 28)
        self.battery = SpindlerBattery(self.last_service_date, self.current_date)

    def test_needs_service_true(self):
        self.battery.last_service_date = self.current_date - timedelta(days=3*365)
        self.assertTrue(self.battery.needs_service())

    def test_needs_service_false(self):
        self.battery.last_service_date = self.current_date - timedelta(days=1*365)
        self.assertFalse(self.battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        self.engine = CapuletEngine(current_mileage=40000, last_service_mileage=0)
        self.assertTrue(self.engine.needs_service())

    def test_needs_service_false(self):
        self.engine = CapuletEngine(current_mileage=10000, last_service_mileage=0)
        self.assertFalse(self.engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        self.engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(self.engine.needs_service())

    def test_needs_service_false(self):
        self.engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(self.engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        self.engine = CapuletEngine(current_mileage=70000, last_service_mileage=0)
        self.assertTrue(self.engine.needs_service())

    def test_needs_service_false(self):
        self.engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        self.assertFalse(self.engine.needs_service())


if __name__ == '__main__':
    unittest.main()

