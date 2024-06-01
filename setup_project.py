import os

def create_project_structure():
    project_name = "vcf-filter-app"
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    # Create directories
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static", exist_ok=True)  # Currently unused, but available
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("downloads", exist_ok=True)

    # Create and write to vcf_filter.py
    with open("vcf_filter.py", "w") as file:
        file.write(
            """from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__)

# Ensure directories for uploads and downloads exist
os.makedirs('uploads', exist_ok=True)
os.makedirs('downloads', exist_ok=True)

@app.route('/')
def index():
    # Render the upload form
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Process uploaded files and return cleaned VCF
    file = request.files['file']
    if file:
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        output_path = os.path.join('downloads', 'clean_' + file.filename)
        process_vcf(filepath, output_path)
        return send_from_directory('downloads', 'clean_' + file.filename, as_attachment=True)

def process_vcf(input_path, output_path):
    # Implement your VCF file processing logic here
    pass

if __name__ == '__main__':
    app.run(debug=True)
"""
        )

    # Create and write to templates/index.html
    with open("templates/index.html", "w") as file:
        file.write(
            """<!DOCTYPE html>
<html>
<head>
    <title>Upload VCF File</title>
</head>
<body>
    <h1>Upload VCF File</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload and Clean">
    </form>
</body>
</html>
"""
        )

    # Create and write to requirements.txt
    with open("requirements.txt", "w") as file:
        file.write(
            """Flask==2.0.1
gunicorn==20.0.4
"""
        )

    # Create and write to Procfile
    with open("Procfile", "w") as file:
        file.write(
            "web: gunicorn vcf_filter:app\n"
        )

    # Create and write to .gitignore
    with open(".gitignore", "w") as file:
        file.write(
            """venv/
*.pyc
__pycache__/
instance/
.webassets-cache
uploads/
downloads/
"""
        )

    print("Project setup complete. You can now proceed to use GitHub Desktop to publish your project.")

if __name__ == "__main__":
    create_project_structure()