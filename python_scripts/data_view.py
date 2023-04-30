from python_scripts.eda import config
import pandas as pd

def data_view():
    universities_database = config()

    cursor = universities_database.cursor(dictionary=True)
    query = """
        select * 
        from indian_colleges join genders on indian_colleges.gender_id = genders.gender_id
        join indian_universities on indian_colleges.university_id = indian_universities.university_id
        join indian_cities on indian_colleges.city_id = indian_cities.city_id 
        join indian_states on indian_colleges.state_id = indian_states.state_id
        join country on indian_colleges.country_id = country.country_id
        join college_type on indian_colleges.college_type_id = college_type.college_type_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    return results

def add_college(college_details):
    try:
        universities_database = config()

        cursor = universities_database.cursor(dictionary=True)
        query = f"""
            insert into indian_colleges (campus_size, gender_id, total_student_enrollments, 
            total_faculty_count, established_year, rating, university_id, courses, 
            facilities, city_id, state_id, country_id, college_type_id, average_fees, college_name) 
            values ({college_details["campus_size"]}, 
            {college_details["gender"]}. 
            {college_details["total_student_enrollments"]}, 
            {college_details["total_faculty_count"]},
            {college_details["eastablished_year"]},
            {college_details["rating"]},
            {college_details["university"]},
            {college_details["courses"]},
            {college_details["facility_name"]},
            {college_details["total_faculty_count"]},
            {college_details["city"]},
            {college_details["state"]},
            {college_details["country"]},
            {college_details["college_type"]},
            {college_details["average_fees"]}
            )
        """
        cursor.execute(query)
        universities_database.commit()
    except:
       return False

    return True

def get_college_details(id):
    # get all the stuff from each tables and insert in the main table
    universities_database = config()

    cursor = universities_database.cursor(dictionary=True)
    query = f"""
        select * 
        from indian_colleges join genders on indian_colleges.gender_id = genders.gender_id
        join indian_universities on indian_colleges.university_id = indian_universities.university_id
        join indian_cities on indian_colleges.city_id = indian_cities.city_id 
        join indian_states on indian_colleges.state_id = indian_states.state_id
        join country on indian_colleges.country_id = country.country_id
        join college_type on indian_colleges.college_type_id = college_type.college_type_id
        where indian_colleges.id = {id};
    """
    cursor.execute(query)
    results = cursor.fetchall()
  
    return results[0]

def update_college_details(college_details):
    try:
        # get all the stuff from each tables and insert in the main table
        universities_database = config()

        cursor = universities_database.cursor(dictionary=True)
        query = f"""
            update indian_colleges set campus_size = {college_details["campus_size"]},
            gender_id = {college_details["gender"]},
            total_student_enrollments = {college_details["total_student_enrollments"]}, 
            total_faculty_count = {college_details["total_faculty_count"]},
            established_year =  {college_details["eastablished_year"]},
            rating = {college_details["rating"]},
            university_id = {college_details["university"]},
            courses = {college_details["courses"]},
            facilities =  {college_details["facility_name"]},
            city_id = {college_details["city"]},
            state_id = {college_details["state"]},
            country_id = {college_details["country"]},
            college_type_id = {college_details["college_type"]},
            average_fees = {college_details["average_fees"]},
            college_name = {college_details["college_name"]}        
            where id = {id}
        """
        cursor.execute(query)
        universities_database.commit()
    except:
        return False

    return True

def delete_college_details(id):
    try:
        universities_database = config()

        cursor = universities_database.cursor(dictionary=True)
        query = f"""
        delete from indian_colleges where id = {id}
        """
        cursor.execute(query)
        universities_database.commit()
        print("deleted records")
    except:
        return False
    return True
    