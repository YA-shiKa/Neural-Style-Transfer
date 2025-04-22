from flask import Flask, render_template, request
import os
from nst import perform_nst

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content_file = request.files['content']
        style_file = request.files['style']

        if content_file and style_file:
            content_path = os.path.join(app.config['UPLOAD_FOLDER'], content_file.filename)
            style_path = os.path.join(app.config['UPLOAD_FOLDER'], style_file.filename)
            content_file.save(content_path)
            style_file.save(style_path)

            output_path = os.path.join(app.config['RESULT_FOLDER'], 'output.jpg')
            perform_nst(content_path, style_path, output_path)

            output_image = 'results/output.jpg'  # path relative to static/
            return render_template('index.html', output_image=output_image)

    return render_template('index.html', output_image=None)

if __name__ == '__main__':
    app.run(debug=True)
