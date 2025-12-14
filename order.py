from datetime import datetime
def get_days_from_today(date_str) -> int:
    target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    current_date = datetime.today().date()
    delta = target_date - current_date
    return delta.days

