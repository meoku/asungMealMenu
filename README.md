## Introduction & Discription
- Asung 본사 식단 메뉴정보를 가져오는 API 및 API서버
- 식단메뉴 공지 자동화를 위한 API

## Installation Guide(설치가이드)
```
pip install requirements.txt
```
## Usage(사용법)
```
python listup_all_meal.py
```
## Examples(예제)

## Features(기능목록)
- json 형태로 받을 수 있는 Flask API 서버
- 식단 정보 아래의 과정을 거쳐 데이터로 저장
  1. Naver Band에 올라온 이미지를 수집
  2. Naver Cloud의 CLOVA OCR을 사용하여 Image -> Text 로 데이터 변환
  3. 1,2 과정을 거쳐 csv형태로 데이터 저장 혹은 바로 json형태로 반환(API)

## Technology Stack(기술스택)
- NAVER BAND API
- NAVER CLOUD CLOVA OCR



## License


## Notes
