from sql.util import change_table_name, tsql_to_duckdb

sql1 = "SELECT cost FROM potions WHERE cost < 50;"
sql2 = change_table_name(sql1, "potions")
print(sql2)
sql3 = tsql_to_duckdb(sql1)
print(sql3)
sql4 = change_table_name(sql3, "potions")
print(sql4)