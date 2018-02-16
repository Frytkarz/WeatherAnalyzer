from bs4 import BeautifulSoup


def parse(result, html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table", {"id": "obsTable"})
    head = table.find("thead")
    columns = []
    for th in head.findAll("th"):
        colspan = int(th.attrs['colspan']) if 'colspan' in th.attrs else 1
        for i in range(0, colspan):
            c = {'name': th.contents[0].replace(".", "").replace(" ", "")}
            columns.append(c)

    first = True
    parse_error = False
    if not result:
        result = {}
    for tbody in table.findAll("tbody"):
        if first:
            c = 0
            for td in tbody.findAll("td"):
                value = td.contents[0].replace(".", "").replace(" ", "") \
                    if td.contents[0] and not td.contents[0].isspace() \
                    else "value"
                if columns[c]['name'] == 'Wind' and value == "high" and columns[c-2]['name'] == 'Wind':
                    value = "low"
                columns[c]['subname'] = value
                c += 1

            first = False
            pass
        else:
            day = {}
            c=0
            first = True
            for td in tbody.findAll("td"):
                if first:
                    if not td.a:
                        parse_error = True
                        break

                    if columns[c]['name'] in result:
                        y = result[columns[c]['name']]
                    else:
                        y = result[columns[c]['name']] = {}
                    if columns[c]['subname'] in y:
                        m = y[columns[c]['subname']]
                    else:
                        m = y[columns[c]['subname']] = {}
                    m[td.a.contents[0]] = day
                    first = False

                if columns[c]['name'] not in day:
                    day[columns[c]['name']] = {}

                if td.a:
                    element = td.a
                elif td.span:
                    element = td.span
                else:
                    element = td

                day[columns[c]['name']][columns[c]['subname']] = element.contents[0]
                c += 1
            if parse_error:
                break

    return result
