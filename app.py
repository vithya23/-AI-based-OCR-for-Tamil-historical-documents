from flask import Flask, render_template, request
import easyocr
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

reader = easyocr.Reader(['ta'])  # Tamil OCR

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = ""
    if request.method == 'POST':
        image = request.files['image']
        if image:
            path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(path)
            result = reader.readtext(path, detail=0)
            result_text = "\n".join(result)
    return render_template('index.html', result=result_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)