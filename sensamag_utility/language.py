import mariadb
from rich import print

def list_languages(conn: mariadb.Connection):
    print("> Fetching languages table")
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM localizationlanguages
    """)
    for r in cur:
        print(r)
    conn.close()