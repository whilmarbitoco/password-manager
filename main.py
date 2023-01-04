import sqlite3, sys



conn = sqlite3.connect("bin/db/database.db")
c = conn.cursor()


def display():
  c.execute("SELECT * FROM passwords")
  rows = c.fetchall()
  for row in rows:
      print(f"""
###############
Site: {row[1]}  
Name: {row[2]}
###############
""")


def passlist(name):
    c.execute("SELECT site, uname, upass FROM passwords WHERE uname=?", (name,))
    rows = c.fetchone()
    site, uname, upass = rows
    print(f"Website: {site} | Username: {uname} | Password: {upass}")
    


def addpass(site, name, upass):
    c.execute("INSERT INTO passwords (site, uname, upass) VALUES (?, ?, ?)", (site, name, upass))
    conn.commit()
    

def delpass(name):
    c.execute("DELETE FROM passwords WHERE uname=?", (name,))
    conn.commit()
    


def main():
    print(""" 
1. View password
2. Add password
3. Delete password
4. Display password
5. Exit
""")
    prompt = input("[choose]> ")
    if prompt == "1":
        name = input("[username]> ")
        passlist(name)
    elif prompt == "2":
        site = input("[website]> ")
        name = input("[username]> ")
        password = input("[password]> ")
        addpass(site, name, password)
    elif prompt == "3":
        name = input("[username]> ")
        delpass(name)
    elif prompt == "4":
        display()
    elif prompt == "5":
        sys.exit()
    else:
        print("404")
        
        
while True:
    main()