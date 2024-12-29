import happybase

# Use Happybase to write to simple HBase weather database.
# See: https://happybase.readthedocs.io/en/latest/user.html
# for more Happybase examples

# Use Happybase to write data to existing table.
connection = happybase.Connection(host='localhost', port=9090, autoconnect=True)
connection.open()

# See happybase_create.py for table creation (or use "hbase shell")

print("Current HBase Tables:")
print(connection.tables())
date='23-May-14'

# Note: the family "members" (temp:low, temp:high; wind:low, wind:high)
# do not need to be specified when the table is created. They can
# be added at any time using the put method.

table = connection.table('weather')
table.put(date,{'temp:low':'10'}) 
table.put(date,{'temp:high':'30'}) 
table.put(date,{'wind:low':'2'}) 
table.put(date,{'wind:high':'6'}) 
table.put(date,{'precip:amount':'0'}) 

print("\nNew Row for %s:" % date)
print(table.row(date))
