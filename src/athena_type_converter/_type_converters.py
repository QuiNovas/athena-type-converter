from binascii import a2b_hex
from datetime import datetime
from decimal import Decimal
from distutils.util import strtobool
from json import loads as jsonloads


TYPE_CONVERTERS = {
  'boolean': lambda x: bool(strtobool(x)) if x else None,
  'tinyint': lambda x: int(x) if x else None,
  'smallint': lambda x: int(x) if x else None,
  'integer': lambda x: int(x) if x else None,
  'bigint': lambda x: int(x) if x else None,
  'float': lambda x: float(x) if x else None,
  'real': lambda x: float(x) if x else None,
  'double': lambda x: float(x) if x else None,
  'char': lambda x: x,
  'varchar': lambda x: x,
  'string': lambda x: x,
  'timestamp': lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f').isoformat() if x else None,
  'date': lambda x: datetime.strptime(x, '%Y-%m-%d').date().isoformat() if x else None,
  'time': lambda x: datetime.strptime(x, '%H:%M:%S.%f').time().isoformat() if x else None,
  'varbinary': lambda x: a2b_hex(''.join(x.split(' '))) if x else None,
  'array': lambda x: x,
  'map': lambda x: x,
  'row': lambda x: x,
  'decimal': lambda x: Decimal(x) if x else None,
  'json': lambda x: jsonloads(x) if x else None,
}
