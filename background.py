#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
고퀄리티 겨울 풍경 - 오두막과 배경
업로드된 이미지를 참고하여 최고 품질로 제작
"""

import random
import time
from cs1graphics import *

# 고퀄리티 겨울 풍경 클래스
class HighQualityWinterScene(Layer):
    """최고 퀄리티 겨울 풍경 - 오두막, 나무, 호수 반사 포함"""
    
    def __init__(self):
        super().__init__()
        
        # 1. 하늘 그라데이션 (화면 전체 커버)
        for i in range(30):
            y = -360 + i * 24
            sky_strip = Rectangle(1280, 24)
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
        
        # 2. 원경 산맥들 (화면 중앙 기준으로 재배치)
        # 가장 뒤쪽 산맥
        far_mountain = Polygon(Point(-640, 50), Point(-400, -50), Point(-200, -30), 
                              Point(0, -80), Point(200, -40), Point(400, -60), 
                              Point(640, -20), Point(640, 360), Point(-640, 360))
        far_mountain.setFillColor('lightGray')
        far_mountain.setBorderColor('gray')
        far_mountain.setBorderWidth(1)
        far_mountain.setDepth(90)
        self.add(far_mountain)
        
        # 중간 산맥
        mid_mountain = Polygon(Point(-500, 80), Point(-300, -20), Point(-100, 0), 
                              Point(100, -50), Point(300, -10), Point(500, -35), 
                              Point(500, 360), Point(-500, 360))
        mid_mountain.setFillColor('gray')
        mid_mountain.setBorderColor('darkGray')
        mid_mountain.setBorderWidth(2)
        mid_mountain.setDepth(85)
        self.add(mid_mountain)
        
        # 앞쪽 산맥 (눈 덮인)
        front_mountain = Polygon(Point(-400, 120), Point(-250, 40), Point(-100, 60), 
                                Point(50, 20), Point(200, 50), Point(350, 30), 
                                Point(400, 360), Point(-400, 360))
        front_mountain.setFillColor('darkGray')
        front_mountain.setBorderColor('black')
        front_mountain.setBorderWidth(2)
        front_mountain.setDepth(80)
        self.add(front_mountain)
        
        # 산 위 눈 덮개들 (화면 중앙 기준)
        snow_peaks = [(-300, 40), (-100, 60), (50, 20), (200, 50), (350, 30)]
        for x, y in snow_peaks:
            snow_cap = Polygon(Point(x-40, y+15), Point(x, y), Point(x+40, y+15),
                              Point(x+35, y+20), Point(x, y+8), Point(x-35, y+20))
            snow_cap.setFillColor('white')
            snow_cap.setBorderColor('lightBlue')
            snow_cap.setBorderWidth(1)
            snow_cap.setDepth(79)
            self.add(snow_cap)
        
        # 3. 언덕들 (눈 덮인 지형) - 화면 중앙에 맞게 조정
        # 뒤쪽 언덕
        back_hill = Polygon(Point(-350, 180), Point(-150, 150), Point(50, 160), 
                           Point(250, 140), Point(350, 170), Point(350, 360), Point(-350, 360))
        back_hill.setFillColor('white')
        back_hill.setBorderColor('lightBlue')
        back_hill.setBorderWidth(1)
        back_hill.setDepth(75)
        self.add(back_hill)
        
        # 앞쪽 언덕
        front_hill = Polygon(Point(-300, 220), Point(-100, 190), Point(100, 200), 
                            Point(300, 180), Point(400, 210), Point(400, 360), Point(-400, 360))
        front_hill.setFillColor('white')
        front_hill.setBorderColor('lightBlue')
        front_hill.setBorderWidth(2)
        front_hill.setDepth(70)
        self.add(front_hill)
        
        # 4. 고퀄리티 오두막 (화면 중앙에 배치)
        self.create_premium_cabin(0, 200)
        
        # 5. 고퀄리티 겨울 나무들 (화면 중앙에 맞게 배치)
        tree_data = [
            (-200, 190, 'large'),   # 왼쪽 큰 나무
            (-120, 205, 'medium'),  # 왼쪽 중간 나무
            (180, 195, 'large'),    # 오른쪽 큰 나무
            (280, 210, 'small'),    # 오른쪽 작은 나무
            (-300, 220, 'medium'),  # 멀리 왼쪽
            (350, 225, 'small')     # 멀리 오른쪽
        ]
        
        for x, y, size in tree_data:
            self.create_winter_tree(x, y, size)
        
        # 6. 얼어붙은 호수 (반사 효과 포함)
        self.create_frozen_lake()
        
        # 7. 대기 효과 (안개, 눈송이)
        self.create_atmosphere_effects()
    
    def create_premium_cabin(self, x, y):
        """최고 퀄리티 오두막 생성"""
        cabin_layer = Layer()
        
        # 오두막 기초 (돌 기초)
        foundation = Rectangle(180, 20)
        foundation.setFillColor('gray')
        foundation.setBorderColor('darkGray')
        foundation.setBorderWidth(2)
        foundation.move(x, y + 80)
        foundation.setDepth(60)
        cabin_layer.add(foundation)
        
        # 통나무 벽체 (고퀄리티)
        main_wall = Rectangle(160, 120)
        main_wall.setFillColor('saddleBrown')
        main_wall.setBorderColor('brown')
        main_wall.setBorderWidth(3)
        main_wall.move(x, y + 20)
        main_wall.setDepth(58)
        cabin_layer.add(main_wall)
        
        # 통나무 디테일 (수평 라인들)
        for i in range(7):
            log_y = y - 20 + i * 18
            log_line = Path(Point(x - 80, log_y), Point(x + 80, log_y))
            log_line.setBorderColor('brown')
            log_line.setBorderWidth(4)
            log_line.setDepth(57)
            cabin_layer.add(log_line)
            
            # 통나무 끝부분 원형 디테일
            left_end = Circle(6, Point(x - 80, log_y))
            left_end.setFillColor('brown')
            left_end.setBorderColor('darkRed')
            left_end.setBorderWidth(2)
            left_end.setDepth(56)
            cabin_layer.add(left_end)
            
            right_end = Circle(6, Point(x + 80, log_y))
            right_end.setFillColor('brown')
            right_end.setBorderColor('darkRed')
            right_end.setBorderWidth(2)
            right_end.setDepth(56)
            cabin_layer.add(right_end)
        
        # 지붕 (삼각형, 눈 덮인)
        roof = Polygon(Point(x - 100, y - 40), Point(x, y - 120), Point(x + 100, y - 40))
        roof.setFillColor('darkRed')
        roof.setBorderColor('black')
        roof.setBorderWidth(3)
        roof.setDepth(55)
        cabin_layer.add(roof)
        
        # 지붕 위 눈 (두꺼운 눈 층)
        snow_roof = Polygon(Point(x - 100, y - 40), Point(x, y - 120), Point(x + 100, y - 40),
                           Point(x + 90, y - 35), Point(x, y - 110), Point(x - 90, y - 35))
        snow_roof.setFillColor('white')
        snow_roof.setBorderColor('lightBlue')
        snow_roof.setBorderWidth(2)
        snow_roof.setDepth(54)
        cabin_layer.add(snow_roof)
        
        # 굴뚝 (연기 포함)
        chimney = Rectangle(25, 50)
        chimney.setFillColor('darkGray')
        chimney.setBorderColor('black')
        chimney.setBorderWidth(2)
        chimney.move(x + 40, y - 90)
        chimney.setDepth(53)
        cabin_layer.add(chimney)
        
        # 굴뚝 연기 (여러 개의 구름)
        for i in range(4):
            smoke = Circle(8 - i)
            smoke.setFillColor('lightGray')
            smoke.setBorderColor('gray')
            smoke.move(x + 40 + i * 10, y - 130 - i * 20)
            smoke.setDepth(52)
            cabin_layer.add(smoke)
        
        # 문 (고퀄리티 나무 문)
        door_frame = Rectangle(50, 80)
        door_frame.setFillColor('darkRed')
        door_frame.setBorderColor('black')
        door_frame.setBorderWidth(2)
        door_frame.move(x, y + 40)
        door_frame.setDepth(51)
        cabin_layer.add(door_frame)
        
        door = Rectangle(45, 75)
        door.setFillColor('orange')
        door.setBorderColor('brown')
        door.setBorderWidth(2)
        door.move(x, y + 40)
        door.setDepth(50)
        cabin_layer.add(door)
        
        # 문 패널 디테일
        for i in range(3):
            panel_y = y + 20 + i * 20
            panel = Path(Point(x - 18, panel_y), Point(x + 18, panel_y))
            panel.setBorderColor('brown')
            panel.setBorderWidth(2)
            panel.setDepth(49)
            cabin_layer.add(panel)
        
        # 문 손잡이
        knob = Circle(4)
        knob.setFillColor('gold')
        knob.setBorderColor('orange')
        knob.setBorderWidth(2)
        knob.move(x + 15, y + 40)
        knob.setDepth(48)
        cabin_layer.add(knob)
        
        # 창문들 (따뜻한 빛이 새어나오는)
        # 왼쪽 창문
        win1_frame = Rectangle(40, 40)
        win1_frame.setFillColor('brown')
        win1_frame.setBorderColor('black')
        win1_frame.setBorderWidth(2)
        win1_frame.move(x - 50, y)
        win1_frame.setDepth(51)
        cabin_layer.add(win1_frame)
        
        win1_glass = Rectangle(35, 35)
        win1_glass.setFillColor('yellow')  # 따뜻한 빛
        win1_glass.setBorderColor('orange')
        win1_glass.setBorderWidth(1)
        win1_glass.move(x - 50, y)
        win1_glass.setDepth(50)
        cabin_layer.add(win1_glass)
        
        # 창문 십자 프레임
        win1_h = Path(Point(x - 67, y), Point(x - 33, y))
        win1_h.setBorderColor('brown')
        win1_h.setBorderWidth(3)
        win1_h.setDepth(49)
        cabin_layer.add(win1_h)
        
        win1_v = Path(Point(x - 50, y - 17), Point(x - 50, y + 17))
        win1_v.setBorderColor('brown')
        win1_v.setBorderWidth(3)
        win1_v.setDepth(49)
        cabin_layer.add(win1_v)
        
        # 오른쪽 창문
        win2_frame = Rectangle(30, 30)
        win2_frame.setFillColor('brown')
        win2_frame.setBorderColor('black')
        win2_frame.setBorderWidth(2)
        win2_frame.move(x + 50, y - 10)
        win2_frame.setDepth(51)
        cabin_layer.add(win2_frame)
        
        win2_glass = Rectangle(25, 25)
        win2_glass.setFillColor('yellow')  # 따뜻한 빛
        win2_glass.setBorderColor('orange')
        win2_glass.setBorderWidth(1)
        win2_glass.move(x + 50, y - 10)
        win2_glass.setDepth(50)
        cabin_layer.add(win2_glass)
        
        # 작은 창문 프레임
        win2_h = Path(Point(x + 37, y - 10), Point(x + 63, y - 10))
        win2_h.setBorderColor('brown')
        win2_h.setBorderWidth(2)
        win2_h.setDepth(49)
        cabin_layer.add(win2_h)
        
        win2_v = Path(Point(x + 50, y - 22), Point(x + 50, y + 2))
        win2_v.setBorderColor('brown')
        win2_v.setBorderWidth(2)
        win2_v.setDepth(49)
        cabin_layer.add(win2_v)
        
        # 오두막 주변 눈 더미
        for i in range(5):
            pile_x = x + random.randint(-120, 120)
            pile_y = y + random.randint(60, 90)
            pile = Ellipse(random.randint(15, 30), random.randint(8, 15))
            pile.setFillColor('white')
            pile.setBorderColor('lightBlue')
            pile.move(pile_x, pile_y)
            pile.setDepth(65)
            cabin_layer.add(pile)
        
        cabin_layer.setDepth(60)
        self.add(cabin_layer)
    
    def create_winter_tree(self, x, y, size):
        """고퀄리티 겨울 나무 생성"""
        tree_layer = Layer()
        
        # 크기별 설정
        if size == 'large':
            trunk_width, trunk_height = 15, 60
            branch_levels = 5
            max_branch_width = 50
        elif size == 'medium':
            trunk_width, trunk_height = 12, 45
            branch_levels = 4
            max_branch_width = 40
        else:  # small
            trunk_width, trunk_height = 8, 30
            branch_levels = 3
            max_branch_width = 25
        
        # 나무 줄기
        trunk = Rectangle(trunk_width, trunk_height)
        trunk.setFillColor('saddleBrown')
        trunk.setBorderColor('brown')
        trunk.setBorderWidth(2)
        trunk.move(x, y + trunk_height//2)
        trunk.setDepth(45)
        tree_layer.add(trunk)
        
        # 나무 가지들 (눈 덮인)
        for level in range(branch_levels):
            branch_y = y - level * (trunk_height // branch_levels)
            branch_width = max_branch_width - level * 8
            
            # 왼쪽 가지 그룹
            for i in range(3):  # 여러 개의 가지로 풍성하게
                offset = i * 8
                left_branch = Polygon(Point(x, branch_y), 
                                    Point(x - branch_width + offset, branch_y + 12), 
                                    Point(x - branch_width + offset + 8, branch_y + 18), 
                                    Point(x, branch_y + 6))
                left_branch.setFillColor('darkGreen')
                left_branch.setBorderColor('green')
                left_branch.setBorderWidth(1)
                left_branch.setDepth(44)
                tree_layer.add(left_branch)
            
            # 오른쪽 가지 그룹
            for i in range(3):
                offset = i * 8
                right_branch = Polygon(Point(x, branch_y), 
                                     Point(x + branch_width - offset, branch_y + 12), 
                                     Point(x + branch_width - offset - 8, branch_y + 18), 
                                     Point(x, branch_y + 6))
                right_branch.setFillColor('darkGreen')
                right_branch.setBorderColor('green')
                right_branch.setBorderWidth(1)
                right_branch.setDepth(44)
                tree_layer.add(right_branch)
            
            # 가지 위 눈 (자연스러운 형태)
            snow_left = Ellipse(branch_width//2, 8)
            snow_left.setFillColor('white')
            snow_left.setBorderColor('lightBlue')
            snow_left.move(x - branch_width//2, branch_y + 15)
            snow_left.setDepth(43)
            tree_layer.add(snow_left)
            
            snow_right = Ellipse(branch_width//2, 8)
            snow_right.setFillColor('white')
            snow_right.setBorderColor('lightBlue')
            snow_right.move(x + branch_width//2, branch_y + 15)
            snow_right.setDepth(43)
            tree_layer.add(snow_right)
        
        tree_layer.setDepth(45)
        self.add(tree_layer)
    
    def create_frozen_lake(self):
        """얼어붙은 호수와 반사 효과 (화면에 맞게 조정)"""
        lake_layer = Layer()
        
        # 호수 본체 (타원형) - 화면 하단에 배치
        lake = Ellipse(600, 120)
        lake.setFillColor('lightBlue')
        lake.setBorderColor('blue')
        lake.setBorderWidth(3)
        lake.move(0, 300)
        lake.setDepth(40)
        lake_layer.add(lake)
        
        # 호수 얼음 표면 효과
        ice_surface = Ellipse(580, 100)
        ice_surface.setFillColor('lightCyan')
        ice_surface.setBorderColor('lightBlue')
        ice_surface.setBorderWidth(1)
        ice_surface.move(0, 295)
        ice_surface.setDepth(39)
        lake_layer.add(ice_surface)
        
        # 얼음 균열들 (호수 위치에 맞게 조정)
        crack_patterns = [
            ((-150, 280), (-80, 310)),
            ((80, 290), (180, 305)),
            ((-200, 300), (-120, 320)),
            ((40, 270), (140, 285)),
            ((-30, 305), (60, 320))
        ]
        
        for start, end in crack_patterns:
            crack = Path(Point(start[0], start[1]), Point(end[0], end[1]))
            crack.setBorderColor('darkBlue')
            crack.setBorderWidth(2)
            crack.setDepth(38)
            lake_layer.add(crack)
        
        # 반사 효과 (오두막과 나무들의 흐릿한 반사)
        # 오두막 반사
        cabin_reflection = Rectangle(100, 60)
        cabin_reflection.setFillColor('lightGray')
        cabin_reflection.setBorderColor('gray')
        cabin_reflection.setBorderWidth(1)
        cabin_reflection.move(0, 320)
        cabin_reflection.setDepth(37)
        lake_layer.add(cabin_reflection)
        
        # 나무 반사들
        tree_reflections = [(-150, 310), (130, 315), (-80, 325)]
        for x, y in tree_reflections:
            reflection = Polygon(Point(x, y), Point(x - 12, y + 25), Point(x + 12, y + 25))
            reflection.setFillColor('darkGray')
            reflection.setBorderColor('gray')
            reflection.move(0, 0)
            reflection.setDepth(37)
            lake_layer.add(reflection)
        
        lake_layer.setDepth(40)
        self.add(lake_layer)
    
    def create_atmosphere_effects(self):
        """대기 효과 - 안개, 눈송이, 빛 효과 (1280×720 최적화)"""
        atmosphere_layer = Layer()
        
        # 안개 효과 (지면 근처) - 화면 중앙에 맞게 조정
        for i in range(6):
            fog_x = random.randint(-400, 400)
            fog_y = random.randint(250, 330)
            fog = Ellipse(random.randint(60, 120), random.randint(15, 30))
            fog.setFillColor('lightGray')
            fog.setBorderColor('lightGray')
            fog.move(fog_x, fog_y)
            fog.setDepth(35)
            atmosphere_layer.add(fog)
        
        # 고퀄리티 눈송이들 (화면 전체에 분포)
        for i in range(50):
            size = random.randint(2, 6)
            snow_x = random.randint(-640, 640)
            snow_y = random.randint(-360, 360)
            
            # 기본 눈송이
            snowflake = Circle(size)
            snowflake.setFillColor('white')
            snowflake.setBorderColor('lightBlue')
            snowflake.setBorderWidth(1)
            snowflake.move(snow_x, snow_y)
            snowflake.setDepth(30)
            atmosphere_layer.add(snowflake)
            
            # 큰 눈송이는 십자 패턴 추가
            if size > 4:
                cross_h = Path(Point(snow_x - size, snow_y), Point(snow_x + size, snow_y))
                cross_h.setBorderColor('white')
                cross_h.setBorderWidth(1)
                cross_h.setDepth(29)
                atmosphere_layer.add(cross_h)
                
                cross_v = Path(Point(snow_x, snow_y - size), Point(snow_x, snow_y + size))
                cross_v.setBorderColor('white')
                cross_v.setBorderWidth(1)
                cross_v.setDepth(29)
                atmosphere_layer.add(cross_v)
        
        # 눈 더미들 (지면에) - 화면 하단에 맞게 조정
        for i in range(12):
            pile_x = random.randint(-400, 400)
            pile_y = random.randint(240, 300)
            pile_width = random.randint(20, 50)
            pile_height = random.randint(8, 20)
            
            pile = Ellipse(pile_width, pile_height)
            pile.setFillColor('white')
            pile.setBorderColor('lightBlue')
            pile.setBorderWidth(1)
            pile.move(pile_x, pile_y)
            pile.setDepth(65)
            atmosphere_layer.add(pile)
        
        # 추가 퀄리티 향상: 빛 효과
        # 오두막 창문에서 나오는 빛 번짐 효과 (오두막 새 위치에 맞게)
        for i in range(3):
            light_glow = Circle(15 + i * 5)
            light_glow.setFillColor('yellow')
            light_glow.setBorderColor('orange')
            light_glow.move(-50, 200)  # 왼쪽 창문
            light_glow.setDepth(25 - i)
            atmosphere_layer.add(light_glow)
            
            light_glow2 = Circle(10 + i * 3)
            light_glow2.setFillColor('yellow')
            light_glow2.setBorderColor('orange')
            light_glow2.move(50, 190)  # 오른쪽 창문
            light_glow2.setDepth(25 - i)
            atmosphere_layer.add(light_glow2)
        
        atmosphere_layer.setDepth(30)
        self.add(atmosphere_layer)

# 메인 함수
def main():
    # 캔버스 설정
    canvas = Canvas(1280, 720)
    canvas.setBackgroundColor('lightBlue')
    canvas.setTitle("High Quality Winter Scene")
    
    # 고퀄리티 겨울 풍경 생성
    winter_scene = HighQualityWinterScene()
    
    # 전체 장면을 화면 중앙으로 이동 (640, 360은 화면 중심)
    winter_scene.move(640, 360)
    
    canvas.add(winter_scene)
    
    # 화면에 표시
    canvas.wait()
    canvas.close()

if __name__ == "__main__":
    main()
