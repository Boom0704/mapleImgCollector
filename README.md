# mapleImgCollector
이 프로그램은 Maple.gg에서 캐릭터 이미지를 자동으로 크롤링하고, 사용자 입력을 기반으로 캐릭터 정보를 관리할 수 있는 간단한 GUI 프로그램입니다. Tkinter를 사용하여 간단한 인터페이스를 제공하며, 캐릭터 생성과 이미지 업데이트 기능을 포함하고 있습니다.

## 기능
캐릭터 생성: 사용자가 입력한 닉네임을 기반으로 character.csv 파일에 캐릭터 정보를 저장합니다.
이미지 업데이트: image.py를 실행하여 Maple.gg에서 캐릭터 이미지를 자동으로 크롤링한 후, 해당 캐릭터의 이미지 URL과 함께 정보를 업데이트합니다.

## 프로그램 구성
create.py: 캐릭터 생성 로직을 담당하는 모듈입니다. 입력된 닉네임을 character.csv 파일에 저장합니다.
image.py: 캐릭터 이미지 크롤링 및 이미지 파일 다운로드를 담당하는 모듈입니다. Maple.gg에서 캐릭터 이미지를 가져와 character.csv 파일에 저장하고, 이미지를 로컬에 저장합니다.
operator_ui.py: 사용자 인터페이스(UI)를 담당하는 메인 프로그램입니다. 입력창과 버튼을 통해 create.py와 image.py의 기능을 쉽게 실행할 수 있습니다.

## 사용법
캐릭터 생성:

프로그램 실행 후, 입력창에 닉네임을 입력합니다.
"생성" 버튼을 클릭하면, 입력한 닉네임이 character.csv 파일에 저장됩니다.
작업 완료 후 상태창에 "캐릭터가 생성되었습니다"라는 메시지가 표시됩니다.
이미지 업데이트:
"불러오기" 버튼을 클릭하면, image.py가 실행되어 Maple.gg에서 캐릭터 이미지를 자동으로 크롤링합니다.
이미지가 크롤링된 후, character.csv 파일에 이미지 URL과 수정 시간이 기록됩니다.
작업 완료 후 상태창에 "이미지 업데이트 완료"라는 메시지가 표시됩니다.

## 시스템 요구 사항
Python 3.x 이상
Tkinter (Python GUI 라이브러리)
Requests (HTTP 라이브러리)
BeautifulSoup4 (HTML 파싱 라이브러리)

## 설치 방법
필요한 패키지 설치:
```pip install requests beautifulsoup4```

## 프로그램 실행:
```python operator_ui.py```

폴더 구조
```/project-directory
│
├── operator_ui.py       # 사용자 인터페이스 프로그램
├── create.py            # 캐릭터 생성 모듈
├── image.py             # 캐릭터 이미지 크롤링 모듈
├── character.csv        # 캐릭터 정보가 저장되는 파일
└── picture/             # 크롤링된 캐릭터 이미지가 저장되는 폴더
```

## 주의 사항
프로그램을 처음 실행하면 character.csv 파일과 picture/ 폴더가 자동으로 생성됩니다.
크롤링된 이미지는 picture/ 폴더에 저장됩니다.
Maple.gg의 페이지 구조가 변경되면 이미지 크롤링이 정상적으로 작동하지 않을 수 있습니다.
