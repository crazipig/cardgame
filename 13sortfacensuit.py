import random
#定義牌面數字大小、花色順序
FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = [ '♣', '♦', '♥','♠']
#初始化樸克牌陣列
deck = []
name=[]
#建立一副牌
for face in FACES:
    for suit in SUITS:
        card = (face, suit)  # Tuple representing a card, e.g., ('2', '♠')
        deck.append(card)

"""#顯示整復牌
print("整副牌：",deck)
print("-----------------")
"""

# Shuffle the deck
random.shuffle(deck)

"""#顯示洗好的52張牌
print("洗好52張：",deck)
"""
while True:
    try:
        member=int(input("please input the num of members:"))
        if member<2 or member>5:
            print("输入错误，玩家限制人數為2~5人，請重新輸入")
        else:
            break
    except ValueError:
        print("輸入錯誤請輸入正整數")

for m in range (1,member+1):
    name=input("請輸入玩家"+str(m)+"的名字：")
    names=append.name

print("--------------遊戲開始--------------")

for i in range (0,member):
    mycard= deck[5*i:5*i+4]
    print("--------------玩家",i+1,"--------------")
    print("手排5張：",mycard)
    faces = [card[0] for card in mycard]
    sortedface_mycard = sorted(mycard, key=lambda x: (FACES.index(x[0]), SUITS.index(x[1])))
    print("-")
    print("sorted by face:",sortedface_mycard)
    #print("-")
    sortedsuit_mycard = sorted(mycard, key=lambda x: (SUITS.index(x[1]),FACES.index(x[0]) ))
    print("sorted by suit:",sortedsuit_mycard)

"""
#0~12
for i in range(0,14)
    orinum=cardset[i]
    suit=0
    hand[i]=
    cardsuit=orinum/13-1
# 
else:
    cardsuit=orinum//13
cardnum=orinum-13*cardsuit


FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A']    # 定義撲克牌的點數
SUITS = ['♥', '♦', '♣', '♠'] 
"""