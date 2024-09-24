import os
import requests
from bs4 import BeautifulSoup

# 닉네임 설정
nick = '시프'

# 크롤링할 URL
url = f'https://maple.gg/u/{nick}'

# 폴더 경로 설정
picture_folder = 'picture'

# 폴더가 없으면 생성
if not os.path.exists(picture_folder):
    os.makedirs(picture_folder)

# 웹 페이지 요청
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 이미지 태그 찾기
    image_element = soup.find('img', class_='character-image')

    if image_element:
        # 이미지 URL 가져오기
        image_url = image_element['src']
        print(f"Image URL: {image_url}")

        # 이미지 데이터 다운로드
        image_response = requests.get(image_url)

        # 파일 저장 경로
        image_path = os.path.join(picture_folder, f"{nick}.png")

        # 이미지 저장
        with open(image_path, 'wb') as file:
            file.write(image_response.content)

        print(f"이미지가 {image_path}에 저장되었습니다.")
    else:
        print(f"{nick}의 캐릭터 이미지를 찾을 수 없습니다.")
else:
    print(f"Failed to fetch the webpage. HTTP Status: {response.status_code}")
