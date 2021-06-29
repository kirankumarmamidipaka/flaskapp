import pymysql
import json
# import aws_credentials as rds

conn = pymysql.connect(
        
        user = "root", # admin
        password = "Narik25$", #adminadmin
        db = "flask", #test
        
        )




def add_user(email,firstname,lastname,password):
    try:
        cur=conn.cursor()
        cur.execute("INSERT INTO users (email,firstname,lastname,password) VALUES (%s,%s,%s,%s)", (email,firstname,lastname,password))
        conn.commit()
    except pymysql.IntegrityError as err:
        return err


def get_user(email):
    cur=conn.cursor()
    cur.execute("SELECT *  FROM users where email= %s",email)
    details = cur.fetchone()
    if details == None:
        return None
    user_details = convert_to_dict(list(details))
    #return json.dumps(user_details)
    return user_details
def convert_to_dict(user_tuple):
    return {'email': user_tuple[0], 'firstname': user_tuple[1],
            'lastname': user_tuple[2], 'password': user_tuple[3]}
def get_all_users():
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    details = cur.fetchall()
    list_users= [convert_to_dict(list(user)) for user in details]
    #return json.dumps(list_users)
    return list_users
def update_user(email,firstname,lastname,password):
    cur=conn.cursor()
    cur.execute("update users set email=%s,firstname=%s,lastname=%s,password=%s where email=%s", (email,firstname,lastname,password,email))
    conn.commit()

def delete_user(email):

    try:
        cur=conn.cursor()
        cur.execute("delete from users where email=%s",email)
        conn.commit() 
    except pymysql.IntegrityError as err:
        return err




print(delete_user("kiran123@gmail.com"))
#print(add_user("kiran123@gmail.com","kiran","kumar","pwdddd"))
#add_user("ramesh123@gmail.com","ramesh","kumar","1234")
#add_user("suresh@gmail.com","suresh","kumar","243555")
#print(get_user("kiran12ghg3@gmail.com"))
#print(get_all_users())
#print(update_user("kiran123@gmail.com","kiran","kalyan","pwdddd1234"))
#print(update_user("kiran123@gmail.com","kiran","kalyan","pwdddd"))
#print(update_user("kiran123@gmail.com","kiran","kalyan","pwdddd"))
#print(update_user("kiran123@gmail.com","kiran","kalyan","pwdddd"))