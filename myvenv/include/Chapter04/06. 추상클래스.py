from abc import * # 추상클래스 사용 시 abc 불러와야함.

class Item (metaclass = ABCMeta ): # metaclass = ABCMeta  적어줘야함.
    '''
    속성 : 이름
    메서드 : 줍기, 버리기
    '''
    def __init__(self,name):
        self.name = name
    def pick(self):
        print(f'[{self.name}]을(를) 주웠습니다.')

    def discard(self):
        print(f'[{self.name}]을(를) 버렸습니다.')

    @abstractclassmethod
    def use(self):
        pass

class Weapon(Item):
    '''
    속성 : 공격력
    메서드 : 공격하기
    '''
    def __init__(self, name, demage):
        super().__init__(name) 
        self.demage = demage

    def use(self):
        print(f'[{self.name}] 을(를) 이용해 {self.demage} 로 공격합니다.')


class HealingItem(Item):
    '''
    속성 : 회복량
    메서드 : 사용하기
    '''
    def __init__(self, name, revcovery_amount):
        super().__init__(name)
        self.revcovery_amount = revcovery_amount

    def use(self):
        print(f'[{self.name}] 을(를) 사용합니다. {self.revcovery_amount} 회복')



m16 = Weapon('m16', 110)
bungdae = HealingItem('붕대', 20)

m16.use()
bungdae.use()