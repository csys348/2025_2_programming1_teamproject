
from cs1graphics import *

# =================================================================
# [수정됨] 테두리 있는 텍스트 클래스
# =================================================================
class OutlinedText(Layer):
    def __init__(self, message, font_size, text_color='white', border_color='black', border_width=2):
        super().__init__()
        
        # 1. 테두리 역할을 할 텍스트들 (뒤쪽)
        # 8방향(좌, 우, 상, 하, 대각선)으로 살짝씩 어긋난 글자를 만들어 테두리처럼 보이게 함
        offsets = [
            (-border_width, 0), (border_width, 0),
            (0, -border_width), (0, border_width),
            (-border_width, -border_width), (border_width, -border_width),
            (-border_width, border_width), (border_width, border_width)
        ]
        
        for dx, dy in offsets:
            border_txt = Text(message, font_size)
            border_txt.setFontColor(border_color)
            # 두께가 너무 과하지 않게 오프셋 조절 (나누기 2)
            border_txt.move(dx/2, dy/2) 
            self.add(border_txt)
            
        # 2. 진짜 글씨 (가장 앞쪽)
        main_txt = Text(message, font_size)
        main_txt.setFontColor(text_color)
        self.add(main_txt)


# =================================================================
# 테스트 실행 코드 (이 파일만 실행할 때 작동)
# =================================================================
if __name__ == "__main__":
    # 캔버스 열기
    paper = Canvas(400, 200, 'skyblue', 'Text Object Test')
    
    # -------------------------------------------------------------
    # [오류 해결 포인트] 이 코드는 클래스 밖으로 나와 있어야 합니다!
    # -------------------------------------------------------------
    # 객체 생성 테스트
    msg = OutlinedText('Merry Christmas!', 40, 'white', 'darkblue', 3)
    msg.moveTo(200, 100)
    
    paper.add(msg)
    paper.wait()
    
