# face_recognitionAttendenceSystem

(I have added obama and biden images too in datset of images so that user can cross check face recognition without doing any extra effort as these image can be found easily in internet)\
(user can also add their one clear front image in image folder for face recognition)</br> 

**I used windows machine while working on this project**

Requirements:</br>
  installed libraries- cmake, opencv-python, face_recognition, os, datetime, numpy</br>
  You can install them using command:</br>
 > on windows: `pip install opencv-python`</br>
                `pip install face_recognition`</br>
             (same way install other libraries)</br>
             
  in windows cmake compiler is most of the time not found so for that install visual studio </br>          
     
To run these files in system. </br>
Create a folder (eg. project) </br>
Download all the files/folders in the project in order </br>
in project folder start cmd  </br>
>(create venv environment to host) </br>
for that run below command </br>
 - mac: `python3 -m venv venv`
 - windows: `python -m venv venv`
  
>activate venv env
 - mac: `source venv/bin/activate`
 - windows: `venv\Scripts\activate`
   
   
Now when venv is active 
>install flask:
    -`pip install flask`
    
    
   **To run program** 
  >run command: `python main.py`
    
server will start
    with `local host`: http://127.0.0.1:5000 </br>
    copy and paste this on your browser(eg. chrome)
    
    
    
# server Hosting getting failed till now 
    
**I tried to host this project on Heroku**
    after resolving many failed deploys  </br>
    finaly when I succeede to depploy without any error, as I got another error saying memory exceeded so got to the conclusion as I had a free account I won't be able to start live server her </br>
    
**Then I shifted to deploy my project on `Microsoft Azure App services`** </br>
    I `created my student account` so was able to access the resources </br>
    **set linux on azure OS**  </br>
    but Currently I am not able to deploy it as it showing `cmake error` </br>
    
   so I added `cmake` in `requirements.txt file` so that it can get installed while deploying  </br>
 but system(azure) was not able to find cmake even after installing ( well it's showing same error which windows OS shows, I corrected that in my OS by downloading Visual Studio and installing required resources from it but don't know what to do here)   </br>
    
