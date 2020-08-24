import random

class Unit_Comman_prats:    #일반 유닛 특성 저장
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

class Our_Unit: #아군 유닛 생성
    def __init__(self, name, hp, damage):
        Unit_Comman_prats.__init__(self, name, hp, damage)
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 : {}, 공격력 : {}".format(self.hp, self.damage))

    def attack(self, location):
        print("{}이 {}시 방향으로 공격합니다. 공격력[{}]".format(self.name, location, self.damage))

    def hp(self):
        return self.hp

class Enemy_Unit:
    def __init__(self, name, hp, damage):
        Unit_Comman_prats(self, name, hp, damage)
        print("적군) {}유닛이 생성되었습니다.".format(self.name))
        print("적군) 체력 : {}, 공격력 : {}".format(self.hp, self.damage))

i = 0   # 커맨드 자동 반복
j = 0   # 게임 스타트 버튼
marine_num = 0   # 아군 마린 수
tank_num = 0    # 아군 탱크 수
enemy_location = 1
marine_all = []
tank_all = []

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
    unit_name = input("확인할 병력을 입력하세요: (help 입력시 생산 가능 유닛 나옴)")
    if unit_name == "marine":
        print("현재 마린의 수는 {}입니다".format(marine_num))
    elif unit_name == "tank":
        print("현재 탱크의 수는 {}입니다.".format(tank_num))
    elif unit_name == "help":
        print("현재 생산 가능한 유닛은 marine, tank 입니다")

def attack_command():   # 유닛별로 조건을 만들어 공격하고 데미지를 입게 한다
    location = input("공격할 위치(시간)을 입력하세요 : (예 : 1)")
    if marine_num > 0:  # 마린이 1기라도 있을 시
        print("마린 {}기가 {}시 방향으로 공격합니다".format(marine_num, location))
        if int(location) == int(enemy_location):  # 공격 위치에 적이 있을 시(적 위치는 랜덤)
            get_damaged("marine", marine_num)   # 유닛 이름, 유닛 갯수

    if tank_num > 0:
        print("탱크 {}기가 {}시 방향으로 공격합니다".format(tank_num, location))
        if int(location) == int(enemy_location):  # 공격 위치에 적이 있을 시(적 위치는 랜덤)
            get_damaged("tank", tank_num)  # 유닛 이름, 유닛 갯수


def get_damaged(unit_name, unit_num):
    unit_count = 0  # 유닛 카운터 초기화
    global marine_num
    global tank_num
    while unit_count < unit_num:
        damage = random.randint(1, 200)
        print("{} 1기가 {}의 데미지를 입었습니다.".format(unit_name, damage))
        if damage >= 40 and unit_name == "marine":
            print("[{} 1기가 죽었습니다]".format(unit_name))
            marine_num -= 1
        elif damage >= 150 and unit_name =="tank":
            print("[{} 1기가 죽엇습니다]".format(unit_name))
            tank_num -= 1


        unit_count += 1


def checkEnemy():
    print("적의 위치는 {}시입니다.".format(enemy_location))


while i == 0:
    command = input("메인 커맨드를 입력하세요 (도움말 : help 입력) : ")
    if command == "qq":
        print("프로그램을 종료합니다.")
        quit()

    elif command == "help":
        print("도움말 목록")
        print("quit : 프로그램 종료")
        print("start : 게임 시작")
        print("create : 유닛 생산")
        print("check : 생성된 유닛 확인")
        print("attack : 모든 유닛 공격 명령")

    elif command == "start" and j == 0:
        print("게임을 시작합니다")
        enemy_location = range(1, 12)
        j = 1

    elif command == "create":
        create_unit()

    elif command == "check":
        check_unit()

    elif command == "attack":
        attack_command()
    elif command == "enemy location":
        checkEnemy()

    else:
        print("커맨드를 다시 입력하세요")
