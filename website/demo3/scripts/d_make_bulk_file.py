"""
to load the resulting file, use:

$  psql demo3 -c "\copy demo3_testme (identifier, name, source) from '/home/chris/learn/demo3/website/pre_digested_file.txt'"

"""
import json
import csv


def run():
    data = json.load(
        open("/home/chris/Downloads/consolidated-pretty.json", "r")
    )

    bulk_file = open("pre_digested_file.txt", "w")

    writer = csv.writer(bulk_file, delimiter="\t", quoting=csv.QUOTE_MINIMAL)

    for i, datum in enumerate(data["results"], 1):
        writer.writerow(
            (
                datum['id'].replace("\n", ''),
                datum['name'].replace('\n', ''),
                datum['source'].replace('\n', ''),
            )
        )

        alt_names = datum.get('alt_names', [])
        if alt_names:
            for alias in alt_names:
                writer.writerow(
                    (
                        datum['id'].replace("\n", ''),
                        alias.replace("\n", ''),
                        datum['source'].replace("\n", ''),
                    )
                )
