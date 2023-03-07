# Angelo Angel (2076005)

def month_conversion(user_month):
    if user_month == 'January':
        month_int = 1
    elif user_month == 'February':
        month_int = 2
    elif user_month == 'March':
        month_int = 3
    elif user_month == 'April':
        month_int = 4
    elif user_month == 'May':
        month_int = 5
    elif user_month == 'June':
        month_int = 6
    elif user_month == 'July':
        month_int = 7
    elif user_month == 'August':
        month_int = 8
    elif user_month == 'September':
        month_int = 9
    elif user_month == 'October':
        month_int = 10
    elif user_month == 'November':
        month_int = 11
    elif user_month == 'December':
        month_int = 12
    else:
        return None

    return month_int


if __name__ == "__main__":
    import datetime

    # gets the value of the current date
    current_date = datetime.date.today()
    current_date_formatted = current_date.strftime("%m/%d/%Y")

    input_file = input("Enter file name: ")

    user_file = open(input_file, "r")
    contents = []

    # read each lines
    for line in user_file:
        contents.append(line)
    user_file.close()
