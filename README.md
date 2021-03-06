# [ICOM5016] DB Project
By Brian Rodríguez Badillo, Sofía O. Saavedra Vélez, & Javier O. Figueroa Ríos

This simple app uses a REST API for the backend of a database application using Flask. The Database engine is PostgreSQL. the application will manage data from a number of tables.

The application is organized in three broad layers:
1. Main - the main app module takes care to setup the routes for the REST API and calling the proper handler objects to process the request.
2. Handlers - the handler modules takes care of implementing the logic of each REST call. In this sense, a handler is a Facade for accessing a given operation on a data collection. Each object handles a particular type of request for a data collection (e.g. Parts). The handlers rely upon the Data Access Objects (DAOs) to extact data from the database. The handlers encode the responses to the client with JSON and provide the appropriate HTTP response code.
3. DAOs - the Data Access Objects (DAOs) take care of moving data in and out of the database engine by making SQL queries and wrapping the results in the objects and object list of appropriate types.

## Requirements
You need the following software installed to run this application:
1. PostgreSQL - database engine
2. Pyscopg2 - library to connect to PostgreSQL form Python
3. PgAdmin3 - app to manage the databases 
4. Flask - web bases framework to implement the REST API.

Base code completed 11/30/17 by Dr. Manuel Rodríguez Martínez.

Project in progress. Currently uses url route values, request.args and request.form for different routes.
