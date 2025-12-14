#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prescene: 달력 넘김 + 산타가 오두막에서 나와 썰매 타고 날아가는 장면
"""

from cs1graphics import *
import time
import math
import random

# =================================================================
# 색상 정의
# =================================================================
COLOR_SKIN = (255, 224, 189)
COLOR_SUIT_RED = (220, 20, 60)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GOLD = (255, 215, 0)
COLOR_SLEIGH = (178, 34, 34)
COLOR_SILVER = (192, 192, 192)
COLOR_FUR = (160, 82, 45)
COLOR_SNOUT = (210, 180, 140)
COLOR_NOSE_RED = (255, 0, 0)
COLOR_GIFT_BOX = (65, 105, 225)
COLOR_RIBBON = (255, 215, 0)

# =================================================================
# 애니메이션 컨트롤러 (카메라 줌/팬)
# =================================================================
class AnimationController:
    """장면의 카메라(시점)를 제어하는 클래스"""
    
    def __init__(self, canvas, world_layer):
        self.canvas = canvas
        self.world = world_layer
        self.current_scale = 1.0
        self.current_x = 640  # 화면 중앙
        self.current_y = 360
        
    def zoom_to_point(self, target_x, target_y, target_scale, duration=1.0):
        """특정 좌표로 줌/팬 이동 (단순화된 버전)"""
        steps = max(int(duration * 30), 1)
        
        cw = self.canvas.getWidth()
        ch = self.canvas.getHeight()
        
        # 시작 상태 저장
        start_scale = self.current_scale
        
        for i in range(steps + 1):
            t = i / steps
            # 부드러운 이동 (Ease in/out)
            t_smooth = t * t * (3 - 2 * t)
            
            # 스케일 보간
            cur_scale_val = start_scale + (target_scale - start_scale) * t_smooth
            
            # 스케일 적용 (상대적)
            if self.current_scale > 0:
                scale_factor = cur_scale_val / self.current_scale
                if abs(scale_factor - 1.0) > 0.001:  # 변화가 있을 때만
                    self.world.scale(scale_factor)
                self.current_scale = cur_scale_val
            
            time.sleep(duration / steps)
    
    def reset_view(self, duration=0.5):
        """카메라를 기본 뷰로 리셋"""
        self.zoom_to_point(0, 0, 1.0, duration)

# =================================================================
# 달력 클래스
# =================================================================
class Calendar(Layer):
    """달력 객체 생성 및 페이지 넘김 애니메이션"""
    
    def __init__(self):
        super().__init__()
        
        # 달력 받침대
        self.base = Rectangle(300, 400)
        self.base.setFillColor('darkRed')
        self.base.setBorderColor('black')
        self.base.setBorderWidth(3)
        self.add(self.base)
        
        # 금속 링 (제본)
        for i in range(5):
            x = -100 + i * 50
            ring_back = Path(Point(x, -180), Point(x, -200))
            ring_back.setBorderWidth(6)
            ring_back.setBorderColor('lightGray')
            self.add(ring_back)
            
        # 페이지 컨테이너
        self.page_layer = Layer()
        self.add(self.page_layer)
        
        # 25일 페이지 (아래쪽)
        self.page25 = self.create_page("25", "Christmas Day", "red", "santa")
        self.page_layer.add(self.page25)
        
        # 24일 페이지 (위쪽)
        self.page24 = self.create_page("24", "Christmas Eve", "darkGreen", "tree")
        self.page_layer.add(self.page24)
        
        # 앞쪽 링
        for i in range(5):
            x = -100 + i * 50
            ring_front = Circle(5, Point(x, -180))
            ring_front.setFillColor('white')
            ring_front.setBorderColor('gray')
            self.add(ring_front)

    def create_page(self, number, subtitle, theme_color, icon_type):
        """달력 페이지 생성"""
        page = Layer()
        
        # 종이
        paper = Rectangle(260, 320)
        paper.setFillColor('white')
        paper.setBorderColor('lightGray')
        paper.move(0, 20)
        page.add(paper)
        
        # 찢어지는 부분 구멍
        for i in range(5):
            x = -100 + i * 50
            hole = Circle(6, Point(x, -140))
            hole.setFillColor('darkRed')
            hole.setBorderColor('darkRed')
            page.add(hole)
        
        # 헤더 라인
        line = Path(Point(-110, -80), Point(110, -80))
        line.setBorderColor('red')
        line.setBorderWidth(2)
        page.add(line)
        
        # 월 (DECEMBER)
        month = Text("DECEMBER", 20)
        month.setFontColor('red')
        month.move(0, -100)
        page.add(month)
        
        # 날짜 숫자
        num = Text(number, 100)
        num.setFontColor('black')
        num.setDepth(10)
        num.move(0, 10)
        page.add(num)
        
        # 부제
        sub = Text(subtitle, 16)
        sub.setFontColor(theme_color)
        sub.move(0, 80)
        page.add(sub)
        
        # 아이콘
        if icon_type == "tree":
            tree = Polygon(Point(0, 110), Point(-20, 140), Point(20, 140))
            tree.setFillColor('forestGreen')
            page.add(tree)
        elif icon_type == "santa":
            face = Circle(15, Point(0, 120))
            face.setFillColor('white')
            page.add(face)
            beard = Polygon(Point(-15, 120), Point(0, 145), Point(15, 120))
            beard.setFillColor('white')
            page.add(beard)
            hat = Polygon(Point(-15, 115), Point(0, 95), Point(15, 115))
            hat.setFillColor('red')
            page.add(hat)
            
        return page

    def tear_page(self):
        """맨 위 페이지가 찢겨 나가는 애니메이션"""
        steps = 25
        
        # 찢어지는 효과 (좌우 흔들림)
        for i in range(6):
            self.page24.move(4, 0)
            time.sleep(0.04)
            self.page24.move(-4, 0)
            time.sleep(0.04)
            
        # 떨어지는 애니메이션
        for i in range(steps):
            self.page24.move(6, 12)
            time.sleep(0.04)
            
        self.page_layer.remove(self.page24)

# =================================================================
# 고퀄리티 겨울 풍경 클래스 (background.py 기반)
# =================================================================
class WinterBackground(Layer):
    """겨울 풍경 배경"""
    
    def __init__(self):
        super().__init__()
        
        # 하늘 그라데이션
        for i in range(30):
            y = -360 + i * 24
            sky_strip = Rectangle(1600, 24)
            if i < 8:
                sky_strip.setFillColor('lightBlue')
            elif i < 16:
                sky_strip.setFillColor('lightCyan')
            elif i < 24:
                sky_strip.setFillColor('white')
            else:
                sky_strip.setFillColor('lightGray')
            sky_strip.setBorderColor(sky_strip.getFillColor())
            sky_strip.move(0, y)
            sky_strip.setDepth(100)
            self.add(sky_strip)
        
        # 원경 산맥
        far_mountain = Polygon(Point(-800, 50), Point(-500, -50), Point(-200, -30), 
                              Point(0, -80), Point(200, -40), Point(500, -60), 
                              Point(800, -20), Point(800, 360), Point(-800, 360))
        far_mountain.setFillColor('lightGray')
        far_mountain.setBorderColor('gray')
        far_mountain.setDepth(90)
        self.add(far_mountain)
        
        # 중간 산맥
        mid_mountain = Polygon(Point(-600, 80), Point(-300, -20), Point(-100, 0), 
                              Point(100, -50), Point(300, -10), Point(600, -35), 
                              Point(600, 360), Point(-600, 360))
        mid_mountain.setFillColor('gray')
        mid_mountain.setBorderColor('darkGray')
        mid_mountain.setDepth(85)
        self.add(mid_mountain)
        
        # 언덕 (눈 덮인 지형)
        back_hill = Polygon(Point(-500, 180), Point(-200, 150), Point(0, 160), 
                           Point(200, 140), Point(500, 170), Point(500, 360), Point(-500, 360))
        back_hill.setFillColor('white')
        back_hill.setBorderColor('lightBlue')
        back_hill.setDepth(75)
        self.add(back_hill)
        
        # 앞쪽 언덕
        front_hill = Polygon(Point(-600, 220), Point(-300, 190), Point(0, 200), 
                            Point(300, 180), Point(600, 210), Point(600, 400), Point(-600, 400))
        front_hill.setFillColor('white')
        front_hill.setBorderColor('lightBlue')
        front_hill.setDepth(70)
        self.add(front_hill)
        
        # 겨울 나무들
        tree_positions = [(-400, 200), (-280, 210), (280, 195), (400, 205), (-500, 220)]
        for x, y in tree_positions:
            self._create_winter_tree(x, y)
        
        # 눈송이들
        for i in range(60):
            size = random.randint(2, 5)
            snow_x = random.randint(-700, 700)
            snow_y = random.randint(-360, 300)
            snowflake = Circle(size)
            snowflake.setFillColor('white')
            snowflake.setBorderColor('lightBlue')
            snowflake.move(snow_x, snow_y)
            snowflake.setDepth(30)
            self.add(snowflake)
    
    def _create_winter_tree(self, x, y):
        """겨울 나무 생성"""
        # 줄기
        trunk = Rectangle(12, 50)
        trunk.setFillColor('saddleBrown')
        trunk.setBorderColor('brown')
        trunk.move(x, y + 25)
        trunk.setDepth(45)
        self.add(trunk)
        
        # 삼각형 나뭇잎 (눈 덮인)
        for level in range(3):
            branch_y = y - level * 25
            width = 50 - level * 12
            branch = Polygon(Point(x, branch_y - 30), 
                           Point(x - width, branch_y + 10), 
                           Point(x + width, branch_y + 10))
            branch.setFillColor('darkGreen')
            branch.setBorderColor('green')
            branch.setDepth(44)
            self.add(branch)
            
            # 눈
            snow = Ellipse(width, 8)
            snow.setFillColor('white')
            snow.setBorderColor('lightBlue')
            snow.move(x, branch_y + 8)
            snow.setDepth(43)
            self.add(snow)

# =================================================================
# 고퀄리티 오두막 클래스
# =================================================================
class PremiumCabin(Layer):
    """상세한 오두막 (문 열림 애니메이션 지원)"""
    
    def __init__(self):
        super().__init__()
        
        # 오두막 기초
        foundation = Rectangle(180, 20)
        foundation.setFillColor('gray')
        foundation.setBorderColor('darkGray')
        foundation.setBorderWidth(2)
        foundation.move(0, 80)
        foundation.setDepth(60)
        self.add(foundation)
        
        # 통나무 벽체
        main_wall = Rectangle(160, 120)
        main_wall.setFillColor('saddleBrown')
        main_wall.setBorderColor('brown')
        main_wall.setBorderWidth(3)
        main_wall.move(0, 20)
        main_wall.setDepth(58)
        self.add(main_wall)
        
        # 통나무 디테일
        for i in range(7):
            log_y = -20 + i * 18
            log_line = Path(Point(-80, log_y), Point(80, log_y))
            log_line.setBorderColor('brown')
            log_line.setBorderWidth(4)
            log_line.setDepth(57)
            self.add(log_line)
            
            # 통나무 끝
            left_end = Circle(6, Point(-80, log_y))
            left_end.setFillColor('brown')
            left_end.setBorderColor('darkRed')
            left_end.setDepth(56)
            self.add(left_end)
            
            right_end = Circle(6, Point(80, log_y))
            right_end.setFillColor('brown')
            right_end.setBorderColor('darkRed')
            right_end.setDepth(56)
            self.add(right_end)
        
        # 지붕
        roof = Polygon(Point(-100, -40), Point(0, -120), Point(100, -40))
        roof.setFillColor('darkRed')
        roof.setBorderColor('black')
        roof.setBorderWidth(3)
        roof.setDepth(55)
        self.add(roof)
        
        # 지붕 위 눈
        snow_roof = Polygon(Point(-100, -40), Point(0, -120), Point(100, -40),
                           Point(90, -35), Point(0, -110), Point(-90, -35))
        snow_roof.setFillColor('white')
        snow_roof.setBorderColor('lightBlue')
        snow_roof.setDepth(54)
        self.add(snow_roof)
        
        # 굴뚝
        chimney = Rectangle(25, 50)
        chimney.setFillColor('darkGray')
        chimney.setBorderColor('black')
        chimney.setBorderWidth(2)
        chimney.move(40, -90)
        chimney.setDepth(53)
        self.add(chimney)
        
        # 굴뚝 연기
        self.smoke_particles = []
        for i in range(4):
            smoke = Circle(8 - i)
            smoke.setFillColor('lightGray')
            smoke.setBorderColor('gray')
            smoke.move(40 + i * 8, -130 - i * 18)
            smoke.setDepth(52)
            self.add(smoke)
            self.smoke_particles.append(smoke)
        
        # 문 프레임
        door_frame = Rectangle(50, 80)
        door_frame.setFillColor('darkRed')
        door_frame.setBorderColor('black')
        door_frame.setBorderWidth(2)
        door_frame.move(0, 40)
        door_frame.setDepth(51)
        self.add(door_frame)
        
        # 문 (애니메이션용)
        self.door = Rectangle(45, 75)
        self.door.setFillColor('orange')
        self.door.setBorderColor('brown')
        self.door.setBorderWidth(2)
        self.door.move(0, 40)
        self.door.setDepth(50)
        self.add(self.door)
        
        # 문 손잡이
        self.knob = Circle(4)
        self.knob.setFillColor('gold')
        self.knob.setBorderColor('orange')
        self.knob.setBorderWidth(2)
        self.knob.move(15, 40)
        self.knob.setDepth(48)
        self.add(self.knob)
        
        # 창문들 (따뜻한 빛)
        self._create_window(-50, 0, 40)
        self._create_window(50, -10, 30)
        
        # 눈 더미
        for i in range(5):
            pile_x = random.randint(-100, 100)
            pile_y = random.randint(60, 85)
            pile = Ellipse(random.randint(15, 30), random.randint(8, 12))
            pile.setFillColor('white')
            pile.setBorderColor('lightBlue')
            pile.move(pile_x, pile_y)
            pile.setDepth(65)
            self.add(pile)
    
    def _create_window(self, x, y, size):
        """창문 생성"""
        frame = Rectangle(size, size)
        frame.setFillColor('brown')
        frame.setBorderColor('black')
        frame.setBorderWidth(2)
        frame.move(x, y)
        frame.setDepth(51)
        self.add(frame)
        
        glass = Rectangle(size - 5, size - 5)
        glass.setFillColor('yellow')
        glass.setBorderColor('orange')
        glass.move(x, y)
        glass.setDepth(50)
        self.add(glass)
        
        # 십자 프레임
        h_line = Path(Point(x - size//2 + 2, y), Point(x + size//2 - 2, y))
        h_line.setBorderColor('brown')
        h_line.setBorderWidth(2)
        h_line.setDepth(49)
        self.add(h_line)
        
        v_line = Path(Point(x, y - size//2 + 2), Point(x, y + size//2 - 2))
        v_line.setBorderColor('brown')
        v_line.setBorderWidth(2)
        v_line.setDepth(49)
        self.add(v_line)
    
    def open_door(self):
        """문 열기 애니메이션"""
        for i in range(15):
            self.door.scale(0.95)
            self.knob.move(-1.5, 0)
            time.sleep(0.03)

# =================================================================
# 루돌프 (순록)
# =================================================================
class Reindeer(Layer):
    """루돌프 사슴"""
    
    def __init__(self):
        super().__init__()
        
        # 뒷다리
        for x_off in [10, 50]:
            leg = Rectangle(12, 40, Point(x_off, 30))
            leg.setFillColor(COLOR_FUR)
            leg.setBorderColor(COLOR_FUR)
            self.add(leg)
            hoof = Rectangle(14, 8, Point(x_off, 50))
            hoof.setFillColor(COLOR_BLACK)
            self.add(hoof)
        
        # 몸통
        body = Ellipse(70, 45, Point(30, 15))
        body.setFillColor(COLOR_FUR)
        body.setBorderColor(COLOR_FUR)
        self.add(body)
        
        # 앞다리
        for x_off in [-5, 35]:
            leg = Rectangle(12, 40, Point(x_off, 30))
            leg.setFillColor(COLOR_FUR)
            leg.setBorderColor(COLOR_FUR)
            self.add(leg)
            hoof = Rectangle(14, 8, Point(x_off, 50))
            hoof.setFillColor(COLOR_BLACK)
            self.add(hoof)
        
        # 꼬리
        tail = Polygon(Point(60, 10), Point(75, 5), Point(60, 20))
        tail.setFillColor(COLOR_FUR)
        tail.setBorderColor(COLOR_FUR)
        self.add(tail)
        
        # 머리 그룹
        head_group = Layer()
        
        neck = Polygon(Point(-10, 10), Point(10, 10), Point(0, -15))
        neck.setFillColor(COLOR_FUR)
        neck.setBorderColor(COLOR_FUR)
        head_group.add(neck)
        
        face = Ellipse(45, 40, Point(-15, -20))
        face.setFillColor(COLOR_FUR)
        face.setBorderColor(COLOR_FUR)
        head_group.add(face)
        
        snout = Ellipse(25, 20, Point(-30, -15))
        snout.setFillColor(COLOR_SNOUT)
        snout.setBorderColor(COLOR_SNOUT)
        head_group.add(snout)
        
        ear = Ellipse(10, 20, Point(0, -35))
        ear.setFillColor(COLOR_FUR)
        ear.rotate(30)
        head_group.add(ear)
        
        # 뿔
        antler = Path(Point(-10, -35), Point(-10, -55), Point(-20, -65))
        antler.addPoint(Point(-10, -55))
        antler.addPoint(Point(0, -65))
        antler.setBorderColor((101, 67, 33))
        antler.setBorderWidth(4)
        head_group.add(antler)
        
        eye = Circle(3, Point(-20, -25))
        eye.setFillColor('black')
        head_group.add(eye)
        
        # 빨간 코 (루돌프!)
        nose = Circle(6, Point(-38, -18))
        nose.setFillColor(COLOR_NOSE_RED)
        nose.setBorderColor('darkred')
        head_group.add(nose)
        
        shine = Circle(2, Point(-40, -20))
        shine.setFillColor('white')
        shine.setBorderColor('white')
        head_group.add(shine)
        
        self.add(head_group)
        
        # 목걸이
        collar = Polygon(Point(-16, 2), Point(6, -8.5), Point(6, 3.5), Point(-16, 4.5))
        collar.setFillColor('red')
        collar.rotate(10)
        self.add(collar)
        
        bell = Circle(3, Point(-5, 2))
        bell.setFillColor(COLOR_GOLD)
        bell.setBorderColor(COLOR_GOLD)
        self.add(bell)

# =================================================================
# 산타 클래스
# =================================================================
class Santa(Layer):
    """산타 클로스"""
    
    def __init__(self):
        super().__init__()
        
        # 몸통
        body = Ellipse(60, 70, Point(0, 20))
        body.setFillColor(COLOR_SUIT_RED)
        body.setBorderColor(COLOR_SUIT_RED)
        self.add(body)
        
        belt = Rectangle(60, 10, Point(0, 25))
        belt.setFillColor(COLOR_BLACK)
        self.add(belt)
        
        buckle = Square(14, Point(0, 25))
        buckle.setBorderColor(COLOR_GOLD)
        buckle.setBorderWidth(3)
        self.add(buckle)
        
        # 머리
        head = Circle(20, Point(0, -10))
        head.setFillColor(COLOR_SKIN)
        head.setBorderColor(COLOR_SKIN)
        self.add(head)
        
        blush = Circle(4, Point(-8, -8))
        blush.setFillColor((255, 192, 203))
        blush.setBorderColor((255, 192, 203))
        self.add(blush)
        
        # 수염
        beard_main = Ellipse(40, 30, Point(0, 5))
        beard_main.setFillColor(COLOR_WHITE)
        beard_main.setBorderColor(COLOR_WHITE)
        self.add(beard_main)
        
        moustache_l = Ellipse(12, 6, Point(-7, -2))
        moustache_l.setFillColor(COLOR_WHITE)
        moustache_l.rotate(-20)
        self.add(moustache_l)
        
        moustache_r = Ellipse(12, 6, Point(3, -2))
        moustache_r.setFillColor(COLOR_WHITE)
        moustache_r.rotate(20)
        self.add(moustache_r)
        
        # 모자
        hat_base = Polygon(Point(-20, -15), Point(20, -15), Point(-10, -65))
        hat_base.setFillColor(COLOR_SUIT_RED)
        hat_base.setBorderColor(COLOR_SUIT_RED)
        self.add(hat_base)
        
        hat_trim = Rectangle(44, 10, Point(0, -15))
        hat_trim.setFillColor(COLOR_WHITE)
        hat_trim.setBorderColor(COLOR_WHITE)
        self.add(hat_trim)
        
        pom = Circle(6, Point(-10, -65))
        pom.setFillColor(COLOR_WHITE)
        self.add(pom)
        
        # 눈
        eye_l = Circle(2, Point(-10, -12))
        eye_l.setFillColor(COLOR_BLACK)
        self.add(eye_l)
        
        eye_r = Circle(2, Point(4, -12))
        eye_r.setFillColor(COLOR_BLACK)
        self.add(eye_r)
        
        # 코
        nose = Circle(4, Point(-5, -5))
        nose.setFillColor(COLOR_SUIT_RED)
        self.add(nose)
        
        # 팔들
        self._create_arm(-35, 10, -70)  # 왼팔
        self._create_arm(18, 10, 70)    # 오른팔
    
    def _create_arm(self, x, y, rotation):
        """팔 생성"""
        arm_layer = Layer()
        
        arm_shape = Ellipse(30, 12, Point(0, 0))
        arm_shape.setFillColor(COLOR_SUIT_RED)
        arm_shape.setBorderColor(COLOR_SUIT_RED)
        arm_layer.add(arm_shape)
        
        mitten = Circle(8, Point(-15, 0))
        mitten.setFillColor(COLOR_WHITE)
        arm_layer.add(mitten)
        
        arm_layer.move(x, y)
        arm_layer.adjustReference(10, 0)
        arm_layer.rotate(rotation)
        self.add(arm_layer)

# =================================================================
# 썰매 클래스
# =================================================================
class Sleigh(Layer):
    """산타 썰매"""
    
    def __init__(self):
        super().__init__()
        
        # 선물 보따리
        bag = Circle(35, Point(35, 30))
        bag.setFillColor('brown')
        bag.setBorderColor('brown')
        self.add(bag)
        
        # 선물 상자
        self._create_gift(45, 10)
        self._create_gift(55, 5)
        
        # 썰매 몸체
        sleigh_body = Polygon(
            Point(-60, 50), Point(-40, 80), Point(50, 80),
            Point(70, 30), Point(20, 30), Point(-10, 50)
        )
        sleigh_body.setFillColor(COLOR_SLEIGH)
        sleigh_body.setBorderColor(COLOR_SLEIGH)
        self.add(sleigh_body)
        
        # 장식
        trim = Path(Point(-60, 50), Point(-10, 50), Point(20, 30), Point(70, 30))
        trim.setBorderColor(COLOR_GOLD)
        trim.setBorderWidth(5)
        self.add(trim)
        
        # 날
        runner_main = Path(Point(-50, 80), Point(60, 80))
        runner_curve = Path(Point(-50, 80), Point(-70, 70), Point(-80, 50))
        for part in [runner_main, runner_curve]:
            part.setBorderColor(COLOR_SILVER)
            part.setBorderWidth(4)
            self.add(part)
        
        support1 = Path(Point(-30, 80), Point(-30, 50))
        support2 = Path(Point(30, 80), Point(30, 50))
        support1.setBorderWidth(3)
        support1.setBorderColor(COLOR_SILVER)
        support2.setBorderWidth(3)
        support2.setBorderColor(COLOR_SILVER)
        self.add(support1)
        self.add(support2)
    
    def _create_gift(self, x, y):
        """선물 상자 생성"""
        box = Square(25, Point(x, y))
        box.setFillColor(COLOR_GIFT_BOX)
        box.setBorderColor('black')
        box.setBorderWidth(1)
        self.add(box)
        
        ribbon_v = Rectangle(6, 25, Point(x, y))
        ribbon_v.setFillColor(COLOR_RIBBON)
        ribbon_v.setBorderColor(COLOR_RIBBON)
        self.add(ribbon_v)
        
        ribbon_h = Rectangle(25, 6, Point(x, y))
        ribbon_h.setFillColor(COLOR_RIBBON)
        ribbon_h.setBorderColor(COLOR_RIBBON)
        self.add(ribbon_h)

# =================================================================
# 전체 썰매 어셈블리 (산타 + 썰매 + 루돌프)
# =================================================================
class SleighAssembly(Layer):
    """산타 + 썰매 + 루돌프 조합"""
    
    def __init__(self):
        super().__init__()
        
        # 고삐
        rein = Path(Point(-25, 20), Point(-80, 20), Point(-120, 40))
        rein.setBorderColor('black')
        rein.setBorderWidth(2)
        self.add(rein)
        
        # 루돌프 (앞쪽)
        self.deer1 = Reindeer()
        self.deer1.move(-140, 60)
        self.deer1.setDepth(20)
        self.add(self.deer1)
        
        # 두 번째 루돌프
        self.deer2 = Reindeer()
        self.deer2.move(-110, 50)
        self.deer2.setDepth(10)
        self.add(self.deer2)
        
        # 썰매
        self.sleigh = Sleigh()
        self.sleigh.setDepth(50)
        self.add(self.sleigh)
        
        # 산타
        self.santa = Santa()
        self.santa.move(0, 25)
        self.santa.setDepth(40)
        self.add(self.santa)

# =================================================================
# 메인 Prescene 클래스
# =================================================================
class Prescene:
    """프리신 - 달력 넘김 + 산타 출발 장면"""
    
    def __init__(self):
        # 캔버스 설정
        self.canvas = Canvas(1280, 720)
        self.canvas.setBackgroundColor('darkBlue')
        self.canvas.setTitle("Christmas Prescene")
        
        # 월드 레이어
        self.world = Layer()
        self.canvas.add(self.world)
        
        # 애니메이션 컨트롤러
        self.ctrl = AnimationController(self.canvas, self.world)
    
    def run_calendar_scene(self):
        """Scene 1: 달력 넘기는 장면"""
        # 간단한 배경
        bg = Rectangle(1600, 900)
        bg.setFillColor('darkBlue')
        bg.setDepth(200)
        self.world.add(bg)
        
        # 별들
        for _ in range(80):
            star = Circle(random.randint(1, 3))
            star.setFillColor('white')
            star.setBorderColor('white')
            star.move(random.randint(-640, 640), random.randint(-360, 300))
            star.setDepth(150)
            self.world.add(star)
        
        # 달력 생성
        calendar = Calendar()
        calendar.move(0, 0)
        calendar.setDepth(10)
        self.world.add(calendar)
        
        # 월드를 화면 중앙으로
        self.world.move(640, 360)
        
        time.sleep(1.5)
        
        # 달력으로 줌인
        for i in range(10):
            self.world.scale(1.04)
            time.sleep(0.04)
        
        time.sleep(0.5)
        
        # 달력 넘기기
        calendar.tear_page()
        
        time.sleep(1.5)
        
        # 줌아웃
        for i in range(10):
            self.world.scale(0.96)
            time.sleep(0.04)
        
        time.sleep(0.5)
        
        # 페이드 아웃 (달력 제거)
        for i in range(20):
            calendar.move(0, -15)
            time.sleep(0.03)
        self.world.remove(calendar)
    
    def run_cabin_scene(self):
        """Scene 2: 산타가 오두막에서 나와 썰매 타고 날아가는 장면"""
        # 기존 월드 제거하고 새로 생성
        self.canvas.remove(self.world)
        
        # 새 월드 레이어 생성
        self.world = Layer()
        self.canvas.add(self.world)
        
        # 컨트롤러 재설정
        self.ctrl = AnimationController(self.canvas, self.world)
        
        # 배경 생성
        background = WinterBackground()
        background.setDepth(100)
        self.world.add(background)
        
        # 오두막 생성 (화면 중앙)
        cabin = PremiumCabin()
        cabin.move(0, 180)
        cabin.setDepth(60)
        self.world.add(cabin)
        
        # 산타 (오두막 앞에서 시작, 숨김 상태)
        santa_walk = Santa()
        santa_walk.scale(0.7)
        santa_walk.move(0, 260)
        santa_walk.setDepth(55)
        
        # 썰매 어셈블리 (화면 바깥에서 대기)
        sleigh_assembly = SleighAssembly()
        sleigh_assembly.scale(0.6)
        sleigh_assembly.move(200, 220)  # 오두막 오른쪽에 배치
        sleigh_assembly.setDepth(50)
        
        # 월드를 화면 중앙으로 이동
        self.world.move(640, 360)
        
        time.sleep(1.0)
        
        # 오두막으로 줌인 (scale 사용)
        for i in range(10):
            self.world.scale(1.05)
            time.sleep(0.05)
        
        time.sleep(0.5)
        
        # 문 열기
        cabin.open_door()
        
        time.sleep(0.3)
        
        # 산타 등장
        self.world.add(santa_walk)
        
        # 산타가 오두막에서 걸어나옴
        for i in range(25):
            santa_walk.move(4, 0)
            time.sleep(0.04)
        
        time.sleep(0.3)
        
        # 줌아웃하며 전체 보기
        for i in range(15):
            self.world.scale(0.96)
            time.sleep(0.04)
        
        # 썰매 등장
        self.world.add(sleigh_assembly)
        
        time.sleep(0.5)
        
        # 산타가 썰매 쪽으로 이동
        for i in range(30):
            santa_walk.move(3, -1)
            time.sleep(0.03)
        
        # 걷는 산타 제거 (썰매에 탑승)
        self.world.remove(santa_walk)
        
        time.sleep(0.5)
        
        # 썰매 출발 애니메이션 (왼쪽 위로 날아감)
        steps = 80
        for i in range(steps):
            # 곡선 경로로 날아감 (왼쪽 위로)
            dx = -12
            dy = -3 - (i / steps) * 4  # 점점 더 위로
            
            sleigh_assembly.move(dx, dy)
            
            # 약간의 흔들림 효과
            if i % 10 < 5:
                sleigh_assembly.move(0, 1)
            else:
                sleigh_assembly.move(0, -1)
            
            time.sleep(0.03)
        
        time.sleep(1.0)
    
    def run(self):
        """전체 프리신 실행"""
        # Scene 1: 달력 장면
        self.run_calendar_scene()
        
        # Scene 2: 오두막 + 산타 출발 장면
        self.run_cabin_scene()
        
        # 대기
        self.canvas.wait()
        self.canvas.close()

# =================================================================
# 메인 실행
# =================================================================
def main():
    prescene = Prescene()
    prescene.run()

if __name__ == "__main__":
    main()
