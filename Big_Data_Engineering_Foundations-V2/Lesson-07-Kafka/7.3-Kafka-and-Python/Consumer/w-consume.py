import io
import json
from kafka import KafkaConsumer
import numpy as np
import pandas as pd
from IPython.display import display
import datetime

topic = "weather"
verbose= "xyes"

# Create the Kafka consumer. Note, the consume is set to read "new" data, i.e. consume
# data as it arrives. If you change auto_offset_reset='latest' to "earliest" and 
# and the consumer will start at the beginning.

consumer = KafkaConsumer(topic,bootstrap_servers='0.0.0.0:9092', \
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')), \
                         auto_offset_reset='latest')

print ("Waiting for weather message")

# Start loop here. At this point data my be placed in a database or 
# otherwise processed.
# In this case, the JSON data are placed in a Pandas dataframe
# Also, we divide message.timestamp by 1000 to remove milliseconds

for message in consumer:
	time=datetime.datetime.fromtimestamp(message.timestamp/1000.0)
	df=pd.DataFrame(message.value)
        # print the data if verbose is selected
	if verbose == 'yes':
		print("RAW Message:\n", message)
		print ("\nOffset=%d:%s:" % (message.offset, time))
		display(df)
	print("Current weather(%s): %s degrees and %s"% (time.strftime('%H:%M:%S'),df.loc[0,'temperature'],df.loc[0,'shortForecast']))
	print ("Waiting for weather message")		
