from pico2d import *
import game_framework
import game_world
from ball import Ball

class Boy:
    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):  # 스스로 이벤트 처리를 해라
        # event  = keyevent 이것을 내부 RD등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 50
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)


    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()  # 현재상태를 나가고
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(self.cur_state, __name__, ' ', event_name[event])

            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        #

    def fire_ball(self):
        print('fireball')
        ball = Ball(self.x, self.y, self.face_dir*2)
        game_world.add_object(ball, 1)

# class AUTO_RUN:
#     @staticmethod
#     def enter(self, event):
#         self.frame = 0
#         self.dir = 1
#         pass
#
#     @staticmethod
#     def exit(self):
#         # a를 다시 입력
#         pass
#
#     @staticmethod
#     def do(self):
#         self.frame = (self.frame + 1) % 8
#         if self.x == 800:
#             self.dir = - 1
#         elif self.x == 0:
#             self.dir = 1
#         pass
#
#     @staticmethod
#     def draw(self):
#         # x 값이 끝에 도달 할때 까지 오른쪽을 입력하고
#         # 오른쪽에 도달하면 왼쪽으로 보낸다.
#         # 그림 사이즈도 키워야함
#         if self.dir == -1:
#             self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
#         elif self.dir == 1:
#             self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
#         pass


class SLEEP:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        pass

    @staticmethod
    def exit(self, event):
        if event == SPACE:
            pass
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           -3.141592 / 2, ' ', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, ' ', self.x - 25, self.y - 25, 100, 100)
        pass


class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir = 0
        self.timer = 1000
        pass

    @staticmethod
    def exit(self, event):
        if event == SPACE:
            self.fire_ball()
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass


class RUN:
    def enter(self, event):
        # self.dir 을 결정해야 함.
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    def exit(self, event):
        self.face_dir = self.dir
        if event == SPACE:
            self.fire_ball()
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass


RD, LD, RU, LU, TIMER, SPACE= range(6)  # == 0,1,2,3
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']
key_event_table = {
    # (SDL_KEYDOWN, SDLK_a): AUTO,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}

next_state = {
    # AUTO: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AUTO: AUTO_RUN},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, SPACE: IDLE},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: SLEEP}
}
