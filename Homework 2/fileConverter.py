# Angelo Angel (2076005)

def month_conversion(month):
    if month == 'January':
        month_int = 1
    elif month == 'February':
        month_int = 2
    elif month == 'March':
        month_int = 3
    elif month == 'April':
        month_int = 4
    elif month == 'May':
        month_int = 5
    elif month == 'June':
        month_int = 6
    elif month == 'July':
        month_int = 7
    elif month == 'August':
        month_int = 8
    elif month == 'September':
        month_int = 9
    elif month == 'October':
        month_int = 10
    elif month == 'November':
        month_int = 11
    elif month == 'December':
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

    # removes dates greater than the current date
    allowed_dates = []
    current_year = int(current_date_formatted.split("/")[2])
    current_day = int(current_date_formatted.split("/")[1])
    current_month = int(current_date_formatted.split("/")[0])
    for dates in converted_dates:
        year = int(dates.split("/")[2])
        day = int(dates.split("/")[1])
        month = int(dates.split("/")[0])
        if year < current_year:
            allowed_dates.append(dates)
        elif year <= current_year:
            if month < current_month:
                allowed_dates.append(dates)
            elif month <= current_month:
                if day < current_day:
                    allowed_dates.append(dates)
                else:
                    continue

    # writes allowed converted dates into the new file
    with open("parsedDates.txt", "w") as new_file:
        for date in allowed_dates:
            new_file.write(f"{date}\n")