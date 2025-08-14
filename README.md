# Online Catering Store (Django)

This is a simple Django project that implements basic user authentication features including registration, login, logout, and account deletion. It serves as a starting point for the 2nd Year Project repeat assignment.

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the site**:
   Visit `http://127.0.0.1:8000/` in your browser. You can register, log in, and delete your account.

## Features

- **Registration**: Users can register with a username, email, and password. Successful registration logs the user in automatically.
- **Login/Logout**: Users can log in using their credentials and log out.
- **Account Deletion**: Logged-in users can delete their accounts after confirmation.

Feel free to extend this project by adding product catalogue, shopping cart, payment integration with Stripe, and other features as described in the assignment.
