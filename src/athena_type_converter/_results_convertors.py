from athena_type_converter._meta_data import map_meta_data


def convert_row(meta_data, row):
  converted_row = {}
  for n in range(len(row)):
      converted_row[meta_data[n][0]] = meta_data[n][1](row[n].get('VarCharValue', None))
  return converted_row


def convert_rows(meta_data, rows):
  converted_rows = []
  for n in range(1, len(rows)):
    converted_rows.append(convert_row(meta_data, rows[n]['Data']))
  return converted_rows


def convert_result_set(result_set):
  return convert_rows(map_meta_data(result_set['ResultSetMetadata']), result_set['Rows'])
