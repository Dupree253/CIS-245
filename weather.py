import requests
import pprint
import re


def data_collect():
    while True:
        zip_code = str(input("Please enter a zip code: "))
        api_results = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=' + str(zip_code) + ','
                                   'us&appid=24658256b62af67c116c8df0435b7782')
        pprint.pprint(api_results.json())
        if zip_code == "Quit" or zip_code == "quit":
            break
    print("Thanks for using the app!")
    data_validator(zip_code)


def data_validator(zip_code):
    # zip_code_pattern = '^[0-9]{5}(?:-[0-9]{4})?$'
    empty_input = ''
    # pattern_match = re.match(zip_code_pattern, str(zip_code))
    if len(zip_code) < 0:
        print("empty")
    else:
        print("Please enter a valid zip code")


data_collect()
