from cs1graphics import *
import time
import math
import random

# =================================================================
# 1. 색상 정의 (RGB)
# =================================================================
COLOR_SKIN = (255, 224, 189)
COLOR_SUIT_RED = (220, 20, 60)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GOLD = (255, 215, 0)
COLOR_SLEIGH = (178, 34, 34)
COLOR_SILVER = (192, 192, 192)
COLOR_NIGHT_SKY = (25, 25, 112)
COLOR_FUR = (160, 82, 45)       
COLOR_SNOUT = (210, 180, 140)   
COLOR_NOSE_RED = (255, 0, 0)
COLOR_GIFT_BOX = (65, 105, 225) # Royal Blue
COLOR_RIBBON = (255, 215, 0)    # Gold Ribbon

# =================================================================
# 2. 루돌프
# =================================================================
class DetailedReindeer(Layer):
    def __init__(self):
        super().__init__()
        
        # 1. 다리
        leg_bl = Rectangle(12, 40, Point(10, 30))
        leg_bl.setFillColor(COLOR_FUR); leg_bl.setBorderColor(COLOR_FUR)
        self.add(leg_bl)
        hoof_bl = Rectangle(14, 8, Point(10, 50))
        hoof_bl.setFillColor(COLOR_BLACK)
        self.add(hoof_bl)

        leg_br = Rectangle(12, 40, Point(50, 30))
        leg_br.setFillColor(COLOR_FUR); leg_br.setBorderColor(COLOR_FUR)
        self.add(leg_br)
        hoof_br = Rectangle(14, 8, Point(50, 50))
        hoof_br.setFillColor(COLOR_BLACK)
        self.add(hoof_br)

        # 2. 몸통
        body = Ellipse(70, 45, Point(30, 15))
        body.setFillColor(COLOR_FUR); body.setBorderColor(COLOR_FUR)
        self.add(body)
        
        # 3. 앞다리
        leg_fl = Rectangle(12, 40, Point(-5, 30))
        leg_fl.setFillColor(COLOR_FUR); leg_fl.setBorderColor(COLOR_FUR)
        self.add(leg_fl)
        hoof_fl = Rectangle(14, 8, Point(-5, 50))
        hoof_fl.setFillColor(COLOR_BLACK)
        self.add(hoof_fl)

        leg_fr = Rectangle(12, 40, Point(35, 30))
        leg_fr.setFillColor(COLOR_FUR); leg_fr.setBorderColor(COLOR_FUR)
        self.add(leg_fr)
        hoof_fr = Rectangle(14, 8, Point(35, 50))
        hoof_fr.setFillColor(COLOR_BLACK)
        self.add(hoof_fr)

        # 4. 꼬리
        tail = Polygon(Point(60, 10), Point(75, 5), Point(60, 20))
        tail.setFillColor(COLOR_FUR); tail.setBorderColor(COLOR_FUR)
        self.add(tail)

        # 5. 머리 그룹
        head_group = Layer()
        neck = Polygon(Point(-10, 10), Point(10, 10), Point(0, -15))
        neck.setFillColor(COLOR_FUR); neck.setBorderColor(COLOR_FUR)
        head_group.add(neck)
        
        face = Ellipse(45, 40, Point(-15, -20))
        face.setFillColor(COLOR_FUR); face.setBorderColor(COLOR_FUR)
        head_group.add(face)
        
        snout = Ellipse(25, 20, Point(-30, -15))
        snout.setFillColor(COLOR_SNOUT); snout.setBorderColor(COLOR_SNOUT)
        head_group.add(snout)
        
        ear = Ellipse(10, 20, Point(0, -35))
        ear.setFillColor(COLOR_FUR)
        ear.rotate(30)
        head_group.add(ear)

        antler = Path(Point(-10, -35), Point(-10, -55), Point(-20, -65))
        antler.addPoint(Point(-10, -55)); antler.addPoint(Point(0, -65))
        antler.setBorderColor((101, 67, 33)); antler.setBorderWidth(4)
        head_group.add(antler)
        
        eye = Circle(3, Point(-20, -25))
        eye.setFillColor('black')
        head_group.add(eye)
        
        nose = Circle(6, Point(-38, -18))
        nose.setFillColor(COLOR_NOSE_RED); nose.setBorderColor('darkred')
        head_group.add(nose)
        
        shine = Circle(2, Point(-40, -20))
        shine.setFillColor('white'); shine.setBorderColor('white')
        head_group.add(shine)

        self.add(head_group)

        # 6. 장식
        collar = Polygon(Point(-16, 2), Point(6, -8.5), Point(6, 3.5), Point(-16, 4.5))
        collar.setFillColor('red')
        collar.rotate(10)
        self.add(collar)
        
        # 방울 (크기 3으로 조정됨)
        bell = Circle(3, Point(-5, 2)) 
        bell.setFillColor(COLOR_GOLD)
        bell.setBorderColor(COLOR_GOLD) 
        self.add(bell)

