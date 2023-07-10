import json
import time

# django.db.connection is a subclass of a PEP-249 connection
from django.db import connection
from django.db import reset_queries


def run():
    # load the JSON file

    data = json.load(
        open("/home/chris/Downloads/consolidated-pretty.json", "r")
    )

    cursor = connection.cursor()

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
            reset_queries()
