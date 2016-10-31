import sqlite3
from flask import g

def CreateDatase(dbname):
    conn = sqlite3.connect(dbname+'.db')
    print ('Opened database successfully');


def CreateTables(dbname):
    #conn = sqlite3.connect(dbnameh+'.db')
    print(dbname)
    #cur = conn.cursor()
    #cur.execute('CREATE TABLE Slider (name SliderHeading, Paragraph TEXT, city TEXT, pin TEXT)')  
    #con.commit()
    #print('reachedssss')
    #willTableName = tablename
    #print ('Table created successfully')
    conn = sqlite3.connect(dbname+'.db')
    sql_and_params ="CREATE TABLE if not exists Slider (SliderID INTEGER PRIMARY KEY AUTOINCREMENT,SliderHeading TEXT,Paragraph1 TEXT,Paragraph2 TEXT,Paragraph3 TEXT,Paragraph4 TEXT, ButtonLinkTitle TEXT, SliderImg TEXT)"
    conn.execute(sql_and_params)
    print ('Table created successfully');

    sql_and_params ="CREATE TABLE if not exists TabsButtons (TabsButtonID INTEGER PRIMARY KEY AUTOINCREMENT,ButtonTitleLineTitle TEXT, Description TEXT, Links1 TEXT,Links1Href TEXT,Links2 TEXT,Links2Href TEXT,Links3 TEXT,Links3Href TEXT,Links4 TEXT,Links4Href TEXT,Links5 TEXT,Links5Href TEXT,Links6 TEXT,Links6Href TEXT, HeaderImages TEXT,TotalLinkTitle TEXT,Icon TEXT)"
    conn.execute(sql_and_params)
    print ('Table created successfully');

    sql_and_params ="CREATE TABLE if not exists ScreenCenter (ScreenCenterID INTEGER PRIMARY KEY AUTOINCREMENT,Heading TEXT, Paragraph TEXT, Bullets1 TEXT, Buttelts2 TEXT, Image TEXT)"
    conn.execute(sql_and_params)
    print ('Table created successfully');

    sql_and_params ="CREATE TABLE if not exists CustomerSlider (CustomerSliderID INTEGER PRIMARY KEY AUTOINCREMENT, CustomerImg1 TEXT, CustomerImg2 TEXT, CustomerImg3 TEXT, CustomerImg4 TEXT, CustomerImg5 TEXT, CustomerImg6 TEXT)"
    conn.execute(sql_and_params)
    print ('Table created successfully');

    sql_and_params ="CREATE TABLE if not exists Testimonial (TestimonialID INTEGER PRIMARY KEY AUTOINCREMENT, CusImg TEXT, Heading TEXT, Title TEXT, Description TEXT)"
    conn.execute(sql_and_params)
    print ('Table created successfully');

    sql_and_params ="CREATE TABLE if not exists Footer (Heading TEXT, Lists1 TEXT, Lists2 TEXT, Lists3 TEXT, Lists4 TEXT, Lists5 TEXT, Lists6 TEXT)"
    conn.execute(sql_and_params)
    print ('Table created successfully');

    #sql_and_params ="CREATE TABLE if not exists AboutTable (Title TEXT, SubTitles TEXT)"
    #conn.execute(sql_and_params)
    #print ('Table created successfully');

    #sql_and_params ="CREATE TABLE if not exists AboutSubTable (Heading TEXT, SubHeading TEXT, TextDes TEXT, img TEXT)"
    #conn.execute(sql_and_params)
    #print ('Table created successfully');

    #sql_and_params ="CREATE TABLE if not exists TeamTable (Title TEXT, SubTitles TEXT, TextDes TEXT, img TEXT)"
    #conn.execute(sql_and_params)
    #print ('Table created successfully');

    #sql_and_params ="CREATE TABLE if not exists TeamSubTable (img TEXT, Heading TEXT, SubHeading TEXT, HrefTwiter TEXT, HrefFacebook TEXT, HrefLinkedIn TEXT)"
    #conn.execute(sql_and_params)
    #print ('Table created successfully');
    
    
    print ('All Table created successfully');




