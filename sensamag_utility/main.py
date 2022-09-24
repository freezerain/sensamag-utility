from typer import Typer

from sensamag_utility import language
from sensamag_utility.connection_manager import ConnectionManager

app = Typer(no_args_is_help=True)
connection_manager = ConnectionManager()


@app.command()
def connect(
    user: str = None,
    password: str = None,
    host: str = None,
    port: int = None,
    database: str = None,
    reset: bool = False,
):
    if reset:
        connection_manager.reset_connection()
    connection_manager.set_connection(user, password, host, port, database)


@app.command()
def addlang(name: str):
    print(f"Hello {name}")


@app.command()
def removelang(name: str):
    print(f"Goodbye {name}")


@app.command()
def listlang():
    language.list_languages(connection_manager.get_connection())
