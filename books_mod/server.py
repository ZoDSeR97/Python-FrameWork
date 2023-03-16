from app import app
from app.controllers import authors, books

if __name__ == "__main__":
    app.run(debug=True)