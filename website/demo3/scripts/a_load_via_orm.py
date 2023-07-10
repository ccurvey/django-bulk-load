"""
loads the test table using the ORM to translate from Python to SQL

Pros:
+ Easy to read
+ Stays in one language (Python)

Cons:
- Slow
- Very Slow
"""
import json
import time

from django.db import reset_queries

from demo3.models import TestMe


def run():
    # load the JSON file
    data = json.load(
        open("/home/chris/Downloads/consolidated-pretty.json", "r")
    )

    start_time = time.time()

    for i, datum in enumerate(data["results"], 1):
        # store the "official" name
        TestMe.objects.create(
            identifier=datum['id'],
            name=datum['name'],
            source=datum['source'],
        )

        # store the aliases
        alt_names = datum.get('alt_names', [])
        if alt_names:
            for alias in alt_names:
                TestMe.objects.create(
                    identifier=datum['id'],
                    name=alias,
                    source=datum['source'],
                )

        if (i % 100) == 0:
            print(
                f"{round(time.time() - start_time, 2)}: processed {i} rows"
            )

            # PROTIP FOR DJANGO: be sure to call reset_queries() occasionally to
            # prevent debugging memory leaks when DEBUG=True
            reset_queries()

    print("--- %s seconds ---" % (time.time() - start_time))
