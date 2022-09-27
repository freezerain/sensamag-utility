import mariadb
from rich import print


def drop_text_table(conn: mariadb.Connection):
    print("> Removing rows from textcontents and textreferences tables!")
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE textcontents; DROP TABLE textreferences;")
        conn.commit()
        print(
            f"> [bold green]Removed successfully [yellow]{cur.affected_rows}[/yellow] rows."
        )
    except mariadb.Error as exception:
        print(f"> [bold red] Error dropping tables:[/] {exception}")
