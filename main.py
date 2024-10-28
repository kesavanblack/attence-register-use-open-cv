import tkinter as tk
import cv2, os
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
from tkinter import messagebox
from tkinter import *
from tkinter import ttk, filedialog
import os
import smtplib
import tkinter as tk
from tkinter import filedialog, messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Attendance:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Online Attendance Marker")
        self.window.geometry("1000x550")
        self.window.configure(background='#FAFAFA')
        self.mark_attendance()

    def mark_attendance(self):
        l1 = Label(self.window, text="Project Title", font=("times new roman",20,"bold "), bg="#FAFAFA",fg="#1A4D2E",width=40)
        l1.place(x=180,y=50)

        b1 = Button(self.window, text="FACE RECOGNITION", command=self.admin_or_student, font=("times new roman",16,"bold "), bg="#FAFAFA", fg="#1A4D2E", width=20)
        b1.place(x=355,y=420)

        self.window.mainloop()

    def admin_or_student(self):
        f2 = Frame(self.window, width=1000, height=550, bg="#FAFAFA")
        f2.place(x=0, y=0)

        l2 = Label(f2, text="Project Title", font=("times new roman",20,"bold "),bg="#FAFAFA",fg="#9090EE",width=40).place(x=180,y=50)

        b2 = Button(f2, text="ADMIN", command=self.admin, font=("times new roman",16,"bold "), bg="#FAFAFA",fg="#9090EE",width=20).place(x=355,y=250)
        b3 = Button(f2, text="STUDENT", command=self.student, font=("times new roman",16,"bold "), bg="#FAFAFA",fg="#9090EE",width=20).place(x=355,y=400)









    def admin(self):
         f1=Frame(self.window,width=1000,height=550,bg="#FAFAFA")
         f1.place(x=0,y=0)
         l2=Label(f1, text="LOGIN", font=("times new roman",24,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=300,y=30)
         l3=Label(f1, text="Username", font=("times new roman",20,"bold "), bg="#FAFAFA",fg="#9090EE",width=10).place(x=280,y=150)
         l4=Label(f1, text="password", font=("times new roman",20,"bold "), bg="#FAFAFA",fg="#9090EE",width=10).place(x=280,y=230,)
         self.e1 = StringVar()
         self.e2 = StringVar()
         e1_txt=Entry(f1,width=30,textvariable=self.e1).place(x=500,y=160)
         e2_txt=Entry(f1,width=30,textvariable=self.e2).place(x=500,y=240)
         b7=Button(f1,text="LOGIN", command=self.log,font=("times new roman",16,"bold "), bg="#FAFAFA",fg="#9090EE",width=20).place(x=550,y=400)
         b8=Button(f1,text="BACK", command=self.admin_or_student, font=("times new roman",16,"bold "), bg="#FAFAFA",fg="#9090EE",width=20).place(x=200,y=400)
 
    
 
    
 
    def student(self):
        f2a = Frame(self.window, width=1000, height=550, bg="#FAFAFA")
        f2a.place(x=0, y=0)

        b4 = Button(f2a, text="REGISTER", command=self.register, font=("times new roman", 16, "bold "), bg="#FAFAFA", fg="#9090EE", width=25).place(x=355, y=100)
        b5 = Button(f2a, text="MARK YOUR ATTENDANCE", command=self.mark, font=("times new roman", 16, "bold "), bg="#FAFAFA", fg="#9090EE", width=35).place(x=320, y=250)
        b6 = Button(f2a, text="BACK", command=self.admin_or_student, font=("times new roman", 16, "bold "), bg="#FAFAFA", fg="#9090EE", width=25).place(x=355, y=400)
        
        
        
        
        
        
    def register(self):
        f3=Frame(self.window,width=1000,height=550,bg="#FAFAFA")
        f3.place(x=0,y=0)
        l2=Label(f3, text="REGISTER", font=("times new roman",20,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=300,y=30)
        x_cord = 75;
        y_cord = 20;
        checker=0;
        from tkinter import ttk, filedialog

        lbl2 = tk.Label(f3, text="Enter Your Name",width=20  ,bg="#FAFAFA",fg="#9090EE"    ,font=('Times New Roman', 15, ' bold ')) 
        lbl2.place(x=300-x_cord, y=120-y_cord)

        self.txt2 = tk.Entry(f3,width=20  ,bg="white"  ,fg="blue",font=('Times New Roman', 15, ' bold ')  )
        self.txt2.place(x=560-x_cord, y=125-y_cord)
        

        lbl = tk.Label(f3, text="Enter Your ID number",width=20    ,bg="#FAFAFA",fg="#9090EE",font=('Times New Roman', 15, ' bold ') ) 
        lbl.place(x=300-x_cord, y=170-y_cord)

        self.txt = tk.Entry(f3,width=20,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        self.txt.place(x=560-x_cord, y=175-y_cord)

        lbl7 = tk.Label(f3, text="Enter Your College Name",width=20    ,bg="#FAFAFA",fg="#9090EE",font=('Times New Roman', 15, ' bold ') ) 
        lbl7.place(x=300-x_cord, y=220-y_cord)

        self.txt7 = tk.Entry(f3,width=20,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        self.txt7.place(x=560-x_cord, y=225-y_cord)
          
        lb3 = tk.Label(f3, text="Department ",width=20    ,bg="#FAFAFA",fg="#9090EE",font=('Times New Roman', 15, ' bold ') ) 
        lb3.place(x=300-x_cord, y=270-y_cord)

        self.txt3 = tk.Entry(f3,width=20,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        self.txt3.place(x=560-x_cord, y=275-y_cord)

        
        lb4 = tk.Label(f3, text="Year",width=20    ,bg="#FAFAFA",fg="#9090EE",font=('Times New Roman', 15, ' bold ') ) 
        lb4.place(x=300-x_cord, y=320-y_cord)

        self.txt4 = tk.Entry(f3,width=20,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        self.txt4.place(x=560-x_cord, y=325-y_cord)

        
        lb5= tk.Label(f3, text="Section",width=20    ,bg="#FAFAFA",fg="#9090EE",font=('Times New Roman', 15, ' bold ') ) 
        lb5.place(x=300-x_cord, y=370-y_cord)

        self.txt5 = tk.Entry(f3,width=20,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        self.txt5.place(x=560-x_cord, y=375-y_cord)
        



        self.message = tk.Label(f3, text="" ,bg="#FAFAFA",fg="black",width=80, activebackground = "white" ,font=('Times New Roman', 15, ' bold ')) 
        self.message.place(x=100-x_cord, y=430-y_cord)

        takeImg = tk.Button(f3, text="IMAGE CAPTURE ",command=self.TakeImages  ,bg="#FAFAFA",fg="#9090EE"  ,width=30  ,height=2, activebackground = "white" ,font=('Times New Roman', 10, ' bold '))
        takeImg.place(x=750-x_cord, y=500-y_cord)

        trainImg = tk.Button(f3, text="TRAIN IMAGE ",command=self.TrainImages   ,bg="#FAFAFA",fg="#9090EE"  ,width=30  ,height=2, activebackground = "white" ,font=('Times New Roman', 10, ' bold '))
        trainImg.place(x=450-x_cord, y=500-y_cord)

        b9=Button(f3,text="BACK", command=self.student  ,bg="#FAFAFA",fg="#9090EE" ,width=30  ,height=2, activebackground = "white" ,font=('Times New Roman', 10,' bold ')).place(x=50,y=480)
    
    
    
    def log(self):
        if(self.e1.get()=="admin" and self.e2.get()=="1234"):
             f5=Frame(self.window,width=1000,height=550,bg="#FAFAFA")
             f5.place(x=0,y=0)
             b7=Button(f5,text="VIEW", command=self.view,font=("times new roman",16,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=350,y=30)
             b7=Button(f5,text="BACK", command=self.admin,font=("times new roman",16,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=100,y=500)
             b8=Button(f5,text="SEND MAIL", command=self.send_mail,font=("times new roman",16,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=550,y=500)
        else:
            tk.messagebox.showerror("Invalid", "Invalid username and password")

    def send_mail(self):
        f7=Frame(self.window,width=1000,height=550,bg="#FAFAFA")
        f7.place(x=0,y=0)
       

        # Create input fields for sender, recipient, and subject
        self.l1=tk.Label(f7, text="SEND MAIL", font=("times new roman",20,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=300,y=30)

        
        self.sender_label = tk.Label(f7, text="Sender email:",width=20  ,bg="#FAFAFA",fg="#9090EE"    ,font=('Times New Roman', 15, ' bold ')) 
        self.sender_label.place(x=250, y=120)
       
        self.sender_entry = tk.Entry(f7,width=30  ,bg="white"  ,fg="blue",font=('Times New Roman', 15, ' bold ')  )
        self.sender_entry.place(x=510, y=125)
        

        self.recipient_label = tk.Label(f7, text="Recipient email:",width=20    ,bg="#FAFAFA",fg="#9090EE",font=('Times New Roman', 15, ' bold ') ) 
        self.recipient_label.place(x=250, y=170)
        
        self.recipient_entry = tk.Entry(f7,width=30,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        self.recipient_entry.place(x=510, y=175)
        

        self.subject_label = tk.Label(f7, text="Email subject:",width=20    ,bg="#FAFAFA",fg="#9090EE",font=('Times New Roman', 15, ' bold ') ) 
        self.subject_label.place(x=250, y=225)

        
        self.subject_entry = tk.Entry(f7, width=30,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        self.subject_entry.place(x=510, y=225)

        # Create a button to select a file to attach to the email
        self.attach_button = tk.Button(f7, text="Attach file", command=self.attach_file ,font=("times new roman", 16, "bold "), bg="#FAFAFA", fg="#9090EE", width=20)
        self.attach_button.place(x=400,y=330)

        # Create a label to display the selected file name
        self.file_label = tk.Label(f7, text="")
        self.file_label.place(x=400,y=380)

        # Create a button to send the email
        self.send_button = tk.Button(f7, text="Send email", command=self.send_email ,font=("times new roman", 16, "bold "), bg="#FAFAFA", fg="#9090EE", width=20)
        self.send_button.place(x=550,y=450)

        self.send_button = tk.Button(f7, text="BACK", command=self.log ,font=("times new roman", 16, "bold "), bg="#FAFAFA", fg="#9090EE", width=20)
        self.send_button.place(x=150,y=450)

##
    def attach_file(self):
        # Prompt the user to select a file to attach to the email
        file_path = filedialog.askopenfilename(title="Select file to attach", filetypes=(("Excel files", "*.csv"), ("All files", "*.*")))

        if file_path:
            # Display the selected file name in the file label
            self.file_label.config(text=os.path.basename(file_path))
            self.attachment = (os.path.basename(file_path), open(file_path, "rb").read())

    def send_email(self):
        # Get the input values from the entry fields
        sender_email = self.sender_entry.get().strip()
        recipient_email = self.recipient_entry.get().strip()
        subject = self.subject_entry.get().strip()

        if not sender_email or not recipient_email or not subject:
            # Display an error message if any of the required fields are blank
            error_message = "Please fill in all fields."
            messagebox.showerror("Error", error_message)
            return

        if not hasattr(self, "attachment"):
            # Display an error message if no file is attached
            error_message = "Please attach a file."
            messagebox.showerror("Error", error_message)
            return

        # Create a message object
        message = MIMEMultipart()

        # Set the message headers
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Add the attachment to the message
        attachment = MIMEApplication(self.attachment[1], _subtype="pdf")
        attachment.add_header("Content-Disposition", "attachment", filename=self.attachment[0])
        message.attach(attachment)

    # Send the email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, "wsbpqyzymwtqnxjm")
            server.sendmail(sender_email, recipient_email, message.as_string())
            server.quit()
            success_message = f"Email sent to {recipient_email} successfully."
            messagebox.showinfo("Success", success_message)
            self.clear_form()
        except Exception as e:
        # Display an error message if the email fails to send
            error_message = f"Error sending email: {e}"
            messagebox.showerror("Error", error_message)

    def clear_form(self):
    # Clear the input fields and file label
        self.sender_entry.delete(0, tk.END)
        self.recipient_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.file_label.config(text="")
       

##        
    


  


        
                                


    def TakeImages(self):
        Id=self.txt.get()
        name=self.txt2.get()
        dept=self.txt3.get()
        year=self.txt4.get()
        section=self.txt5.get()
        clgname=self.txt7.get()
        if not Id:
            res="Please enter Id"
            message.configure(text = res)
            MsgBox = tk.messagebox.askquestion ("Warning","Please enter roll number properly , press yes if you understood",icon = 'warning')
            if MsgBox == 'no':
                tk.messagebox.showinfo('Your need','Please go through the readme file properly')
        elif not name:
            res="Please enter Name"
            message.configure(text = res)
            MsgBox = tk.messagebox.askquestion ("Warning","Please enter your name properly , press yes if you understood",icon = 'warning')
            if MsgBox == 'no':
                tk.messagebox.showinfo('Your need','Please go through the readme file properly')

        elif not dept:
            res="Please enter Department"
            message.configure(text = res)
            MsgBox = tk.messagebox.askquestion ("Warning","Please enter your department properly , press yes if you understood",icon = 'warning')
            if MsgBox == 'no':
                tk.messagebox.showinfo('Your need','Please go through the readme file properly')

        elif not year:
            res="Please enter Year"
            message.configure(text = res)
            MsgBox = tk.messagebox.askquestion ("Warning","Please enter your year properly , press yes if you understood",icon = 'warning')
            if MsgBox == 'no':
                tk.messagebox.showinfo('Your need','Please go through the readme file properly')

        elif not section:
            res="Please enter section"
            message.configure(text = res)
            MsgBox = tk.messagebox.askquestion ("Warning","Please enter your section properly , press yes if you understood",icon = 'warning')
            if MsgBox == 'no':
                tk.messagebox.showinfo('Your need','Please go through the readme file properly')

        elif not clgname:
            res="Please enter College Name"
            message.configure(text = res)
            MsgBox = tk.messagebox.askquestion ("Warning","Please enter your College name properly , press yes if you understood",icon = 'warning')
            if MsgBox == 'no':
                tk.messagebox.showinfo('Your need','Please go through the readme file properly')
            
        elif(self.is_number(Id) and name.isalpha() and dept.isalpha() and self.is_number(year) and section.isalpha()and clgname.isalpha()):
                cam = cv2.VideoCapture(0)
                harcascadePath = "C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\haarcascade_frontalface_default.xml"
                detector=cv2.CascadeClassifier(harcascadePath)
                sampleNum=0
                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                        #incrementing sample number 
                        sampleNum=sampleNum+1
                        #saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\TrainingImage\\ "+name +"."+Id +'.'+dept+'.'+year+'.'+section+'.'+clgname+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                        #display the frame
                        cv2.imshow('frame',img)
                    #wait for 100 miliseconds 
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    # break if the sample number is morethan 100
                    elif sampleNum>60:
                        break
                cam.release()
                cv2.destroyAllWindows() 
                res = "Images Saved for ID : " + Id +" ||  Name : "+ name+" || Dept : "+ dept+"  || Year : "+ year+" ||  Section : "+ section+"  || College Name : "+ clgname
                row = [Id , name,dept,year,section,clgname]
                with open('C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\StudentDetails\\StudentDetails.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                self.message.configure(text= res)
##        else:
##            if(self.is_number(Id)):
##                res = "Enter Alphabetical Name"
##                self.message.configure(text= res)
##            if(name.isalpha()):
##                res = "Enter Numeric Id"
##                self.message.configure(text= res)


    def mark(self):
        f4=Frame(self.window,width=1000,height=550,bg="#FAFAFA")
        f4.place(x=0,y=0)

        x_cord = 75;
        y_cord = 20;
        checker=0;
        self.message2 = tk.Label(f4, text="" ,bg="#FAFAFA",fg="black",activeforeground = "green",width=50  ,height=2  ,font=('times', 18, ' bold ')) 
        self.message2.place(x=150, y=430-y_cord)

        self.message = tk.Label(f4, text="" ,bg="#FAFAFA",fg="#9090EE" ,width=30  ,height=2, activebackground = "white" ,font=('Times New Roman', 10, ' bold ')) 
        self.message.place(x=1075-x_cord, y=300-y_cord)
         
        b10=Button(f4,text="MARK YOUR ATTENDANCE", command =self.TrackImages,font=("times new roman",15,"bold "),bg="#FAFAFA",fg="#9090EE",width=25).place(x=355,y=100)

        b6=Button(f4,text="BACK",command=self.student,font=("times new roman",15,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=380,y=250)



             
    def TrackImages(self):
         recognizer = cv2.face.LBPHFaceRecognizer.create()#cv2.createLBPHFaceRecognizer()
         recognizer.read("C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\TrainingImageLabel\\Trainner.yml")
         harcascadePath = "C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\haarcascade_frontalface_default.xml"
         faceCascade = cv2.CascadeClassifier(harcascadePath);    
         df=pd.read_csv("C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\StudentDetails\\StudentDetails.csv")
         cam = cv2.VideoCapture(0)
         font = cv2.FONT_HERSHEY_SIMPLEX        
         col_names =  ['Id','Name','Date','Time']
         attendance = pd.DataFrame(columns = col_names)    
         while True:
             ret, im =cam.read()
             gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
             faces=faceCascade.detectMultiScale(gray, 1.2,5)    
             for(x,y,w,h) in faces:
                 cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                 Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                 if(conf < 50):
                     ts = time.time()      
                     date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                     timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                     aa=df.loc[df['Id'] == Id]['Name'].values
                     tt=str(Id)+"-"+aa
                     attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                    
                 else:
                     Id='Unknown'                
                     tt=str(Id)  
                 if(conf > 75):
                     noOfFile=len(os.listdir("ImagesUnknown"))+1
                     cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                 cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
             attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
             cv2.imshow('im',im) 
             if (cv2.waitKey(1)==ord('q')):
                 break
         ts = time.time()      
         date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
         timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
         Hour,Minute,Second=timeStamp.split(":")
         fileName="C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
         attendance.to_csv(fileName,index=False)
         cam.release()
         cv2.destroyAllWindows()
         res=attendance
         self.message2.configure(text= res)
         res = "Attendance Taken"
         self.message.configure(text= res)
         tk.messagebox.showinfo('Completed','Congratulations ! Your attendance has been marked successfully for the day!!')

    def clear1(self):
        self.txt.delete(0, 'end')    
        res = ""
        self.message.configure(text= res)

    def clear2(self):
        self.txt2.delete(0, 'end')    
        res = ""
        self.message.configure(text= res)


    def TrainImages(self):
        recognizer = cv2.face.LBPHFaceRecognizer.create()
        faces,Id = self.getImagesAndLabels("C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("C:\\Users\\DELL\\Desktop\\PRO\\Attendance\\TrainingImageLabel\\Trainner.yml")
        res = "Image Trained"
        self.clear1();
        self.clear2();
        self.message.configure(text= res)
        tk.messagebox.showinfo('Completed','Your model has been trained successfully!!')
        

    def getImagesAndLabels(self,path):

        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        
        faces=[]

        Ids=[]

        for imagePath in imagePaths:
            from PIL import Image, ImageTk
            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)        
        return faces,Ids








    

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass
     
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
     
        return False

    def view(self):

        f5=Frame(self.window,width=1000,height=550,bg="#FAFAFA")
        f5.place(x=0,y=0)
        b7=Button(f5,text="VIEW", command=self.view,font=("times new roman",16,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=350,y=30)
        b7=Button(f5,text="BACK", command=self.admin,font=("times new roman",16,"bold "),bg="#FAFAFA",fg="#9090EE",width=20).place(x=350,y=500)
                    
        f5.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
    ##                 f5.resizable(0, 0) # makes the root window fixed in size.
        

        # Frame for TreeView
        frame1 = tk.LabelFrame(f5, text="Attendance Data",bg="#FAFAFA",fg="#9090EE")
        frame1.place(height=300, width=600,rely=0.15, relx=0.20)

        # Frame for open file dialog
        file_frame = tk.LabelFrame(f5, text="Open File",bg="#FAFAFA",fg="#9090EE")
        file_frame.place(height=100, width=400, rely=0.70, relx=0.30)

        # Buttons
        button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog(self),bg="#FAFAFA",fg="#9090EE")
        button1.place(rely=0.65, relx=0.50)

        button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data(self),bg="#FAFAFA",fg="#9090EE")
        button2.place(rely=0.65, relx=0.30)

        # The file/file path text
        label_file = ttk.Label(file_frame, text="No File Selected")
        label_file.place(rely=0, relx=0)


        ## Treeview Widget
        tv1 = ttk.Treeview(frame1)
        tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

        treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
        treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
        treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
        treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


        def File_dialog(self):
            filename = filedialog.askopenfilename(initialdir="/",title="Select A File",filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
            label_file["text"] = filename
            return None


        def Load_excel_data(self):
            file_path = label_file["text"]
            try:
                excel_filename = r"{}".format(file_path)
                if excel_filename[-4:] == ".csv":
                    df = pd.read_csv(excel_filename)
                else:
                    df = pd.read_excel(excel_filename)

            except ValueError:
                tk.messagebox.showerror("Information", "The file you have chosen is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {file_path}")
                return None

            clear_data(self)
            tv1["column"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column) # let the column heading = column name

            df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
            for row in df_rows:
                tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
            return None


        def clear_data(self):
            tv1.delete(*tv1.get_children())
            return None






# Create an instance of the Attendance class
attendance = Attendance()
