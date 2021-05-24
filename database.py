import datetime
import MySQLdb
import uuid
import random
import string
from flask import session
from datetime import date


def db_connect():
    _conn = MySQLdb.connect(host="localhost", user='root',
                            password='root', db='speechtotext')
    c = _conn.cursor()

    return c, _conn

# ............................Login Action Start.............................................


def uloginact(utype, username, password):
    try:
        if utype == "user":
            c, conn = db_connect()
            j = c.execute("select * from user where email='" +
                          username+"' and password='"+password+"'")
            data = c.fetchall()
            a = data[0][1]
            print(a)
            conn.close()
            print(j)
            return a
        else:
            if(username == "admin" and password == "admin"):
                return True
            else:
                return False
    except Exception as e:
        return(str(e))

# ........................Login Action End....................................................
# .........................Registration Action Start..........................................


def ureg(name, email, pswd, mob):
    try:
        id = ''.join([random.choice(string.ascii_letters + string.digits)
                      for n in range(10)])
        print(id)
        c, conn = db_connect()
        j = c.execute("insert into user (id,name,email,password,mob) values ('" +
                      id+"','"+name+"','"+email+"','"+pswd+"','"+mob+"')")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
# .........................Registration Action End...............................................
# .........................View Action Start.....................................................


def getvoices(meeting):
    c, conn = db_connect()
    c.execute("select * from speechdata where meeting='"+meeting+"'")
    result = c.fetchall()
    conn.close()
    return result


def meetingnames():
    c, conn = db_connect()
    c.execute("select * from meetings")
    result = c.fetchall()
    conn.close()
    return result


def getcombinedchats(mname):
    c, conn = db_connect()
    c.execute("select * from combined where meeting='"+mname+"'")
    result = c.fetchall()
    conn.close()
    return result

# .........................View Action End.........................................................
# .........................Add Action Start........................................................


def storedata(voice, meeting, time):
    try:
        name = session['name']
        c, conn = db_connect()
        j = c.execute("insert into speechdata (name,voice,meeting,time) values ('" +
                      name+"','"+voice+"','"+meeting+"','"+time+"')")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        return(str(e))


def storecombinedchats(chats, mname):
    try:
        c, conn = db_connect()
        print("insert into combined (meeting,chats) values ('"+mname+"','"+chats+"')")
        j = c.execute(
            "insert into combined (meeting,chats) values ('"+mname+"','"+chats+"')")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        return(str(e))


def aaddmeeting(meeting):
    try:
        c, conn = db_connect()
        j = c.execute(
            "insert into meetings (meetingname) values ('"+meeting+"')")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

# .........................Add Action Start........................................................


if __name__ == "__main__":
    print(db_connect())
