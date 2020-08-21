class Unit_Comman_prats:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
class Our_Unit:
    def __init__(self, name, hp, damage):
        Unit_Comman_prats.__init__(self, name, hp, damage)
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 : {}, 공격력 : {}".format(self.hp, self.damage))

    def attack(self, location):
        print("{}이 {}시 방향으로 공격합니다. 공격력[{}]".format(self.name, location, self.damage))

class Enemy_Unit:
    def __init__(self, name, hp, damage):
        Unit_Comman_prats(self, name, hp, damage)
        print("적군) {}유닛이 생성되었습니다.".format(self.name))
        print("적군) 체력 : {}, 공격력 : {}".format(self.hp, self.damage))

i = 0   # 커맨드 자동 반복
j = 0   # 게임 스타트 버튼
marine_num = 0   # 아군 마린 수
tank_num = 0    # 아군 탱크 수

def create_unit():
    global marine_num
    Unit_name = input("생성할 유닛 이름을 입력하세요 : ")
    if Unit_name == "marine":
        marine = Our_Unit(Unit_name, 40, 5)
        marine_num += 1
        print("마린의 전체 수는 {}입니다".format(marine_num))
    elif Unit_name == "tank":
        global tank_num
        tank = Our_Unit(Unit_name, 180, 35)
        tank_num += 1
        print("탱크의 전체 수는 {}입니다".format(tank_num))

# def mineral():    # 스레드를 아직 배우지 않아서 불가능
#     our_mineral = 50     # 미네랄 초기값
#     while globals(i) == 0:

def check_unit():
    unit_name = input("확인할 병력을 입력하세요: ")
    if unit_name == "marine":
        print("현재 마린의 수는 {}입니다".format(marine_num))
    elif unit_name == "tank":
        print("현재 탱크의 수는 {}입니다.".format(tank_num))


while i == 0:
    command = input("메인 커맨드를 입력하세요 (도움말 : help 입력) : ")
    if command == "qq":
        print("프로그램을 종료합니다.")
        quit()

    elif command == "help":
        print("도움말 목록")
        print("quit : 프로그램 종료")

    elif command == "start" and j == 0:
        print("게임을 시작합니다")
        j = 1

    elif command == "create":
        create_unit()

    elif command == "check":
        check_unit()

    else:
        print("커맨드를 다시 입력하세요")
