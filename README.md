# Edenthought Django Web App
*No longer online*
Edenthought
Application Screenshot

Table of Contents
Description
Features
Demo
Installation
Usage
Configuration
Contributing
License
Description
Edenthought is a web application built using Django, designed to allow users to register with email confirmation and manage their thoughts. It provides full CRUD (Create, Read, Update, Delete) functionality for users' thoughts and offers a user-friendly interface for organizing and accessing their ideas.

Features
User Registration and Email Confirmation.
User Authentication and Authorization.
Create, Read, Update, and Delete (CRUD) operations for managing thoughts.
Hosted PostgreSQL database on AWS for user and thought data models.
Static files, including profile pictures, hosted on AWS S3 buckets.
Responsive design using Bootstrap for a seamless user experience.
Demo
You can access a live demo of Edenthought at Demo Link.

Installation
To run Edenthought locally, follow these steps:

Clone this repository to your local machine using Git:

bash
Copy code
git clone https://github.com/yourusername/edenthought.git
Navigate to the project directory:

bash
Copy code
cd edenthought
Install the required Python packages:

Copy code
pip install -r requirements.txt
Create a .env file and configure the following settings:

SECRET_KEY: Django secret key.
DEBUG: Set to True for development, False for production.
DATABASE_URL: PostgreSQL database connection URL.
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY: AWS S3 credentials.
Other project-specific settings.
Apply migrations:

Copy code
python manage.py migrate
Create a superuser for administrative access:

Copy code
python manage.py createsuperuser
Start the development server:

Copy code
python manage.py runserver
Access the application at http://localhost:8000/.

Usage
Register an account using your email. An email confirmation link will be sent.
Log in with your registered credentials.
Create, read, update, or delete your thoughts as needed.
Customize your profile and upload a profile picture.
Enjoy organizing and managing your thoughts effortlessly!
Configuration
Edenthought relies on several external services and configurations, including:

PostgreSQL Database: The application uses PostgreSQL to store user and thought data. Ensure your database is properly configured and connected in the .env file.

AWS S3: Profile pictures and other static files are hosted on AWS S3 buckets. Provide your AWS credentials in the .env file.

Django Settings: Customize Django settings in the settings.py file as per your requirements.

Contributing
Contributions to Edenthought are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear messages.
Push your changes to your fork.
Submit a pull request to the main repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.
