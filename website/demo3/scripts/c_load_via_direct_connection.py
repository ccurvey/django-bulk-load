"""
load the table in the most traditional way -- by getting your own connection
(rather than the Django-provided one) and using that

Pro:
+ Surprisingly faster than the Django connection

Con:
- you need to write your own SQL
- you lose all the ORM goodness like inheritance and type checking


"""
import json
import os
import time

import psycopg2


def run():
    # load the JSON file

    data = json.load(
        open("/home/chris/Downloads/consolidated-pretty.json", "r")
    )

    direct_connection = psycopg2.connect(os.environ['DATABASE_URL'])
    cursor = direct_connection.cursor()

    start_time = time.time()

    for i, datum in enumerate(data["results"], 1):
        # rather than use TestMe.objects.create(...), we can just build the insert
        # statements ourselves
        cursor.execute(
            "insert into demo3_testme(identifier, name, source) values (%s, %s, %s)",
            (datum['id'], datum['name'], datum['source']),
        )

        alt_names = datum.get('alt_names', [])
        if alt_names:
            for alias in alt_names:
                cursor.execute(
                    "insert into demo3_testme(identifier, name, source) values (%s, %s, %s)",
                    (datum['id'], alias, datum['source']),
                )

        if (i % 100) == 0:
            print(
                f"{round(time.time() - start_time, 2)}: processed {i} rows"
            )
