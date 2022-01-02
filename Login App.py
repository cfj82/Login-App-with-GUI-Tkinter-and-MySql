
import tkinter as tk
from tkinter import messagebox
import sqlite3

# create db using SQLite
con = sqlite3.connect('userdata.db')
# create table for database
cur = con.cursor()
# below creates columns for table
# tabel population below...
cur.execute('''CREATE TABLE IF NOT EXISTS record(name text, 
        email text, 
        contact number, 
        gender text, 
        country text, 
        password text)''')
con.commit()  # send to sql


root = tk.Tk()
root.config(bg="#0B5A81")
root.geometry("1010x525")
root.title("Login Page")


def login_check():
    # check db for record
    global username, pwd
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[1]
            pwd = row[5]
    except Exception as ep:
        messagebox.showerror('', str(ep))

    # validate login credentials
    uname = v_email_etr.get()  # variable used below for db check
    upw = v_pw_etr.get()  # variable used below for db check
    login_counter = 0
    if v_email_etr.get() == "":
        messagebox.showwarning('Warning', 'Enter Your Email')
    else:
        login_counter += 1
    if v_pw_etr.get() == "":
        messagebox.showwarning('Warning', 'Enter Your Password')
    else:
        login_counter += 1
    if login_counter == 2:  # count 2 means both fields populated
        if (uname == username and upw == pwd):
            messagebox.showinfo("Login Status", "Login Successfull")
        else:
            messagebox.showerror("Login Status", "Wrong Email or Password")


def registration_form():
    check_counter = 0  # count for confirming all fields filled
    if r_name_etr.get() == "":
        messagebox.showwarning('Warning', 'Enter Your Name')
    else:
        check_counter += 1
    if r_email_etr.get() == "":
        messagebox.showwarning('Warning', 'Enter Your Email')
    else:
        check_counter += 1
    if r_phone_etr.get() == "":
        messagebox.showwarning('Warning', 'Enter Your Phone Number')
    else:
        check_counter += 1
    if r_pw_etr.get() == "":
        messagebox.showwarning('Warning', 'Enter Your Password')
    else:
        check_counter +=1
    if r_repw_etr.get() == "":
        messagebox.showwarning('Warning', 'Re-Enter Your Password')
    else:
        check_counter += 1
    if r_pw_etr.get() != r_repw_etr.get():  # check for re-enter pw to match pw
        messagebox.showwarning('Warning', 'Passwords Must Match')
    else:
        check_counter += 1

    if check_counter == 6:  # count 6 means all fields filled
        # populate db table
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
                'name': r_name_etr.get(),
                'email': r_email_etr.get(),
                'contact': r_phone_etr.get(),
                'gender': gender_choice.get(),
                'country': county_option.get(),
                'password': r_pw_etr.get()
            })
            con.commit()  # write to db
            messagebox.showinfo("Confirmation", "Record Saved")

        except Exception as ep:
            messagebox.showerror("", str(ep))
    else:
        messagebox.showerror('Error', 'Save Failed')


# set for font
f = ("Times", 14)

# verification form
vef_frame = tk.Frame(root, bd=2, bg="#CCCCCC", relief='solid', padx=10, pady=10)  # bd is border
v_email_lbl = tk.Label(vef_frame, text="Enter Email", bg="#CCCCCC", font=("f"), )
v_email_lbl.grid(row=0, column=0, sticky="w", pady=10)

v_pw_lbl = tk.Label(vef_frame, text="Enter Password", bg="#CCCCCC", font=("f"), )
v_pw_lbl.grid(row=1, column=0, sticky="w", pady=10)

v_email_etr = tk.Entry(vef_frame, font=("f"), )
v_email_etr.grid(row=0, column=1, pady=10, padx=20)

# todo bind pw Entry
v_pw_etr = tk.Entry(vef_frame,  show="*", font=("f"), )  # show="*" shows star for characters
v_pw_etr.grid(row=1, column=1, pady=10, padx=20)

