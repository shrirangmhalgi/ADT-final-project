import pickle
from flask import Flask, render_template, request, redirect, url_for, flash
from python_scripts import eda
from python_scripts import data_view
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# loading all the eda graphs
# overview = eda.get_db_overview()
# gender_pie_chart = eda.get_gender_pie_chart()
# facilities_count_plot, facilities_count_list = eda.facilities_count_plot() 
# top25_universities_college_count_plot, universities_count_list = eda.top25_universities_college_count_plot()
# top25_states_college_count_plot, top25_states_college_count_plot_list = eda.top25_states_college_count_plot()

overview = None
gender_pie_chart = None
facilities_count_plot, facilities_count_list = None, None
top25_universities_college_count_plot, universities_count_list = None, None
top25_states_college_count_plot, top25_states_college_count_plot_list = None, None

with open('pickles/eda/overview.pkl','rb') as f:
    overview = pickle.load(f)

with open('pickles/eda/gender_pie_chart.pkl','rb') as f:
    gender_pie_chart = pickle.load(f)

with open('pickles/eda/facilities_count_plot.pkl','rb') as f:
    facilities_count_plot = pickle.load(f)

with open('pickles/eda/facilities_count_list.pkl','rb') as f:
    facilities_count_list = pickle.load(f)

with open('pickles/eda/top25_universities_college_count_plot.pkl','rb') as f:
    top25_universities_college_count_plot = pickle.load(f)

with open('pickles/eda/universities_count_list.pkl','rb') as f:
    universities_count_list = pickle.load(f)

with open('pickles/eda/top25_states_college_count_plot.pkl','rb') as f:
    top25_states_college_count_plot = pickle.load(f)

with open('pickles/eda/top25_states_college_count_plot_list.pkl','rb') as f:
    top25_states_college_count_plot_list = pickle.load(f)

# login page
@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        email = request.form.get('email').strip()
        password = request.form.get('password')
        
        if password == "root":
            return render_template("eda.html", overview=overview, gender_pie_chart=gender_pie_chart, facilities_count_plot=facilities_count_plot, facilities_count_list=facilities_count_list, top25_universities_college_count_plot=top25_universities_college_count_plot, universities_count_list=universities_count_list, top25_states_college_count_plot=top25_states_college_count_plot, top25_states_college_count_plot_list=top25_states_college_count_plot_list)
        else:
            return render_template("login.html", placeholder="Check your credentials and try again")    
    elif request.method == "GET":
        return render_template("login.html")

# eda dashboard page
@app.route("/eda", methods=["GET", "POST"])
def eda_page():
    return render_template("eda.html", overview=overview, gender_pie_chart=gender_pie_chart, facilities_count_plot=facilities_count_plot, facilities_count_list=facilities_count_list, top25_universities_college_count_plot=top25_universities_college_count_plot, universities_count_list=universities_count_list, top25_states_college_count_plot=top25_states_college_count_plot, top25_states_college_count_plot_list=top25_states_college_count_plot_list)

# about us page
@app.route('/about-us', methods=["GET", "POST"])
def about_us_page():
    return render_template("about-us.html")

# create read update delete page
@app.route("/data-view", methods=["GET", "POST"])
def data_view_page():
    data = data_view.data_view()
    return render_template("data-view.html", data=data)

@app.route('/add_college', methods=["POST", "GET"])
def add_college():
    college_details = {"college_name" : None,
                        "campus_size": None,
                        "gender":None,
                        "total_student_enrollments" : None,
                        "total_faculty_count": None,
                        "eastablished_year" : None,
                        "rating" : None,
                        "university":None,
                        "courses": None,
                        "facility_name": None,
                        "city": None,
                        "state": None,
                        "country":None,
                        "college_type": None,
                        "average_fees": None}

    if request.method == "POST":
        college_details = {"college_name" : request.form["college_name"],
                        "campus_size": request.form["campus_size"],
                        "gender": request.form["gender"],
                        "total_student_enrollments" : request.form["total_student_enrollments"],
                        "total_faculty_count": request.form["total_faculty_count"],
                        "eastablished_year" : request.form["eastablished_year"],
                        "rating" : request.form["rating"],
                        "university": request.form["university"],
                        "courses": request.form["courses"],
                        "facility_name": request.form["facility_name"],
                        "city": request.form["city"],
                        "state": request.form["state"],
                        "country": request.form["country"],
                        "college_type": request.form["college_type"],
                        "average_fees": request.form["average_fees"]}
        
        data_view.add_college(college_details)


        flash("College added successfully")
        return redirect(url_for('data_view_page'))

@app.route("/edit/<id>", methods=["POST", "GET"])
def get_college_details(id):
    college_details = data_view.get_college_details(id)
    print(college_details)
    return render_template("edit.html", college_details=college_details)


@app.route("/update/<id>", methods=["POST"])
def update_contact(id):
    college_details = {"college_name" : None,
                        "campus_size": None,
                        "gender":None,
                        "total_student_enrollments" : None,
                        "total_faculty_count": None,
                        "eastablished_year" : None,
                        "rating" : None,
                        "university":None,
                        "courses": None,
                        "facility_name": None,
                        "city": None,
                        "state": None,
                        "country":None,
                        "college_type": None,
                        "average_fees": None}

    if request.method == "POST":
        college_details = {"college_name" : request.form["college_name"],
                        "campus_size": request.form["campus_size"],
                        "gender": request.form["gender"],
                        "total_student_enrollments" : request.form["total_student_enrollments"],
                        "total_faculty_count": request.form["total_faculty_count"],
                        "established_year" : request.form["established_year"],
                        "rating" : request.form["rating"],
                        "university": request.form["university"],
                        "courses": request.form["courses"],
                        "facility_name": request.form["facility_name"],
                        "city": request.form["city"],
                        "state": request.form["state"],
                        "country": request.form["country"],
                        "college_type": request.form["college_type"],
                        "average_fees": request.form["average_fees"]}
    
        data_view.update_college_details(college_details)


    flash("College updated successfully")
    return redirect(url_for('data_view_page'))
    
@app.route("/delete/<id>", methods=["POST", "GET"])
def delete_record(id):
    print("Records deleted successfully")
    data_view.delete_college_details(id)

    flash("College Deleted Successfully")
    return redirect(url_for('data_view_page'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)