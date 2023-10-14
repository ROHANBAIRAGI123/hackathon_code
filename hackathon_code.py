from tkinter import *
from tkinter import messagebox as mg
import pickle

class Book:
    def __init__(self, title):
        self.title = title
        self.checked_out = False
        self.borrower = None

    def check_out(self, borrower):
        if not self.checked_out:
            self.checked_out = True
            self.borrower = borrower
            print(f"{self.title} has been checked out by {borrower}")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            self.borrower = None
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")
studentdetail = []
books = []
def student_detail():
    global studentdetail
    try:
        with open("student_details.xyz", "rb") as f:
            books = pickle.load(f)
    except FileNotFoundError:
        books = []
def save_student_details():
    with open("student_details.xyz", "ab") as file:
        pickle.dump(books, file)

root = Tk()
root.title('LIBRARY MANAGEMENT SYSTEM')
root.geometry("800x600")
root.config(background='grey')

def borrow_book():
    new = Tk()
    new.title('BORROW BOOK')
    new.geometry("1000x800")

    def checkbook():
        title_to_borrow = borrowentry.get()
        book_found = False
        for book in books:
            if book.title == title_to_borrow and not book.checked_out:
                mg.showinfo('Borrow Book', f"{title_to_borrow} is available.")
                book_found = True
                break
        if not book_found:
            mg.showinfo('Borrow Book', f"{title_to_borrow} is not available for now.")

    f = Frame(new)
    Label(f, text='Enter book name you want to borrow', font='timesnewroman 15 ').grid(row=0)
    borrowentry = Entry(f)
    borrowentry.grid(row=1)
    Button(f, text='CHECK IF BOOK IS AVAILABLE', pady=20, command=checkbook).grid(row=2)
    f.pack()


    import smtplib
    from email.mime.text import MIMEText
    import datetime
    from datetime import datetime, timedelta

    b_d = datetime.today() 
    days_to_add = 30
    r_d = b_d +timedelta(30)


    borrow_date = b_d.strftime("%Y-%m-%d")
    return_date = r_d.strftime("%Y-%m-%d")
    date= datetime.today().strftime("%Y-%m-%d")

    d1 = datetime.strptime(date,"%Y-%m-%d")
    d2 = datetime.strptime(return_date,"%Y-%m-%d")
    d3 = d2-timedelta(5)

    subject = "Reminder:Please Return Library Book"
    body = "Dear Student,\n\nThis is a friendly reminder to return the library book that you have borrowed. Please return it by due date to avoid any late fees\n\nThank you!\n\nSincerely, Your Library."
    sender = "joshiambika100@gmail.com"
    recipients = ["rohanbairagi40@gmail.com"]
    password = "qkhn yfqd mlfb bcqw"

  
    if d1==d3:
        def send_email(subject, body, sender, recipients, password): 
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
            print("Message sent!")
            send_email(subject, body, sender, recipients, password)

    if d1==d2:
        def send_email(subject, body, sender, recipients, password):
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
            print("Message sent!")
            send_email(subject, body, sender, recipients, password)

    body = "Dear Student,\n\nThis is a friendly reminder to return the library book that you have borrowed. Please return it as you have exceeded the due date.\n\nThank you!\n\nSincerely, Your Library."

    if d1>d2:
        def send_email(subject, body, sender, recipients, password):
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, MIMEText(body).as_string())
        print("Message sent!")
        send_email(subject, body, sender, recipients, password)

    d = d1 - d2
    difference = d.days
    if(d1>d2):
        print("Your fine is", difference*2,"rs \n as you are delayed by", difference,"days.")
    else:
        pass

def return_book():
    new = Tk()
    new.title('ADD BOOK')
    new.geometry("800x600")

    def add_book_to_library():
        title = booktitle.get()
        if title:
            new_book = Book(title)
            books.append(new_book)
            mg.showinfo('return Book', f"{title} has been added to the library.")
            new.destroy()
        else:
            mg.showwarning('Return Book', 'Please enter a book title.')
        save_student_details()

    f = Frame(new)
    Label(f, text='Enter the book title you want to return', font='timesnewroman 15 ').grid(row=0)
    booktitle = Entry(f)
    booktitle.grid(row=1)
    Button(f, text='ADD BOOK', pady=20, command=add_book_to_library).grid(row=2)
    f.pack()


def add_book():
    new = Tk()
    new.title('ADD BOOK')
    new.geometry("800x600")

    def add_book_to_library():
        title = booktitle.get()
        if title:
            new_book = Book(title)
            books.append(new_book)
            mg.showinfo('Add Book', f"{title} has been added to the library.")
            new.destroy()
        else:
            mg.showwarning('Add Book', 'Please enter a book title.')
        save_student_details()

    f = Frame(new)
    Label(f, text='Enter the book title you want to add', font='timesnewroman 15 ').grid(row=0)
    booktitle = Entry(f)
    booktitle.grid(row=1)
    Button(f, text='ADD BOOK', pady=20, command=add_book_to_library).grid(row=2)
    f.pack()

studentid = StringVar(value='')
studentname = StringVar(value='')
studentdep = StringVar(value='')
studentgmail = StringVar(value='')
def student_update_details():
    new = Tk()
    new.title('STUDENT UPDATION WINDOW')
    new.geometry("800x600")
    f = Frame(new)

    def detail():
        student_data = (id.get(),name.get(),dep.get(),gmail.get())
        studentdetail.append(student_data)
        print(studentdetail)

    Label(f, text='enter student id:', font='cambria 35').grid()
    id = Entry(f, textvariable=studentid, width=35)
    id.grid(row=1)
    Label(f, text='enter student name:', font='cambria 35').grid(row=2)
    name= Entry(f, textvariable=studentname, width=35)
    name.grid(row=3)
    Label(f, text='enter student department:', font='cambria 35').grid(row=4)
    dep= Entry(f, textvariable=studentdep, width=35)
    dep.grid(row=5)
    Label(f, text='enter student Gmail:', font='cambria 35').grid(row=6)
    gmail= Entry(f, textvariable=studentgmail, width=35)
    gmail.grid(row=7)
    Button(f, text='Enter', padx=15, pady=15, command=detail).grid(row=8)
    Button(f, text='Click here to update more details', command=student_update_details).grid(row=9)
    f.grid()

mb = Menubutton(root, text="WHAT YOU WANT TO DO", font='lucida 45 bold', background='white',foreground='blue')
mb.pack()

menu = Menu(mb, tearoff=0)
mb["menu"] = menu

bVar = IntVar()
rVar = IntVar()
aVar = IntVar()
studentVar = IntVar()

menu.add_checkbutton(label='BORROW BOOK', variable=bVar, command=borrow_book, font='lucida 35')
menu.add_checkbutton(label='RETURN BOOK', variable=rVar, command=return_book, font='lucida 35')
menu.add_checkbutton(label='ADD BOOK', variable=aVar, command=add_book, font='lucida 35')
menu.add_checkbutton(label='UPDATE STUDENT DETAILS', variable=studentVar, command=student_update_details, font='lucida 35')

root.mainloop()