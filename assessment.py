"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages that object orientation can provide are:

   1) Abstraction: 

    Hides the details of how a method is processed and only shows
    relevant data.

    For example, we know what the method .remove() does by looking at its name, 
    but how the method works internally is hidden from the user.

   2) Encapsulation: 

    Wraps everything together.  This protects the method from being modified by
    the user.

   3) Polymorphism: 
    
    Classes give you the flexibility to use the same method with the same amount
    arguments for different types and eliminates the need for conditionals.


2. What is a class?

    A class can be thought of a factory for making a type of thing.  For example,
    if we have a class for dogs, every dog that is instantiated will have a common
    set of core features described in the parameters in the init (i.e. color,
    floppy ears, barks, is_furry, etc.)  


3. What is an instance attribute?
    
    When instantiating a thing, it will have the instance attribute
    as defined in the init. These are the common set of core values that each
    object will have it is instantiated.

4. What is a method?
    
    Methods are similar to functions but they are defined within classes and
    they take their class instance as their first parameter.

5. What is an instance in object orientation?

    Once a thing is instantiated, it is called an instance.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    Class attributes are the common set of core features that each thing will
    have once it is instantiated.  Instance attributes override class attributes.

    For example, for a fish class to keep track of fish added to a tank. 

    I would use class attribute 'is_alive' and instance attributes for name and
    color.  This assumes that when a fish is added to the tank it is alive.

    If a fish dies, I can override the is_alive attribute to False.

    class Fish(object):
        is_alive = True

        def __init__(self, name, color):
            self.name = name
            self.color = color


"""

# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """Generic student class to store data such as name and address."""

    def __init__(self, first_name, last_name, address):
        """Initializes student attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions."""

    def __init__(self, question, correct_answer):
        """Initializes question attributes."""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Asks a question and prompts the user for an answer"""

        # gets user input to answer the question
        user_answer = raw_input("{} > ".format(self.question))

        # checks if user's answer is correct, if so returns True.
        if user_answer == self.correct_answer:
            return True

        else:
            return False


class Exam(object):
    """Exam."""

    def __init__(self, name):
        """Initializes exam attributes."""

        self.questions = []
        self.name = name

    def add_question(self, question):
        """Add question to list of exam questions"""

        self.questions.append(question)

    def administer(self):
        """Administer's all of the exam questions"""

        points = 0.0

        # iterates over each question in self.questions, if the user's answer
        # is correct, one point is added
        for question in self.questions:
            if question.ask_and_evaluate():
                points += 1

        # gets the score percentage
        return (points / len(self.questions)) * 100


class Quiz(Exam):
    """Quiz is a subclass of Exam"""

    def administer(self):
        """Administer's all of the quiz questions"""

        # inherits administer functionality from Exam class
        score = super(Quiz, self).administer()

        # checks if score is greater than 50, if so returns 1 for pass,
        # and 0 for fail.
        if score > 50:
            return 1
        
        else:
            return 0


class StudentExam(object):
    """Stores student, exam, and score info"""

    def __init__(self, student, exam):
        """Initializes StudentExam attributes"""

        self.student = student
        self.exam = exam
        self.score = 0


def take_test(exam, student):
    """Admisisters exam and assigns the actual score"""

    student.score = exam.administer()

    print "Score: {}".format(student.score)


"""PART 4"""

def example():

    midterm = Exam('midterm')

    set_q = Question('What is the method for adding an element to a set?', '.add()')
    midterm.add_question(set_q)

    pwd_q = Question('What does pwd stand for?', 'print working directory')
    midterm.add_question(pwd_q)

    list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
    midterm.add_question(list_q)

    jasmine = Student('Jasmine', 'Debugger', '0101 Computer Street')

    take_test(midterm, jasmine)

# example()


"""PART 5"""

def example2():

    quiz = Quiz('quiz')

    q_one = Question('What is the capital of Alberta?', 'Edmonton')
    quiz.add_question(q_one)

    q_two = Question('Who is the author of Python?', 'Guido Van Rossum')
    quiz.add_question(q_two)

    q_three = Question('Where is Hackbright Academy located?', 'San Francisco')
    quiz.add_question(q_three)

    jasmine = Student('Jasmine', 'Debugger', '0101 Computer Street')

    take_test(quiz, jasmine)

# example2()









