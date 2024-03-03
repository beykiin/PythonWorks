# def topla(a,b):
#     return a+b
# def cikar(a,b):
#     return a-b
# def carp(a,b):
#     return a*b
# def bol(a,b):
#     return a/b

# Bir database oluştur adı okul olacak ve bu data basede kullanıcılar ve öprenciler olarak iki tablomuz olacak kullanıcılarda kullanıcıadı şifre ve id olacak kullanıcı sisteme kullanıcı adı ve şifre yazarak girsin ve öğrenciler tablosuna ekleme günceclleme ve silme işlemi gerçekleştirsin ve sistemde yeni bir kullanıcı oluşturulabilsin ve çıkış gerçkeleşene kadar bu şekilde devam etsin kullanıcı 3defa hatlı şifrede bloke olsun ve kullnıcı adı bloke olsun öğrenciler tablosunda id ad soyad ve not bulunsun
import sqlite3 as sql
con=sql.connect("school.db")
cur=con.cursor()
def userss():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
                id INTEGER,
                username TEXT UNIQUE,
                password TEXT,
                PRIMARY KEY('id' AUTOINCREMENT)
    )""")
    con.commit()

def studentss():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
                id INTEGER,
                name TEXT,
                surname TEXT,
                grade INTEGER,
                PRIMARY KEY('id' AUTOINCREMENT)
    )""")
    con.commit()
def user_register(username,password):
    cur.execute(f"insert into users (username,password) values('{username}','{password}')")
    con.commit()
def studentSignUp(name,surname,grade):
    cur.execute(f"insert into students (name,surname,grade) values('{name}','{surname}',{grade})")
    con.commit()
def studentUpdate(id,grade):
    cur.execute(f"update students set grade={grade} where id={id}")
    con.commit()
def studentDelete(id):
    cur.execute(f"delete from students where id={id}")
    con.commit()
def userLogin(username,password):
    cur.execute(f"select username,password from users where username='{username}' and password='{password}'")
    info=cur.fetchone()
    if info is not None:
        return True
    else:
        return False
userss()
studentss()
count=0
while True:
    new=input("1-Login\n2-Create a new user\n3-Exit\nPlease enter the choice:")
    if new=='1':
        userName=input("Please enter the Username: ")
        userPassword=input("Please enter the your password: ")
        if userLogin(userName,userPassword)==False:
            print("Error of Username or Password!")
            count+=1
            if count==3:
                print("Unlock your accounts!")
                break
            continue
        count=0
        while True:
            islem=input("\tMenu\n1-Save the student\n2-Update the student\n3-Delete the student\n4-Exit")
            if islem=="1":
                names=input("Enter the student's name: ")
                surnames=input("Enter the student's surname: ")
                grades=int(input("Enter the student's grade: "))
                studentSignUp(names,surnames,grades)
            elif islem=="2":
                ids=int(input("Please enter the Id: "))
                newGrade=int(input("Please enter the student's new grade: "))
                studentUpdate(ids,newGrade)
            elif islem=="3":
                ids=int(input("Please you want delete student's Id: "))
                studentDelete(ids)
            elif islem=="4":
                break
            else:
                print("You make error of choice. Plaese try again.")
    elif new=='2':
        newUsername=input("Please enter the username: ")
        newUserPass=input("Please enter the password: ")
        user_register(newUsername,newUserPass)
    elif new=='3':
        break
    else:
        "Error of your a choice!"

        
