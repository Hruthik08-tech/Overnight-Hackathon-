# Overnight-Hackathon-
An AI-powered website to automate the task labelling process 

This project is a simple, lightweight system for uploading multiple PDF files through choose file option. The frontend is created using HTML, CSS and javascript for basic interactivity, and the backend uses Flask to handle file uploads and routing and rendering templates. 

/HACKATHON
1. app.py
2. templates
   landing.html
3. static
   css/
           landing.css
           base.css
   js/
           landing.js

4. uplaods
   
   

# How it works 
Frontend:
1. Choose PDF's manually
2. Shows list of selected files
3. Sends files to server using FormData() and fetch()

Backend:
1. Recives files on /upload_handler (POST)
2. Saves them safely using secure_filename
3. stores everything in uploads/ directory
4. Returns a json response confirming how many files were saved

# Run the App 

1. Install Flask
pip install flask

2. Go the command prompt
python "app.py"

3. Open your brower and visit
http://127.0.0.1:5000/


