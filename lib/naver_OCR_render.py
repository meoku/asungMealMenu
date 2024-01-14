import json
import uuid
import time
import requests
def naver_OCR_reader(naver_ocr_url, naver_api_scret_key, templateids, image_url):
    request_json = {
        'images': [
            {
                'format': 'png',
                'name': 'demo',
                'url' : image_url,
                'templateIds': [templateids]
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V1',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = json.dumps(request_json).encode('UTF-8')

    headers = {
    'X-OCR-SECRET': naver_api_scret_key,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", naver_ocr_url, headers=headers, data = payload)
    
    return response

def request_naver_OCR_reader_api_by_file(naver_ocr_url, naver_api_scret_key, templateids, image_file_path):
    #바이너리 형태로 읽어오기
    menu_img = [('file', open(image_file_path, 'rb'))]

    request_json = {
        'images': [
            {
                'format': 'png',
                'name': 'demo',
                'templateIds': [templateids]
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V1',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = json.dumps(request_json).encode('UTF-8')

    headers = {
        'X-OCR-SECRET': naver_api_scret_key
        #, 'Content-Type': 'application/json'
    }

    response = requests.request("POST", naver_ocr_url, headers=headers, data = payload, files = menu_img)
    
    return response