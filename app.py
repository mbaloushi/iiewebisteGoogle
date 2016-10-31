from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os
import sqlite3
from flask import g
import modules.Myfn

app = Flask(__name__)


print('Program Started')
modules.Myfn.CreateDatase('myDb')
modules.Myfn.CreateTables('myDb')

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/admin')
def index():
    return render_template('/admin/index.html')

@app.route('/slider')
def Slider():
    return render_template('/admin/slider.html')


@app.route('/tabsbtn')
def tabsbutton():
    return render_template('/admin/TabsSection.html')

@app.route('/ScreenCenter')
def ScreenCenter():
    return render_template('/admin/CenterScreenNew.html')


#Slider Start
@app.route('/viewslider')
def ViewSlider():
    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #Slider
    myqry = 'SELECT * FROM Slider'
    print(myqry)
    cur.execute(myqry)
    SliderData = cur.fetchall();
    print(SliderData[0])
    con.commit()
    con.close()
    return render_template('/admin/ViewSliders.html',**locals())


@app.route('/Delete', methods=['POST'])
def DeleteSlider():
    con = sqlite3.connect('myDb'+'.db')
    DeleteFileNo = request.form['Record_to_delete']
    #Slider
    myqry = 'DELETE FROM Slider WHERE SliderID ='+DeleteFileNo
    print(myqry)
    con.execute(myqry)
    con.commit()
    con.close()
    ShowDeleteMsg='Yes'
    return render_template('/admin/ViewSliders.html',**locals())




