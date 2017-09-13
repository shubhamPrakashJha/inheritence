class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,no_of_toys):
        print("child constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys = no_of_toys

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)
        print("No Of Toys " + str(self.no_of_toys))



# shiv_jha = Parent("jha","black")
# shiv_jha.show_info()
# print("the eye color of shiv "+shiv_jha.last_name+" is " + shiv_jha.eye_color)

shubham_jha = Child("jha","black",5)
shubham_jha.show_info()
# print(shubham_jha.last_name)
# print(shubham_jha.no_of_toys)
