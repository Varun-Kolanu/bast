# BAST

## Getting Started Locally

Follow these steps to set up the project locally:

### Prerequisites

- Python
- Django (you can install it via pip install django)
- Git (for cloning the repository)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Varun-Kolanu/bast.git


2. Activate the virtual environment (optional but recommended)
 - On Windows:

   ```bash
   .\venv\Scripts\activate    

- On MacOs or Linux:

   ```bash
   source venv/Scripts/activate   

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt

4. Create a .env taking reference of .env.example and replace your database credentials

5. Apply database migrations
   ```bash
   python manage.py migrate

6. Start the development server
   ```bash
   python manage.py runserver

7. Open http://localhost:8000/ to open the local development server of the url shortener
