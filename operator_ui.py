import tkinter as tk
from create import create_character
from image import update_all_characters  # image.py에서 불러오는 함수

# 생성 버튼 클릭 시 호출되는 함수
def create_character_action():
    nick_value = nick_entry.get().strip()  # 입력한 닉네임 값 가져오기
    result = create_character(nick_value)  # create.py에서 데이터 저장
    status_label.config(text=result)  # 상태창에 결과 출력

# 불러오기 버튼 클릭 시 image.py 실행
def fetch_images_action():
    update_all_characters()  # image.py에서 캐릭터 이미지 업데이트 실행
    status_label.config(text="이미지 업데이트 완료")  # 상태창에 메시지 출력

# Tkinter 기본 설정
root = tk.Tk()
root.title("캐릭터 관리")

# 입력 필드와 생성 버튼
nick_label = tk.Label(root, text="닉네임 입력:", font=("Arial", 12))
nick_label.grid(row=0, column=0, padx=10, pady=10)

nick_entry = tk.Entry(root, font=("Arial", 12))
nick_entry.grid(row=0, column=1, padx=10, pady=10)

create_button = tk.Button(root, text="생성", command=create_character_action, font=("Arial", 12))
create_button.grid(row=0, column=2, padx=10, pady=10)

# 불러오기 버튼
fetch_button = tk.Button(root, text="불러오기", command=fetch_images_action, font=("Arial", 12))
fetch_button.grid(row=1, column=1, pady=10)

# 상태창
status_label = tk.Label(root, text="상태창", font=("Arial", 12), fg="blue")
status_label.grid(row=2, column=0, columnspan=3, pady=10)

# Tkinter 이벤트 루프 시작
root.mainloop()
