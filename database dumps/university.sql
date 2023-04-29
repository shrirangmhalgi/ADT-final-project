#CREATE SCHEMA university_database;

use universities_database;


create table college_type(
college_type_id int primary key auto_increment,
college_type varchar(100) not null
);

create table country(
country_id int primary key auto_increment,
country_code varchar(100) not null,
country_name varchar(100) not null
);

create table indian_states(
state_id int primary key auto_increment,
state varchar(100) not null
);

create table indian_cities(
city_id int primary key auto_increment,
city varchar(100) not null
);

create table facilities(
facility_id int primary key auto_increment,
facility varchar(100) not null
);

create table indian_universities(
university_id int primary key auto_increment,
university_name varchar(400) not null
);

create table genders(
gender_id int primary key auto_increment,
gender varchar(100) not null
);

create table courses(
course_id int primary key auto_increment,
course_name varchar(5000)
);

create table indian_colleges(
id int primary key auto_increment,
college_name varchar(500) not null,
campus_size double,
gender_id int,
total_student_enrollments double,
total_faculty_count double,
established_year int, 
rating double,
university_id int,
courses varchar(5000), 
facilities varchar(5000),
city_id int,
state_id int,
country_id int,
college_type_id int,
average_fees double,
constraint university_id_fk foreign key (university_id) references indian_universities(university_id),
constraint city_id_fk foreign key (city_id) references indian_cities(city_id),
constraint state_id_fk foreign key (state_id) references indian_states(state_id),
constraint country_id_fk foreign key (country_id) references country(country_id),
constraint college_type_id_fk foreign key (college_type_id) references college_type(college_type_id),
constraint gender_id_fk foreign key (gender_id) references genders(gender_id)
);


create table user_details(
user_id int primary key auto_increment,
user_first_name varchar(400) not null,
user_last_name varchar(400) not null,
email varchar(400) not null,
password varchar(400) not null,
mobile_number bigint
);

create table us_cities(
city_id int primary key auto_increment,
city varchar(100) not null
);

create table us_states(
state_id int primary key auto_increment,
state_name varchar(100) not null,
state_code varchar(400) not null
);

create table us_county(
county_id int primary key auto_increment,
county_name varchar(100) not null
);

create table university_status(
status_id int primary key auto_increment,
status_code varchar(400),
status_description varchar(400) not null
);

create table naics_details(
naics_id int primary key auto_increment,
naics_code int,
naics_description varchar(400)
);


create table usa_universities(
university_id int primary key auto_increment,
university_object_id int,
geo_point varchar(400), 
geo_shape varchar(400),
ipedsid int,
university_name varchar(500),
university_address varchar(1000),
city_id int,
state_id int,
zipcode int,
zip4 varchar(200),
telephone varchar(15),
university_type int, 
status_id int,
population int,
county_id int,
county_fips varchar(400),
country_id int,
latitude double,
longitude double,
naics_id int,
source varchar(400),
source_date date,
validation_method varchar(400),
validation_date date,
website varchar(400),
stfips varchar(400),
cofips varchar(400),
sector int,
level int,
hi_offer int,
degree_grant int, 
locale int,
close_date date,
merge_id int,
alias varchar(400),
size_set int,
inst_size int,
part_time_enroll int,
full_time_enroll int,
total_enroll int,
housing int,
dorm_capacity int,
shelter_id varchar(400),
constraint city_us_id_fk foreign key (city_id) references us_cities(city_id),
constraint state_us_id_fk foreign key (state_id) references us_states(state_id),
constraint status_us_id_fk foreign key (status_id) references university_status(status_id),
constraint county_us_id_fk foreign key (county_id) references us_county(county_id),
constraint country_us_id_fk foreign key (country_id) references country(country_id)
);


insert into country (country_id, country_code, country_name) values(-1, '', 'None');
insert into indian_universities values(-1, 'None');
insert into indian_cities values(-1, 'None');
insert into indian_states values(-1, 'None');
insert into college_type values(-1, 'None');
insert into genders values(-1, 'None');
insert into user_details (user_first_name, user_last_name, email, password, mobile_number)
values("Manali", "Shelar", "manalivs@gmail.com", "manali", 9876543201);
insert into user_details (user_first_name, user_last_name, email, password, mobile_number)
values("Shrirang", "Mhalgi", "shrirangmhalgi@gmail.com", "root", 9876543210);

