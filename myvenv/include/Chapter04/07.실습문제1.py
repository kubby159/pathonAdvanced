# 유닛 정보
unit_info = {
    "probe":{
        "name":"프로브",
        "mineral": 50,
        "gas": 0,
        "hp":20,
        "shield": 20,
        "demage": 5
    },
        "zealot":{
        "name":"질럿",
        "mineral": 100,
        "gas": 0,
        "hp":100,
        "shield": 60,
        "demage": 16
    },   
     "dragon":{
        "name":"드라군",
        "mineral": 125,
        "gas": 50,
        "hp":100,
        "shield": 80,
        "demage": 20
    }
}
# 유닛 클래스
class Unit:
    '''
    속성 : 이름, 체력, 방어막, 공격력
    '''
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
    def __str__(self) :
        return f"[{self.name}] 체력: {self.hp} 방어막: {self.shield} 공격력: {self.demage}" 
# 플레이어 클래스
class Player:
    '''
    속성 : 닉네임, 미네랄, 가스
    메서드 : 유닛 생산하기
    '''
    def __init__(self,nick_name,mineral,gas, unit_list = []):
        self.nick_name =nick_name
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list

    def produce(self, name,mineral,gas,hp,shield,demage):
        if self.mineral - mineral  < 0:
            print("미네랄이 부족합니다.")
        elif self.gas - gas < 0:
            print("가스가 부족합니다.")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name,hp,shield,demage)
            self.unit_list.append(unit)

player_one = Player('bisu', 200, 200)
player_one.produce(unit_info['probe']['name'],unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])
player_one.produce(unit_info['probe']['name'],unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])
player_one.produce(unit_info['probe']['name'],unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])
player_one.produce(unit_info['probe']['name'],unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])
player_one.produce(unit_info['probe']['name'],unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])
player_one.produce(unit_info['probe']['name'],unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])

for x in player_one.unit_list:
    print(x)