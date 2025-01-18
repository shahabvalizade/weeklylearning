## What is Cassandra
* NoSQL databse
* peer-to-peer architecture (There is no Master node)
* No Join / No Transaction Therefore:
  * Denormalization of data required duing design

## Install on system level
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

## running cqlsh
> cqlsh

## Basic concepts and simple test
* keyspace is like db in relational dbs
> CREATE KEYSPACE demo_keyspace
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

* using keyspace
> USE demo_keyspace;

* create table
> CREATE TABLE users (
    id UUID PRIMARY KEY,
    name TEXT,
    age INT
);

* insert data
> INSERT INTO users (id, name, age) VALUES (uuid(), 'Alice', 30);
> 
>INSERT INTO users (id, name, age) VALUES (uuid(), 'Bob', 25);
> 
>INSERT INTO users (id, name, age) VALUES (uuid(), 'Charlie', 35);

* Query data
> SELECT * FROM users;

* update data
> UPDATE users SET age = 40 WHERE id = 5cf6f4c2-b3c8-4b1b-9c74-9fbdbb6295d;

* delete data
> DELETE FROM users WHERE id = 4e1276f7-52cb-4c70-8d6b-3d708c3f0dcb;

* drop table and keyspace
> DROP TABLE users;
>
> DROP KEYSPACE demo_keyspace;
