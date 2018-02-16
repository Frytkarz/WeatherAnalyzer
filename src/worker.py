import json
import os

import requests

import src.parser as parser


def parse_websites(city_code, start_year, end_year):
    filename = get_filename(city_code, start_year, end_year)
    if not os.path.exists('out'):
        os.makedirs('out')
    if not os.path.exists("/home/el/myfile.txt"):
        open(filename, 'w').close()

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            parse_website("https://english.wunderground.com/history/airport/" + city_code + "/"
                          + str(year) + "/" + str(month) + "/1/MonthlyHistory.html", filename)


def parse_website(url, filename):
    print("Parsing: " + url)
    with open(filename, 'r+') as f:
        content = f.read()

    result = json.loads(content) if len(content) > 0 else {}
    r = requests.get(url)

    # with open("../test_res/page.html") as html:
    #     result = parser.parse(result, html)
    result = parser.parse(result, r.text)

    with open(filename, "w") as f:
        f.write(json.dumps(result))


def open_result(city_code, start_year, end_year):
    with open(get_filename(city_code, start_year, end_year), "r") as f:
        content = f.read()
        obj = json.loads(content)
        print("Avg temp on 18 Jan " + start_year + ": " + obj[start_year]['Jan']['18']['Temp']['avg'])
        # print(obj)


def get_filename(city_code, start_year, end_year):
    return "out/weather_" + city_code + "_" + str(start_year) + "-" + str(end_year) + ".json"
