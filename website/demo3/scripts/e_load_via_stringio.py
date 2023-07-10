"""
Create a pre-formatted file for loading, but write it into a StringIO object and
use the "copy_from" command for this

Pro:
+ Suprisingly fast
+ Only one program/step
+ No intermediate file needed

Con:
- no ORM goodness
- single table only
- The bulk commands can be a bit fiddly and brittle (and they're another thing to learn)

"""
import json
import csv
import io
import time

from django.db import connection, reset_queries


def run():
    data = json.load(
        open("/home/chris/Downloads/consolidated-pretty.json", "r")
    )

    connection = psycopg2.connect(os.environ['DATABASE_URL'])
    cursor = connection.cursor()

    bulk_file = io.StringIO()
    writer = csv.writer(bulk_file, delimiter="\t", quoting=csv.QUOTE_MINIMAL)

    start_time = time.time()

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

        if (i % 1000) == 0:
            # every 100 rows, rewind the bulk file
            bulk_file.seek(0)

            # use the "copy_from" method to copy the file into the database
            cursor.copy_from(
                bulk_file,
                "demo3_testme",
                sep="\t",
                null='None',
                columns=('identifier', 'name', 'source'),
            )

            print(
                f"{round(time.time() - start_time, 2)}: processed {i} rows"
            )

            # reset everything for the next batch
            bulk_file = io.StringIO()
            writer = csv.writer(
                bulk_file, delimiter="\t", quoting=csv.QUOTE_MINIMAL
            )
            reset_queries()

    # don't forget our last few items
    bulk_file.seek(0)

    cursor.copy_from(
        bulk_file,
        "demo3_testme",
        sep="\t",
        null='None',
        columns=('identifier', 'name', 'source'),
    )
