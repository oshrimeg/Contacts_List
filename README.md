# Project Name

A brief description of the project, what it does, and its main features.

## Table of Contents

- [Use](#use)
- [Installation](#installation)
- [Screenshots](#Screenshots)
- [License](#license)
- [Contact](#contact)


# Flask contacts

![alls](/Screenshots/viewContacts.png)

## Use

* Flask (Obvious!)
* Flask-SQLAlchemy (ORM for database)
* Flask-WTF (Generation of forms and validations)
* Faker (Generates fake data)

## installation
#### Python installation(Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
alias python=python3
alias pip=pip3
```
#### .venv creation (Optional)
```bash
python -m venv .venv
source .venv/bin/activate
```

#### Install dependencies
```bash
pip install -r requirements.txt
```


## Run

#### environment variables
This project requires the following environment variables to be set:
Create a .env file in the root of your project and add the following lines:
#### Required Variables:

 - DB_HOST: The hostname of your MySQL database. default localhost
 - DB_USER: The username for your MySQL database. default root
 - DB_PASSWORD: The password for your MySQL database. default admin
 - DB_NAME: The name of your MySQL database. default contacts_app

#### Optional Variables
 - OPENAI_API_KEY: Your OpenAI API key. Obtain this from the OpenAI API settings page.

#### Set environment variables by script (Linux optional)
```bash
export OPENAI_API_KEY=your_openai_api_key
export DB_HOST=your_database_host
export DB_USER=your_database_user
export DB_PASSWORD=your_database_password
export DB_NAME=your_database_name
```


#### For MYSQL RUN Migration
```bash
python migrate.py
```


```bash
python app.py
```

## Access the application :
application should be available at port 5032
Route examples:
- http://localhost:5032/
- http://127.0.0.1:5032/ContactPage
- http://127.0.0.1:5032/AddContact

## Screenshots
![new](/Screenshots/addContact.png)
![search](/Screenshots/search.png)

## Contact
contact Oriya-Hen from Qiryat Gat
```