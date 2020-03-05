from athena_type_converter._type_converters import TYPE_CONVERTERS


def map_meta_data(result_meta_data):
  mapped_meta_data = []
  for column in result_meta_data['ColumnInfo']:
      mapped_meta_data.append((column['Name'], TYPE_CONVERTERS[column['Type']]))
  return mapped_meta_data