# =================================================================
# 3. 고퀄리티 선물 상자
# =================================================================
class DeluxeGift(Layer):
    def __init__(self):
        super().__init__()
        
        # 1. 상자 본체
        box = Square(35, Point(0, 0))
        box.setFillColor(COLOR_GIFT_BOX)
        box.setBorderColor('black')
        box.setBorderWidth(1)
        self.add(box)
        
        # 2. 리본
        ribbon_v = Rectangle(8, 35, Point(0, 0))
        ribbon_v.setFillColor(COLOR_RIBBON)
        ribbon_v.setBorderColor(COLOR_RIBBON)
        self.add(ribbon_v)
        
        ribbon_h = Rectangle(35, 8, Point(0, 0))
        ribbon_h.setFillColor(COLOR_RIBBON)
        ribbon_h.setBorderColor(COLOR_RIBBON)
        self.add(ribbon_h)
        
        # 3. 리본 매듭
        bow_l = Ellipse(12, 6, Point(-8, -18))
        bow_l.setFillColor(COLOR_RIBBON)
        bow_l.rotate(-30)
        self.add(bow_l)
        
        bow_r = Ellipse(12, 6, Point(8, -18))
        bow_r.setFillColor(COLOR_RIBBON)
        bow_r.rotate(30)
        self.add(bow_r)
        
        knot = Circle(4, Point(0, -18))
        knot.setFillColor(COLOR_RIBBON)
        self.add(knot)

