import sqlglot
import sqlglot.errors

def change_table_name(query: str, table_name: str) -> str:
    new_table = "'" + table_name + ".csv'"
    return query.replace(table_name, new_table)

def tsql_to_duckdb(query: str) -> str:
    ret = ""
    try:
        ret = sqlglot.transpile(query, read="tsql", write="duckdb", unsupported_level=sqlglot.ErrorLevel.RAISE)[0]
    except sqlglot.errors.ParseError as e:
        errors = e.errors
        for e in errors:
            ret += f"The following error, {e['description']}, occurred on line {e['line']} column {e['col']}.\n"
    except sqlglot.errors.UnsupportedError as e:
        ret = str(e)
    return ret