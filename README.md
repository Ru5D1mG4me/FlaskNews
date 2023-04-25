# News portal
A news site where anyone can share the news!

## Description
A news site built using the Flask microframework.

## Technologies
* Python
* Flask
* WTForms
* SQLAlchemy

## How to start
1. Clone the repository
2. Create and activate a virtualокружение
```commandline
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
```commandline
pip install -r requirements.txt
```
4. Create an .env file and specify the database connection settings and other parameters.
```commandline
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
5. Run the flask app
```commandline
flask run
```