# =================================================================
# 4. 산타 (수정 완료: 에러 해결 + 왼팔 위치 + 따봉)
# =================================================================
class AnimatedSanta(Layer):
    def __init__(self):
        super().__init__()
        
        # 1. 몸통
        body = Ellipse(60, 70, Point(0, 20))
        body.setFillColor(COLOR_SUIT_RED); body.setBorderColor(COLOR_SUIT_RED)
        self.add(body)
        
        belt = Rectangle(60, 10, Point(0, 25))
        belt.setFillColor(COLOR_BLACK)
        self.add(belt)
        
        buckle = Square(14, Point(0, 25))
        buckle.setBorderColor(COLOR_GOLD); buckle.setBorderWidth(3)
        self.add(buckle)
        
        # 2. 머리
        head = Circle(20, Point(0, -10))
        head.setFillColor(COLOR_SKIN); head.setBorderColor(COLOR_SKIN)
        self.add(head)
        
        blush = Circle(4, Point(-8, -8))
        blush.setFillColor((255, 192, 203)); blush.setBorderColor((255, 192, 203))
        self.add(blush)

        # 3. 수염
        beard_main = Ellipse(40, 30, Point(0, 5))
        beard_main.setFillColor(COLOR_WHITE); beard_main.setBorderColor(COLOR_WHITE)
        self.add(beard_main)
        
        moustache_l = Ellipse(12, 6, Point(-7, -2))
        moustache_l.setFillColor(COLOR_WHITE); moustache_l.rotate(-20)
        self.add(moustache_l)
        
        moustache_r = Ellipse(12, 6, Point(3, -2))
        moustache_r.setFillColor(COLOR_WHITE); moustache_r.rotate(20)
        self.add(moustache_r)

        # 4. 모자
        hat_base = Polygon(Point(-20, -15), Point(20, -15), Point(-10, -65))
        hat_base.setFillColor(COLOR_SUIT_RED); hat_base.setBorderColor(COLOR_SUIT_RED)
        self.add(hat_base)
        
        hat_trim = Rectangle(44, 10, Point(0, -15))
        hat_trim.setFillColor(COLOR_WHITE); hat_trim.setBorderColor(COLOR_WHITE)
        self.add(hat_trim)
        
        pom = Circle(6, Point(-10, -65))
        pom.setFillColor(COLOR_WHITE)
        self.add(pom)

        # 5. 눈 & 코
        self.eye_l = Circle(2, Point(-10, -12))
        self.eye_l.setFillColor(COLOR_BLACK)
        self.add(self.eye_l)
        self.eye_r = Circle(2, Point(4, -12))
        self.eye_r.setFillColor(COLOR_BLACK)
        self.add(self.eye_r)

        self.smile_eye_l = Path(Point(-12, -12), Point(-10, -14), Point(-8, -12))
        self.smile_eye_l.setBorderWidth(2); self.smile_eye_l.setDepth(100)
        self.add(self.smile_eye_l)
        self.smile_eye_r = Path(Point(2, -12), Point(4, -14), Point(6, -12))
        self.smile_eye_r.setBorderWidth(2); self.smile_eye_r.setDepth(100)
        self.add(self.smile_eye_r)

        nose = Circle(4, Point(-5, -5))
        nose.setFillColor(COLOR_SUIT_RED)
        self.add(nose)

        # ---------------------------------------------------------
        # 6. 팔 (오른쪽 - 따봉용)
        # ---------------------------------------------------------
        self.arm_r = Layer()
        
        # 팔뚝
        arm_shape = Ellipse(30, 12, Point(0, 0))
        arm_shape.setFillColor(COLOR_SUIT_RED)
        arm_shape.setBorderColor(COLOR_SUIT_RED)
        self.arm_r.add(arm_shape)
        
        # 오른손 (Layer)
        self.hand_r = Layer()
        
        # 손바닥
        mitten = Circle(8, Point(0, 0))
        mitten.setFillColor(COLOR_WHITE)
        self.hand_r.add(mitten)
        
        # 엄지
        self.thumb = Ellipse(5, 10, Point(-2, -5))
        self.thumb.setFillColor(COLOR_WHITE)
        self.thumb.adjustReference(0, 3) 
        self.thumb.rotate(70) 
        self.hand_r.add(self.thumb)
        
        # 손을 팔 끝으로 이동
        self.hand_r.move(-15, 0) 
        self.arm_r.add(self.hand_r)
        
        # 오른팔 전체 위치 잡기
        self.arm_r.move(18, 10) 
        self.arm_r.adjustReference(10, 0) 
        self.arm_r.rotate(70) 
        self.add(self.arm_r)

        # ---------------------------------------------------------
        # 7. 왼쪽 팔 (수정됨: 레이어로 묶고 위치 밖으로 뺌)
        # ---------------------------------------------------------
        self.arm_l_layer = Layer()

        # 왼팔 팔뚝
        arm_l = Ellipse(30, 12, Point(0, 0))
        arm_l.setFillColor(COLOR_SUIT_RED)
        arm_l.setBorderColor(COLOR_SUIT_RED)
        self.arm_l_layer.add(arm_l)
        
        # 왼손 (팔 끝에 붙임)
        mitten_l = Circle(8, Point(-15, 0))
        mitten_l.setFillColor(COLOR_WHITE)
        self.arm_l_layer.add(mitten_l)

        # [위치 수정] -18 -> -28 (바깥으로 더 뺌)
        self.arm_l_layer.move(-35, 10) 
        self.arm_l_layer.adjustReference(10, 0) 
        self.arm_l_layer.rotate(-70) 
        self.add(self.arm_l_layer)

    # ---------------------------------------------------------
    # [추가] 에러 해결을 위해 추가된 함수
    # ---------------------------------------------------------
    def action_smile(self):
        self.eye_l.setDepth(100)
        self.eye_r.setDepth(100)
        self.smile_eye_l.setDepth(-10)
        self.smile_eye_r.setDepth(-10)

    # ---------------------------------------------------------
    # [수정] 따봉 애니메이션 업그레이드
    # ---------------------------------------------------------
    def action_thumbs_up(self):
        # 팔을 들어올리며 엄지 척!
        for _ in range(20):
            self.arm_r.rotate(-4) # 팔 위로 회전
            if _ < 10: 
                self.thumb.rotate(-10) # 엄지 펴기
            time.sleep(0.02)
        
        # 마지막에 살짝 강조
        for _ in range(2):
            self.thumb.rotate(-10)
            time.sleep(0.1)
            self.thumb.rotate(10)
            time.sleep(0.1)

