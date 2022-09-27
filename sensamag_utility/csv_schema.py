from enum import Enum

from rich.table import Table
from rich import print


class CSVSchema(Enum):
    REFERENCE_NAME = "Reference"
    CONTENT_NAME = "Content"
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
