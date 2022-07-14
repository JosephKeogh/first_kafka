# first_kafka

Following tutorial located at: https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

## download and setup files

###
download the zookeeper and kafka zip files and unzip completely
I stored mine at 
C:/tools/zookeeper-3.7.1 
and 
C:/tools/kafka

###
copy c/tools/zookeeper-3.7.1/conf/sample_zoo.cfg and rename to zoo.cfg in same location

###
Open file c/tools/zookeeper-3.7.1/conf/zoo.cfg 
Change "dataDir=" to  "dataDir=C:/tools/zookeeper-3.7.1/data"

###
open file C:/tools/kafka/config/server.properties
change "log.dirs=" to "log.dirs=C:/tools/kafka/kafka-logs"

###
open file C:/tools/kafka/config/zookeeper.properties
change "log.dirs=" to "log.dirs=C:/tools/kafka/zookeeper-data"

###
add the bottom to your system env variables
ZOOKEEPER_HOME: C:/tools/kafka/zookeeper-data
and add %ZOOKEEPER_HOME%\bin to your system path

## run initial commands
cd into c/tools/kafka
run:
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

open a new terminal

cd into c\tools\kafka
run:
.\bin\windows\kafka-server-start.bat .\config\server.properties

## start new topic
open a new terminal
cd into c/tools/kafka/bin/windows
run:
kafka-topics --create --topic numtest --bootstrat-server localhost:9092

you can close this terminal when the command has run

## Test everything is working
open two terminals and cd into c/tools/kafka/bin/windows

run:
kafka-console-producer --broker-list localhost:9092 --topic numtest
and
kafka-console-consumer --broker-list localhost:9092 --topic numtest

this is a basic messaging application, what you type (and then hit enter to send) in the producer terminal, will show up in the consumer terminal

## pip installs
pip install kafka-python

## Running code

### Basics
Make sure both your zookeeper and kafka are running (commands up above)

open two terminals for your coding directory

run the producer file in one terminal, you will see the data being printed out {'number': 0} etc

run the consumer file in the second terminal, you will see the data being 'processed'

### Extra fun
After doing the above 'Basics' start a new terminal and run the producer again, you will see a new data set being outputted. You will then also see the consumer processing this secondary dataset.

You can finally start a fourth terminal and run the consumer file again to see the two sets of data being processed by two consumers


