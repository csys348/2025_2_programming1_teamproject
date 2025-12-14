
from cs1graphics import *
import time
import math

# =================================================================
# 1. 목도리 클래스 (Scarf Layer)
# =================================================================
class Scarf(Layer):
    def __init__(self, scale_factor=1.0):
        super().__init__()  # 부모 클래스(Layer) 초기화

        # 색상 정의
        main_color = (200, 80, 40)
        stripe_color = (230, 140, 60)
        outline_color = (130, 40, 20)
        shadow_color = (160, 60, 30)

        # ---------------------------------------------------------
        # 내부 헬퍼 함수: 술(Fringes) 그리기
        # ---------------------------------------------------------
        def create_fringes(start_x, start_y, width, num_fringes):
            step = width / num_fringes
            for i in range(num_fringes + 1):
                x = start_x + (i * step)
                fringe = Path(Point(x, start_y), Point(x, start_y + 15), Point(x - 2, start_y + 18))
                fringe.setBorderColor(outline_color)
                fringe.setBorderWidth(3)
                fringe.setDepth(60)
                self.add(fringe)

        # A. 왼쪽 아래로 늘어진 부분 (Left Tail)
        left_tail = Polygon(Point(-40, 50), Point(10, 50), Point(20, 180), Point(-50, 180))
        left_tail.setFillColor(main_color)
        left_tail.setBorderColor(outline_color)
        left_tail.setBorderWidth(2)
        left_tail.setDepth(50)
        self.add(left_tail)

        # 왼쪽 줄무늬
        l_stripe1 = Path(Point(-48, 150), Point(18, 150))
        l_stripe1.setBorderColor(stripe_color)
        l_stripe1.setBorderWidth(8)
        l_stripe1.setDepth(49)
        self.add(l_stripe1)

        l_stripe2 = Path(Point(-46, 130), Point(16, 130))
        l_stripe2.setBorderColor(stripe_color)
        l_stripe2.setBorderWidth(8)
        l_stripe2.setDepth(49)
        self.add(l_stripe2)

        create_fringes(-50, 180, 70, 7)

        # B. 오른쪽 아래로 늘어진 부분 (Right Tail)
        right_tail = Polygon(Point(10, 50), Point(60, 50), Point(70, 160), Point(10, 160))
        right_tail.setFillColor(main_color)
        right_tail.setBorderColor(outline_color)
        right_tail.setBorderWidth(2)
        right_tail.setDepth(40)
        self.add(right_tail)

        # 오른쪽 줄무늬
        r_stripe1 = Path(Point(12, 135), Point(68, 135))
        r_stripe1.setBorderColor(stripe_color)
        r_stripe1.setBorderWidth(8)
        r_stripe1.setDepth(39)
        self.add(r_stripe1)

        r_stripe2 = Path(Point(14, 115), Point(66, 115))
        r_stripe2.setBorderColor(stripe_color)
        r_stripe2.setBorderWidth(8)
        r_stripe2.setDepth(39)
        self.add(r_stripe2)

        create_fringes(10, 160, 60, 6)

        # C. 목 뒤쪽 부분 (Back Loop)
        back_loop = Polygon(Point(-30, 20), Point(10, 10), Point(50, 20), Point(50, 40), Point(10, 50), Point(-30, 40))
        back_loop.setFillColor(shadow_color)
        back_loop.setBorderColor(outline_color)
        back_loop.setDepth(100)
        self.add(back_loop)

        # D. 목 앞쪽 부분 (Front Loop / Collar)
        front_collar = Polygon(
            Point(-50, 25), Point(0, 15), Point(70, 25), 
            Point(80, 45),                               
            Point(70, 65), Point(0, 75), Point(-50, 65), 
            Point(-60, 45)                               
        )
        front_collar.setFillColor(main_color)
        front_collar.setBorderColor(outline_color)
        front_collar.setBorderWidth(2)
        front_collar.setDepth(10)
        
        front_collar.move(0, -10)
        self.add(front_collar)

        # 크기 조정
        if scale_factor != 1:
            self.scale(scale_factor)


