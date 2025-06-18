from flask import Flask, render_template, request
import os
from nst import perform_nst

# Initialize Flask app
app = Flask(__name__)

# Define upload and result folders
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Configure app folders
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content_file = request.files['content']
        style_file = request.files['style']

        if content_file and style_file:
            # Save uploaded content and style images
            content_filename = content_file.filename
            style_filename = style_file.filename

            content_path = os.path.join(app.config['UPLOAD_FOLDER'], content_filename)
            style_path = os.path.join(app.config['UPLOAD_FOLDER'], style_filename)

            content_file.save(content_path)
            style_file.save(style_path)

            # Output image will be saved as 'output.jpg' in results
            output_filename = 'output.jpg'
            output_path = os.path.join(app.config['RESULT_FOLDER'], output_filename)

            # Call NST logic
            perform_nst(content_path, style_path, output_path)

            # Pass image paths (relative to static/) to HTML
            return render_template(
                'index.html',
                output_image=f'results/{output_filename}',
                content_image=f'uploads/{content_filename}',
                style_image=f'uploads/{style_filename}'
            )

    # GET request: no images to show yet
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
