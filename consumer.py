from ensurepip import bootstrap
import json
from kafka import KafkaConsumer


# create a kafka consumer
consumer = KafkaConsumer(
  # the name of the topic
  'numtest',
  # location of the broker
  bootstrap_servers=['localhost:9092'],
  # where this consumer will look in the stream for the next data packet
  auto_offset_reset='earliest',
  # makes sure the consumer commits its read offset every interval
  enable_auto_commit=True,
  # the consumer group to which this consumer belongs
  group_id='my-group',
  # how the consumer will unpack the data it reads from the broker
  value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
  print(message.value, flush=True)





# end of file
