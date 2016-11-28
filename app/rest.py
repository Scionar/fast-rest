# rest.py
# Pycnic REST service.

from pycnic.core import WSGI, Handler
import psycopg2

db_cred = {
    'host': '127.0.0.1',
    'name': 'fast-rest',
    'user': 'scionar'
}

# Helper functions for output
def dbSelect(query):
    conn = psycopg2.connect(host=db_cred['host'], database=db_cred['name'], user=db_cred['user'])
    cur = conn.cursor()
    cur.execute(query)
    db_result = cur.fetchall()
    cur.close()
    conn.close()
    return db_result


class Root(Handler):
    def get(self, name="Root"):
        return {
            "lines" : dbSelect("SELECT * FROM test;")
        }

class app(WSGI):
    routes = [
        ('/', Root()),
        ('/([\w]+)', Root())
    ]
