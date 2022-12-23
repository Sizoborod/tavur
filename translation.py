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


def update(name_file):
    with open('static/js/data.json', 'r', encoding="utf-8") as cat_file:
        data_json = json.load(cat_file)['features']
        # print(data_json)
        '''for i in data_json:
            if name_file in i['properties'].values():
                print('объект уже добавлен')
                return'''
    with open(f'static/txt/{name_file}.txt', 'r', encoding="utf-8") as txt_file:
        data_file = txt_file.readlines()
        data = data_file[0][:-1]
        coord = [float(data_file[1][:-1]), float(data_file[2][:-1])]
        text = ' '.join(data_file[3:])
        # print(data, coord, text)
    text_link = f'/delete/{name_file}'
    ss = {"type": "FeatureCollection",
          "features": []}
    ff = '<table  style="border-collapse: collapse; width: 100%;"><tbody><tr><td style="width: 35%;">'
    ff += f'<img class="imageLeft" src="static/img/{name_file}.jpg" width=100% alt="Ed" /></td><td style="width: 65%;">'
    ff += f'<p align="justify">{text}</p></td></tr></tbody></table><p align="justify"></p>'
    link = f"<a  href=\"{text_link}\">Удалиь запись</a>"

    p = {"type": "Feature", "id": len(data_json),
         "geometry": {"type": "Point", "coordinates": coord},
         "properties": {"balloonContentHeader": f"<p align=\"center\">{name_file}</p>", "balloonContentBody": ff,
                        "balloonContentFooter": link, "clusterCaption": f"{name_file}",
                        "hintContent": f"{name_file}"}}
    ss['features'].extend(data_json)
    ss['features'].append(p)
    # print(ss)

    with open('static/js/data.json', 'w', encoding="utf-8") as cat_file:
        json.dump(ss, cat_file)
    print('запись успешно добавлена')

def delete(name_file):
    with open('static/js/data.json', 'r', encoding="utf-8") as cat_file:
        data_json = json.load(cat_file)['features']
        # print(len(data_json))
        del_index = False
        # for i in data_json:
            # print(i)
        for i in range(len(data_json)):
            # print(i,'  =====    ', data_json[i])
            if name_file in data_json[i]['properties'].values():
                del_index = i
    if del_index:
        del data_json[del_index]
        ss = {"type": "FeatureCollection",
              "features": []}
        ss['features'].extend(data_json)

        # print(ss)

        with open('static/js/data.json', 'w', encoding="utf-8") as cat_file:
            json.dump(ss, cat_file)
        print('запись успешно удалена')
    else:
        print('запись не найдена')




