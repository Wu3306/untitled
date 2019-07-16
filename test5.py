#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 10:44
# @Author  : Ryu
# @Site    :
# @File    : test5.py
# @Software: PyCharm
from datetime import datetime
import pyodbc
import random
import uuid

class ODBC_MS:
    def __init__(self, DRIVER, SERVER, DATABASE, UID, PWD):
        self.DRIVER = DRIVER
        self.SERVER = SERVER
        self.DATABASE = DATABASE
        self.UID = UID
        self.PWD = PWD
        # initialization

    def __GetConnect(self):
        # Connect to the DB
        if not self.DATABASE:
            raise (NameError, "no setting db info")
        self.conn = pyodbc.connect(DRIVER=self.DRIVER, SERVER=self.SERVER, DATABASE=self.DATABASE, UID=self.UID,
                                   PWD=self.PWD, charset="UTF-8")
        # self.conn = pyodbc.connect(DRIVER=self.DRIVER, SERVER=self.SERVER, DATABASE=self.DATABASE, UID=self.UID, PWD=self.PWD)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "connected failed!")
        else:
            print('connect success')
        return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()  # 建立链接并创建数据库操作指针
        cur.execute(sql)  # 通过指针来执行sql指令
        ret = cur.fetchall()  # 通过指针来获取sql指令响应数据
        cur.close()  # 游标指标关闭
        self.conn.close()  # 关闭数据库连接
        return ret
    def ExecNoQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()  # 连接句柄来提交
        cur.close()
        self.conn.close()

