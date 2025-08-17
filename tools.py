from typing import Dict, Tuple, List

# def create_table_sql_verbose(table_name: str, fields: Dict, foreign_keys=None) -> str:
#     field_list = []
#     for field_name, field_options in fields.items():
#         field_list.append(f'{field_name} {field_options}')

#     if foreign_keys:
#         for fk in foreign_keys:
#             field_list.append(f'FOREIGN KEY ({fk['key']}) REFERENCES {fk['ref_table']}({fk['ref_key']})')

#     fields_and_options = ', '.join(field_list)
#     return f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_and_options});'

# def create_insert_sql_verbose(table_name: str, fields) -> str:
#     field_list = [field for field in fields]
#     qmark_list = ['?' for field in fields]
#     return f'INSERT INTO {table_name} ({', '.join(field_list)}) VALUES ({', '.join(qmark_list)});'

def get_fields(schema: Dict) -> Tuple:
    return tuple([field for field in schema['fields'] if field != 'id'])

def create_table_sql(table_schema: Dict) -> str:
    field_list = []
    for field_name, field_options in table_schema['fields'].items():
        field_list.append(f'{field_name} {field_options}')

    if 'foreign_keys' in table_schema.keys():
        for fk in table_schema['foreign_keys']:
            field_list.append(f'FOREIGN KEY ({fk['key']}) REFERENCES {fk['ref_table']}({fk['ref_key']})')

    fields_and_options = ', '.join(field_list)
    return f'CREATE TABLE IF NOT EXISTS {table_schema['name']} ({fields_and_options});'

def create_insert_sql(table_schema: Dict, is_ignore: bool = True) -> str:
    field_list = [field for field in table_schema['fields'] if field != 'id']
    qmark_list = ['?' for field in table_schema['fields'] if field != 'id']
    return f'INSERT{' OR IGNORE' if is_ignore else ''} INTO {table_schema['name']} ({', '.join(field_list)}) VALUES ({', '.join(qmark_list)});'

def dataframe_to_list_of_tuples(df) -> List:
    if df.columns[0] == 'id':
        return [tuple(row) for row in df.iloc[:, 1:].values.tolist()]
    else:
        return [tuple(row) for row in df.values.tolist()]
