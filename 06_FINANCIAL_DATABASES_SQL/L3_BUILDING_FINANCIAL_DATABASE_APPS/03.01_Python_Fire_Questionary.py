# INTRODUCTION TO FINANCIAL APPLICATIONS WITH DATABASES
# Previously, you learned how to access data by using APIs.
# The fact is, databases often power APIs. 
# Financial APIs are simply financial applications that use databases to store and access.
# Databases also power many financial services and applications that you encounter via webpages.
# That's because databases allow applications to efficiently access only the data that they need.
# This is perfect for those applications that need to quickly access data across the internet of a network.
# In this lesson, you'll learn how to use databases to build financial applications by integrating Python and SQL.
# You'll explore two types of applications that can use databases: Command Line Interfaces (CLIs) and web applications.
# Finally, you'll be able to create sophisticated financial applications that can access data from almost any relational database.

# SET UP THE CLI APPLICATION WITH PYTHON FIRE AND QUESTIONARY
# First we'll use Python and SQL to create a simple CLI application that can access a database.
# CLIs can prove useful when we try to rapidly build a prototype of an application.
# They also prove useful when we create internal tools that an individual or team might use to access a company database.
# Because not everyone has the same Python and SQL skills, a CLI offers a friendlier database interface for non-SQL programmers.

# Import the dependencies
import pandas as pd
import sqlalchemy
import numpy as np
import fire
import questionary

# IMPORT PYTHON FIRE
# Previously, we used the Python Fire library to add a CLI to Python functions.

# IMPORTANT
# To integrate our CLI with SQL, we use a Python file and VSCode.
# To run a Python file that we build from within Visual Studio Code, we do so in the terminal.
# We use the `python` command along with the name of the file - for example, `app.py`.

# With the Python Fire library, we can interact with any Python function in our code directly from the terminal.
# For example, a Python file named `app.py` stores the following code:
    # def run_crud(message='Running CRUD'):
        # print(message)
    # if _name_ == '_main_':
        # fire.Fire(run_crud)
        
        
# ADD QUESTIONARY TO THE CLI
# To make our CLI application interactive and polished, we'll use the Questionary library to prompt the user for inputs and selection responses.
# Later, we'll use Questionary as the main interface for our database.
# Questionary provides a wide range of custom prompts that we can use to add interactivity to an application.
# The following is an example of code that prompts the user for text input:
# import questionary
# table_name = questionary.text('What is the name of the database table that you would like to create?').ask()
# print(table_name)

# PERFORMING CRUD OPERATIONS DATABASE APPLICATION
# Almost every applicaation that uses databases accesses or stores data by using CRUD operations.
# We can make these operations easier to use by supplying a CLI that uses Python Fire and Questionary.
# This will simplify some of the SQL complexity for users who don't have a SQL background.
# Let's start examining how the create operation integrates with Python Fire and Questionary.

# CREATE TABLES VIA THE CLI
# We can create our database tables in two ways.
# The first way uses raw SQL statements to create the tables and insert the values, like we did in Lesson 1.
# However, because we want to built a Python application, we can use the second way: Have Pandas create and insert the tables for us.
# First we'll create our database engine and load test data:
database_connection_string = 'sqlite:///'

# Create an engine to interact with the database:
engine = sqlalchemy.create_engine(database_connection_string)

# Create a test DataFrame:
stocks_dataframe = pd.DataFrame({'AAPL': [1,2], 'GOOG': [3,4]})

# Now we only need to create a function that wraps, or ABSTRACTS AWAY, our code to create a table.

# IMPORTANT:
# 'Abstract Away' is a term that you'll often find in computer science.
# It means to hide the details of houw something works to simplify things conceptually.
# In this case, we'll hide our code inside a function, which we'll name `create_table`, to simplify the experience of the application user.
# When the user interacts with the application, that interaction will call `create_table` - automatically createing the table.
# The user won't need to do anything to create it.

# Here's the code to create our function:
def create_table(engine, table_name, table_data_df):
    table_data_df.to_sql(table_name, engine, index=False, if_exists='replace')
# By abstracting away the `create_table` operation, we can dynamically create tables from the CLI by using Python Fire Questionary.
# Now that we've written the code to create a table, we'll add a function to confirm the createion of the table:
def confirm_tables(engine):
    tables = engine.table_names()
    print(f'The tables in the database ar: {tables}.')
    
