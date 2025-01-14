from datetime import datetime, timedelta
from random import randint

class CustomFunctions:
    @staticmethod
    def get_current_timestamp_millis(delta_days: int = 0) -> int:
        if delta_days:
            past_date = datetime.now() - timedelta(days=delta_days)
            return int(past_date.timestamp() * 1000)
        return int(datetime.now().timestamp() * 1000)
    
    @staticmethod
    def get_random_number() -> int:
        return randint(1, 100)
