import random 
import math

deck =[f'{v}{s}' for s in '♠♥♦♣' for v in '6789TJQKA']
random.seed(7)
print('Всего карт в колоде: ', len(deck))

hand = random.sample(deck, 5)
print('Рука игрока (sample): ', hand)

print('Карта для (choise): ', random.choice(deck))

weights = {'обычная': 70, 'редкая': 25, 'легендарная': 5}
loot = random.choices(list(weights), weights=list(weights.values()), k=5)
print('Лут (choise, 5 шт.):', loot)

random.shuffle(deck)
print('после shuffle      :', deck[:6], '...')

print('\n--- Раздача 3 игрокам по 5 карт---')
players = ["Алиса", "Борис", "Вера"]
pool = deck.copy()
for p in players:
    print(f'{p:6s}: {random.sample(pool, 5)}')

print('\n--- Лотерея "6 из 45" ---')
numbers = sorted(random.sample(range(1,46), 6))
print('Ваши номера: ', *numbers)

total = math.comb(45,6)
print(f'Всего возможных комбинаций: {total:,}'.replace(',', ' '))
print(f'Вероятность угадвать все 6: 1 / {total} =  {1 / total:.10f} ({1 / total * 100:.7f}%)')
