#-----------------------------import statements
import sqlite3
#------------------------------Create the SQLite file
conn = sqlite3.connect('counter.sqlite')
cur = conn.cursor()

#-------------------------------------define functions
print("simple counter")

def reset_count():
    cur.executescript('''
    DROP TABLE IF EXISTS Count;

    CREATE TABLE Count (
        id  INTEGER PRIMARY KEY NOT NULL UNIQUE,
        number  INTEGER
    );
    ''')
    cur.execute('''INSERT OR IGNORE INTO Count (number) 
            VALUES ( ? )''', ( 0,) )
    conn.commit()

def find_current():
    cur.execute('SELECT number FROM Count ')
    current = cur.fetchone()[0]
    return(current)

def plus_one():
    cur.execute('''UPDATE Count SET number = ( ? )''', ((find_current() + 1), ))
    conn.commit()


def minus_one():
    cur.execute('''UPDATE Count SET number = ( ? )''', ((find_current() - 1), ))
    conn.commit()
#----------------------------------begin operations
while True:
    inp = input("add or subtract? ")
    if inp == "add":
        plus_one()
        print(find_current())
        
    if inp == "subtract":
        minus_one()
        print(find_current())
        
        quit()
    if inp == "restart": 
        reset_count()
        print(find_current())
