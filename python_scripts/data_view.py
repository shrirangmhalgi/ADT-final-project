from python_scripts.eda import config
import mysql.connector
import pandas as pd

def data_view():
    universities_database = config()

    cursor = universities_database.cursor(dictionary=True)
    query = """
        select * from indian_colleges
    """
    cursor.execute(query)
    results = cursor.fetchall()

    return results

def add_college(college_details):
    # get all the stuff from each tables and insert in the main table
    universities_database = config()

    cursor = universities_database.cursor(dictionary=True)
    query = f"""
        insert into _dummy values ({1})
    """
    cursor.execute(query)
    universities_database.commit()
    

    return True

def get_college_details(id):
    # get all the stuff from each tables and insert in the main table
    universities_database = config()

    cursor = universities_database.cursor(dictionary=True)
    query = f"""
        select * from indian_colleges where id = {id}
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    return results[0]

def update_college_details(college_details):
     # get all the stuff from each tables and insert in the main table
    universities_database = config()

    cursor = universities_database.cursor(dictionary=True)
    query = f"""
        update _dummy set id = 10 where id = 1
    """
    cursor.execute(query)
    universities_database.commit()
    print("college updated successfully", college_details)
    return True

def delete_college_details(id):
    universities_database = config()

    cursor = universities_database.cursor(dictionary=True)
    query = f"""
       delete from _dummy where id = 10
    """
    cursor.execute(query)
    universities_database.commit()
    print("deleted records")
    return True
    