# =================================================================
# 2. 선물 상자 구성 요소 클래스 (Body & Lid)
# =================================================================
class GiftBoxBody(Layer):
    def __init__(self, width=140, height=140):
        super().__init__()
        box_color = (255, 215, 70)   # 노란색
        ribbon_color = (255, 80, 80) # 빨간색
        outline_color = 'black'
        outline_width = 3

        base = Rectangle(width, height)
        base.setFillColor(box_color)
        base.setBorderColor(outline_color)
        base.setBorderWidth(outline_width)
        base.setDepth(50)
        self.add(base)

        v_ribbon_width = width * 0.25
        v_ribbon = Rectangle(v_ribbon_width, height)
        v_ribbon.setFillColor(ribbon_color)
        v_ribbon.setBorderColor(outline_color)
        v_ribbon.setBorderWidth(outline_width)
        v_ribbon.setDepth(40)
        self.add(v_ribbon)

        h_ribbon_height = height * 0.25
        h_ribbon = Rectangle(width, h_ribbon_height)
        h_ribbon.setFillColor(ribbon_color)
        h_ribbon.setBorderColor(outline_color)
        h_ribbon.setBorderWidth(outline_width)
        h_ribbon.setDepth(30)
        self.add(h_ribbon)


class GiftBoxLid(Layer):
    def __init__(self, width=200, height=40):
        super().__init__()
        box_color = (255, 215, 70)
        ribbon_color = (255, 80, 80)
        knot_color = (255, 60, 60)
        outline_color = 'black'
        outline_width = 3

        lid_base = Rectangle(width, height)
        lid_base.setFillColor(box_color)
        lid_base.setBorderColor(outline_color)
        lid_base.setBorderWidth(outline_width)
        lid_base.setDepth(20)
        self.add(lid_base)

        v_ribbon_width = width * 0.22 
        lid_ribbon = Rectangle(v_ribbon_width, height)
        lid_ribbon.setFillColor(ribbon_color)
        lid_ribbon.setBorderColor(outline_color)
        lid_ribbon.setBorderWidth(outline_width)
        lid_ribbon.setDepth(19)
        self.add(lid_ribbon)

        tail_left = Polygon(Point(-10, 0), Point(-40, 50), Point(-20, 60), Point(0, 10))
        tail_left.setFillColor(ribbon_color)
        tail_left.setBorderColor(outline_color)
        tail_left.setBorderWidth(outline_width)
        tail_left.setDepth(15)
        tail_left.move(0,-10)
        self.add(tail_left)

        tail_right = Polygon(Point(10, 0), Point(40, 50), Point(20, 60), Point(0, 10))
        tail_right.setFillColor(ribbon_color)
        tail_right.setBorderColor(outline_color)
        tail_right.setBorderWidth(outline_width)
        tail_right.setDepth(15)
        tail_right.move(0,-10)
        self.add(tail_right)

        loop_left = Ellipse(70, 40)
        loop_left.setFillColor(ribbon_color)
        loop_left.setBorderColor(outline_color)
        loop_left.setBorderWidth(outline_width)
        loop_left.move(-35, -25) 
        loop_left.rotate(20)    
        loop_left.setDepth(10)
        self.add(loop_left)

        loop_right = Ellipse(70, 40)
        loop_right.setFillColor(ribbon_color)
        loop_right.setBorderColor(outline_color)
        loop_right.setBorderWidth(outline_width)
        loop_right.move(35, -25) 
        loop_right.rotate(-20)    
        loop_right.setDepth(10)
        self.add(loop_right)

        knot = Square(30)
        knot.setFillColor(knot_color)
        knot.setBorderColor(outline_color)
        knot.setBorderWidth(outline_width)
        knot.move(0, -15) 
        knot.setDepth(5)  
        self.add(knot)

        knot_detail = Path(Point(-5, -25), Point(-5, -15))
        knot_detail.setBorderColor(outline_color)
        knot_detail.setDepth(4)
        self.add(knot_detail)


