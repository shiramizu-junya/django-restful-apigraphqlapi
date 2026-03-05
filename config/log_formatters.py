import logging

import sqlparse
from pygments import highlight
from pygments.formatters import TerminalTrueColorFormatter
from pygments.lexers import SqlLexer


class SqlFormatter(logging.Formatter):
    def format(self, record):
        sql = record.getMessage()
        if "SELECT" in sql or "INSERT" in sql or "UPDATE" in sql or "DELETE" in sql:
            formatted_sql = sqlparse.format(sql, reindent=True, keyword_case="upper")
            colored_sql = highlight(formatted_sql, SqlLexer(), TerminalTrueColorFormatter(style="monokai"))
            record.msg = f"\n{colored_sql}"
            record.args = None
        return super().format(record)
