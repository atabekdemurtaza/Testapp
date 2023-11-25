# Installation
Clone the repository:

        git clone https://github.com/atabekdemurtaza/test.git

cd library
Create a virtual environment:

python -m venv venv
Activate the virtual environment:

On Windows:

    venv\Scripts\activate

On macOS/Linux:

    source venv/bin/activate

# Install dependencies:

    pip install -r requirements/development.txt

Run database migrations:

    python manage.py migrate

# Usage

Run the Django development server:

    python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/books/.

Open your browser or use tools like **curl** or **Postman** to interact with the API.

# API Endpoints

**GET /api/books/: Get a list of all books.**

**GET /api/books/{id}/: Get information about a specific book.**

**POST /api/books/: Create a new book.**

**PUT /api/books/{id}/: Update information about a book.**

**DELETE /api/books/{id}/: Delete a book.**