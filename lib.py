
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

# Load books
books = []
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        for line in f:
            if line.strip():
                books.append(json.loads(line.strip()))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        book = {"title": title, "author": author}
        books.append(book)

        with open("data.json", "a") as f:
            f.write(json.dumps(book) + "\n")

        return redirect('/books')
    return render_template("add.html")

@app.route('/books')
def view_books():
    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
