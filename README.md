

Bookstore Management System
The Bookstore Management System is a RESTful API built using Flask, SQLAlchemy, and Flask-Migrate. It provides functionalities for managing book information, including adding, retrieving, updating, and deleting book details.

Installation
Ensure you have Python installed on your system.
Install dependencies using pip install -r requirements.txt.
Set up a PostgreSQL database named bookstore.
Run the Flask application using python app.py.
Usage
Use tools like cURL, Postman, or Python requests to interact with the API endpoints.
Certain endpoints require basic authentication (Username: admin, Password: password).
Endpoints
Adding a New Book: POST /books
Retrieving All Books: GET /books
Retrieving a Specific Book: GET /books/{isbn}
Updating Book Details: PUT /books/{isbn}
Deleting a Book: DELETE /books/{isbn}
Testing
Navigate to the unit_testcases directory.
Run unit tests using python -m unittest discover -s . -p 'testing.py'.
Troubleshooting
If you encounter any issues or have questions, please refer to the troubleshooting section in the documentation or reach out to our team.
