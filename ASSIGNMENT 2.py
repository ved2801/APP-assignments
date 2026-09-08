#STUDENT REPORT BY MAGIC,CLASS & DECODER METHOD:

def add_border(func):
    def wrapper(self):
        print("=" * 40)
        result = func(self)
        print("=" * 40)
        return result
    return wrapper


class Report:
    # Class variable - default template
    template = "Student Report"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Magic method
    def __str__(self):
        return f"{self.template} --> {self.name} - Marks: {self.marks}"

    # Class method
    @classmethod
    def set_template(cls, new_template):
        cls.template = new_template

    # Custom decorator
    @add_border
    def generate_report(self):
        print(self.template)
        print("Student Name:", self.name)
        print("Marks:", self.marks)

        if self.marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Create objects
r1 = Report("Rahul", 85)
r2 = Report("Sneha", 35)

# Generate reports using decorator
r1.generate_report()
r2.generate_report()

# Change report template dynamically
Report.set_template("Student Performance Report")

print("\nAfter changing template:\n")

r1.generate_report()
r2.generate_report()

# Using magic method __str__
print("\nObject Information:")
print(r1)
