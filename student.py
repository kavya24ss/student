import sys
if len(sys.argv) != 3:
    print("Usage: python3 student.py <name> <rollno")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]

print(f"Script Name:", script_name)
print(f"Name:",name)
print(f"Roll No:",rollno)