if __name__ == '__main__':
    try:
        now = datetime.now()
        nowstr = now.strftime("%Y-%m-%d")
        nowtime = now.strftime("%H")
        nowweek = now.weekday()
        if nowweek < 5:
            if int(nowtime) < 9:
                time = []
                time3 = []
                time4 = []
                for i in range(0, 10):
                    a = random.randrange(10, 29)
                    b = random.randrange(0, 59)
                    c = random.randrange(1, 10)
                    time.append(nowstr + " 08:" + str(a) + ":" + str(b))
                    time4.append(nowstr + " 08:" + str(a + c) + ":" + str(b))
                    time3.append('08' + ':' + str(a))
                print(time, time3, time4)

                person = [['巫啸', '058113', '393'], ['张华', '057928', '386'], ['尹志刚', '057710', '387'],
                          ['华婧丽', '057656', '388'],
                          ['吴素青', '057570', '389'], ['张国平', '057554', '390'], ['贡元', '058321', '391'],
                          ['张文彬', '058217', '392'],
                          ['徐志辉', '058160', '394'], ['徐国栋', '000271', '974']]
                ms = ODBC_MS('{SQL SERVER}', r'172.21.153.239', 'yun11131', 'sa', 'Admin123')

                for i in range(0, 10):
                    sql = '''
                                    insert
                                    into
                                    KQ_Download
                                    (
                                        Person_ID,
                                        Card_No,
                                        Brush_Date,
                                        Brush_Time,
                                        Moc_No,
                                        Data_Flag,
                                        Brush_DateTime,
                                        Is_Falsity,
                                        FileName,
                                        eventUuid,
                                        Create_DateTime
                                    ) VALUES( '''
                    sql = sql + "" + person[i][2] + ","
                    sql = sql + "'" + person[i][1] + "',"
                    sql = sql + "'" + nowstr + "',"
                    sql = sql + "'" + time3[i] + "',"
                    sql = sql + "'19',"
                    sql = sql + "10,"
                    sql = sql + "'" + time[i] + "',"
                    sql = sql + "0,"
                    sql = sql + "'_,_',"
                    sql = sql + "'" + str(uuid.uuid1()) + "',"
                    sql = sql + "'" + time4[i] + "'"
                    sql = sql + ")"
                    print(sql)
                    ms.ExecNoQuery(sql)
            elif int(nowtime) > 10 and int(nowtime) < 12:
                time = []
                time3 = []
                time4 = []
                for i in range(0, 10):
                    a = random.randrange(20, 39)
                    b = random.randrange(0, 59)
                    c = random.randrange(1, 10)
                    time.append(nowstr + " 11:" + str(a) + ":" + str(b))
                    time4.append(nowstr + " 11:" + str(a + c) + ":" + str(b))
                    time3.append('11' + ':' + str(a))
                print(time, time3, time4)

                person = [['巫啸', '058113', '393'], ['张华', '057928', '386'], ['尹志刚', '057710', '387'],
                          ['华婧丽', '057656', '388'],
                          ['吴素青', '057570', '389'], ['张国平', '057554', '390'], ['贡元', '058321', '391'],
                          ['张文彬', '058217', '392'],
                          ['徐志辉', '058160', '394'], ['徐国栋', '000271', '974']]
                ms = ODBC_MS('{SQL SERVER}', r'172.21.153.239', 'yun11131', 'sa', 'Admin123')

                for i in range(0, 10):
                    sql = '''
                                    insert
                                    into
                                    KQ_Download
                                    (
                                        Person_ID,
                                        Card_No,
                                        Brush_Date,
                                        Brush_Time,
                                        Moc_No,
                                        Data_Flag,
                                        Brush_DateTime,
                                        Is_Falsity,
                                        FileName,
                                        eventUuid,
                                        Create_DateTime
                                    ) VALUES( '''
                    sql = sql + "" + person[i][2] + ","
                    sql = sql + "'" + person[i][1] + "',"
                    sql = sql + "'" + nowstr + "',"
                    sql = sql + "'" + time3[i] + "',"
                    sql = sql + "'19',"
                    sql = sql + "10,"
                    sql = sql + "'" + time[i] + "',"
                    sql = sql + "0,"
                    sql = sql + "'_,_',"
                    sql = sql + "'" + str(uuid.uuid1()) + "',"
                    sql = sql + "'" + time4[i] + "'"
                    sql = sql + ")"

                    print(sql)
                    ms.ExecNoQuery(sql)
            elif int(nowtime) > 12 and int(nowtime) < 14:
                time = []
                time3 = []
                time4 = []
                for i in range(0, 10):
                    a = random.randrange(20, 59)
                    b = random.randrange(0, 59)
                    c = random.randrange(1, 10)
                    time.append(nowstr + " 13:" + str(a) + ":" + str(b))
                    time4.append(nowstr + " 13:" + str(a + c) + ":" + str(b))
                    time3.append('13' + ':' + str(a))
                print(time, time3, time4)

                person = [['巫啸', '058113', '393'], ['张华', '057928', '386'], ['尹志刚', '057710', '387'],
                          ['华婧丽', '057656', '388'],
                          ['吴素青', '057570', '389'], ['张国平', '057554', '390'], ['贡元', '058321', '391'],
                          ['张文彬', '058217', '392'],
                          ['徐志辉', '058160', '394'], ['徐国栋', '000271', '974']]
                ms = ODBC_MS('{SQL SERVER}', r'172.21.153.239', 'yun11131', 'sa', 'Admin123')

                for i in range(0, 10):
                    sql = '''
                                    insert
                                    into
                                    KQ_Download
                                    (
                                        Person_ID,
                                        Card_No,
                                        Brush_Date,
                                        Brush_Time,
                                        Moc_No,
                                        Data_Flag,
                                        Brush_DateTime,
                                        Is_Falsity,
                                        FileName,
                                        eventUuid,
                                        Create_DateTime
                                    ) VALUES( '''
                    sql = sql + "" + person[i][2] + ","
                    sql = sql + "'" + person[i][1] + "',"
                    sql = sql + "'" + nowstr + "',"
                    sql = sql + "'" + time3[i] + "',"
                    sql = sql + "'19',"
                    sql = sql + "10,"
                    sql = sql + "'" + time[i] + "',"
                    sql = sql + "0,"
                    sql = sql + "'_,_',"
                    sql = sql + "'" + str(uuid.uuid1()) + "',"
                    sql = sql + "'" + time4[i] + "'"
                    sql = sql + ")"

                    print(sql)
                    ms.ExecNoQuery(sql)
            else:
                time = []
                time3 = []
                time4 = []
                for i in range(0, 10):
                    a = random.randrange(1, 59)
                    b = random.randrange(0, 59)
                    c = random.randrange(1, 10)
                    time.append(nowstr + " 18:" + str(a) + ":" + str(b))
                    time4.append(nowstr + " 18:" + str(a + c) + ":" + str(b))
                    time3.append('18' + ':' + str(a))

                person = [['巫啸', '058113', '393'], ['张华', '057928', '386'], ['尹志刚', '057710', '387'],
                          ['华婧丽', '057656', '388'],
                          ['吴素青', '057570', '389'], ['张国平', '057554', '390'], ['贡元', '058321', '391'],
                          ['张文彬', '058217', '392'],
                          ['徐志辉', '058160', '394'], ['徐国栋', '000271', '974']]
                ms = ODBC_MS('{SQL SERVER}', r'172.21.153.239', 'yun11131', 'sa', 'Admin123')

                for i in range(0, 10):
                    sql = '''
                                    insert
                                    into
                                    KQ_Download
                                    (
                                        Person_ID,
                                        Card_No,
                                        Brush_Date,
                                        Brush_Time,
                                        Moc_No,
                                        Data_Flag,
                                        Brush_DateTime,
                                        Is_Falsity,
                                        FileName,
                                        eventUuid,
                                        Create_DateTime
                                    ) VALUES( '''
                    sql = sql + "" + person[i][2] + ","
                    sql = sql + "'" + person[i][1] + "',"
                    sql = sql + "'" + nowstr + "',"
                    sql = sql + "'" + time3[i] + "',"
                    sql = sql + "'19',"
                    sql = sql + "10,"
                    sql = sql + "'" + time[i] + "',"
                    sql = sql + "0,"
                    sql = sql + "'_,_',"
                    sql = sql + "'" + str(uuid.uuid1()) + "',"
                    sql = sql + "'" + time4[i] + "'"
                    sql = sql + ")"

                    ms.ExecNoQuery(sql)
        else:
            print("today is not workday")


    except Exception as e:
        print(str(e))
        a = input('Please press enter key to exit ...')
        if a:
            exit()

