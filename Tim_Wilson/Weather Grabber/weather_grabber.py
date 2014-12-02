#! /usr/bin/env python3

import urllib
import re
import datetime

SITE_TEMPLATE = "http://www.aviationweather.gov/adds/metars/?station_ids={station}&std_trans=standard&chk_metars=on&hoursStr=most+recent+only&submitmet=Submit"

def get_station():
    while True:
        try:
            station = input("Get weather from what station? ").upper()
            if len(station) != 4:
                raise ValueError("Station id must be 4 letters!")
            elif not station.isalpha():
                raise ValueError("Station id must contain only letters!")
            return station
        except ValueError as err:
            print(err)


def get_METAR():
    while True:
        try:
            station_id = get_station()
            response = urllib.request.urlopen(SITE_TEMPLATE.format(station = station_id))
            html_string = str(response.read())
            match = re.search(station_id+'.*</FONT>', html_string)
            excerpt_temp = match.group(0)
            return excerpt_temp[:excerpt_temp.index('<')]
        except urllib.error.URLError:
            print("This station is currently not available, try again.")
        except AttributeError:
            print("Cannot find METAR record in the response, check format.")

def print_METAR(string_METAR):
    METAR_entries = string_METAR.split()
    if len(METAR_entries) != 11:
        print("The METAR record doesn not have the right number of fields\n--> {0}".format(string_METAR))
    else:
        now = datetime.datetime.utcnow()
        year = now.year
        month = now.month
        print("Current conditions for {0}".format(METAR_entries[0]))
        print("Last observation: {0}/{1}/{2} at {3}:{4} GMT".format(year, month, METAR_entries[1][0:2], METAR_entries[1][2:4], METAR_entries[1][4:6]))
        t_string = METAR_entries[6].split('/')[0]
        if t_string.startswith('M'):
            t = -int(t_string[1:])
        else:
            t = int(t_string)
        print("Temperature: {0} C".format(t))

        print("Wind: direction {0} at {1} knots".format(METAR_entries[3][0:3], int(METAR_entries[3][3:5])))

def main():
    print("Current weather conditions\n\nThis program retrieves the current weather conditions from the National Weather Services. Enter a four_letter station ID (e.g., 'KSGS')")
    print('\n')
    string_METAR = get_METAR()
    print_METAR(string_METAR)

if __name__ == "__main__":
    main()