v_btn = tk.Button(vef_frame, width=15, text="Login", font=("f"), relief='solid', cursor="hand2", command=login_check)  # cursor=hand2 changes cursor image
v_btn.grid(row=2, column=1, pady=10, padx=20)

# registration form
reg_frame = tk.Frame(root, bd=2, bg="#CCCCCC", relief='solid', padx=10, pady=10)

r_name_lbl = tk.Label(reg_frame, text="Enter Name", bg="#CCCCCC", font=("f"), )
r_name_lbl.grid(row=0, column=0, sticky="w", pady=10)

r_email_lbl = tk.Label(reg_frame, text="Enter Email", bg="#CCCCCC", font=("f"), )
r_email_lbl.grid(row=1, column=0, sticky="w", pady=10)

r_phone_lbl = tk.Label(reg_frame, text="Enter Phone Number", bg="#CCCCCC", font=("f"), )
r_phone_lbl.grid(row=2, column=0, sticky="w", pady=10)

r_gender_lbl = tk.Label(reg_frame, text="Select Gender", bg="#CCCCCC", font=("f"), )
r_gender_lbl.grid(row=3, column=0, sticky="w", pady=10)

r_county_lbl = tk.Label(reg_frame, text="Select Country", bg="#CCCCCC", font=("f"), )
r_county_lbl.grid(row=4, column=0, sticky="w", pady=10)

r_pw_lbl = tk.Label(reg_frame, text="Enter Password", bg="#CCCCCC", font=("f"), )
r_pw_lbl.grid(row=5, column=0, sticky="w", pady=10)

r_repw_lbl = tk.Label(reg_frame, text="Re-Enter Password", bg="#CCCCCC", font=("f"), )
r_repw_lbl.grid(row=6, column=0, sticky="w", pady=10)

r_name_etr = tk.Entry(reg_frame, font=("f"), )
r_name_etr.grid(row=0, column=1, pady=10, padx=20)

r_email_etr = tk.Entry(reg_frame, font=("f"), )
r_email_etr.grid(row=1, column=1, pady=10, padx=20)

r_phone_etr = tk.Entry(reg_frame, font=("f"), )
r_phone_etr.grid(row=2, column=1, pady=10, padx=20)

# radio; frame and radiobuttons
gender_frame = tk.LabelFrame(reg_frame, bg="#CCCCCC", padx=10, pady=10)
gender_frame.grid(row=3, column=1, pady=10, padx=20)

# radio button
gender_choice = tk.StringVar()
gender_choice.set('robot')
male_gen_radio = tk.Radiobutton(gender_frame, text="Robot", bg="#CCCCCC", value="robot", variable=gender_choice, font=("Times", 13))
male_gen_radio.pack(expand=True, side='left')
female_gen_radio = tk.Radiobutton(gender_frame, text="Alien", bg="#CCCCCC", value="alien",  variable=gender_choice, font=("Times", 13))
female_gen_radio.pack(expand=True, side='left' )

# options menu
county_option = tk.StringVar()
countries = ["United States", "Earth", "Mars"]    # options for dropdown
# county_option.set(countries[2])  # default set on open
r_county = tk.OptionMenu(reg_frame, county_option, *countries)
r_county.config(width=15, font=("Times", 13))
r_county.grid(row=4, column=1, pady=10, padx=20)


r_pw_etr = tk.Entry(reg_frame, font=("f"), show="*")
r_pw_etr.grid(row=5, column=1, pady=10, padx=20)

r_repw_etr = tk.Entry(reg_frame, font=("f"), show="*")
r_repw_etr.grid(row=6, column=1, pady=10, padx=20)

r_register_btn = tk.Button(reg_frame, width=15, text="Register", font=("f"), relief='solid', cursor='hand2', command=registration_form)  # cursor=hand2 changes cursor image
r_register_btn.grid(row=7, column=1, pady=10, padx=20)

vef_frame.place(x=25, y=25)  # placement of registration frame
reg_frame.place(x=500, y=25)


root.mainloop()