@app.route('/SliderNew', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file

        try:
         SliderHeading = request.form['SliderHeading']
         Paragraph1 = request.form['Paragraph1']
         Paragraph2 = request.form['Paragraph1']
         Paragraph3 = request.form['Paragraph3']
         Paragraph4 = request.form['Paragraph4']
         ButtonLinkTitle = request.form['ButtonLinkTitle']
         FinalFileName = finalFileDB
         print(SliderHeading)
         
         with sqlite3.connect("myDb.db") as con:
            cur = con.cursor()
            cur.execute('INSERT INTO Slider (SliderHeading, Paragraph1, Paragraph2, Paragraph3, Paragraph4, ButtonLinkTitle, SliderImg) values (?, ?, ?, ?, ?, ?, ?)', [SliderHeading, Paragraph1, Paragraph2, Paragraph3, Paragraph4, ButtonLinkTitle, FinalFileName])
            con.commit()
            msg = "Record successfully added"
        except:
         con.rollback()
         msg = "error in insert operation"
      
        finally:
         return render_template("admin/Slider.html")
         con.close()

#Slider End        
       


#TabsButton Start

@app.route('/DeleteTabs', methods=['POST'])
def DeleteTabs():
    con = sqlite3.connect('myDb'+'.db')
    DeleteFileNo = request.form['Record_to_delete']
    #Slider
    myqry = 'DELETE FROM TabsButtons WHERE TabsButtonID ='+DeleteFileNo
    print(myqry)
    con.execute(myqry)
    con.commit()
    con.close()
    ShowDeleteMsg='Yes'
    return render_template('/ViewTabsButton.html',**locals())



@app.route('/ViewTabsBtn')
def ViewTabsBtn():
    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #TabsBtn
    myqry = 'SELECT * FROM TabsButtons'
    print(myqry)
    cur.execute(myqry)
    tabsButtonData = cur.fetchall();
    con.commit()
    con.close()
    return render_template('/admin/ViewTabsButton.html',**locals())


@app.route('/tabsMenu', methods=['POST'])
def tabsMenuupload():
    print('insdside')
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('upload ok')
    try:
         print('upload ok')  
         #start
         print('upload ok')
            
         ButtonTitle = request.form['ButtonTitle']
         print(ButtonTitle)
         Description = request.form['Description']
         print(Description)
         Links1 = request.form['Links1']
         print(Links1)
         Links1Href = request.form['Links1Href']
         print(Links1Href)
         Links2 = request.form['Links2']
         print('line2')
         Links2Href = request.form['Links2Href']
         print(Links2Href)
         Links3 = request.form['Links3']
         print(Links3)
         Links3Href = request.form['Links3Href']
         print(Links3Href)
         Links4 = request.form['Links4']
         print(Links4)
         Links4Href = request.form['Links4Href']
         print(Links4Href)
         Links5 = request.form['Links5']
         print(Links5)
         Links5Href = request.form['Links5Href']
         print(Links5Href)
         Links6 = request.form['Links6']
         print(Links6)
         Links6Href = request.form['Links6Href']
         print(Links6Href)
         TotalLinkTitle = request.form['TotalLinkTitle']
         print(TotalLinkTitle)
         Icon = request.form['Icon']
         print(Icon)
         FinalFileName = finalFileDB
         print(FinalFileName)
         
         print('All OK Going')

         
         
         #end
         FinalFileName = finalFileDB
         print('OK ONSIDE')
         
         with sqlite3.connect("myDb.db") as con:
             print('OK ONSIDE')
             cur = con.cursor()
             qoutes ="'"
             print(qoutes)
             MYQUERY = 'INSERT INTO TabsButtons (ButtonTitleLineTitle, Description, Links1, Links1Href, Links2, Links2Href, Links3, Links3Href, Links4, Links4Href, Links5, Links5Href, Links6, Links6Href, HeaderImages, TotalLinkTitle, Icon) VALUES ('+qoutes+ButtonTitle+qoutes+','+qoutes+Description+qoutes+','+qoutes+Links1+qoutes+','+qoutes+Links1Href+qoutes+','+qoutes+Links2+qoutes+','+qoutes+Links2Href+qoutes+','+qoutes+Links3+qoutes+','+qoutes+Links3Href+qoutes+','+qoutes+Links4+qoutes+','+qoutes+Links4Href+qoutes+','+qoutes+Links5+qoutes+','+qoutes+Links5Href+qoutes+','+qoutes+Links6+qoutes+','+qoutes+Links6Href+qoutes+','+qoutes+FinalFileName+qoutes+','+qoutes+TotalLinkTitle+qoutes+','+qoutes+Icon+qoutes+')'
             print(MYQUERY)
             cur.execute(MYQUERY)
             con.commit()
             msg = "Record successfully added"
    except:
            
            con.rollback()
            msg = "error in insert operation"
      
    finally:
            msg = "error in insert operation"
            return render_template("admin/TabsSection.html")
            con.close()


#TabsButtonEnd


#CenterScreen Start


@app.route('/ViewCenterScreen')
def viewCenterScreen():
    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #Slider
    myqry = 'SELECT * FROM ScreenCenter'
    print(myqry)
    cur.execute(myqry)
    ScreenCenter = cur.fetchall();
    con.commit()
    con.close()
    return render_template('/admin/ViewCenterScreen.html',**locals())


@app.route('/DeleteCenter', methods=['POST'])
def DeleteCenter():
    con = sqlite3.connect('myDb'+'.db')
    DeleteFileNo = request.form['Record_to_delete']
    #Slider
    myqry = 'DELETE FROM ScreenCenter WHERE ScreenCenterID ='+DeleteFileNo
    print(myqry)
    con.execute(myqry)
    con.commit()
    con.close()
    ShowDeleteMsg='Yes'
    return render_template('admin/CenterScreenNew.html',**locals())


@app.route('/CenterScreenNew', methods=['POST'])
def CenterScreenNew():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')

    try:
        
        ScreenHeading = request.form['Heading']
        print(ScreenHeading)
        Paragraph = request.form['Paragraph']
        print(Paragraph)
        Bullets1 = request.form['Bullets1']
        print(Bullets1)
        Buttelts2 = request.form['Buttelts2']
        print(Buttelts2)
        FinalFileName = finalFileDB
        
         
        with sqlite3.connect("myDb.db") as con:
            
            qoute="'"
            myquery2 ='INSERT INTO ScreenCenter (Heading, Paragraph, Bullets1, Buttelts2, Image) values ('+qoute+ScreenHeading+qoute+','+qoute+Paragraph+qoute+','+qoute+Bullets1+qoute+','+qoute+Buttelts2+qoute+','+qoute+FinalFileName+qoute+')'
            print(myquery2)
            cur = con.cursor()
            cur.execute(myquery2)
            con.commit()
            msg = "Record successfully added"
    except:
        
        con.rollback()
        msg = "error in insert operation"
      
    finally:
        
        return render_template("admin/CenterScreenNew.html")
        con.close()


#CenterScree End
      

#CutomerIcons



@app.route('/DeleteCutomerIcon', methods=['POST'])
def DeleteCutomerIcon():
    con = sqlite3.connect('myDb'+'.db')
    DeleteFileNo = request.form['Record_to_delete']
    #DeleteCustomer Query
    myqry = 'DELETE FROM CustomerSlider WHERE CustomerSliderID ='+DeleteFileNo
    print(myqry)
    con.execute(myqry)
    con.commit()
    con.close()
    ShowDeleteMsg='Yes'
    return render_template('admin/ViewCutomers.html',**locals())


@app.route('/ViewCutomerIcons')
def ViewCutomerIcons():
    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #Slider
    myqry = 'SELECT * FROM CustomerSlider'
    print(myqry)
    cur.execute(myqry)
    CustomerSlider = cur.fetchall();
    con.commit()
    con.close()
    return render_template('/admin/ViewCutomers.html',**locals())


@app.route('/CutomerCreate')
def CutomerCreate():
    return render_template('/admin/CustomersIconCreate.html')

@app.route('/CustomersIconNew', methods=['POST'])
def CustomersIconNew():
    # Get the name of the uploaded file
    CustomerImg1 = request.files['CustomerImg1']
    CustomerImg2 = request.files['CustomerImg2']
    CustomerImg3 = request.files['CustomerImg3']
    CustomerImg4 = request.files['CustomerImg4']
    CustomerImg5 = request.files['CustomerImg5']
    CustomerImg6 = request.files['CustomerImg6']
    
    # Check if the file is one of the allowed types/extensions
    if CustomerImg1 and allowed_file(CustomerImg1.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(CustomerImg1.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        CustomerImg1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB1 = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')

    # Check if the file is one of the allowed types/extensions
    if CustomerImg2 and allowed_file(CustomerImg2.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(CustomerImg2.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        CustomerImg2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB2 = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')


    # Check if the file is one of the allowed types/extensions
    if CustomerImg3 and allowed_file(CustomerImg3.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(CustomerImg3.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        CustomerImg3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB3 = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')


        # Check if the file is one of the allowed types/extensions
    if CustomerImg4 and allowed_file(CustomerImg4.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(CustomerImg4.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        CustomerImg4.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB4 = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')


        # Check if the file is one of the allowed types/extensions
    if CustomerImg5 and allowed_file(CustomerImg5.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(CustomerImg5.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        CustomerImg5.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB5 = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')


        
        # Check if the file is one of the allowed types/extensions
    if CustomerImg6 and allowed_file(CustomerImg6.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(CustomerImg6.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        CustomerImg6.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB6 = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')
        

    try:
        
        print(finalFileDB1)
        print(finalFileDB2)
        print(finalFileDB3)
        print(finalFileDB4)
        print(finalFileDB4)
        print(finalFileDB6)
        
        
         
        with sqlite3.connect("myDb.db") as con:
            
            qoute="'"
            myquery2 ='INSERT INTO CustomerSlider (CustomerImg1, CustomerImg2, CustomerImg3, CustomerImg4, CustomerImg5, CustomerImg6) values ('+qoute+finalFileDB1+qoute+','+qoute+finalFileDB2+qoute+','+qoute+finalFileDB3+qoute+','+qoute+finalFileDB4+qoute+','+qoute+finalFileDB5+qoute+','+qoute+finalFileDB6+qoute+')'
            print(myquery2)
            cur = con.cursor()
            cur.execute(myquery2)
            print(myquery2)
            con.commit()
            msg = "Record successfully added"
    except:
        
        con.rollback()
        msg = "error in insert operation"
      
    finally:
        
        return render_template("admin/CustomersIconCreate.html")
        con.close()




#CutomerIconsEnd


#TeamWork START


@app.route('/CreateTeamWork')
def CreateTeamWork():
    return render_template('/admin/TeamWorkCreate.html')



@app.route('/DeleteTeamWork', methods=['POST'])
def DeleteTeamWork():
    con = sqlite3.connect('myDb'+'.db')
    DeleteFileNo = request.form['Record_to_delete']
    #DeleteCustomer Query
    myqry = 'DELETE FROM TeamWorkPages WHERE TeamWorkPagesID ='+DeleteFileNo
    print(myqry)
    con.execute(myqry)
    con.commit()
    con.close()
    ShowDeleteMsg='Yes'
    return render_template('admin/ViewTeamWork.html',**locals())





@app.route('/ViewTeamworkAll')
def ViewTeamworkAll():
    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #Slider
    myqry = 'SELECT * FROM TeamWorkPages'
    print(myqry)
    cur.execute(myqry)
    TeamWorkPages = cur.fetchall();
    con.commit()
    con.close()
    return render_template('TeamWorkDynamic.html',**locals())



@app.route('/ViewTeamWork')
def ViewTeamWork():
    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #Slider
    myqry = 'SELECT * FROM TeamWorkPages'
    print(myqry)
    cur.execute(myqry)
    TeamWorkPages = cur.fetchall();
    con.commit()
    con.close()
    return render_template('admin/ViewTeamWork.html',**locals())




@app.route('/TeamWorkNewReuest', methods=['POST'])
def TeamWorkNewReuest():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')

    try:
        
        Heading = request.form['Heading']
        print(Heading)
        Title = request.form['Title']
        print(Title)
        FB = request.form['FB']
        print(FB)
        TW = request.form['TW']
        print(TW)
        FinalFileName = finalFileDB
        
         
        with sqlite3.connect("myDb.db") as con:
            
            qoute="'"
            myquery2 ='INSERT INTO TeamWorkPages (Heading, Title, FB, TW, Image) values ('+qoute+Heading+qoute+','+qoute+Title+qoute+','+qoute+FB+qoute+','+qoute+TW+qoute+','+qoute+FinalFileName+qoute+')'
            print(myquery2)
            cur = con.cursor()
            cur.execute(myquery2)
            con.commit()
            msg = "Record successfully added"
    except:
        
        con.rollback()
        msg = "error in insert operation"
      
    finally:
        
        return render_template("admin/TeamWorkCreate.html")
        con.close()






#TeamWork END


#Testimonals Start
 


@app.route('/TestimonalsNew')
def TestimonalsNew():
    return render_template('/admin/TestimonalsNew.html')



@app.route('/DeleteTestimonals', methods=['POST'])
def DeleteTestimonals():
    con = sqlite3.connect('myDb'+'.db')
    DeleteFileNo = request.form['Record_to_delete']
    #DeleteCustomer Query
    myqry = 'DELETE FROM Testimonial WHERE TestimonialID ='+DeleteFileNo
    print(myqry)
    con.execute(myqry)
    con.commit()
    con.close()
    ShowDeleteMsg='Yes'
    return render_template('admin/ViewTestimonals.html',**locals())


@app.route('/ViewTestimonals')
def ViewTestimonals():
    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #Slider
    myqry = 'SELECT * FROM Testimonial'
    print(myqry)
    cur.execute(myqry)
    Testimonial = cur.fetchall();
    con.commit()
    con.close()
    return render_template('/admin/ViewTestimonals.html',**locals())

@app.route('/TestimonalsNewReuest', methods=['POST'])
def TestimonalsNewReuest():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finalFileDB = 'static/uploads/'+filename
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print('file uploaded')

    try:
        
        Heading = request.form['Heading']
        print(Heading)
        Title = request.form['Title']
        print(Title)
        Description = request.form['Description']
        print(Description)
        FinalFileName = finalFileDB
        
         
        with sqlite3.connect("myDb.db") as con:
            
            qoute="'"
            myquery2 ='INSERT INTO Testimonial (CusImg, Heading, Title, Description) values ('+qoute+FinalFileName+qoute+','+qoute+Heading+qoute+','+qoute+Title+qoute+','+qoute+Description+qoute+')'
            print(myquery2)
            cur = con.cursor()
            cur.execute(myquery2)
            con.commit()
            msg = "Record successfully added"
    except:
        
        con.rollback()
        msg = "error in insert operation"
      
    finally:
        
        return render_template("admin/TestimonalsNew.html")
        con.close()





#Testimonals End


@app.route('/AboutIIE/<ProjectID>')
def found(ProjectID):

    con = sqlite3.connect('myDb'+'.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    #SubPages
    myqry = 'SELECT * FROM AboutIIE1Basic WHERE AboutIieID ='+ProjectID
    print(myqry)
    cur.execute(myqry)
    con.row_factory = dict_factory
    AboutIIEBasic = cur.fetchall()[0];

    myqry = 'SELECT * FROM AboutIIE1SubImages WHERE AboutIieID ='+ProjectID
    print(myqry)
    cur.execute(myqry)
    AboutIIESub = cur.fetchall();
    con.commit()
    con.close()



    
    return render_template("TestPageSub.html",**locals())



@app.route('/')
def list():
   con = sqlite3.connect('myDb'+'.db')
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()

   #Slider
   myqry = 'SELECT * FROM Slider'
   print(myqry)
   cur.execute(myqry)
   Slider = cur.fetchall();
   print(Slider[0])

   #SliderCountAll
   myqry = 'SELECT COUNT(*) FROM Slider'
   print(myqry)
   cur.execute(myqry)
   con.row_factory = dict_factory
   SliderCount = cur.fetchall()[0];
   print(SliderCount[0])
   
   #Slider
   #myqry = 'SELECT * FROM SliderTble'
   #print(myqry)
   #con.row_factory = dict_factory
   #cur.execute(myqry)
   #SliderTable = cur.fetchall()[0];

   #TabsButtons
   myqry = 'SELECT * FROM TabsButtons'
   print(myqry)
   cur.execute(myqry)
   TabsButtons = cur.fetchall();


   #ScreenCenter
   myqry = 'SELECT * FROM ScreenCenter'
   print(myqry)
   cur.execute(myqry)
   con.row_factory = dict_factory
   ScreenCenter = cur.fetchall()[0];


   #CustomerSlider
   myqry = 'SELECT * FROM CustomerSlider'
   print(myqry)
   cur.execute(myqry)
   CustomerSlider = cur.fetchall();

   #CustomerSliderCountAllSlids
   #myqry = 'SELECT COUNT(*) FROM CustomerSlider'
   #print(myqry)
   #cur.execute(myqry)
   #con.row_factory = dict_factory
   #CustomerSliderCount = cur.fetchall()[0];
   #print(CustomerSliderCount[0])
   
   


   
   #Testimonial
   myqry = 'SELECT * FROM Testimonial'
   print(myqry)
   cur.execute(myqry)
   Testimonial = cur.fetchall();


   #TestimonialCountAll
   myqry = 'SELECT COUNT(*) FROM Testimonial'
   print(myqry)
   cur.execute(myqry)
   con.row_factory = dict_factory
   TestimonialCount = cur.fetchall()[0];
   print(TestimonialCount[0])

   


   #Footer
   myqry = 'SELECT * FROM Footer'
   print(myqry)
   cur.execute(myqry)
   Footer = cur.fetchall();
   con.close()


   
  
   return render_template("Index.html",**locals())
                        




if __name__ == '__main__':
    app.run()




