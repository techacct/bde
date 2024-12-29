import happybase

# See: https://happybase.readthedocs.io/en/latest/user.html
# for more Happybase examples

# Tables can be created from within Happybase. It is often more
# convenient to use the HBase shell to create tables.
# The following will create the table used in the happybase_write.py
# example. It only needs to be run one time. If table already exists
# it will return an error.

connection = happybase.Connection(host='localhost', port=9090, autoconnect=True)
connection.open()

connection.create_table(
    'weather',
    {'temp':dict(),
      'wind':dict(),
      'precip':dict()
     }
)
print(connection.tables())
