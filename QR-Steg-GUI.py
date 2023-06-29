from tkinter.ttk import Progressbar
import tkinter
from tkinter import *
import SSteg as stg
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox as mb
from PIL import ImageTk
import time
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2
import os
from stegano import exifHeader as stg
from PIL import Image
from stegano import lsb
from stegano.lsb import generators
from Crypto.Util.number import long_to_bytes
import customtkinter
from Crypto.Util.Padding import pad,unpad
from Crypto.Cipher import AES
from base64 import b64encode
import base64
import random
import qrcode as q

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def main():
    Auth = customtkinter.CTk()
    Auth.geometry("650x450")
    Auth.title("Authentication !")
    # scrollbar = Scrollbar(Auth)
    # scrollbar.pack(side = RIGHT, fill = Y )
    # mylist = Listbox(Auth,yscrollcommand = scrollbar.set )

    # scrollbar1 = Scrollbar(Auth)
    # scrollbar1.pack(side = BOTTOM, fill = X )
    # mylist = Listbox(Auth,xscrollcommand = scrollbar1.set )

    def Steggg():
        GUI = customtkinter.CTk()
        GUI.title("HOME")
        label = customtkinter.CTkLabel(GUI,text="Image Steganography :",font=("Times New Roman",35)).place(x=210,y=10)
        d3label= customtkinter.CTkLabel(GUI,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=70)
        text_label = customtkinter.CTkLabel(GUI,text="Please Select the operation you need to do : ",font =("Times New Roman",20)).place(x=20,y=113)
        GUI.geometry("750x550")

        def encoder():
            # res4=mb.askquestion('Start Decoding', 'Do you really want to encode ?')
            GUI.destroy()
            EncScreen = customtkinter.CTk()
            EncScreen.title("ENCODER")
            label = customtkinter.CTkLabel(EncScreen,text="ENCODER :",font=("Times New Roman",30)).place(x=272,y=30)
            d1label=customtkinter.CTkLabel(EncScreen,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=86)
            EncScreen.geometry("700x700")
            # EncScreen.config(bg="black")

            def get_data_path():
                pathh=entry.get()
                mb.showinfo("Pop Up","Data to be encrypted : "+pathh)
                return pathh

            def submit_Data():
                d=get_data_path()
                # data=get_data_path
                print("The data to be enrypted : ",d)
                return d

            def subk():
                k=kentry.get()
                mb.showinfo("Pop Up","The Input Private Key : "+k)
                return k

            def subkk():
                k=kentry.get()
                # mb.showinfo("Pop Up","The Input Private Key : "+k)
                return k

            def lenkey():
                k=subkk()
                kk=str(k)
                key = bytes(k,'utf-8')
                if ((len(kk)==16 or len(kk)==24 or len(kk)==32)):
                    subk()
                else:    
                    mb.showerror("Error !","Invalid Key !")

            def aescall():
                aese()

            def aese():
                data=submit_Data()
                # print(data)
                k=subk()
                kk=str(k)
                key = bytes(k,'utf-8')
                text=bytes(data,'utf-8')
                # text = b"sample"
                cipher = AES.new(key,AES.MODE_ECB)
                ct_bytes = cipher.encrypt(pad(text,AES.block_size))
                print(ct_bytes)
                ct = b64encode(ct_bytes).decode('utf-8')
                print("Cipher Text : ",ct)
                f = open("Encrypteddata.txt",'w')
                f.write(ct)
                mb.showinfo("Encrypted Successfully !","Encrypted confidential data : "+ct)
                return ct
                
            def get_q_path():
                qpath=qentry.get()
                return qpath
                            
            def qrgen():
                data=get_q_path()
                rq(data)
                mb.showinfo("Pop Up","QR generated Successfully !")

            def rq(data):
                # data="www.sastra.edu"
                # img = q.make(data)
                # img.save("QR.jpeg")
                # print(img.size)
                # im = Image.open("QR.jpeg")
                # new_img = im.resize((1280,1280))
                # new_img.save("FINAL_QR.jpeg")
                # print(new_img.size)

                version=random.randint(1,5)
                qr = q.QRCode(version,box_size = 10,border = 5)
                qr.add_data(data)
                qr.make(fit = True)
                img = qr.make_image()
                img.save('QR.jpeg')
                im = Image.open("QR.jpeg")
                new_img = im.resize((1280,1280))
                new_img.save("FINAL_QR.jpeg")
                print(new_img.size)

            def OpenFile():
                global FileOpen
                FileOpen=StringVar()
                FileOpen = askopenfilename(initialdir =os.getcwd(),title="SelectFile",filetypes=(("only jpeg files","*jpeg"),("all type of files","*.*")))
                # label2 = customtkinter.CTkLabel(EncScreen,text=FileOpen,font=('Bahnschrift',14))
                # label2.place(relx=0.5,rely=0.4)
                SaveEntry.insert(0,FileOpen)

            def Encoder():
                Response= mb.askyesno("PopUp","Do you want to encode the image?")
                if Response == 1:
                    data=aese()
                    stg.hide(FileOpen,"Encoded-payload.jpeg",data)
                    # secret=lsb.hide(FileOpen,entry.get(),generators.eratosthenes())
                    # secret.save("secret.jpg")
                    mb.showinfo("Pop Up","Successfully Encoded")
                else:
                    mb.showwarning("Pop Up","Returning to Encoding Page")

            def mainmenu():
                EncScreen.destroy()
                Steggg()

            def aboutproject():
                ws = customtkinter.CTk()
                ws.title('About Project')
                ws.geometry('400x400')
                ws.config(bg="black")

                message ='''
             MINI-PROJECT
                                        
     Project Done By : 
        Lokesh
                                                        
            Thanks You <3  '''

                text_box = Text(ws,height=12,width=40)
                text_box.pack(expand=True)
                text_box.insert('end', message)
                text_box.config(state='disabled')
                button = customtkinter.CTkButton(ws,text="CLOSE",width=12,command=ws.destroy).place(x=165,y=300)
                ws.resizable(False,False)
                ws.mainloop()

            def backtomenu():
                res4=mb.askquestion('Menu !', 'Do you really want to go back to Main Menu ?')
                if(res4 == 'yes'):
                    mainmenu()
                else:
                    mb.showinfo('Return', 'Returning to Encode application')

            label = customtkinter.CTkLabel(EncScreen,text="Enter the Confidential Message : ",font=('Times New Roman',19))
            label.place(relx=0.1,rely=0.194)
            entry=customtkinter.CTkEntry(EncScreen,width=250,font=('Bahnschrift',14))
            entry.place(relx=0.5,rely=0.2)
            klabel = customtkinter.CTkLabel(EncScreen,text="Enter the Private Key : ",font=('Times New Roman',19))
            klabel.place(relx=0.1,rely=0.298)
            kentry=customtkinter.CTkEntry(EncScreen,width=250,font=('Bahnschrift',14))
            kentry.place(relx=0.5,rely=0.298)
            kbutton = customtkinter.CTkButton(EncScreen,text="Submit Key",width=11,font=('Bahnschrift',14),command=lenkey)
            kbutton.place(relx=0.5025,rely=0.3525)
            qlabel = customtkinter.CTkLabel(EncScreen,text="Enter the QR Data : ",font=('Times New Roman',19))
            qlabel.place(relx=0.1,rely=0.398)
            qentry=customtkinter.CTkEntry(EncScreen,width=250,font=('Bahnschrift',14))
            qentry.place(relx=0.5,rely=0.4015)
            label1 = customtkinter.CTkLabel(EncScreen,text="Select the File (Path of the File) : ",font=('Times New Roman',19))
            label1.place(relx=0.1,rely=0.498)
            SaveEntry = customtkinter.CTkEntry(EncScreen,width=250,font=('Bahnschrift',14))
            SaveEntry.place(relx=0.5,rely=0.5015)

            SelectButton = customtkinter.CTkButton(EncScreen,text="Select the file",width=11,font=('Bahnschrift',14),command=OpenFile)
            SelectButton.place(relx=0.5025,rely=0.5525)
            qrbutton = customtkinter.CTkButton(EncScreen,text="Generate QR",width=11,font=('Bahnschrift',14),command=qrgen)
            qrbutton.place(relx=0.720,rely=0.4525)
            submitbutton = customtkinter.CTkButton(EncScreen,text="Submit data",width=11,font=('Bahnschrift',14),command=submit_Data)
            submitbutton.place(relx=0.5025,rely=0.248)
            aesBUTTON = customtkinter.CTkButton(EncScreen,text="Encrypt",width=90,font=('Bahnschrift',14),command=aese)
            aesBUTTON.place(relx=0.725,rely=0.3525)
            EncodeButton=customtkinter.CTkButton(EncScreen,text="Embed",width=100,font=('Bahnschrift',14),command=Encoder).place(x=298,y=432)
            # EncodeButton.place(relx=0.4,rely=0.5)
            button12= customtkinter.CTkButton(EncScreen, text="Menu",width=100,font=('Bahnschrift',14), command= backtomenu).place(x=297,y=482)
            button7= customtkinter.CTkButton(EncScreen, text="Close",width=100,font=('Bahnschrift',14), command= EncScreen.destroy).place(x=297,y=532)
            button33= customtkinter.CTkButton(EncScreen, text="About",width=100,font=('Bahnschrift',14), command= aboutproject).place(x=297,y=582)
            # clabel = customtkinter.CTkLabel(EncScreen,text="Done By : Lokesh",font=("Times New Roman",15),).place(x=210,y=560)
            # rlabel = customtkinter.CTkLabel(EncScreen,text="B.Tech - CSE(CS & BT)",font=("Times New Roman",15),).place(x=250,y=600)
            # EncScreen.resizable(False,False)
            dlabel=customtkinter.CTkLabel(EncScreen,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",).place(x=0,y=635)
            EncScreen.maxsize(700,700)
            EncScreen.mainloop()


        def get_d_path():
            d_path=d_path.get();print(d_path)
            return d_path

            # def validate_user(username):
            #     # Checks the text file for a username/password combination.
            #     try:
            #         with open("credentials.txt", "r") as credentials:
            #             for line in credentials:
            #                 line = line.split(",")
            #                 if line[1] == username:
            #                     return False
            #         return True
            #     except FileNotFoundError:
            #         return True


        def decode(path):
            GUI.destroy()
            DecScreen = customtkinter.CTk()
            DecScreen.title("DECODER")
            label31 = customtkinter.CTkLabel(DecScreen,text="DECODER :",font=("Times New Roman",30)).place(x=225,y=23)
            d1label=customtkinter.CTkLabel(DecScreen,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=86)
            DecScreen.geometry("600x600")
            # DecScreen.config(bg="black")

            def OpenFile():
                global FileOpen
                FileOpen=StringVar()
                FileOpen = askopenfilename(initialdir =os.getcwd(),title="Select the File",filetypes=(("only jpeg files","*jpeg"),("all type of files","*.*")))
                # label2 = customtkinter.CTkLabel(DecScreen,text=FileOpen,width=27,font=('Bahnschrift',13))
                # label2.place(relx=0.5,rely=0.250)
                SaveEntry.insert(0,FileOpen)

            def subdk():
                dk=decodedk.get()
                mb.showinfo("Pop Up","The Input Private Key : "+dk)
                return dk

            def subdkk():
                k=decodedk.get()
                # mb.showinfo("Pop Up","The Input Private Key : "+k)
                return k

            def lendkey():
                k=subdkk()
                kk=str(k)
                key = bytes(k,'utf-8')
                if (len(kk)==16 or len(kk)==24 or len(kk)==32):
                    subdk()
                else:    
                    mb.showerror("Error !","Invalid Key ! Try Again !")
                                    
            def aesd(cdata):
                kkk=subdk()
                kkkk=str(kkk)
                key = bytes(kkkk,'utf-8')
                cipher = AES.new(key,AES.MODE_ECB)  
                f=cdata
                t = base64.b64decode(f)
                print(t)
                plaintextb = unpad(cipher.decrypt(t),16)
                plaintext = plaintextb.decode('utf-8')
                print((plaintext))
                f = open("decrypteddata.txt",'w')
                f.write(plaintext)
                return plaintext
            
            def ssim():
                img1 = cv2.imread(r"")
                img2 = cv2.imread(r"")
                
                gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

                ssim_value = ssim(gray_img1, gray_img2)
                return ssim_value

            def psnr():
                stego_img = cv2.imread("Encoded-payload.jpeg")
                cover_img = cv2.imread("FINAL_QR.jpeg")

                mse = ((stego_img - cover_img) ** 2).mean()
                if mse == 0:
                    psnr = float('inf')
                else:
                    max_pixel_value = 255.0
                    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

                return psnr
                                
            def insert(ssss):
                decoded.insert(0,f'ssss')

            def Decoder():
                Response= mb.askyesno("PopUp","Do you want to decode the image?")
                if Response == 1:
                    Message=stg.reveal(FileOpen)
                    ssss=aesd(Message)
                    # ss=lsb.reveal(FileOpen, generators.eratosthenes())
                    # label3 = customtkinter.CTkLabel(text=ss).place(x=250,y=281)
                    # label3 = customtkinter.CTkLabel(DecScreen,text=ssss,font=('Bahnschrift', 13)).place(x=300,y=257)
                    decoded.insert(0,ssss)
                    mb.showinfo("Pop-Up","Successfully Decoded !")
                    # insert(ssss)
                    # disp_tf.insert(0,f'{age} years old {name} became {desc}.')
                else:
                    mb.showwarning("Pop Up","Returning to Decoding Page")
                            
            def mainmenu1():
                DecScreen.destroy()
                Steggg()

            def backtomenu1():
                res4=mb.askquestion('Menu !', 'Do you really want to go back to Main Menu ?')
                if(res4 == 'yes'):
                    mainmenu1()
                else:
                    mb.showinfo('Return', 'Returning to Decode application')

            def aboutproject2():
                ws = customtkinter.CTk()
                ws.title('About Project')
                ws.geometry('400x400')
                ws.config(bg="black")
                message ='''
             MINI-PROJECT
                                            
    Project Done By : 
        Lokesh
                                                            
            Thank You <3  '''

                text_box = Text(ws,height=12,width=40)
                text_box.pack(expand=True)
                text_box.insert('end', message)
                text_box.config(state='disabled')
                button = customtkinter.CTkButton(ws,text="CLOSE",width=12,command=ws.destroy).place(x=165,y=300)
                ws.resizable(False,False)
                ws.mainloop()
                
            SelectButton = customtkinter.CTkButton(DecScreen,text="Select the file",font=('Bahnschrift',14),command=OpenFile).place(x=300,y=190)
            datalabel = customtkinter.CTkLabel(DecScreen,text="Decoded Secret Info : ",font=("Times New Roman",18)).place(x=62,y=317)
            # SelectButton.place(relx=0.1,rely=0.4)
            # SaveEntry = customtkinter.CTkEntry(DecScreen).place(x=300,y=230)
            label1 = customtkinter.CTkLabel(DecScreen,text="Select the File :",font=("Times New Roman",18))
            label1.place(relx=0.1,rely=0.25)
            labelkd = customtkinter.CTkLabel(DecScreen,text="Enter the Private Key :",font=("Times New Roman",18))
            labelkd.place(relx=0.1,rely=0.388)
            SaveEntry = customtkinter.CTkEntry(DecScreen,width=240,font=('Bahnschrift', 14))
            SaveEntry.place(relx=0.5,rely=0.250)
            kdButton = customtkinter.CTkButton(DecScreen,text="Submit Key",font=('Bahnschrift',14),command=lendkey).place(x=300,y=270)
            decodedk = customtkinter.CTkEntry(DecScreen,width=240,font=('Bahnschrift', 14))
            decodedk.place(relx=0.5,rely=0.388)
            decodeButton=customtkinter.CTkButton(DecScreen,text="Decode",width=100,font=('Bahnschrift',14),command=Decoder).place(x=255,y=368)
            decoded = customtkinter.CTkEntry(DecScreen,width=240,font=('Bahnschrift', 14))
            decoded.place(relx=0.5,rely=0.528)
            button22= customtkinter.CTkButton(DecScreen,text="Menu",width=100,font=('Bahnschrift',13),command = backtomenu1).place(x=255,y=415)
            # EncodeButton.place(relx=0.4,rely=0.5)
            Closebutton=customtkinter.CTkButton(DecScreen,text="Close",font=('Bahnschrift',14),width=100,command=DecScreen.destroy).place(x=255,y=460)
            abbutton=customtkinter.CTkButton(DecScreen,text="About",font=('Bahnschrift',14),width=100,command=aboutproject2).place(x=255,y=505)
            # clabel3 = customtkinter.CTkLabel(DecScreen,text="Done By : Lokesh",font=("Times New Roman",15),).place(x=160,y=490)
            # rlabel3 = customtkinter.CTkLabel(DecScreen,text="B.Tech - CSE(CS & BT)",font=("Times New Roman",15),).place(x=200,y=520)
            # DecScreen.resizable(False,False)
            DecScreen.maxsize(600,600)
            dlabel=customtkinter.CTkLabel(DecScreen,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=547)
            # dlabel=customtkinter.CTkLabel(DecScreen,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=547)
            DecScreen.mainloop()

        def enncoder():
            res3=mb.askquestion('Start Encoding', 'Do you really want to encode ?')
            if(res3 == 'yes'):
                encoder()
            else:
                mb.showinfo('Return', 'Returning to main application')

        def decoder():
            res3=mb.askquestion('Start Decoding', 'Do you really want to decode ?')
            if(res3 == 'yes'):
                dpath=get_d_path
                decode(dpath)
            else:
                mb.showinfo('Return', 'Returning to main application !')

        def logout():
            GUI.destroy()
            main()

        def backtologin():
            res4=mb.askquestion('Log Out !', 'Do you really want to log out ?')
            if(res4 == 'yes'):
                logout()
            else:
                mb.showinfo('Return', 'Returning to main application')

        def about():
            ws = customtkinter.CTk()
            ws.title('About Project')
            ws.geometry('400x400')
            ws.config(bg='black')

            message ='''
             MINI-PROJECT
                    
    Project Done By : 
        Lokesh
                                    
            Thanks You <3  '''

            text_box = Text(ws,height=12,width=40)
            text_box.pack(expand=True)
            text_box.insert('end', message)
            text_box.config(state='disabled')
            button = customtkinter.CTkButton(ws,text="CLOSE",width=12,command=ws.destroy).place(x=169,y=300)
            ws.resizable(False,False)
            ws.mainloop()

        def analysispage():
            GUI.destroy()
            analyzeui=customtkinter.CTk()
            analyzeui.geometry("500x550")
            analyzeui.maxsize(500,550)
            analyzeui.title("Analysis")

            def OpenFile1():
                global FileOpen
                FileOpen=StringVar()
                FileOpen = askopenfilename(initialdir =os.getcwd(),title="Select the File",filetypes=(("only jpeg files","*jpeg"),("all type of files","*.*")))
                SaveEntryaz1.insert(0,FileOpen)
                return FileOpen
            
            def mainmenu():
                analyzeui.destroy()
                Steggg()
            
            def backtomenu():
                res4=mb.askquestion('Menu !', 'Do you really want to go back to Main Menu ?')
                if(res4 == 'yes'):
                    mainmenu()
                else:
                    mb.showinfo('Return', 'Returning to Encode application')

            def OpenFile2():
                global FileOpen
                FileOpen=StringVar()
                FileOpen = askopenfilename(initialdir =os.getcwd(),title="Select the File",filetypes=(("only jpeg files","*jpeg"),("all type of files","*.*")))
                SaveEntryaz2.insert(0,FileOpen)
                return FileOpen

            def get_a1_path():
                a1path=SaveEntryaz1.get()
                return a1path

            def get_a2_path():
                a2path=SaveEntryaz2.get()
                return a2path

            def SSIM(a,b):
                try:
                    img1 = cv2.imread(a)
                    img2 = cv2.imread(b)
                                    
                    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

                    ssim_value = ssim(gray_img1, gray_img2)
                    return ssim_value
                except:
                    print("No file found !")
                    mb.showerror("SSIM Analysis Error","Specified file not found ! Please check and proceed.")

            def ssimmm():
                apath=str(get_a1_path())
                bpath=str(get_a2_path())
                # a=OpenFile1
                # b=OpenFile2
                fname = "FINAL_QR.jpeg"
                print(os.path.abspath(fname))
                f2name = "Encoded-payload.jpeg"
                print(os.path.abspath(f2name))
                ss=SSIM(apath,bpath)
                sss=str(ss)
                mb.showinfo("SSIM Analysis Result","SSIM Value : "+sss)

            def psnr():
                a=get_a1_path()
                b=get_a2_path()
                psm=PSNR(a,b)
                psmm=str(psm)
                mb.showinfo("PSNR Analysis Result","PSNR Value : "+psmm)

            def PSNR(a,b):
                try:
                    stego_img = cv2.imread(a)
                    cover_img = cv2.imread(b)

                    mse = ((stego_img - cover_img) ** 2).mean()
                    if mse == 0:
                        psnr = float('inf')
                    else:
                        max_pixel_value = 255.0
                        psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

                    return psnr
                except:
                    print("No file found !")
                    mb.showerror("PSNR Analysis Error","Specified file not found ! Please check and proceed.")

            azlabel=customtkinter.CTkLabel(analyzeui,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=475)
            azlabel1=customtkinter.CTkLabel(analyzeui,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=75)
            label123 = customtkinter.CTkLabel(analyzeui,text="IMAGE ANALYSIS:",font=("Times New Roman",30)).place(x=135,y=23)
            label55 = customtkinter.CTkLabel(analyzeui,text="Select the Cover Work :",font=("Times New Roman",18))
            label55.place(relx=0.1,rely=0.25)
            label57 = customtkinter.CTkLabel(analyzeui,text="Select the Stego Work :",font=("Times New Roman",18))
            label57.place(relx=0.1,rely=0.418)
            psnrbutton=customtkinter.CTkButton(analyzeui,text="PSNR",width=100,font=('Bahnschrift',14),command=psnr).place(x=205,y=338)
            ssimbutton=customtkinter.CTkButton(analyzeui,text="SSIM",width=100,font=('Bahnschrift',14),command=ssimmm).place(x=205,y=388)
            closingbutton=customtkinter.CTkButton(analyzeui,text="Menu",width=100,font=('Bahnschrift',14),command=backtomenu).place(x=205,y=438)
            button33= customtkinter.CTkButton(analyzeui, text="Select file", width=125,font=('Bahnschrift',14),command=OpenFile1).place(x=250,y=180)
            SaveEntryaz1 = customtkinter.CTkEntry(analyzeui,width=240,font=('Bahnschrift', 14))
            SaveEntryaz1.place(relx=0.5,rely=0.250)
            button32= customtkinter.CTkButton(analyzeui, text="Select File",width=125, font=('Bahnschrift',14),command=OpenFile2).place(x=250,y=270)
            SaveEntryaz2 = customtkinter.CTkEntry(analyzeui,width=240,font=('Bahnschrift', 14))
            SaveEntryaz2.place(relx=0.5,rely=0.420)
            analyzeui.configure(bg="black")
            analyzeui.mainloop()

        button= customtkinter.CTkButton(GUI, text="Encode", width=125,font=('Bahnschrift',14),command=enncoder).place(x=320,y=160)
        button2= customtkinter.CTkButton(GUI, text="Decode",width=125, font=('Bahnschrift',14),command=decoder).place(x=320,y=210)
        button6= customtkinter.CTkButton(GUI, text="Analyse", width=125,font=('Bahnschrift',14),command=analysispage).place(x=320,y=260)

        button9= customtkinter.CTkButton(GUI, text="Close", width=125,font=('Bahnschrift',14),command=GUI.destroy).place(x=320,y=310)
        button19= customtkinter.CTkButton(GUI, text="Log-Out", width=125,font=('Bahnschrift',14),command=backtologin).place(x=320,y=360)
        abbbbutton=customtkinter.CTkButton(GUI,text="About",width=125,font=('Bahnschrift',14),command=about).place(x=320,y=420)
        
        dlabel=customtkinter.CTkLabel(GUI,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=500)

        # clabel = customtkinter.CTkLabel(GUI,text="Done By : Lokesh",font=("Times New Roman",15),).place(x=235,y=480)
        # rlabel = customtkinter.CTkLabel(GUI,text="B.Tech - CSE(CS & BT)",font=("Times New Roman",15),).place(x=270,y=510)
        GUI.configure(bg="black")
        # GUI.resizable(False,False)
        GUI.maxsize(750,550)
        GUI.mainloop()

    def SignupPage():
        signupp=customtkinter.CTk()
        signupp.geometry("300x300")
        signupp.maxsize(300,300)
        signupp.title("Registration")

        def validate_user(username):
            # Checks the text file for a username/password combination.
            try:
                with open("Credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username:
                            return False
                return True
            except FileNotFoundError:
                return True

        def signup():
            # Creates a text file with the Username and password
            user = entry_user.get()
            pw = entry_pw.get()
            validation = validate_user(user)
            if not validation:
                mb.showerror("Information", "That Username already exists")
            else:
                if len(pw) > 3:
                    credentials = open("Credentials.txt", "a")
                    credentials.write(f"Username,{user},Password,{pw},\n")
                    credentials.close()
                    mb.showinfo("Information", "Succesfully Registered ! Please Log In")
                    signupp.destroy()
                else:
                    mb.showerror("Information", "Your password needs to be longer than 3 values.")

        title1_styles = {"font": ("Trebuchet MS Bold", 20), "background": "black","foreground":"white"}

        text_styles = {"font": ("Verdana", 11),
                    "background": "#3F6BAA",
                    "foreground": "#E1FFFF"}
        
        # bb=tkinter.PhotoImage(file="pattern2.png")
        # limg= Label(signupp, i=bb)
        # limg.pack()

        label_signup = customtkinter.CTkLabel(signupp,font=('Trebuchet MS Bold', 20), text="Sign Up !")
        label_signup.place(relx=0.38, rely=0.05)
        
        label_user = customtkinter.CTkLabel(signupp, font=('Consolas',16), text="New Username:")
        label_user.place(relx=0.08, rely=0.2)

        label_pw = customtkinter.CTkLabel(signupp,font=('Consolas',16), text="New Password:")
        label_pw.place(relx=0.08, rely=0.4)

        entry_user = customtkinter.CTkEntry(signupp, width=116,font=('Bahnschrift',14))
        entry_user.place(relx=0.50, rely=0.21)

        entry_pw = customtkinter.CTkEntry(signupp, width=116,font=('Bahnschrift',14),show="*")
        entry_pw.place(relx=0.50, rely=0.41)

        button = customtkinter.CTkButton(signupp, text="Create Account",font=('Bahnschrift',15),height=1,width= 60,command=lambda: signup())
        button.place(relx=0.313, rely=0.63)

        button = customtkinter.CTkButton(signupp, text="Close",height=1,width= 60,font=('Bahnschrift',15),command=signupp.destroy)
        button.place(relx=0.383, rely=0.75)

        signupp.configure(bg="black")
        signupp.mainloop()

        def validate_user(username):
            # Checks the text file for a username/password combination.
            try:
                with open("Credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username:
                            return False
                return True
            except FileNotFoundError:
                return True

    def signup_pageee():
        SignupPage()

    def validate(username, password):
        # Checks the text file for a username/password combination.
        try:
            with open("Credentials.txt", "r") as credentials:
                for line in credentials:
                    line = line.split(",")
                    if line[1] == username and line[3] == password:
                        return True
                return False
        except FileNotFoundError:
            print("You need to Register first")
            return False

    def gettlogin():
            username = entry1.get()
            password = entry2.get()

            # if your want to run the script as it is set validation = True
            validation = validate(username, password)

            if validation:
                mb.showinfo("Login Successful","Welcome {} ! <3".format(username))
                Auth.destroy()
                Steggg()
            else:
                mb.showerror("Information", "The Username or Password you have entered are incorrect ")

    def getlogin():
        gettlogin()

    def totalclose():
                res4=mb.askquestion('Menu !', 'Do you really want to QUIT ?')
                if(res4 == 'yes'):
                    Auth.destroy()
                else:
                    mb.showinfo('Return', 'Returning to Tool !')

    title_styles = {"font": ("Trebuchet MS Bold", 21), "background": "black","foreground":"white"}

    text_styles = {"font": ("Consolas", 14),
                        "background": "black",
                        "foreground": "white"}

    # frame_login = customtkinter.CTkLabel(Auth,"LOGIN Page")  # this is the frame that holds all the login details and buttons
    # frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

    label_title = customtkinter.CTkLabel(Auth, text="Login Page",font=('Trebuchet MS Bold',30))  
    label_title.place(relx=0.400,rely=0.135)

    label_user = customtkinter.CTkLabel(Auth, text="Username:",font=('Consolas',18))
    label_user.place(relx=0.2,rely=0.28)

    label_pw = customtkinter.CTkLabel(Auth, text="Password:",font=('Consolas',18))
    label_pw.place(relx=0.2, rely=0.39)

    entry_user = customtkinter.CTkEntry(Auth,font=('Bahnschrift',15), width=270,corner_radius=7)
    entry_user.place(relx=0.4, rely=0.275)

    entry_pw = customtkinter.CTkEntry(Auth,width=270, font=('Bahnschrift',15),corner_radius=7,show="*")
    entry_pw.place(relx=0.4, rely=0.395)

    button = customtkinter.CTkButton(Auth, text="Login", font=('Bahnschrift',14),width=123 ,command=getlogin)
    button.place(rely=0.49, relx=0.4)

    signup_btn = customtkinter.CTkButton(Auth, text="Register",font=('Bahnschrift',14), width=123, command=signup_pageee)
    signup_btn.place(rely=0.49, relx=0.62)

    signup_btn = customtkinter.CTkButton(Auth, text="Close",font=('Bahnschrift',14), width=123, command=totalclose)
    signup_btn.place(rely=0.58, relx=0.49)
    
    # Auth.configure(bg="black")
    imga1=ImageTk.PhotoImage(Image.open("pattern.png"))
    l1=customtkinter.CTkLabel(Auth,image=imga1)
    l1.pack()

    frame=customtkinter.CTkFrame(l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(frame, text="Log In :)",font=('Century Gothic',21))
    l2.place(x=130, y=45)

    entry1=customtkinter.CTkEntry(frame, width=220,font=('Bahnschrift',16), placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2=customtkinter.CTkEntry(frame, width=220,font=('Bahnschrift',16), placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    # l3=customtkinter.CTkLabel(frame, text="Forget password?",font=('Century Gothic',12))
    # l3.place(x=155,y=195)

    buttonlog = customtkinter.CTkButton(frame, width=220, text="Login", command=getlogin, font=('Bahnschrift',16),corner_radius=6)
    buttonlog.place(x=50, y=220)

    buttonsign = customtkinter.CTkButton(frame, width=220, text="Sign-Up", command=signup_pageee,font=('Bahnschrift',16), corner_radius=6)
    buttonsign.place(x=50, y=270)

    clb = customtkinter.CTkButton(frame, width=220, text="Close", command=Auth.destroy,font=('Bahnschrift',16), corner_radius=6)
    clb.place(x=50, y=320)

    # Auth.resizable(False,False)
    Auth.maxsize(650,450)
    # sv_ttk.set_theme("dark")
    # dlabel=customtkinter.CTkLabel(Auth,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------",).place(x=0,y=400)
    Auth.mainloop()

w=Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)

# s = ttk.Style()
# s.theme_use('clam')
# s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')

progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')

def new_win():
  #w.destroy()
  main()

def bar():
    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Consolas',10)
    l4.config(font=lst4)
    l4.place(x=172,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    w.destroy()
    new_win()

    image_b=ImageTk.PhotoImage(Image.open("c1.png"))
    image_a=ImageTk.PhotoImage(Image.open("c2.png"))

    for i in range(3):
        l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=210)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=210)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=210)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=210)
        w.update_idletasks()
        time.sleep(0.3)

        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.3)

        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.3)

        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.3)
        
progress.place(x=-10,y=235)

'''
def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''

a='black'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)
b1=Button(w,width=13,height=1,text='Start Tool',font=('bahnschrift',10),command=bar,border=0,fg=a,bg='white')
b1.place(x=160,y=180)

l1=Label(w,text='Mini Project.',fg='white',bg=a)
lst1=('Bahnschrift',20,'bold')
l1.config(font=lst1)
l1.place(x=135,y=70)

# l2=Label(w,text='SCREEN',fg='white',bg=a)
# lst2=('Calibri (Body)',18)
# l2.config(font=lst2)
# l2.place(x=155,y=82)

l3=Label(w,text='[ By Lokesh]',fg='white',bg=a)
lst3=('Bahnschrift',15)
l3.config(font=lst3)
l3.place(x=150,y=110)

w.mainloop()