# What This Is

It's the sample code for a presentation comparing different methods of loading
bulk data into a Postgres database using Python -- sometimes with Django, sometimes
without

# Running the Samples

Once you create the table (in some form of Postgres), the good stuff is in
website/demo3/scripts.  You can run the scripts with

`python manage.py runscript <script-name>`

(without the .py extension).  Some of the scripts don't use any part of Django, but
I'm still using the django-extensions "runscript" command just for consistency

# Observations

* The obvious speed champion is `d_make_bulk_file` -- if you don't mind the complexity
* I'm surprised at how much faster it is to create a psycopg2 connection and use that,
  rather than using the one you get by `from django.db import connection`

# Future Research

* psycopg3 is out, and it supports prepared statements under certain conditions.
  - You can't use prepared statements with PgBouncer (maybe you could fake it with
    transactions
  - There are syntax and behavioral changes in psycopg3, but you're probably going to
    have to deal with that sooner or later
* PgBouncer might be the cheapest win ever for production-level numbers of connections
