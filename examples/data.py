#!/usr/bin/env python
"""
@author: Mori
@contact: moridisa@moridisa.com
@file: data
@time: 2018/8/29 11:26 AM
@desc: Code By Mori
"""

from mori_utils import *

# query from db
query_mysql('mysql_db', 'SELECT * FROM test_table')  # return row as Tuple
query_mysql('mysql_db', 'SELECT test_data FROM test_table', True)  # return row as Dict

# execute on db
effect_row = execute_mysql('mysql_db', 'DELETE FROM test_table WHERE test_data < 10')  # effect row
test_id = execute_mysql('mysql_db', 'INSERT INTO test_table VALUE (20)')  # last insert id

# query on mongo
print(query_mongo('mongo_db', {}))
print(query_mongo('mongo_db', {'_id': '123'}, 'other_collection'))

# query odps
print(query_odps('odps_db', 'SELECT * FROM test'))

# get connection of mysql
with conn_mysql('mysql_db') as conn:
    cursor = conn.cursor()
    pass

# get connection of mongo
with conn_mongo('mongo_db') as conn:
    db = conn.get_database('a_db')
    db.get_collection('a_collection')

# get connection of odps
instance = conn_odps('odps')
with instance.execute_sql('SELECT * FROM test').open_reader(use_tunnel=True, limit_enabled=False) as reader:
    pass
