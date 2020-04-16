import json
import csv
from urllib import request

gist_url='https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'

def slurp_json_from_url(json_url):
    r = request.urlopen(json_url)
    body = r.read()
    return json.loads(body)


def cities_to_csv(gist_url, csv_filename):
    json_dicts = slurp_json_from_url(gist_url)
    sorted_json_dicts = sorted(json_dicts, key=lambda j: j['rank'])
    with open(csv_filename, "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        for jdict in json_dicts:
            csv_writer.writerow([jdict['city'], jdict['state'], jdict['rank'], jdict['population']])


if __name__ == '__main__':
    cities_to_csv(gist_url, "slurpburptest.csv")
