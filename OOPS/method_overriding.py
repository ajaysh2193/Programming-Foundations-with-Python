class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_info(self):
       print("Last Name - "+self.last_name)
       print("Eye Color - "+self.eye_color)
       
class Child(Parent):
        def __init__(self, last_name, eye_color, no_of_toys):
            print("Child Constructor called")
            Parent.__init__(self, last_name, eye_color)
            self.no_of_toys = no_of_toys

        def show_info(self):
            print("Last Name - "+self.last_name)
            print("Eye Color - "+self.eye_color)
            print("No of toys - "+str(self.no_of_toys))
       
#billy_cyrus = Parent("Cyrus","Blue")
#print(billy_cyrus.last_name)
miley_cyrus = Child("Cyrus", "Blue", "5")
#print(miley_cyrus.last_name)
#print(miley_cyrus.no_of_toys)
miley_cyrus.show_info()
