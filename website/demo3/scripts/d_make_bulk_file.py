"""
Create a pre-formatted text file and use the Postgres database utility to load it.

After creating the file, use this to load it

$  psql demo3 -c "\copy demo3_testme (identifier, name, source) from '/home/chris/learn/demo3/website/pre_digested_file.txt'"

Pros:
+ Easily the fastest execution

Cons:
- no ORM goodness
- Two steps
- The bulk commands can be a bit fiddly and brittle (and they're another thing to learn)
- You need a filesystem big enough to hold the file
- Single table only

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
