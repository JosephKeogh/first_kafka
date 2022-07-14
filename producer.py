import time
import json
from kafka import KafkaProducer

# create a kafka producer
producer = KafkaProducer(

  # the host and port that the producer should contact to dump the data
  # also known as the location of the broker
  bootstrap_servers=['localhost:9092'],

  # how the producer should serialize the data being sent to the broker
  # conver the data into json and then encode into utf-8
  value_serializer= lambda x: json.dumps(x).encode('utf-8'),
)


# sending data to the broker
for tick in range(1000):

  # the data we want to send
  data = {
    'another another number': tick,
  }

  # tell the producer to send the data
  producer.send(
    # the topic we are sending to
    'numtest',

    # the value of the key value pair we are sending
    value=data
  )

  print(data, flush=True)

  # sleep for five seconds
  time.sleep(5)




# end of file
