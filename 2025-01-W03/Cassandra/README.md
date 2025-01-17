## Install on system level:
Steps:
> sudo apt-get install openjdk-11-jdk

> java -version

> echo "deb [signed-by=/etc/apt/keyrings/apache-cassandra.asc] https://debian.cassandra.apache.org 41x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list

> curl -o /etc/apt/keyrings/apache-cassandra.asc https://downloads.apache.org/cassandra/KEYS

> sudo apt update

> sudo apt install cassandra

## problem with python3.12
cqlsh is not working with python 3.12. I used 3.11 version.
> sudo add-apt-repository ppa:deadsnakes/ppa

> sudo apt install python3.11

> sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

## running cqlsh:
> cqlsh
