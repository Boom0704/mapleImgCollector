import os
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# CSV 파일 경로 설정
csv_file = 'character.csv'
picture_folder = 'picture'

# 폴더가 없으면 생성
if not os.path.exists(picture_folder):
    os.makedirs(picture_folder)


# 이미지 크롤링 및 저장 함수
def fetch_and_save_image(nick):
    url = f'https://maple.gg/u/{nick}'
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
            return image_url  # 이미지 URL 반환
        else:
            print(f"{nick}의 캐릭터 이미지를 찾을 수 없습니다.")
            return None
    else:
        return None


# CSV 파일에서 데이터를 불러오는 함수
def load_csv_data():
    if not os.path.exists(csv_file):
        return []

    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


# CSV 파일을 덮어씌우는 함수
def overwrite_csv_data(data):
    fieldnames = ['nick', 'url', 'create_at', 'update_at']

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# 모든 캐릭터의 이미지를 크롤링하고 CSV에 업데이트하는 함수
def update_all_characters():
    data = load_csv_data()  # character.csv 읽기
    result = []  # 결과를 저장할 리스트

    for row in data:
        nick = row['nick']
        image_url = fetch_and_save_image(nick)  # 이미지 크롤링

        if image_url:
            # 이미지 URL과 현재 시간을 CSV에 저장할 데이터에 업데이트
            row['url'] = image_url
            row['update_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result.append(f"{nick}: 이미지가 성공적으로 저장되었습니다.")
        else:
            result.append(f"{nick}: 이미지를 찾을 수 없습니다.")

    overwrite_csv_data(data)  # 업데이트된 데이터를 덮어씌우기
    return result  # 결과를 리턴


# 실행
if __name__ == '__main__':
    results = update_all_characters()  # 실행 결과 받아오기
    for res in results:
        print(res)  # 각 캐릭터별 결과 출력
