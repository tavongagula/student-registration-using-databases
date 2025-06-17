import psycopg2
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter.ttk import Combobox

hostname = "localhost"
database = "postgres"
username = "postgres"
pwd = "gula"
port_id = 5432

cur = None
conn = None

try:

    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS students (
                        REGNUMBER VARCHAR PRIMARY KEY, 
                        FIRSTNAME VARCHAR,
                        LASTNAME VARCHAR, 
                        IDNUMBER VARCHAR, 
                        ADDRESS VARCHAR, 
                        EMAILADDRESS VARCHAR,
                        LEVEL int, 
                        PROGRAMCODE VARCHAR, 
                        FACULTYNAME VARCHAR)


    '''
    cur.execute(create_script)


    def color():
        color1 = colorchooser.askcolor()
        print(color1)


    def show_data():
        cur.execute("SELECT * FROM students")
        records = cur.fetchall()
        output = ''

        for record in records:
            output_label.config(text=f'{output}\n {record[0]} {record(1)}')
            output = output_label['text']
        conn.commit()
        conn.close()


    def clear():
        reg_entry.delete(0, END)
        id_entry.delete(0, END)
        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        physical_address_entry.delete(0, END)
        email_address_entry.delete(0, END)
        level_entry.delete(0, END)
        program_name_entry.delete(0, END)
        faculty_entry.delete(0, END)


    root = Tk()
    root.title("University of Zimbawe")
    root.geometry("1500x970")
    root.config(bg='khaki')
    # root.iconbitmap("Screenshot (183).png")

    # my first label
    label = Label(root, text="UNIVERSITY OF ZIMBABWE ", fg="#fff", bg='#f0687c', font=("arial", 40, "bold"), bd=8,
                  relief=GROOVE)
    label.pack(fill=X)

    # creating a frame for student
    myframe = Frame(root)
    myframe.pack()

    # creating a label frame
    mylabelframe = LabelFrame(myframe, text="Student Profile", fg="black", bg='#f7f8de', font=("arial", 12, "bold"),
                              bd=8, relief=GROOVE)
    mylabelframe.grid(row=0, column=0)

    # creating labels
    reg_number = Label(mylabelframe, text="Enter the registration number :", fg="black", bg="#f7f8de",
                       font=("arial", 12), bd=6, relief=GROOVE)
    reg_number.grid(row=0, column=0, sticky="w")
    reg_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    reg_entry.grid(row=0, column=1, padx=15)

    id_number = Label(mylabelframe, text="Enter the national identity number :", fg="black", bg="#f7f8de",
                      font=("arial", 12), bd=8, relief=GROOVE).grid(row=0, column=2, sticky="w")
    id_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    id_entry.grid(row=0, column=3, padx=18)

    firstname = Label(mylabelframe, text="Enter the first name :", fg="black", bg="#f7f8de", font=("arial", 12), bd=8,
                      relief=GROOVE).grid(row=1, column=0, sticky="w", pady=10)
    firstname_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    firstname_entry.grid(row=1, column=1)

    lastname = Label(mylabelframe, text="Enter the last name :", fg="black", bg="#f7f8de", font=("arial", 12), bd=8,
                     relief=GROOVE).grid(row=1, column=2, sticky="w")
    lastname_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    lastname_entry.grid(row=1, column=3)

    physical_address = Label(mylabelframe, text="Enter the physical address :", fg="black", bg="#f7f8de",
                             font=("arial", 12), bd=8, relief=GROOVE).grid(row=2, column=0, sticky="w", pady=10)
    physical_address_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    physical_address_entry.grid(row=2, column=1)

    email_address = Label(mylabelframe, text="Enter the email address:", fg="black", bg="#f7f8de", font=("arial", 12),
                          bd=8, relief=GROOVE).grid(row=2, column=2, sticky="w", pady=10)
    email_address_entry = Entry(mylabelframe, width=30, font=("arial", 12), bd=8, relief=GROOVE)
    email_address_entry.grid(row=2, column=3)

    level = Label(mylabelframe, text="Enter the level of your study :", fg="black", bg="#f7f8de", font=("arial", 12),
                  bd=8, relief=GROOVE).grid(row=3, column=0, sticky="w", pady=10)
    level_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    level_entry.grid(row=3, column=1)

    program_name = Label(mylabelframe, text="Enter your program code :", fg="black", bg="#f7f8de", font=("arial", 12),
                         bd=8, relief=GROOVE).grid(row=3, column=2, sticky="w")
    program_name_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    program_name_entry.grid(row=3, column=3)

    faculty = Label(mylabelframe, text="Enter the faculty name:", fg="black", bg="#f7f8de", font=("arial", 12), bd=8,
                    relief=GROOVE).grid(row=4, column=0, sticky="w")
    faculty_entry = Entry(mylabelframe, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    faculty_entry.grid(row=4, column=1)

    variable4 = StringVar()
    gender = Label(mylabelframe, text="Select the gender :", fg="black", bg="#f7f8de", font=("arial", 12), bd=8,
                   relief=GROOVE).grid(row=4, column=2, sticky="w")
    radiobutton = Radiobutton(mylabelframe, text="Male", value="Male", var_=variable4, fg="red", bg="#f7f8de", bd=8,
                              relief=GROOVE)
    radiobutton.grid(row=4, column=3, sticky="w")
    radiobutton = Radiobutton(mylabelframe, text="Female", value="Female", var_=variable4, fg="red", bg="#f7f8de", bd=8,
                              relief=GROOVE)
    radiobutton.grid(row=4, column=4, sticky="w")

    labelframe_button = LabelFrame(myframe, text="                              Enter   key", font=('arial', 14),
                                   fg="purple", bg="#f7f8de")
    labelframe_button.grid(row=1, column=0)


    def submit_data():
        insert_script = 'INSERT INTO students(REGNUMBER,FIRSTNAME,LASTNAME,IDNUMBER,ADDRESS,EMAILADDRESS,LEVEL,PROGRAMCODE,FACULTYNAME) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        e1 = reg_entry.get()
        e2 = firstname_entry.get()
        e3 = lastname_entry.get()
        e4 = id_entry.get()
        e5 = physical_address_entry.get()
        e6 = email_address_entry.get()
        e7 = level_entry.get()
        e8 = program_name_entry.get()
        e9 = faculty_entry.get()
        insert_value = (e1, e2, e3, e4, e5, e6, e7, e8, e9)

        cur.execute(insert_script, insert_value)
        conn.commit()


    def Exit():
        root.destroy()


    submit_button = Button(labelframe_button, text="Submit", fg="black", bg="orange", font=("arial", 12), width=12,
                           command=submit_data)
    submit_button.grid(row=0, column=0)

    exit_button = Button(labelframe_button, text="EXIT", fg="black", bg="orange", font=("arial", 12, "bold"), width=12,
                         padx=10, command=Exit)
    exit_button.grid(row=0, column=1)

    reset_button = Button(labelframe_button, text="RESET", fg="black", bg="orange", font=("arial", 12), width=12,
                          command=clear)
    reset_button.grid(row=0, column=2)

    check = LabelFrame(myframe, text="ENTER YOUR ALGORITHM SELECTION", fg="black", bg="#f7f8de", font=("arial", 14))
    check.grid(row=3, column=0)

    sorting_algorithm = Label(check, text="SORTING ALGORITHM:", fg="purple", bg="#f7f8de", font=("arial", 12), padx=20)
    sorting_algorithm.grid(row=0, column=0)
    sorting_algorithm_entry = Entry(check, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    sorting_algorithm_entry.grid(row=0, column=2)

    order = Label(check, text="ORDER OF SORT:", fg="purple", bg="#f7f8de", font=("arial", 12), padx=20)
    order.grid(row=1, column=0)
    order_entry = Entry(check, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    order_entry.grid(row=1, column=2)

    sort_button = Button(check, text="SORT", bg="orange", font=("arial", 12), width=12, padx=20)
    sort_button.grid(row=3, column=2)

    searching_algorithm = Label(check, text="SEARCHING ALGORITHM:", fg="purple", bg="#f7f8de", font=("arial", 12))
    searching_algorithm.grid(row=0, column=6)
    searching_algorithm_entry = Entry(check, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    searching_algorithm_entry.grid(row=0, column=7)

    search_button = Button(check, text="SEARCH", bg="orange", font=("arial", 12), width=12, padx=20)
    search_button.grid(row=3, column=7)

    exit1 = Label(check, text="SEARCH KEY", fg="purple", bg="#f7f8de", font=("arial", 12), padx=20)
    exit1.grid(row=1, column=6)
    key_entry = Entry(check, width=20, font=("arial", 12), bd=8, relief=GROOVE)
    key_entry.grid(row=1, column=7)

    text1 = LabelFrame(myframe, text="Entry for student Quiries", fg="black", bg="#f7f8de", font=("arial", 14))
    text1.grid(row=4, column=0)

    textbox = Text(text1, width=150, height=10, font=("arial", 12))
    textbox.grid(row=0, column=0)

    submit = Button(text1, text="Submit", fg="black", bg="yellow", font=("arial", 12), width=10, height=4, padx=20)
    submit.grid(row=0, column=1)

    output_label = Label(root, text='')
    output_label.pack(pady=50)

    root.mainloop()

    conn.commit()



except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



