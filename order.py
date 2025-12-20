from datetime import datetime

def get_days_from_today(date):
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    current_date = datetime.today().date()
    return (current_date - target_date).days
if __name__ == "__main__":
    print(f"Дней с 2023-12-25: {get_days_from_today('2023-12-25')}")
    print(f"Дней до 2025-12-19: {get_days_from_today('2025-12-19')}")
    today_str = datetime.today().strftime("%Y-%m-%d")
    print(f"Дней с сегодня ({today_str}): {get_days_from_today(today_str)}")