"""Carl Phillips, this program tells you your half birthday"""
from datetime import datetime, timedelta

def half_birthday(birthday):
    """
    :param birthday: your birthday
    :return: your half birthday
    """
    half_date = birthday + timedelta(6*365/12)
    print("Your birthday: " + str(birthday) + "\nYour half birthday: " + str(half_date))
    return half_date

if __name__ == '__main__':
    half_birthday()
