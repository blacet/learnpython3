#要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
#连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

#导入SQLite驱动
import sqlite3
#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')
#创建一个Cursor
cursor = conn.cursor()
#执行一条SQL语句，创建user表
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
#通过rowcount获得插入的行数
cursor.rowcount

#关闭cursor
cursor.close()
#提交事务
conn.commit()
#关闭Connection
conn.close()