# =================================================================
# 5. 썰매 부품
# =================================================================
class SleighParts(Layer):
    def __init__(self):
        super().__init__()
        
        # 선물 보따리
        bag = Circle(35, Point(35, 30))
        bag.setFillColor('brown'); bag.setBorderColor('brown')
        self.add(bag)
        
        # 고퀄리티 선물 상자
        gift = DeluxeGift()
        gift.move(45, 10)
        gift.rotate(10)
        self.add(gift)
        
        # 썰매 몸체
        sleigh_body = Polygon(
            Point(-60, 50), Point(-40, 80), Point(50, 80),
            Point(70, 30), Point(20, 30), Point(-10, 50)
        )
        sleigh_body.setFillColor(COLOR_SLEIGH); sleigh_body.setBorderColor(COLOR_SLEIGH)
        self.add(sleigh_body)
        
        # 장식
        trim = Path(Point(-60, 50), Point(-10, 50), Point(20, 30), Point(70, 30))
        trim.setBorderColor(COLOR_GOLD); trim.setBorderWidth(5)
        self.add(trim)
        
        # 날
        runner_main = Path(Point(-50, 80), Point(60, 80)) 
        runner_curve = Path(Point(-50, 80), Point(-70, 70), Point(-80, 50)) 
        for part in [runner_main, runner_curve]:
            part.setBorderColor(COLOR_SILVER); part.setBorderWidth(4)
            self.add(part)
            
        support1 = Path(Point(-30, 80), Point(-30, 50))
        support2 = Path(Point(30, 80), Point(30, 50))
        support1.setBorderWidth(3); support1.setBorderColor(COLOR_SILVER)
        support2.setBorderWidth(3); support2.setBorderColor(COLOR_SILVER)
        self.add(support1)
        self.add(support2)
        
        rein = Path(Point(-25, 20), Point(-80, 20), Point(-120, 40))
        rein.setBorderColor('black'); rein.setBorderWidth(2)
        self.add(rein)

#테두리 있는 텍스트 클래스
class mytext(Layer):
    def __init__(self, message, font_size, text_color='white', border_color='black', border_width=2):
        super().__init__()
        
        # 1. 테두리 역할을 할 텍스트들 (뒤쪽)
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
# 6. 전체 장면 조립
# =================================================================
class FullScene(Layer):
    def __init__(self):
        super().__init__()
        
        self.sleigh = SleighParts()
        self.sleigh.setDepth(50)
        self.add(self.sleigh)
        
        self.santa = AnimatedSanta()
        self.santa.move(0, 25)
        self.santa.setDepth(40)
        self.add(self.santa)
        
        self.deer1 = DetailedReindeer()
        self.deer1.move(-140, 60)
        self.deer1.setDepth(20)
        self.add(self.deer1)
        
        self.deer2 = DetailedReindeer()
        self.deer2.move(-110, 50)
        self.deer2.setDepth(10)
        self.add(self.deer2)

# =================================================================
# 7. 메인 실행
# =================================================================
def run_santa_ending(canvas):
    # 1. 배경 전환 (낮 -> 밤)
    canvas.clear() # 기존 펭귄 그림 싹 지우기
    canvas.setBackgroundColor(COLOR_NIGHT_SKY)
    
    # 2. 별 생성
    for _ in range(150):
        star = Circle(random.randint(1, 3), Point(random.randint(0, 1280), random.randint(0, 720)))
        star.setFillColor(COLOR_WHITE); star.setBorderColor(COLOR_WHITE)
        canvas.add(star)

    # 3. 산타 장면 배치
    scene = FullScene()
    scene.move(640, 360)
    canvas.add(scene)
    
    canvas.refresh()
    time.sleep(1)

    # 4. 줌인 (Zoom In)
    steps = 3        
    scale_step = 1.5 
    
    for i in range(steps):
        scene.scale(scale_step)
        scene.move(1.0, 0.5) 
        canvas.refresh()
        time.sleep(0.02)

    time.sleep(0.5)

    # 5. 애니메이션 (스마일 & 따봉)
    scene.santa.action_smile()
    scene.santa.action_thumbs_up()
    
    # 6. The End 텍스트 (선택사항)
    the_end = mytext("The End", 100, 'white', 'darkblue', 3)
    
    # 위치 설정 (화면 중앙: 640, 높이: 600 정도가 적당)
    the_end.moveTo(640, 600)
    
    # 캔버스에 추가
    canvas.add(the_end)
    
    canvas.refresh()
    time.sleep(3) # 3초 보여주고 종료
