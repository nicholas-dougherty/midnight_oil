from env import host, username, password, get_db_url
import os
import pandas as pd 

# 1.) Make a function named get_titanic_data that returns the titanic data from the codeup
# data science database as a pandas data frame.

def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_db_url('titanic_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
    return df  

# 2.) Make a function named get_iris_data that returns the data from the iris_db on the codeup data 
# science database as a pandas data frame. The returned data frame should include the actual name
#  of the species in addition to the species_ids.

def get_iris_data():
    filename = "iris_df.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''
                        SELECT 
                            species_id,
                            species_name,
                            sepal_length,
                            sepal_width,
                            petal_length,
                            petal_width
                        FROM measurements
                        JOIN species USING(species_id)
                        '''
                , get_db_url('iris_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
    return df  

# 3.) Make a function named get_telco_data that returns the data from the telco_churn database in SQL.
# In your SQL, be sure to join all 4 tables together, so that the resulting dataframe contains
# all the contract, payment, and internet service options.

def get_telco_data():
    
    filename = 'telco_churn.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('''   
                        SELECT * 
                            FROM customers
                            JOIN contract_types USING(contract_type_id)
                            JOIN internet_service_types USING(internet_service_type_id)
                            JOIN payment_types USING(payment_type_id)
                        '''
                , get_db_url('telco_churn'))
    
    df.to_file(filename)
    
    return df


# 4.) Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, now it's time
# to add caching to them. To do this, edit the beginning of the function to check for the local filename of
# telco.csv, titanic.csv, or iris.csv. If they exist, use the .csv file. If the file doesn't exist, then produce the
# SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.
 # FINISHED. 
