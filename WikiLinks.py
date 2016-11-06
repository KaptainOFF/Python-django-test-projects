import datetime
import logging

logging.basicConfig(filename='dates.log', level=logging.DEBUG)
logging.basicConfig(filename='dates.log', level=logging.INFO)


def get_day():

    while True:
        print("Please provide a day(1 - 31): ")
        try:
            day = int(input("> "))
            if day < 1 or day > 31:
                print("Day needs to be a number between 1 and 31")
                logging.warning("The day needs to be a number between 1 and 31")
                continue
            else:
                break
        except ValueError:
            logging.warning("User provided a letter instead of number")
            continue
    return day


def get_month():

    while True:
        print("Please provide a month(1 - 12): ")
        try:
            month = int(input("> "))
            if month < 1 or month > 12:
                print("Month needs to be between 1 and 12")
                continue
            else:
                break
        except ValueError:
            print("The month needs to be a number between 1 and 12")
            continue
    return month


def wiki_link():
    while True:
        day = get_month()
        month = get_day()
        try:
            date = datetime.datetime.strptime("%d-%d" % (day, month), "%m-%d" )
            break
        except ValueError:
            print("Day is out of range for month")
            continue

    wiki_date = datetime.datetime.strftime(date, "%B_%d")
    url = "https://en.wikipedia.org/wiki/{}".format(wiki_date)
    logging.info(url)
    return url


print(wiki_link())
