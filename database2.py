import tkinter as tk
import sqlite3

root = tk.Tk()
root.geometry("500x500")
root.configure(background = "blue")
conn = sqlite3.connect("database.db")

c = conn.cursor()
##if sqlite3.OperationalError:
##    c.execute("""CREATE TABLE addresses(
##
##    first_name text,
##    last_name text,
##    age integer
##    )
##
##
##
##       """)

def submit():
    try:
        conn = sqlite3.connect("database.db")

        c = conn.cursor()

        c.execute("""INSERT INTO addresses VALUES (:first, :last, :age)""",
                {
                    "first": f.get(),
                    "last": l.get(),
                    "age": a.get()

                    })



        conn.commit()
        conn.close
        f.delete(0, tk.END)
        l.delete(0, tk.END)
        a.delete(0, tk.END)
        
    except:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE addresses(

        first_name text,
        last_name text,
        age integer
        )



           """)
        

        

        c.execute("""INSERT INTO addresses VALUES (:first, :last, :age)""",
                {
                    "first": f.get(),
                    "last": l.get(),
                    "age": a.get()

                    })



        conn.commit()
        conn.close
        f.delete(0, tk.END)
        l.delete(0, tk.END)
        a.delete(0, tk.END)


def query():
    conn = sqlite3.connect("database.db")

    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    p = c.fetchall()
    w = ""
    for t in p:
        w += str(t) + "\n" 
       # print (w)
   # print (w)
    label = tk.Label(root, text = w)
    label.grid(row = 7, column = 1, columnspan = 2)
    


    conn.commit()
    conn.close


def delete():
    
    conn = sqlite3.connect("database.db")

    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + d.get())

    

    conn.commit()
    conn.close

f = tk.Entry(root, width = 30)
f.grid(row = 0, column = 1, columnspan = 2, padx = 10)

fm = tk.Label(root, text = "Firstname", font = ("arial", 14))
fm.grid(row = 0, column=0, padx = 10)

l = tk.Entry(root, width = 30)
l.grid(row = 1, column = 1, columnspan = 2, padx = 10)

lm = tk.Label(root, text = "Lastname", font = ("arial", 14))
lm.grid(row = 1, column=0, padx = 10)

a = tk.Entry(root, width = 30)
a.grid(row = 2, column = 1, columnspan = 2, padx = 10)

am = tk.Label(root, text = "Age", font = ("arial", 14))
am.grid(row = 2, column=0, padx = 10)

dm = tk.Label(root, text = "Delete Id", font = ("arial", 14))
dm.grid(row = 6, column=0, padx = 10)

d = tk.Entry(root, width = 30)
d.grid(row = 6, column = 1, columnspan = 2, padx = 10)

s = tk.Button(root, text = "SUBMIT", font = ("arial", 13), command = submit)
s.grid(row = 3, column = 0, columnspan = 3, padx = 10)

q = tk.Button(root, text = "QUERY", font = ("arial", 13), command = query)
q.grid(row = 4, column = 0, columnspan = 3, padx = 10)

v = tk.Button(root, text = "DELETE", font = ("arial", 13), command = delete)
v.grid(row = 5, column = 0, columnspan = 3, padx = 10)

conn.commit()
conn.close
root.mainloop()
