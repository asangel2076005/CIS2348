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

    # removes newline characters
    dates = []
    for content in contents:
        dates.append(content.strip())

    # removes unwanted dates based on their format
    pseudo_allowed_dates = []
    for date in dates:
        month = month_conversion(date.split()[0])
        if month is not None:
            day_comma = date.split()[1][-1]
            if day_comma == ",":  # if the day has a comma after it, then include it, otherwise dispose of it as well
                pseudo_allowed_dates.append(date)
        else:
            continue

    # converts allowed dates into the new format
    converted_dates = []
    for date in pseudo_allowed_dates:
        new_date = date.split(" ")
        new_date[0] = str(month_conversion(new_date[0]))
        new_date[1] = new_date[1].replace(",", "")
        converted_dates.append("/".join(new_date))
