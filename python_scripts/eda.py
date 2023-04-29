import plotly
import plotly.figure_factory as ff 
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import mysql.connector
import pandas as pd

def config():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': 8889,
        'database': 'universities_database',
        'raise_on_warnings': True
    }

    universities_database = mysql.connector.connect(**config)
    return universities_database


def get_db_overview():
    overview = {"Total Users" : -1, 
                "Total Tables": -1,
                "Total Records": -1,
                "Average Rating": -1,
                "Total Colleges" : -1}

    universities_database = config()
    
    # get the user count
    cursor = universities_database.cursor(dictionary=True)
    query = """
        select count(1) as cnt from user_details
    """
    cursor.execute(query)
    user_count = cursor.fetchall()[0]["cnt"]
    overview["Total Users"] = user_count

    # get the total tables
    cursor = universities_database.cursor(dictionary=True)
    query = """
        SELECT count(*) as cnt
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE' and TABLE_SCHEMA = "universities_database"
    """

    cursor.execute(query)
    table_count = cursor.fetchall()[0]["cnt"]
    overview["Total Tables"] = table_count

    # get the average rating of the colleges
    cursor = universities_database.cursor(dictionary=True)
    query = """
        SELECT AVG(rating) as cnt
        FROM indian_colleges
        WHERE rating > 0
    """

    cursor.execute(query)
    average_rating = "{:.3f}".format(cursor.fetchall()[0]["cnt"]) 
    overview["Average Rating"] = average_rating

    # get the count of the colleges
    cursor = universities_database.cursor(dictionary=True)
    query = """
        SELECT count(1) as cnt
        FROM indian_colleges
    """

    cursor.execute(query)
    college_count = cursor.fetchall()[0]["cnt"]
    overview["Total Colleges"] = college_count

    # get the total number of records present in schema
    cursor = universities_database.cursor(dictionary=True)
    query = """
        SELECT SUM(TABLE_ROWS) as cnt
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = 'universities_database';
    """

    cursor.execute(query)
    total_records = cursor.fetchall()[0]["cnt"]
    overview["Total Records"] = total_records

    return overview

def get_gender_pie_chart():
    universities_database = config()
    cursor = universities_database.cursor(dictionary=True)
    query = """
        select gender, count(1) as cnt
        from indian_colleges join genders on indian_colleges.gender_id = genders.gender_id
        group by gender
    """

    cursor.execute(query)
    result = cursor.fetchall()
    gender_dataframe = pd.DataFrame(result)[:-1]

    pio.templates.default = "plotly_white"
    gender_dataframe.sort_values('cnt', inplace=True, ascending=False)
    fig = go.Figure(data=[
        go.Pie(labels=gender_dataframe["gender"], values=gender_dataframe["cnt"], textinfo="label+percent", pull=[0.1, 0, 0], rotation=45)
    ])

    return plotly.offline.plot(fig, output_type='div')

def facilities_count_plot():
    universities_database = config()

    # getting all the facility id from university database
    facilities_dict = {}
    cursor = universities_database.cursor(dictionary=True)
    query = """
        select facilities from indian_colleges
    """
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        facility_list = row['facilities'].split(",")

        for facility_id in facility_list:
            if facility_id in facilities_dict.keys():
                facilities_dict[facility_id] += 1
            else:
                facilities_dict[facility_id] = 1

    facilities_dict.pop("", None)
    values = list(facilities_dict.values())

    cursor = universities_database.cursor(dictionary=True)
    query = """
        select * from facilities 
    """
    cursor.execute(query)
    result = cursor.fetchall()

    facilities_id_name_dict = {}
    for row in result:
        facilities_id_name_dict[row["facility_id"]] = row["facility"]

    keys = list(facilities_id_name_dict.values())
    final_facilities_dict = {keys[i]: values[i] for i in range(len(keys))}

    
    final_facilities_dict = sorted(final_facilities_dict.items(), key=lambda x:x[1], reverse=True)
    
    x_list = list()
    y_list = list()
    for item in final_facilities_dict:
        x_list.append(item[0])
        y_list.append(item[1])

    pio.templates.default = "xgridoff"
    fig = go.Figure(data=[
        go.Bar(name='Facility Count', x=x_list, y=y_list)
    ])

    fig.update_layout(barmode='stack',
                      xaxis_title="Facility name",
                      yaxis_title="Count")

    return plotly.offline.plot(fig, output_type='div'), x_list

def top25_universities_college_count_plot():
    universities_database = config()

    # getting all the facility id from university database
    facilities_dict = {}
    cursor = universities_database.cursor(dictionary=True)
    query = """
        SELECT university_name, count(university_name) as cnt
        FROM indian_colleges join indian_universities on 
        indian_colleges.university_id = indian_universities.university_id
        group by university_name
        order by count(university_name) desc
        limit 16
    """
    cursor.execute(query)
    result = cursor.fetchall()

    x_list = list()
    y_list = list()

    for i in range(1, len(result)):
        x_list.append(result[i]["university_name"])
        y_list.append(result[i]["cnt"])

    pio.templates.default = "xgridoff"
    fig = go.Figure(data=[
        go.Bar(name='University Count', x=x_list, y=y_list)
    ])

    fig.update_layout(barmode='stack',
                      xaxis_title="University name",
                      yaxis_title="Count")

    return plotly.offline.plot(fig, output_type='div'), x_list


def top25_states_college_count_plot():
    universities_database = config()

    # getting all the facility id from university database
    facilities_dict = {}
    cursor = universities_database.cursor(dictionary=True)
    query = """
        SELECT state, count(state) as cnt
        FROM indian_colleges join indian_states on 
        indian_colleges.state_id = indian_states.state_id
        group by state
        order by count(state) desc 
    """
    cursor.execute(query)
    result = cursor.fetchall()

    x_list = list()
    y_list = list()

    for i in range(1, len(result)):
        x_list.append(result[i]["state"])
        y_list.append(result[i]["cnt"])
    
    print(x_list)
    print(y_list)

    pio.templates.default = "xgridoff"
    fig = go.Figure(data=[
        go.Bar(name='State Count', x=x_list, y=y_list)
    ])

    fig.update_layout(barmode='stack',
                      xaxis_title="State",
                      yaxis_title="Count")

    return plotly.offline.plot(fig, output_type='div'), x_list
