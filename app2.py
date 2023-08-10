from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Define the SQLAlchemy base class
Base = declarative_base()

# Define the Book class representing the table structure
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
# Create a SQLite database in memory (you can change the connection URL to use a file-based database)
engine = create_engine('sqlite:///books.db', echo=True)

# Create the table
Base.metadata.create_all(engine)

# Flask route for the index page
# ... (previous code)

# Flask route to render the index page with existing books
@app.route('/')
def index():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    books = session.query(Book).all()
    
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    book_name = request.form.get('book_name')
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Insert the new book record
    new_book = Book(name=book_name)
    session.add(new_book)
    session.commit()
    session.close()
    
    return redirect(url_for('index'))

# Flask route to update a book
@app.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    book = session.query(Book).filter_by(id=book_id).first()
    
    if request.method == 'POST':
        new_name = request.form.get('new_name')
        book.name = new_name
        session.commit()
        return redirect(url_for('index'))
    
    return render_template('update.html', book=book)

# Flask route to delete a book
@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    book = session.query(Book).filter_by(id=book_id).first()
    
    if book:
        session.delete(book)
        session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

