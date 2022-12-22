import sys
import csv
import json


def up():
    s = 'people.csv'
    # print(s)
    ss = {"type": "FeatureCollection",
          "features": []}
    with open(s, encoding="utf8") as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))[1:]
        for i in reader:
            coord = list(map(float, i[5].split(', ')))
            # print(coord)

            ff = '<table  style="border-collapse: collapse; width: 100%;"><tbody><tr><td style="width: 35%;">'
            ff += f'<img class="imageLeft" src="static/img/{i[4]}" width=100% alt="Ed" /></td><td style="width: 65%;">'
            ff += f'<p align="justify">{i[2]}</p></td></tr></tbody></table><p align="justify">{i[3]}</p>'
            link = f"<a  href=\"{i[6]}\">Ссылка</a>" if i[6] else ''

            p = {"type": "Feature", "id": int(i[0]),
                 "geometry": {"type": "Point", "coordinates": coord},
                 "properties": {"balloonContentHeader": f"<p align=\"center\">{i[1]}</p>", "balloonContentBody": ff,
                                "balloonContentFooter": link, "clusterCaption": f"{i[1]}",
                                "hintContent": f"{i[1]}"}}
            # print(p)
            ss['features'].append(p)
    # print(ss)

    with open('static/js/data.json', 'w', encoding="utf-8") as cat_file:
        json.dump(ss, cat_file)


up()