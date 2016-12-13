#导入mysql驱动
import mysql.connector


# conn=mysql.connector.connect(user='root',password='password',database='test')
# cusor=conn.cursor()

# cusor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cusor.execute('insert into user (id,name) values (%s,%s)',['1','Michael'])
# print(cusor.rowcount)

# conn.commit()
# conn.close()

conn=mysql.connector.connect(user='root',password='password',database='test')
cusor=conn.cursor()
cusor.execute('select * from user where id =%s',('1',))
values=cusor.fetchall()
print(values)

cusor.close()
conn.close()