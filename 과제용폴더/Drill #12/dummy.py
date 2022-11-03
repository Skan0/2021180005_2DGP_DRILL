# class Player:
#     type = 'Player'
#
#     def __init__(self):
#         self.x = 100
#
#     def where(self):
#         print(self.x)
#
#
# player = Player()
# player.where()
#
# print(Player.type)  # 클래스 변수 출력
# print(Player.name)  # name이라는 객체 변수가 없으면 같은 이름의 클래스 변수가 선택됨
#
# Player.where(player)  # 원칙적인 파이썬 스타일의 멤버  함수 호출
# player.where()  # Player.where 와 동일
#
table = {
     "SLEEP" : {"HIT" : "WAKE"},
     'WAKE': {"TIMER", "SLEEP"}
}
cur_state = "SLEEP"
next_state = table[cur_state]["HIT"]
