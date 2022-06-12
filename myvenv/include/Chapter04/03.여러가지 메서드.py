# Unit 클래스
from re import S


class Unit:
    '''
    인스턴스 속성: 이름, 체력, 방어막, 공격력
    -> 객체마다 다른 값을 가지는 속성

    클래스 속성
    -> 모든 객체가 공유하는 속성

    #비공개 속성
    -> 클래스 안에서만 사용이 가능.

    '''
    count = 0
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp # __ 비공개 클래스
        self.shield = shield
        self.demage = demage
        Unit.count+=1
        print(f'[{self.name}]가 생성 되었습니다.')

    def __str__(self):
        return f"[{self.name}] 체력: {self.hp} 방어막: {self.shield} 공격력: {self.demage}" 

    # 인스턴스 메서드(instance method)
    # 인스턴스 속성에 접근할 수 있는 메서드
    def hit(self,demage) :
        # 방어막 변경
        if self.shield >= self.hp :
            self.shield-= demage
            demage = 0

        else:
            demage -= self.shield
            self.shield = 0
        # 체력 변경
        if demage > 0:
            if self.hp > demage:
                self.hp-= demage
                
            else:
                self.hp = 0
        
    # 클래스 메서드 (class method)
    # 클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f'생성된 유닛 개수 : {cls.count}개') # Unit.count


probe = Unit('프로브',20,20,5)
zealot = Unit('질럿',100,60,16)
dragoon = Unit('드라군',100,80,20)

# 인스턴스 속성 수정
probe.demage += 1
print(probe)

# 비공개 속성 접근
# probe.__hp = 9999

# 네임 맹글링(name mangling) : 비공개 속성에 접근가능.
# probe._Unit__hp = 9999
print(probe)

# 전체 유닛 갯수
print(Unit.count)
probe.hit(zealot.demage)
probe.hit(zealot.demage)


Unit.print_count()