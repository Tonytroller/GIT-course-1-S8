from datetime import datetime

class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello, my name is {self.name}")

    @staticmethod
    def give_date_and_time(self):
        current_datetime = datetime.now()
        print(current_datetime)