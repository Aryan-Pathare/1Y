# Demonstrating the use of sets for student enrollments in multiple exams

def display_set(name, data):
    print(f"{name}: {', '.join(data) if data else 'No students'}")

# Sample student enrollments
cet_students = {"Alice", "Bob", "Charlie", "David"}
jee_students = {"Charlie", "David", "Eve", "Frank"}
neet_students = {"Alice", "Frank", "Grace", "Hannah"}

# Display original sets
display_set("CET Students", cet_students)
display_set("JEE Students", jee_students)
display_set("NEET Students", neet_students)

# Perform set operations
all_students = cet_students | jee_students | neet_students  # Union
common_students = cet_students & jee_students & neet_students  # Intersection
cet_only = cet_students - (jee_students | neet_students)  # Difference

# Display results
display_set("All Students (Union)", all_students)
display_set("Common Students (Intersection)", common_students)
display_set("CET Only Students (Difference)", cet_only)