# Finally, we'll incorporate our CLI into this code:
def run():
    """The main function for running the application."""
    
    # Prompt the user for the table name:
    table_name = questionary.text('What name would you like us to use for your table?').ask()
    
    # Create the table in the database:
    create_table(engine, table_name, stocks_dataframe)
    
    # Confirm the table in the database:
    confirm_tables(engine)
    
if __name__ == '__main__':
    fire.Fire(run)
    
# Now, let's confirm that our function created that table and that the table exists in the database.
# Then, we'll run the application to make sure that it works as intended.
# We can test all this by running the application in the terminal.
# We need to make one final imporvement. 
# We used a test DataFrame, but we want our application to be dynamic.
# So, we can use Questionary to prompt the user for a CSV file for the DataFrame:
def run():
    """The main function for running the application."""
    
    # Dynamically load data into a DataFrame:
    csv_name = questionary.text('What is the name of your CSV file?').ask()
    csvpath = Path(csv_name)
    stocks_dataframe = pd.read_csv(csvpath)
    
    # Prompt the user for the table name:
    table_name = questionary.text('What name would you like us to use for your table?').ask()
    
    # Create the table in the database:
    create_table(engine, table_name, stocks_dataframe)
    
    # Confirm the table in the database:
    confirm_tables(engine)
    
if __name__ == '__main__':
    fire.Fire(run)

# READ TABLES VIA CLI
# We can read tables in various ways, we'll start with an example that uses the `read_sql_table` function first:
def read_table(engine, table_name):
    return pd.read_sql_table(table_name, con=engine)

# Next we'll add a prompt in our CLI to ask for the name of the table to read:
def run():
    """The main function for running the application."""
    
    table_name = questionary.text('What table would you like to display?').ask()
    table_dataframe = read_table(engine, table_name)
    print(table_dataframe)
    
if __name__ == "__main__":
    fire.Fire(run)
    
# To test this new code, we can use a file named `stocks.csv` that contains the same information as the `stocks_dataframe` that we created earlier.
# When we run the application in our terminal, the following steps should occur:
    # 1. A prompt asks for the name of the CSV file.
    # 2. A prompt asks for the name of the new database table.
    # 3. A list of the table names displays, confirming the table creation.
    # 4. A prompt asks for the table for which to displlay the table contents.
    # 5. The contents of the table display.
# Notice that the applicatino reads the entire table into a DataFrame.
# However, we know from experience that this doesn't offer the most efficient way to query a database.
# Specifically, we might receive more data than we need.
# To remedy this situation, we can use custom queries.

# CREATE CUSTOM QUERIES FOR CRUD OPERATIONS
# To create custom queries that support CRUD operations, two main options exist:
    # 1. Create distinct functions that incorporate a custom query as a multiline string in a function.
    # 2. Use f-strings to built the query string.
# You might find that you need a combination of these options to supply a robust CLI interface for non-SQL programmers.
# Suppose that we want to read a table, sort the results, and then limit the results to the top n values in the sorted list.
# We can create a custom read function for this query named `read_top_n`:
def read_top_n(engine, table_name, number_results=1):
    top_n_query = """
    SELECT * FROM {table_name}
    ORDER BY AAPL DESC
    LIMIT {number_results};
    """
    
    return pd.read_sql_query(top_n_query, con=engine)

# We then call the `read_top_n` function from the CLI:
def run():
    """The main function for running this application."""
    
    top_n_results = read_top_n(engine, 'stocks', 1)
    print('The top 1 result was: ', top_n_results)
    
if __name__ == '__main__':
    fire.Fire(run)
    
# BREAKDOWN:
# Once `stocks_csv` has been saved as a table called `stocks` to our database, the `read_top_n` function returns the first row of data, which is sorted in descending order based on the values contained in the 'AAPL' column.
# The result in the row containing the data '2' for 'AAPL' and '4' for GOOG.
# The benefit to writing custom code like this is that it abstracts away the SQL code.
# This both simplifies the SQL code and allows us to use the CLI to interact with the database.
# In this case, users can get the top n results without having to write any SQL code themselves.
# This enhances the usability of the application, because it offers a simple interface that doesn't require the user to know an entire programming language like SQL.