import requests
import json
import yaml
import lib.naver_OCR_render as nc
from lib.util import *

# Access token, band key 등 민감한 정보는 파일에 담아 한번에 관리
with open('lib/config.yaml', 'r') as f:
    config = yaml.load(f)

band_api_url = config['band_api_url']
access_token = config['access_token']
band_key = config['band_key']


result_content_list = []

def run(band_api_url, access_token, band_key, after_param, level):
    
    if level > 3: return #1Level당 20개씩 이므로 총 60 개 불러온다.
    
    url = band_api_url
    if after_param is None:
        url += f"?access_token={access_token}&band_key={band_key}"
    else:
        url += f"?after={after_param}&access_token={access_token}&band_key={band_key}"

    response = requests.get(url, timeout = 2)# 2초지나면 예외발생

    if response.status_code == 200:
        response_to_json = json.loads(response.text)
        content_list = response_to_json['result_data']['items']

        for content in content_list:
            result_content_list.append(content)

        # Band API는 20개씩 페이징 되어서 값 반환하기 때문에 다음 페이지 목록은 재귀형식으로 불러옴
        next_params = response_to_json['result_data']['paging']['next_params']
        if next_params is not None:
            run(band_api_url, access_token, band_key, next_params['after'], level+1)


def app():
    run(band_api_url, access_token, band_key, None, 1)

    # 55번째 까지가 2023년1월2일
    print(result_content_list[55]['photos'][0]['url'])

    error_images = []
    total_running_count = 0
    success_count = 0
    fail_count = 0
    for i in range(55,-1,-1):
        print(f"success : {success_count}, fail : {fail_count} - {(total_running_count/55)*100}% 진행중")

        if fail_count > 5 : break  #너무 많은 오류 발생시 프로그램 정지(Naver Cloud Api 무료 호출 카운트가 월 300이기 때문에 아껴야함)

        try:
            temp_img_url = result_content_list[i]['photos'][0]['url']

            this_meal_menu = json.loads(nc.naver_OCR_reader(config['naver_ocr_url']
                                , config['naver_api_scret_key']
                                , config['TEMPLATEIDS']
                                , temp_img_url).text
                                )
            
            save_meal_menu_all_weekend(this_meal_menu)

            success_count += 1
        except:
            error_images.append(result_content_list[i])
            fail_count +=1

        total_running_count += 1
    
if __name__ == "__main__":
    app()