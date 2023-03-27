from abc import ABC
from datetime import datetime

from car import Car


class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = datetime.strptime(current_date, '%Y-%m-%d')

    def engine_should_be_serviced(self):
        last_service_date = datetime.strptime(self.last_service_date, '%Y-%m-%d')
        days_since_last_service = (self.current_date - last_service_date).days
        return days_since_last_service > 730

