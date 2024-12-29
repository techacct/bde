
import sys
import os
import shutil
import time
from json import dumps
from kafka import KafkaProducer
from noaa_sdk import NOAA

topic = 'weather'
verbose = 'xyes'
# NYC zip code
zipcode = '18018'
producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092', \
                         value_serializer=lambda v: dumps(v).encode('utf-8') \
                        )

n = NOAA()
# Can use forecast, forecastHourly, forecastGridData for "type"
noaa_result = n.get_forecasts(zipcode, 'US', type='forecast')
if verbose == 'yes':
	for i in noaa_result:
		print(i)
producer.send(topic, value=noaa_result)
producer.flush()
