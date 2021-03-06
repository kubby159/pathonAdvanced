# Unit 클래스
class Unit:
    '''
    속성 : 이름, 체력, 방어막, 공격력

    '''
    # 생성자(constructor)
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, shield, demage):
        self.name = name # self 는 객체 자기 자신을 의미한다.
        self.hp = hp
        self.shield = shield
        self.demage = demage
        print(f'[{self.name}]가 생성 되었습니다.')

    # 객체를 출력할 때 호출되는 메서드
    def __str__(self):
        return f"[{self.name}] 체력: {self.hp} 방어막: {self.shield} 공격력: {self.demage}" 

    
# 프로브 객체를 생성
probe = Unit('프로브',20,20,5)

# 질럿 객체를 생성
zealot = Unit('질럿',100,60,16)

# 드라군 객체를 생성
dragoon = Unit('드라군',100,80,20)

print(probe)
print(zealot)
print(dragoon)