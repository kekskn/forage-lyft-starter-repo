from utils import add_years_to_date
from battery.battery import Battery



class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False

