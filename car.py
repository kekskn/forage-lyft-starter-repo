from abc import ABC, abstractmethod

import battery as battery
import engine as engine


class Car(ABC, battery, engine):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
