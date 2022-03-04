import sqlite3

conn=sqlite3.connect('test.db')

def insertdata(task):
    query="INSERT INTO todo(task) VALUES(?);"
    conn.execute(query,(task,))
    conn.commit()

def deletebyid(taskid):
    query="DELETE FROM todo WHERE id=?;"
    conn.execute(query,(taskid,))
    conn.commit()

def updatedata(taskid,newtask):
    query="UPDATE todo SET task=? WHERE id=?;"
    conn.execute(query,(newtask,taskid))
    conn.commit()

def listdata():
    query="SELECT task from todo"
    dataarry=[]
    # query='SELECT * FROM todo;'
    # for rows in conn.execute(listdata):
    # print(rows)
    # return SELECT * FROM todo;
    dayaarry=conn.execute(query,())
    conn.commit()
    return dataarry

print(listdata())

conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);''')

# query="INSERT INTO todo(task) VALUES('Record');"
# conn.execute(query)
# conn.commit()

# insertdata("Record")

# updatedata(4,"Welcome back! Warmth welcome on our website.")

# deletebyid(4)

listdata()

# updatedata(2,"congratulations! You have updated this task successfully.")
# updatedata(4,"Welcome back! Warmth welcome on our website.")

query='SELECT * FROM todo;'
for rows in conn.execute(listdata):
    print(rows)

print("Database connected")
conn.close()