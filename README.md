# Pixels json to csv

Tool that converts the exported pixels of [Pixels v4.3.2](https://teovogel.me/pixels/)
to a simplified csv file

# Getting started

```
$ git clone https://github.com/LuukHenk/pixels_json_to_csv
$ cd pixels_json_to_csv
$ pip install .
```

Now you can use the 'pixels_json_to_csv' function in the pixels_json_to_csv.py file

```
# Python3 example

from pixels_json_to_csv.pixels_json_to_csv import pixels_json_to_csv

pixels_json_to_csv(json_file_path="json/file/path.json", csv_file_path="csv/file/path.csv")
```