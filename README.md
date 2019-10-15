# Assignment 7

Utilizing Flask and HTML + CSS to develop a website for a todo list

Edit this file to complete the following information below:

* Name: Kevin Chen

## Description

Due: Tuesday, April 2nd, 2019 11:55 PM

At this point, we have a fully functioning front end and back end for our todo list application.

Now we will add a database to store our todo list data.

The front end portion (HTML/CSS/JS) and back end (python) portion is written for you. All you have to do is write the SQL queries for the database transactions.

## Connecting to the database

The host or domain of the database is `cs1122.c1icwtbkfcxn.us-east-1.rds.amazonaws.com`

The username and password for your database user is your netid.

The name of the database you will be connecting to is also your netid.

The todos table has already been created for you. The definition of the table is as follows:

```
CREATE TABLE todos (
	item TEXT
);
```


## Requirements

There are 3 queries you will need to write.

The first query will be in the home() function (aka "/" route). This query must fetch all rows of the todos table.

The second query will be in the add() function (aka "/add" route). This query must insert a row to the todos table containing the provided parameter.

The third query will be in the delete() function (aka "/delete" route). This query must delete the row that contains the value matching the provided parameter.

Your code must be in app.py. Make sure you test your code before submitting.

This is an individual assignment.
