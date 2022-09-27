from enum import Enum

from rich import print
from rich.table import Table


class CSVSchema(Enum):
    REFERENCE_NAME = "Reference"
    CONTENT_TEXT = "Content"
    LANGUAGE_NAME = "Language"
    REFERENCE_ID = "ReferenceId"
    CONTENT_ID = "ContentId"
    LANGUAGE_ID = "LanguageId"

    @staticmethod
    def print_schema():
        table = Table("Field", "CSV Column", title="CSV Schema")
        for field in CSVSchema:
            table.add_row(field.name, field.value)

        print(table)
