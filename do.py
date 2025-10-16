import sqlite3
conn = sqlite3.connect('to_do_list\\list.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS todo 
    (id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    completed BOOLEAN NOT NULL CHECK (completed IN ('❌', '✅')))''')

    
def add_task():
        while True:
            task = input("Enter the task you want to add: ")
            cur.execute('''INSERT INTO todo (task, completed) VALUES (?, '❌')''', (task,))
            conn.commit()
            print("Task added successfully.")
            extra = input("Do you want to add another task? (yes/no): ").lower()
            if extra == 'yes':
                continue
            elif extra == 'no':
                print("ok")
                break

def view_tasks():
    show=cur.execute('''select * from todo''')
    for line in show:
        x = ' || '.join(str(item) for item in line)
        print(x + "\t\t")
        print("-----------------------------")

def delete_task():
    view_tasks()
    id=int(input("Enter the id of the task you want to delete: "))
    cur.execute('''DELETE FROM todo WHERE id = ?''', (id,))
    conn.commit()
    print("Task deleted successfully.")

def mark_completed():
    view_tasks()
    id = int(input("Enter the id of the task you want to mark as completed: "))
    cur.execute('''update todo set completed='✅' where id=?''',(id,))
    view_tasks()
    conn.commit()
    print("Task marked as completed.")

while True:
    user=int(input("Welcome to the to do list command line interface/app: \n" 
     "1. Add a task\n"
     "2. Do you want to see all the tasks you have?\n"
     "3. Delete a task\n"
     "4. Mark a task as completed\n"
     "5. Exit the application\n"
     "Enter the response you want from the ID(i.e: 1,2,3):"))
    
    if user==1:
        add_task()
    elif user==2:
        view_tasks()
    elif user==3:
        delete_task()
    elif user==4:
        mark_completed()
    elif user==5:
        print("Exiting the application.")
        break