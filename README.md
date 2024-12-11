# The Recipe Vault

The Recipe Vault is a platform for sharing recipes and articles related to food and diets. It is built with Django and PostgreSQL as the database backend.

## Features

### Permissions

#### Non-Registered Users
- Can view published articles and recipes, including attached comments and ratings.
- Can view the profile of the user who published the article or recipe.
- Attempting to edit or delete any articles, recipes, or user data will result in redirection:
  - To the details page of the respective article or recipe.
  - To the login page for user data modifications. If logged in as a different user, they will be redirected to the home page.

#### Registered Users
- Have all the permissions of non-registered users.
- Can create, update, and delete their own recipes.
- Can modify their own profiles.
- Can comment on and rate articles and recipes.

### Admin Groups

#### Staff
- Responsible for moderating user-generated content.
- Can edit or delete recipes and comments.
- Can create/edit/delete articles aswell.

#### Superusers
- Have all the permissions of staff members.
- Can edit and delete user profiles, a permission not granted to staff members.

---

## Setup Guide

### Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/StoichoManolov/my_recipes.git
```

### Step 2: Configure Environment Variables
Set up the environment variables required to run the project. A `.env.template` file is included in the repository for guidance.

1. Copy the `.env.template` file:

   ```bash
   cp .env.template .env
   ```

2. Edit the `.env` file and provide the required values:

   ```env
   SECRET_KEY=<your-secret-key>
   DEBUG=<True-or-False>
   ALLOWED_HOSTS=<your-allowed-hosts>
   DB_NAME=<your-database-name>
   DB_USER=<your-database-user>
   DB_PASSWORD=<your-database-password>
   DB_HOST=<your-database-host>
   DB_PORT=<your-database-port>
   CSRF_TRUSTED_ORIGINS=<your-csrf-trusted-origins>
   ```

### Step 3: Install Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database
Ensure PostgreSQL is running and configure the database using the credentials provided in the `.env` file.

Apply database migrations:

```bash
python manage.py migrate
```

### Step 5: Run the Development Server
Start the development server:

```bash
python manage.py runserver
```

By default, the server will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Users for testing purposes:

