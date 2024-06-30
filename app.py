from flask import Flask, render_template, request, redirect
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

db = mysql.connector.connect(
   host=os.getenv("DB_HOST"),
   user=os.getenv("DB_USER"),
   password=os.getenv("DB_PASSWORD"),
   database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

def get_contacts():
   cursor.execute("SELECT * FROM contacts")
   result = cursor.fetchall()
   return result

def create_contact(name, phone, email, gender, photo):
    cursor.execute("INSERT INTO contacts (name, phone, email, gender, photo) VALUES (%s, %s, %s, %s, %s)", (name, phone, email, gender, photo))
    db.commit()
    return "New contact added successfully"

def check_contact_exist(name, email):
    cursor.execute("SELECT * FROM contacts WHERE name = %s OR email = %s", (name, email))
    result = cursor.fetchone()
    return bool(result)

def delete_contact(number):
    cursor.execute("DELETE FROM contacts WHERE number = %s", (number,))
    db.commit()
    return "Contact deleted successfully"

def search_contacts(search_name):
    cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", ('%' + search_name + '%',))
    result = cursor.fetchall()
    return result


app = Flask(__name__)

@app.route('/')
def welcome():
    return redirect('/AddContact')

@app.route('/ContactPage')
def viewContacts():
    return render_template('index.html', contacts=get_contacts())

@app.route('/AddContact', methods=['GET', 'POST'])
def add_contact():
    return render_template("AddContact.html")

@app.route('/createContact', methods=['POST'])
def createContact():
    # adding additional contact to the database (contacts_list)
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']   
    gender = request.form['gender']
    photo = request.files['photo']
    if not check_contact_exist(fullname, email):
        if photo:
            # create a name for the file to be saved
            file_path = 'static/images/' + fullname + '.jpg'
            # save the file in the server
            photo.save(file_path)
        # create a new contact
        create_contact(fullname, phone, email, gender, f'{fullname}.jpg')
    else:
        return render_template('addContact.html', message='Contact already exists')
    return redirect('/ContactPage')

@app.route('/deleteContact/<int:number>')
def deleteContact(number):
    delete_contact(number)
    return redirect('/ContactPage')

@app.route('/search', methods=['POST'])
def search():
    search_name = request.form['search_name']
    search_results = search_contacts(search_name)
    return render_template('index.html', contacts=search_results)


if __name__ == "__main__":
    app.run(port=5005, debug=True)
    
