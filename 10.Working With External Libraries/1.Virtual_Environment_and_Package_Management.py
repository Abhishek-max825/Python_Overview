'''
Virtual_Environment_and_Package_Management

Virtual Environments:
-> A virtual environment is a self-contained directory that contains its own Python
interpreter and libraries.
-> This means that libraries installed in one virtual
environment won’t interfere with libraries in another.

'''

'''
1. Creating a virtual environment (using venv - recommended):

-> python3 -m venv my_env  # Creates a virtual environment named "my_env"

2. Activating the virtual environment

a. Windows:
     -> my_env\Scripts\activate
b. macOS/Linux:
     -> source my_env/bin/activate

3.Package Management (using pip ):

-> pip is Python’s package installer.
-> It’s used to install, upgrade, and manage external libraries.     

4. Installing a package:

-> pip install requests  # Installs the "requests" library
-> pip install numpy==1.20.0 # Installs a specific version

5. Listing installed packages:

-> pip list

6. Upgrading a package:

-> pip install --upgrade requests

7. Uninstalling a package:

-> pip uninstall requests

8. Generating a requirements file:

-> A requirements.txt file lists all the packages your project depends on.
-> This makes it easy to recreate the environment on another machine.

-> pip freeze # returns the current version of modules used in project same as pip list 
-> pip freeze > requirements.txt  # Creates the requirements file
-> pip install -r requirements.txt  # Installs packages from the file

9. Deactivating the virtual environment

-> deactivate


'''

# import moviepy
# its not exist in requirements.txt so we need to install it in our env2 


