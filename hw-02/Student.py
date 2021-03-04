# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, years=0):
        self.name = name
        self.gpa = gpa
        self.years = year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def enroll(self, courses):
        listOfCourses = []
        for course in courses:
            listOfCourses.append(course)
        return listOfCourses
        
    def display_courses(self, courses):
        return "I am enrolled in:" + enroll(courses)
    
    def years_until_graduation(self):
        return 4 - self.years
        
    
            
        