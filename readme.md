## Table of contents
1. [Python and Django Installation](#python-and-django-installation)
2. [Creating a Django Project](#creating-django-project)
3. [Django Unchained](#django-unchained)

## Python and Django Installation
- [Windows](#windows)
- [Linux](#linux)
- [macOS](#macos)

### Windows

1. **Python Installation**
   Download the Python installer from the official website [python.org](https://www.python.org/downloads). Run the installer and follow the instructions.

2. **Django Installation**
   Django can be installed using pip. Open your terminal and run the following command:

   ```
   pip install django
   ```

### Linux

1. **Python Installation**
   Most Linux distributions come with Python pre-installed. If not, use the package manager to install Python. For Ubuntu, you can use the following command:

   ```
   sudo apt-get install python3
   ```

2. **Django Installation**
   Django can be installed using pip. Open your terminal and run the following command:

   ```
   pip install django
   ```

### MacOS

1. **Python Installation**
   MacOS comes with Python pre-installed. If you want to install a different version, you can use Homebrew. If you don't have Homebrew installed, you can install it using the following command:

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Then, to install Python, use the following command:

   ```
   brew install python
   ```

2. **Django Installation**
   Django can be installed using pip. Open your terminal and run the following command:

   ```
   pip install django
   ```

3. **Verify Installation**
   After installing Python and Django, you can verify the installation by checking their versions. Use the following commands:

   ```
   python3 --version
   python3 -m django --version
   ```

## Creating Django Project
After installing Django, you can create a new Django project using the following command:

```
django-admin startproject myproject
```

This will create a new Django project named 'myproject'. You can replace 'myproject' with the name of your choice. The new project will be created in your current directory.

To run the server, navigate into your new project directory and run the following command:

```
python manage.py runserver
```
or
```
python3 manage.py runserver
```

This will start the Django development server. You can access your application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


# Django Unchained

This project is a result of the ["Django Unchained"](https://lu.ma/Django-unchained) workshop conducted by the ["MDC Club"](https://www.linkedin.com/company/meta-developer-circles-gitam-visakhapatnam/). To run this project on your local machine, follow the steps outlined in the "Django Project Setup" section below.

## Django Project Setup

Follow the steps below to setup the Django project that was built in the event on your local machine.

1. **Install Django**
   Django can be installed using pip. Run the following command in your terminal:

   ```
   pip install django
   ```

2. **Clone the Repository**
   Use git to clone the repository.

   ```
   git clone https://github.com/Sai-Akshit/DjangoUnchained
   ```

3. **Navigate to the Project Directory**
   Change your current directory to the project's directory.

   ```
   cd django_unchained
   ```

4. **Run the Server**
   Use Django's built-in server to run your project locally.
   ```
   python manage.py runserver
   ```

Now, you should be able to see your Django project running at `http://127.0.0.1:8000/` in your web browser.
