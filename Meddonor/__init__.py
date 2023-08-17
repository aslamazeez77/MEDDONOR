def connect():
    import pymysql
    con=pymysql.connect(host="localhost",user="root",password="",database="meddonor")
    return con
def ccdate():
    import datetime
    now=datetime.datetime.now()
    y=now.year
    m=now.month
    d=now.day
    cdate=str(y)+"-"+str(m)+"-"+str(d)
    return(cdate)
