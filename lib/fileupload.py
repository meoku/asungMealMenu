import os

UPLOAD_FOLDER = os.getcwd() + '\\uploadfile'  # 절대 파일 경로
ALLOWED_EXTENSIONS = ['pdf', 'png', 'jpg', 'jpeg']

def file_check(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
