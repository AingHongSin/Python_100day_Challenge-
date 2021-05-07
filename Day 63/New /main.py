from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()



@app.route('/')
def home():
    print(url_for('home') )

    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template("index.html", data=all_books)


@app.route("/add",methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book\
            (title=request.form['title'],
             author=request.form['author'],
             rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return home()
    return render_template("add.html")

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        print(book_to_update)
        book_to_update.rating = request.form['new_rating']
        db.session.commit()
        return home()
    book_id = request.args.get('id')
    book_selection = Book.query.get(book_id)
    return render_template("edit.html", book=book_selection)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_for_delete = Book.query.get(book_id)
    db.session.delete(book_for_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)



































####################################################################################################################################
####################################################################################################################################





# Read all records in Database
"""
all_books = db.session.query(Books).all()
"""
# Read a Particular Record by Query
"""
book = Books.query.filter_by(title="Harry Potter").first()
"""
# Update A Particular Record By Query
"""
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()  
"""

# Update A Record By PRIMARY KEY
"""
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()  
"""

# Delete A Particular Record By PRIMARY KEY
"""
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
"""
