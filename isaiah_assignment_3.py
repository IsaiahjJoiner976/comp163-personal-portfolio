#Personal Information Storage(string values)
full_name = "Isaiah Joiner"
student_email = "ijjointer@aggies.ncat.edu"
hometown = "Loganville, GA"
grad_semester = "Spring 2029"
major = "Computer Science"

#Academic Data Organization(list)
courses_current = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
courses_completed = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours = ["3", "3", "3", "3"]
GPA_history = ["3.2", "3.6", "3.4", "3.7"]

#Contact Information Storage(tuple)
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte", "NC", "28202")
insta_info = ("Instagram", "@jordan_codes", "312")
twitter_info = ("Twitter", "@jordandev", "127")
birthday_info = ("Birthday", "5", "22", "2006")

#Interest Tracking(set)
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertain_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

#Organizational Mapping(dictionary)
course_credit = {
    "COMP 163": 3,
    "MATH 150": 3,
    "ENG 101": 3,
    "HIS 105": 3
}
course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 150": "Dr. Lee",
    "ENG 101": "Dr. Martinez",
    "HIS 105": "Dr. Brown"
}
course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 101": "Crosby 121",
    "HIS 105": "Crosby 210"
}
monthly_budget = {
    "Food": 450,
    "Entertainment": 200,
    "Books": 125,
    "Transportation": 100
}
study_per_subject = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3
}
directory_contact = {
    "Mom": "704-555-0199",
    "Roommate": "336-555-7821",
    "Academic Advisot": "336-334-5000"
}

#Required Calculations
total_credits = int(credit_hours[0]) + int(credit_hours[1]) + int(credit_hours[2]) + int(credit_hours[3])
cumulative_gpa = (float(GPA_history[0]) + float(GPA_history[1]) + float(GPA_history[2]) + float(GPA_history[3])) / 4
completed_courses_count = len(courses_completed)
total_weekly_study = study_per_subject["Programming"] + study_per_subject["Math"] + study_per_subject["English"] + study_per_subject["History"]
academic_load = total_credits + total_weekly_study
total_monthly_budget = monthly_budget["Food"] + monthly_budget["Books"] + monthly_budget["Entertainment"] + monthly_budget["Transportation"]
food_budget = round(monthly_budget["Food"] / 30, 2)
annual_budget_projection = total_monthly_budget * 12
study_cost = round(monthly_budget["Books"] / total_weekly_study, 2)

#Analytics Calculations
total_followers = int(insta_info[2]) + int(twitter_info[2])
skills_comparison = len(current_skills) / len(skills_learn)
#contact_directory_count = len(directory_contact)
entertain_backlog_count = len(entertain_backlog)
academic_workload = int(total_weekly_study) + int(total_credits)

#First Section
print("=" * 64)
print(" " * 14 + "PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 64)
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {grad_semester}")
print(f"Major: {major}")
print("")
print("=" * 3 + " " + "ACADEMIC PROFILE" + " " + "=" * 3)
print(f"Current Semester: {total_credits} credits across {len(courses_current)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_weekly_study} hours")
print(f"Academic Investment: ${study_cost:.1f} per study hour")
print("")


print("Current Courses:")
print(f"{courses_current[0]} - {course_credit['COMP 163']} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"{courses_current[1]} - {course_credit['MATH 150']} credits - {course_professors['MATH 150']} - {course_rooms['MATH 150']}")
print(f"{courses_current[2]} - {course_credit['ENG 101']} credits - {course_professors['ENG 101']} - {course_rooms['ENG 101']}")
print(f"{courses_current[3]} - {course_credit['HIS 105']} credits - {course_professors['HIS 105']} - {course_rooms['HIS 105']}")
print("")

#Second Section
print("=" * 3 + " " + "PERSONAL DEVELOPMENT" + " " + "=" * 3)
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_learn}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_learn)}")
print("")

#Third Section
print("=" * 3 + " " + "FINANCIAL OVERVIEW" + " " + "=" * 3)
print(f"Monthly Budget: ${total_monthly_budget}")
print(f"Food: ${monthly_budget['Food']} (${food_budget}/day)")
print(f"Entertainment: ${monthly_budget['Entertainment']}")
print(f"Books: ${monthly_budget['Books']}")
print(f"Transportation: ${monthly_budget['Transportation']}")
print(f"Annual Projection: ${annual_budget_projection}")
print("")

#Fourth Section
print("=" * 3 + " " + "CONNECTIONS & CONTACTS" + " " + "=" * 3)
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {len(directory_contact)} people in directory")
print("")

#Fifth Section
print("=" * 3 + " " + "LIFE STATISTICS" + " " + "=" * 3)
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_workload} weekly commitments")
print(f"Entertainment Backlog: {entertain_backlog_count} items")
print(f"Current Hobbies: {len(hobbies)} activities")

print("=" * 64)

