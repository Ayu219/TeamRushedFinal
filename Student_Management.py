from flask import Flask,request,render_template,send_file
import pickle
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import img2pdf
from PIL import Image

# from qr import qrgen
import pyqrcode
from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files_upload'

#Login Screen
@app.route('/')
def index():
    return render_template ("Login.html")

#Database
database = {"Manu Mishra":"0000", "Vishu Mishra":"5555", "Shreya Mishra":"4444","Ayush Tomar":"1111","Faculty":"7777","Admin":"2222"} 

#Login Authentication
@app.route('/form_login', methods = ['POST','GET'])
def login():
    name_input = request.form['username']
    pwd        = request.form['password']

    if name_input  not in database:
        return render_template('Invalid_user.html')
    else:
        if database[name_input]!=pwd:
            return render_template('Invalid_pwd.html')  

        else:
            if name_input=="Faculty":
                return render_template('Faculty.html') 
            if name_input=="Admin":
                return render_template('Admin.html')     
            else:
                return render_template('Dashboard.html', Name = name_input )      



#Logout Screen
@app.route('/Logout')
def Logout():
    return render_template ("Login.html")


#Assignment Screen
@app.route('/Assignment')
def Assignment():
    return render_template ("Assignment.html")


#CS Screen
@app.route('/CS')
def CS():
    return render_template ("CS.html")


#DSA Screen
@app.route('/DSA')
def DSA():
    return render_template ("DSA.html")


#DSD Screen
@app.route('/DSD')
def DSD():
    return render_template ("DSD.html")


#Upload Window for student
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/Upload', methods=['GET',"POST"])
def Upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data 
        
        # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
        app.config['UPLOAD_FOLDER'],
        secure_filename(file.filename))) 
        
        # Then save the file
        return "File has been uploaded."

    return render_template('Upload.html', form=form)


#Faculty Assignment Screen
@app.route('/Faculty_assgn')
def Faculty_assgn():
    return render_template ("Faculty_assgn.html")


#Student Update Check Screen
@app.route('/Student_update')
def Student_update():
    return render_template ("Student_update.html")
 

#Student Assignment View Screen
@app.route('/View_assgn')
def View_assgn():
    return render_template ("View_assgn.html")


#File Downloader
@app.route('/download')
def download_file():
    file="Code.jpg"
    return send_file (file, as_attachment=True)

# QR Page
@app.route('/QR_Code_Generater')
def QR_page():
    return render_template('QR_page.html')

# QR Text Input
@app.route('/converted',methods = ['POST'])
def convert():
    global tex
    tex = request.form['test']
    return render_template('converted.html')

#QR Generator
def qrgen(s):
    qr = pyqrcode.create(s)
    qr.png(s+'.png',scale = 8)

#QR Downloader
@app.route('/qr_download')
def qr_download():
    qrgen(tex)
    filename = "Code.jpg"
    # filename = tex+'.png'
    return send_file(filename,as_attachment=True)


#Running Command
if __name__ == '__main__':
    app.run(debug=True)

