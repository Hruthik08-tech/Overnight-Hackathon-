import os 
from flask import Flask, render_template, url_for, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__) 

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def intro():
    return render_template('landing.html')

# This is a "reciever function"
@app.route('/upload_handler', methods=['POST'])
def upload_handler():
    if 'files[]' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    files = request.files.getlist('files[]')
    
    saved_files = []
    for file in files:
        if file.filename == '':
            continue
            
        if file:
            # secure_filename makes sure the filename is safe to save
            filename = secure_filename(file.filename)
            
            # Construct the full path: "pdf list/filename.pdf"
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Write the file to the disk
            file.save(save_path)
            saved_files.append(filename)
            print(f"Saved: {save_path}")

    return jsonify({"message": f"Successfully saved {len(saved_files)} files", "files": saved_files})

if __name__ == "__main__":
    app.run(debug= True)

