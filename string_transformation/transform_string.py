# the original string 
record = "   alice_2026, nanjing, cs101, alice2026@university.edu   "

# 1. Remove leading and trailing spaces
record = record.strip()

# 2. Split into parts
parts = record.split(",")

# 3. Clean each part
parts = [part.strip() for part in parts]
username, city, course, email = parts

# 4. Format values so that they match the output
name_formatted = username.capitalize()   # alice_2026 -> Alice_2026
city_formatted = city.capitalize()       # nanjing    -> Nanjing
course_formatted = course.upper()        # cs101      -> CS101

# 5. Validate username 
username_valid = username != "" and username[0].isalpha()

# 6. Check course prefix
has_letters_prefix = course_formatted[:2].isalpha()

# 7. Check whether the course ends with digits
ends_with_digits = course_formatted[2:].isdigit()

valid_course_code = has_letters_prefix and ends_with_digits

# 8. Find @ position
at_position = email.find("@")

# 9. Extract email domain
email_domain = email[at_position + 1:]

# 10. Count occurrences of lowercase i
i_count = username.count("i")

# 11. Replace email domain
new_email = email.replace("university.edu", "campus.edu")

# 12. Format the final output
print("Name:", name_formatted)
print("City:", city_formatted)
print("Course:", course_formatted)
print("Email domain:", email_domain)
print("Valid course code:", valid_course_code)