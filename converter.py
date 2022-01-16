import csv
import json
from venv import main

csvFilePath = 'original.csv'
jsonFilePath = 'result.json'
yamlFilePath = 'result.yaml'


# json
def csv2json():
    data = {}
    with open(csvFilePath) as csvFile:
        csv_reader = csv.DictReader(csvFile)
        for rows in csv_reader:
            id = int(rows['id'])
            data[id] = rows

    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


# yaml
def csv2yaml():
    with open(csvFilePath) as csvFile:
        csv_reader = csv.reader(csvFile)
        data_headings = []

        # clearing file before appending to it
        open(yamlFilePath, 'w')
        for row_index, row in enumerate(csv_reader):
            if row_index == 0:
                data_headings = row
            else:
                new_yaml = open(yamlFilePath, 'a')
                yaml_text = ""
                for cell_index, cell in enumerate(row):
                    line_separator = "    "
                    cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")

                    cell_text = line_separator + cell_heading + " : " + cell.replace("\n", ", ") + "\n"
                    yaml_text += cell_text
                new_yaml.write(yaml_text + '\n')


def main():
    csv2json()
    csv2yaml()


if __name__ == '__main__':
    main()
