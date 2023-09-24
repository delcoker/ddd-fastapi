# Flask DDD
Flask DDD is boilerplate for DDD with flask.


## Project Structure
- `app.py`: Main application entry point.
- `config.py`: Configuration settings for the application.
- `container.py`: Dependency injection/IoC container for the application.
- `mypy.ini`: Configuration settings for `mypy` type checking.
- `src`: The main source directory containing application logic.
- `tests`: Directory containing unit and integration tests.


## Library Defaults
pip install Flask Flask-Injector Flask-SQLAlchemy mysqlclient

- `pipreqs`: For managing project dependencies.
- `Flask-Injector`: For dependency injection.
- `mypy`: For type checking.
- `Flask`: flask.
- `Flask-SQLAlchemy`: ORM.
- `mysqlclient`: mysql.


## Getting Started
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create a database with you config variables. 
4. Create a table called: `user`
   - columns: id, username, email
   - insert some data


## Testing
To run tests, execute the following:


## DDD-oriented microservice
https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice


### Note
For hierarchical DI you can include the modules in each layer.
