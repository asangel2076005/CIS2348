def sort_by_name(name):
    return name[1]


def sort_by_date(date):
    from datetime import datetime
    return datetime.strptime(date[4], '%m/%d/%Y')


def sort_by_name_date(name_date):
    from datetime import datetime
    return name_date[1], datetime.strptime(name_date[4], '%m/%d/%Y')


def sort_by_id(i_d):
    return i_d[0]


def sort_by_price(price):
    return int(price[3])
