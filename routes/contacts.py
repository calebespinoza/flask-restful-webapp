from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from models.contact import Contact

contacts = Blueprint('contacts', __name__)

@contacts.route('/', methods=['GET'])
def index():
    contacts_list = Contact.query.all()
    return render_template("index.html", contacts_list = contacts_list)

@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    new_contact = Contact(fullname, email, phone)
    db.session.add(new_contact)
    db.session.commit()
    flash(f"Contact {new_contact.fullname} added successfully!")
    return redirect(url_for('contacts.index'))
    #return redirect('/')
    #return f"Add a contact... \n{fullname}\n{email}\n{phone}"

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()
        flash(f"Contact {contact.fullname} updated successfully!")
        return redirect(url_for('contacts.index'))
    return render_template("update.html", contact = contact)

@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash(f"Contact {contact.fullname} deleted successfully!")
    return redirect(url_for('contacts.index'))
    #return f"Delete a contact... {contact.fullname}"

@contacts.route('/about')
def about():
    return render_template("about.html")