# =================================================================
# 3. 통합 선물 상자 클래스
# =================================================================
class GiftBox(Layer):
    def __init__(self):
        super().__init__()
        self.body_w, self.body_h = 190, 140
        self.lid_w, self.lid_h = 210, 40
        
        self.body = GiftBoxBody(self.body_w, self.body_h)
        self.lid = GiftBoxLid(self.lid_w, self.lid_h)
        
        self.body.move(0, 20)
        self.lid.move(0, -70)
        
        self.add(self.body)
        self.add(self.lid)

    def shake(self):
        delay = 0.01
        for _ in range(20):
            self.rotate(1)
            time.sleep(delay)
            
        for _ in range(10):
            for _ in range(40):
                self.rotate(-1)
                time.sleep(delay)
            for _ in range(40):
                self.rotate(1)
                time.sleep(delay)
                
        for _ in range(20):
            self.rotate(-1)
            time.sleep(delay)

    def open(self):
        delay = 0.001
        for _ in range(110):
            self.lid.rotate(1)
            self.lid.move(1.5, 0.8) 
            time.sleep(0.0001)
"""

# =================================================================
# 4. Main 함수: 애니메이션 시나리오 실행
# =================================================================
def main():
    # 1. 캔버스 설정 (1280 x 720)
    width, height = 1280, 720
    paper = Canvas(width, height, 'skyblue', 'Gift Reveal Animation')

    # 2. 객체 생성
    # - 선물 상자
    box = GiftBox()
    
    # - 목도리 (선물 상자 안에 들어갈 크기로 조정)
    #   상자 너비가 약 200픽셀이므로, 화면의 1/12배(약 280픽셀) 면적에 맞추기 위해 1.5배 확대
    #   목도리는 상자보다 조금 작게 1.3배 정도로 설정
    box.scale(0.7) 
    scarf = Scarf(scale_factor=0.7)

    # 3. 위치 설정 (화면 중앙 하단)
    center_x = width / 2
    center_y = 550 # 약간 아래쪽

    box.moveTo(center_x, center_y)
    
    # 목도리는 상자랑 같은 위치에서 시작 (숨겨져 있음)
    # 올라올 것을 대비해 y 위치를 살짝 아래로 잡아줍니다.
    scarf.moveTo(center_x, center_y + 20) 

    # 4. Depth(깊이) 설정 [중요]
    # cs1graphics에서 Depth 숫자가 작을수록 '앞(Front)', 클수록 '뒤(Back)'입니다.
    # 선물상자가 목도리를 가려야 하므로, 선물상자 Depth < 목도리 Depth
    box.setDepth(20)   # 앞
    scarf.setDepth(80) # 뒤 (상자 뒤에 숨음)

    # 5. 캔버스에 추가 (순서는 상관없으나 Depth로 제어됨)
    paper.add(scarf)
    paper.add(box)

    # -------------------------------------------------------------
    # 애니메이션 시나리오 시작
    # -------------------------------------------------------------
    time.sleep(1) # 잠시 대기
    
    time.sleep(0.5)

    # Scene 2: 상자 열기 (뚜껑 날아감)
    box.open()

    time.sleep(0.3)

    # Scene 3: 목도리 등장 (위로 올라옴)
    # for-loop를 사용하여 천천히 올라오게 구현
    rise_height = 240 # 위로 올라올 거리
    step_size = 2      # 한 번에 움직이는 거리
    steps = int(rise_height / step_size)

    for _ in range(steps):
        scarf.move(0, -step_size) # y좌표를 빼면 위로 이동
        time.sleep(0.005)

    # 애니메이션 종료 후 대기
    paper.wait()

# =================================================================
# 실행
# =================================================================
if __name__ == "__main__":
    main()
"""
