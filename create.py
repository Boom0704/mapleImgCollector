import csv
import os
from datetime import datetime

# CSV 파일 경로 설정
csv_file = 'character.csv'


# CSV 파일에서 데이터를 불러오는 함수
def load_csv_data():
    # 파일이 존재하지 않으면 빈 리스트 반환
    if not os.path.exists(csv_file):
        return []

    # 파일을 열어서 데이터를 읽어옴
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


# CSV 파일에 데이터를 저장하는 함수
def save_csv_data(data):
    # 필드명 정의
    fieldnames = ['nick', 'url', 'create_at', 'update_at']

    # 파일이 없으면 새로 생성하면서 헤더 추가
    file_exists = os.path.exists(csv_file)

    with open(csv_file, mode='a' if file_exists else 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # 파일이 없으면 헤더 작성

        writer.writerow(data)  # 데이터를 파일에 추가


# 닉네임 존재 여부 확인 및 데이터 저장 함수
def create_character(nick_value):
    if not nick_value:
        return "닉네임을 입력해주세요."

    existing_data = load_csv_data()

    # 닉네임 중복 확인
    for row in existing_data:
        if 'nick' in row and row['nick'] == nick_value:
            return "이미 존재합니다."

    # 새로운 데이터 추가
    new_data = {
        'nick': nick_value,
        'url': '',  # url은 빈값
        'create_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # 현재 시간 저장
        'update_at': ''  # update_at은 빈값
    }

    save_csv_data(new_data)
    return "새로운 항목이 저장되었습니다."


# CSV 파일에서 데이터 불러오기 함수
def fetch_characters():
    data = load_csv_data()
    if not data:
        return "데이터가 없습니다."
    return data
