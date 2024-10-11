months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ")
    try:

        if '/' in date:
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        elif ',' in date:
            month_day, year = date.split(',')
            month, day = month_day.split(' ')

            if month in months:
                month_number = months.index(month) + 1
                day = int(day)
                year = int(year)

                if 1 <= day <= 31:
                    print(f"{year}-{month_number:02}-{day:02}")
                    break
    except (ValueError, IndexError):
        pass


