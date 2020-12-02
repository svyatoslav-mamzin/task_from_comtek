from datetime import datetime


def date_validation(date):
    try:
        valid_date = datetime.strptime(date, '%d.%m.%Y')
        return valid_date.date()
    except ValueError:
        return None
