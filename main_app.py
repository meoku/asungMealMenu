from flask import Flask, request, render_template
from lib.fileupload import *
from lib.util import *

import lib.naver_OCR_render as nc
import os
import json
import yaml

with open('lib/config.yaml', 'r') as f:
    config = yaml.load(f)
    
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #최대 업로드 파일 16MB 제한


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/uploadMealMenu')
def fileupload_page():
    return render_template('uploadMealMenu.html')

@app.route('/fileupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['savefile']
        if file and file_check(file.filename):
            filename = file.filename
            filepathtosave = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepathtosave)
            #naver cloud OCR api 사용해서 text로 메뉴 받아오기
            latest_meal_menu = json.loads(nc.naver_OCR_reader(config['naver_ocr_url']
                       , config['naver_api_scret_key']
                       , config['TEMPLATEIDS']
                       , filepathtosave).text
                    )
            
            save_meal_menu_this_weekend(latest_meal_menu)
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)