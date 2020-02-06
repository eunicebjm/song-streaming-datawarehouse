# Building a Data Warehouse and ETL Pipeline for a Music Streaming App

Creates tables in a Postgres database to enable optimized queries for analyses of a song plays for a music streaming app. 

Data from this music streaming app currently resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. 

The ETL pipeline created will migrate the collected data to the Postgres database.

## Deployment

```
create_tables.py
```
Drops and creates the following tables in a Postgres database: 
* songplay (Fact Table)
* user (Dimension Table)
* song (Dimension Table)
* artist (Dimension Table)
* time (Dimension Table)

You run this file to reset your tables before each time you run your ETL script.


```
etl.py
```
Reads and processes JSON logs of user activity and song metadata, loads the data into the tables created above.

## Other Files

```
sql_queries.py
```
Contains all the sql queries, and is imported into the deployment files above.

```
*.ipnyb 
```
Exploratory and planning stage files which can be ignored during the Postgres database and ETL pipeline deployment.

Description of Jupyter Notebooks:

* `data_exploration.ipnyb` explores the JSON data collected from Sparkify.
* `test.ipnyb` displays the first few rows of each table to let you check your database.


## Authors

**Eunice Boon** - [eunicebjm](https://github.com/eunicebjm)