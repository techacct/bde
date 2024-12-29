import happybase

# Use Happybase to read data from HBase database (based on Apple-stock.csv)
# See: https://happybase.readthedocs.io/en/latest/user.html
# for more Happybase examples

# Note: data are returned as "byte strings" (e.g. b'result' in Python) 
# and are 8 bit ASCII

connection = happybase.Connection(host='localhost', port=9090, autoconnect=True)
connection.open()

print(connection.tables())
table = connection.table('apple')

# Get single row, convert to regular ASCII
# Set "date" to a date key in the database
date=b'23-May-14'
priceData=[b'price:open', b'price:close', b'price:high', b'price:low']

print("Date: %s" % date.decode('ASCII'))
data=table.row(date)
for value in priceData:
	print("  %s: %s" % (value.decode('ASCII').replace('price:',''), data.get(value).decode('ASCII')))
print("  volume: %s" % (data.get(b'volume:amount').decode('ASCII')))

# Get specific data for specific rows (and include time stamp)
dates=[b'22-Apr-15',b'1-Dec-14',b'23-May-14']
print("\nSpecific Table Rows with price:low and Time Stamp:")
rows = table.rows(dates,columns=[b'price:low'],include_timestamp=True)
for key, data in rows:
	print(key, data)

# scan for a keys using "prefix"
# collect all row keys that start with "31-"
prefix=b'31-'
print("\nScan Results (prefix=%s):" % prefix)
for key, data in table.scan(row_prefix=prefix):
	print(key, data)
