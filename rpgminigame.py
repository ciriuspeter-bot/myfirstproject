import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack = 15
        self.potions = 3
    
    def show_status(self):
        print(f"\n⚔️ {self.name} 상태 ⚔️")
        print(f"❤️ HP: {self.hp}/{self.max_hp}")
        print(f"🧪 포션: {self.potions}개")
    
    def heal(self):
        if self.potions > 0 and self.hp < self.max_hp:
            heal_amount = random.randint(20, 30)
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.potions -= 1
            print(f"✨ {heal_amount} HP를 회복했습니다!")
            return True
        return False

class Monster:
    def __init__(self, level):
        self.level = level
        self.name = f"Lv.{level} 몬스터"
        self.hp = 30 + level * 20
        self.attack = 5 + level * 3
    
    def show_status(self):
        print(f"👾 {self.name} 👾")
        print(f"❤️ HP: {self.hp}")

def battle(player, monster):
    print(f"\n⚔️ {monster.name}와 전투 시작! ⚔️")
    
    while player.hp > 0 and monster.hp > 0:
        print("\n" + "="*30)
        player.show_status()
        monster.show_status()
        
        print("\n행동을 선택하세요:")
        print("1. ⚔️ 공격")
        print("2. 🧪 포션 사용")
        
        action = input("선택: ")
        
        if action == "1":
            # 플레이어 공격
            damage = random.randint(player.attack - 5, player.attack + 5)
            monster.hp -= damage
            print(f"⚡ {damage} 데미지를 입혔습니다!")
            
            if monster.hp <= 0:
                print(f"🎉 {monster.name}를 처치했습니다!")
                return True
            
            # 몬스터 반격
            damage = random.randint(monster.attack - 3, monster.attack + 3)
            player.hp -= damage
            print(f"💥 몬스터의 공격! {damage} 데미지!")
            
        elif action == "2":
            if not player.heal():
                print("❌ 포션을 사용할 수 없습니다!")
        else:
            print("❌ 잘못된 선택입니다!")
        
        time.sleep(1)
    
    return False

# 게임 시작
print("🎮 텍스트 RPG 게임에 오신 것을 환영합니다!")
player_name = input("당신의 이름을 입력하세요: ")
player = Player(player_name)

print(f"\n반갑습니다, {player_name}님!")
print("던전에 입장합니다...")
time.sleep(2)

# 메인 게임 루프
for level in range(1, 6):
    print(f"\n📌 레벨 {level} 던전에 입장했습니다!")
    monster = Monster(level)
    
    if not battle(player, monster):
        print(f"\n💀 {player.name}는 쓰러졌습니다... 게임 오버!")
        break
    
    if level < 5:
        print(f"\n✨ 레벨 {level}을 클리어했습니다!")
        player.hp = min(player.hp + 20, player.max_hp)
        print("❤️ 체력을 20 회복했습니다.")
        input("계속하려면 Enter를 누르세요...")
else:
    print(f"\n🏆 축하합니다! {player.name}는 모든 던전을 클리어했습니다!")

