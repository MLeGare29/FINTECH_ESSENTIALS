# MODULAR PROGRAMMING: SOFTWARE DESIGNED TO SCALE
# Software developers have to keep track of fine-grained functionality for different types of users and buisness neeeds.
# Many of these emerge over time and requre changing an existing application while it's being used, which can risk breaking the existing functionality of the software, or even taking it offline completely.
# Developers mitigate this risk through MODULAR PROGRAMMING - A software design technique in which we build programs primarily of smaller, independent parts.

# MODULAR PROGRAMMING
# Software devs have to keep track of fine grained functionality for different types of users and business needs.
# Many of these needs emerge over time.
# They often require changing an existing app while being used.
# This risks breaking existing functionality of the software or taking it offline completely.
# MODULAR PROGRAMMING is a design technique that mitigates this risk.
# MODULAR PROGRAMMING is a technique in which we built programs primarily of smaller, independent parts.
# This approach makes it easier to change a complex program.
# Because each component is self contained, you can iterate on one of them with less risk of impacting the entire program.
# The opposite of Modular Programming is MONOLITHIC PROGRAMMING. 
# In this case, the UI code, data access code, and data manipulation code exists on the same program.

# MODULAR BENEFITS:
# 1. You can reuse functions throughout the application or in others without having to retype them.
# 2. They require less maintenance. Updates are done in only one place because modules are independent.
# 3. Debugging is easier. If a problem exists in your code, you can easily find the affected code.

# CRYPTO TRACKING APP EXAMPLE - Will include the following:
# The UI
# The process of getting data
# The process of visualizing that data
# Each cryptocurrency that you track

# WHAT ARE PYTHON MODULES?
# Modular programming is a software design technique that we can use with most programming languages. In Python, you can create modules

# Links to an external site., which are files containing definitions and statements that are intended to serve a smaller, specific purpose within a larger, more complex program. We need files like this because of the way that programming languages like Python work.

# Specifically, Python uses an interpreter. This is a program that reads, or interprets, Python code and translates it into a lower-level language that the computer can understand.

# When you type python at the command line, you’re launching the interpreter in interactive mode. This means that you can type and run Python code directly at the command line. When you exit the live Python interpreter and then relaunch it, the functions and variables that you created are gone and can no longer be referenced.

# That’s why we write a program in a text editor, save it as a file, and then pass the program name to the Python interpreter. This way, we can always reinitialize the functions and variables. This is called creating a script, or scripting, and we've been doing it regularly in this course. When you run a script by typing something like python application.py, you’re telling Python to use the interpreter to run the lines of Python code that the application.py file includes.

# As projects and programs grow, we need to split our code into several files, which are called (you guessed it!) modules. This eases maintenance and helps us avoid rewriting code. This also enables a modular programming approach. The reason is that the Python modules will include groups of functions, organized by their functionality, that we’ll be able to import, use, and reuse in many places.

# IMPORTING MODULES:
# Say you want to add Dogecoin tracking to you crypto app and you want to plot the value over time
# Fortunately, you wrote that function in your crypto_viz.py module.
# You can access the function plot_value_over_time in three ways:
# 1. Import just the function at the beginning of the file.
    # If you intend to use only plot_value_over_time from crypto_viz.py module.
    # In that case, at the beginnning of the file use the function 'from crypto_viz import plot_value_over_time(dogecoin)
    # The variable dogecoin is a parameter containing the data that you'll plot.
# 2. Import the entire module:
    # This applies if you think you'll use more visualization functions from this module
    # In this case, it makes more sense to import the entire module.
    # To do this, type 'import crypto_viz' at the beginning of the file.
    # After that, call the function 'crypto_viz.plot_value_over_time(dogecoin).
# 3. Import the entire module, but give it a shortened name.
    # This is used if the preceding function call is too long for your tase
    # You can import the entire module but give it a shortened name.
    # For example: if you decide to name your module 'cv' for short you'll type the following:
    # 'import crypto_viz as cv' and then plot your Dogecoin as such:
    # 'cv.plot_value_over_time(dogecoin)'

# IMPORTING FUNCTIONS:
# Let's create a file named calculator.py

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def div_round(num1, num2):
    return num1 // num2

def exp(num1, num2):
    return num1 ** num2


