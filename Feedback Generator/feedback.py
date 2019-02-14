# Automatic Feedback System Solution.

# This program provide a solution for generating feedback for the student.
# This program can read a file which holds student records in the order:
# Student ID-Student name- Email- Task A mark- Task B mark- Task C mark
# It also provide a option to login in the system using a predefined username and
# password. It reads the file and ask the teacher only the student ID.
# The program search student all details and shows the obtained grade.
# It then provide a option to generate feedback and save it as a text file
# Login is required to operate the program entirely.
# All of the given feedback will be on a single .txt file
# Limitations: There is no sign up options.
# To generate feedback it works normally fine but if the user enter incorrect
# student id it is also possible to generate feedback based on previous student
#credential on the program cache. but this is not possible for first attempt.



# Attention:
# Usename and password both are : "TUT"

#simple operation: use username and password 'TUT'. then click login. Enter
# file name 'record.csv' and enter student ID 1001 or 1002 or 1003. Then click generate
# feedback. you will find feedback as f_to_student.txt format in your folder.



import tkinter
import tkinter.messagebox

class Feedback:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create  frames to group widgets.
        self.frame0 = tkinter.Frame(self.main_window)
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)
        self.frame9 = tkinter.Frame(self.main_window)

        # Create the widget for Frame 0
        # Create the title and show who is logged in
        self.welcome_level = tkinter.Label(self.frame0,text='Welcome to the feedback Sytem ! \n')
        self.login_status = tkinter.Label(self.frame0, text='Logged in as: ')
        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of characters.

        self.login_value_variable = tkinter.StringVar()
        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.

        self.login_value = tkinter.Label(self.frame0,textvariable=self.login_value_variable)

        # Pack the frame 0
        self.welcome_level.pack(side='top')
        self.login_value.pack(side='right')
        self.login_status.pack(side='right')

        # Create the widget for the  frame 1
        # Create login system
        self.prompt_label = tkinter.Label(self.frame1,text='Enter your login Credentials:')
        self.name_entry_label = tkinter.Label(self.frame1, text='Username')
        self.name_entry = tkinter.Entry(self.frame1, width=20)

        # Pack the frame 1 widget
        self.prompt_label.pack(side = 'top')
        self.name_entry_label.pack(side = 'left')
        self.name_entry.pack(side = 'left')

        # Create the widget for the  frame 2
        self.password_entry_label = tkinter.Label(self.frame2, text='Password')
        self.password_entry = tkinter.Entry(self.frame2, width=20)

        # Pack the frame 2 widget
        self.password_entry_label.pack(side = 'left')
        self.password_entry.pack(side = 'left')

        # create the frame 3 widget
        # Login buttom creation and checking the entered credentials with logincheck
        #function
        self.login_button = tkinter.Button(self.frame3, text='Login',command=self.loginCheck)

        # Pack the frame 3 widget
        self.login_button.pack(side='left')

        # Create frame 4 widget
        # Taking student record file in csv format
        self.student_record_label = tkinter.Label(self.frame4,text='Enter student record file name: ')
        self.student_record_file_name_entry = tkinter.Entry(self.frame4,width=20)


        # Pack the frame 4 widget
        self.student_record_label.pack(side = 'left')
        self.student_record_file_name_entry.pack(side='left')


        # Create frame 5 widget
        # Take student id and search for the details and find student marks with
        #mark_evaluation function
        self.student_id = tkinter.Label(self.frame5, text='Enter student ID: ')
        self.student_id_entry = tkinter.Entry(self.frame5, width=20)
        self.student_id_search_button = tkinter.Button(self.frame5,text = 'Search',command = self.mark_evaluation)

        # Pack the frame 5 widget
        self.student_id.pack(side = 'left')
        self.student_id_entry.pack(side = 'left')
        self.student_id_search_button.pack(side = 'left')

        # Create frame 6 widget
        # Displaying student all details
        self.student_name = tkinter.Label(self.frame6, text = 'Student Name: ')
        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of characters.
        self.student_name_variable = tkinter.StringVar()
        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.student_name_result = tkinter.Label(self.frame6,textvariable=self.student_name_variable)
        self.student_email = tkinter.Label(self.frame6, text='Student Email: ')
        self.student_email_variable = tkinter.StringVar()
        self.student_email_result = tkinter.Label(self.frame6,textvariable=self.student_email_variable)

        # Pack the frame 6 widget
        self.student_name.pack(side='left')
        self.student_name_result.pack(side='left')
        self.student_email.pack(side='left')
        self.student_email_result.pack(side='left')

        # Create frame 7 widget
        # Display student exam points

        self.design= tkinter.Label(self.frame7,text='--------------------------------------------')
        self.exam_points = tkinter.Label(self.frame7, text = 'Earned Exam Points: ')
        self.task_a_label= tkinter.Label(self.frame7, text = 'Task A: ')
        self.task_a_variable = tkinter.StringVar()
        self.task_a_result = tkinter.Label(self.frame7,textvariable = self.task_a_variable)
        self.task_b_label = tkinter.Label(self.frame7, text = 'Task B: ')
        self.task_b_variable = tkinter.StringVar()
        self.task_b_result = tkinter.Label(self.frame7,textvariable = self.task_b_variable)
        self.task_c_label = tkinter.Label(self.frame7, text = 'Task C: ')
        self.task_c_variable = tkinter.StringVar()
        self.task_c_result = tkinter.Label(self.frame7,textvariable = self.task_c_variable)

        # Pack the frame 7 widget
        self.design.pack(side = 'top')
        self.exam_points.pack(side = 'top')
        self.task_a_label.pack(side = 'left')
        self.task_a_result.pack(side = 'left')
        self.task_b_label.pack(side = 'left')
        self.task_b_result.pack(side = 'left')
        self.task_c_label.pack(side = 'left')
        self.task_c_result.pack(side = 'left')

        # Create frame 8 widget
        # Display student grade
        self.grade_label = tkinter.Label(self.frame8, text = 'Grade: ',font='bold')
        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of characters.
        self.grade_variable = tkinter.StringVar()
        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.grade_obtained = tkinter.Label(self.frame8,textvariable = self.grade_variable)


        # Pack the frame 8 widget
        self.grade_label.pack(side =  'left')
        self.grade_obtained.pack(side = 'left')

        # Create frame 9 widget
        # Display the buttom for generatimg feedback
        self.feedback_label = tkinter.Button(self.frame9, text = 'Generate Feedback',\
                                             font = 'bold',command = self.feedback_generator)


        # Pack the frame 9 widget
        self.feedback_label.pack(side = 'bottom')

        # Pack the frame
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.frame9.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()
    # This function will check whether the entered username and password is correct
    # or not. if it is correct it will destroy login window again.
    def loginCheck(self):
        u_name_test = str(self.name_entry.get())
        password_test = str(self.password_entry.get())
        if u_name_test == 'TUT' and password_test == 'TUT':
            tkinter.messagebox.showinfo('Login', 'Login Successful !')
            self.login_value_variable.set(u_name_test)
            self.frame1.destroy()
            self.frame2.destroy()
            self.frame3.destroy()
        else:
            tkinter.messagebox.showerror('Login', 'Login Unsuccessful')

    def studentRecordUpload(self,nameOfTheFile):
        try:
            file_cont = open(nameOfTheFile, "r")
            tkinter.messagebox.showinfo('Successful', 'File Processed Successfully !')
            Fullcontact = {}
            for line in file_cont:
                contacts = {}
                ContentOfTheFile = line.strip().split(";")
                key = ContentOfTheFile[0]
                contacts["name"] =  ContentOfTheFile[1]
                contacts["email"] = ContentOfTheFile[2]
                contacts["taska"] = ContentOfTheFile[3]
                contacts["taskb"] = ContentOfTheFile[4]
                contacts["taskc"] = ContentOfTheFile[5]
                Fullcontact[key] = contacts
            file_cont.close()
            return Fullcontact
        except:
            tkinter.messagebox.showerror('Upload Failed', 'File not found!')


    # This function is to get student details and decide which grade he obtained.
    def mark_evaluation(self):

        try:
            info = self.studentRecordUpload(
                self.student_record_file_name_entry.get())
            student_id = self.student_id_entry.get()
            obtained_student_name = info[student_id]["name"]
            self.student_name_variable.set(obtained_student_name)
            obtained_student_email = info[student_id]["email"]
            self.student_email_variable.set(obtained_student_email)
            obtained_task_a_mark = info[student_id]["taska"]
            self.task_a_variable.set(obtained_task_a_mark)
            obtained_task_b_mark = info[student_id]["taskb"]
            self.task_b_variable.set(obtained_task_b_mark)
            obtained_task_c_mark = info[student_id]["taskc"]
            self.task_c_variable.set(obtained_task_c_mark)
            total_mark = int(obtained_task_a_mark)+int(obtained_task_b_mark)+int(obtained_task_c_mark)
            if total_mark < 100 :
                self.grade_variable.set(0)
            elif total_mark >= 100 and total_mark < 200:
                self.grade_variable.set(1)
            elif total_mark >= 200 and total_mark < 300:
                self.grade_variable.set(2)
            elif total_mark >= 300 and total_mark < 400:
                self.grade_variable.set(3)
            else:
                self.grade_variable.set(4)
        except:
            tkinter.messagebox.showerror('Invalid ID', 'Invalid Student ID !')

    # This function generate feedback based on his grade
    def feedback_generator(self):

        try:
            grade = int(self.grade_variable.get())
            feedback_to_students = open('f_to_student.txt', 'a')
            id = self.student_id_entry.get()
            name = self.student_name_variable.get()
            teacher_name= self.login_value_variable.get()
            if grade == 4 or grade == 3:
                feedback_to_students.write('Attention: ' + '\n' + 'ID: ' + str(id)\
                        +'\n' + 'Name: '+ str(name)+'\n' + 'I am pleased to inform'+'\n'+\
                        'you that you can continue your journey to the next'+'\n'+\
                        'level programming courses! ' + '\n' + \
                        '-----' + '\n' + 'Tervesin' + '\n' + str(teacher_name) + '\n'+'\n')
            else:
                feedback_to_students.write('Attention: ' + '\n' + 'ID: ' + str(id) \
                        + '\n' + 'Name: ' + str(name) + '\n' + 'I am sorry to inform' + '\n' + \
                        'you that you can not continue your journey to the next' + '\n' + \
                        'level programming courses! ' + '\n' + \
                        '-----' + '\n' + 'Tervesin' + '\n' +str(teacher_name) + '\n' + '\n')
            tkinter.messagebox.showinfo('Successfull','Feedback Generated!')
        except:
            tkinter.messagebox.showerror('Error', 'Unable to generate feedback!')

def main():
    # Create an instance of the Feedback class.
    Generate_student_feedback = Feedback()
main()