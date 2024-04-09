#0402 01:36
import random
import numpy as np

#輸入欲玩遊戲玩家數
while True:
    try:
        players_num=int(input("please input the num of players(minimum 2, maximum 5):"))
        if players_num<2 or players_num>5:
            print("input error,players only allow from 2 to 5,please enter again")
        else:
            break
    except ValueError: #若輸入錯誤型態則要求重新輸入
        print("please input positive integer")

players = []
for i in range(players_num):
    name = input('Please input the name for player {}: '.format(i+1)) #讓遊戲者依序輸入他們的名字
    players.append(name)

#定義牌面數字大小、花色順序
FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #定義撲克牌的點數
SUITS = ['♣', '♦', '♥','♠']
deck = []#初始化樸克牌陣列
#建立一副牌
for face in FACES:
    for suit in SUITS:
        card = (face, suit)  # Tuple representing a card, e.g., ('2', '♠')
        deck.append(card)
random.shuffle(deck) #洗牌
print("")
print("--------------------遊戲開始--------------------")
print("")
players_cards = []  #儲存玩家牌面

#建立玩家資訊之dictionary
def play_game(players_num):
    for i in range(0, players_num):
        mycard = deck[5 * i:5 * i + 5]
        #faces = [card[0] for card in mycard]
        sortedface_mycard = sorted(mycard, key=lambda x: (FACES.index(x[0]), SUITS.index(x[1])))
        sortedsuit_mycard = sorted(mycard, key=lambda x: (SUITS.index(x[1]), FACES.index(x[0])))
        player_info = {
            "player_number": i + 1,
            "hand_cards": mycard,
            "sorted_by_face": sortedface_mycard,
            "sorted_by_suit": sortedsuit_mycard
        }
        players_cards.append(player_info)

#取得牌面之花色
def getsuits(player_info):
    suits = [card[1] for card in player_info["hand_cards"]]
    #print("show suit:", set(suits))
    suits_count=len(set(suits))
    #print("Number of unique suits:", suits_count)
    return suits_count

#取得牌面之數字
def getfaces(player_info):
    faces=[card[0] for card in player_info["sorted_by_face"]]
    return faces

#判斷牌型是否為葫蘆、四條、三條、兩對、一對、單張，回傳key確認牌型
def of_a_kind(faces):     
    faces, counts = np.unique([card[0] for card in player_info["sorted_by_face"]], return_counts=True)   #  np.unique()：去除重複的數字
    sorted_counts = sorted(counts, reverse=True)
    #計算手牌中每種點數出現的次數，並返回點數列表和對應的出現次數
    maximum_count = sorted_counts[0] #最多相同牌數的數量
    second_max_count=sorted_counts[1] #第二多相同牌數的數量
    maxi_faces = [faces[i] for i, count in enumerate(counts) if count == maximum_count] #最多相同牌數的牌面
    maxi_faces.sort(key=lambda x: FACES.index(x)) #排序以便面判斷是兩對中較大的牌面為何
    secondmaxi_faces = [faces[i] for i, count in enumerate(counts) if count == second_max_count] #第二多相同牌數的牌面
    secondmaxi_faces.sort(key=lambda x: FACES.index(x))
    thirdmaxifaces=[] 
    if maximum_count == 3 and second_max_count == 2:
        key=3.5  # 葫蘆
    elif maximum_count == 4:
        key=4  # 四條
    elif maximum_count == 3 and second_max_count==1:
        key=3  # 三條
        secondmaxi_faces=secondmaxi_faces[-1]
    elif maximum_count == 2 and second_max_count == 2:
        key=2.5  # 兩對
        secondmaxi_faces=maxi_faces[0]
        maxi_faces=maxi_faces[1]
    elif maximum_count == 2:
        key=2  # 一對
        secondmaxi_faces=secondmaxi_faces[-1]
    else:
        key=1  # 無(單張)
        maxi_faces=maxi_faces[-1]
        secondmaxi_faces=secondmaxi_faces[-2]
    return key, maxi_faces, secondmaxi_faces

#判斷是否為順子
def is_straight(faces):
    for i in range(len(faces)-1):
        if FACES.index(faces[i+1])-FACES.index(faces[i])!=1:
            return False
    return True

#判斷是否為同花
def isflush(player_info):
    if(suits_count==1):
      return True

#判斷是否為同花順
def is_straight_flush(faces, suits_count):
    if is_straight(faces) and suits_count == 1:
        return True
    return False

#開始遊戲
play_game(players_num)

#顯示玩家資訊
for i in range(0, players_num):
    player_info = players_cards[i]  # 取得特定玩家的資訊
    print("---------------------玩家", player_info["player_number"], "--------------------")#印出玩家資訊
    print("手排5張：", player_info["hand_cards"])
    print("-")
    #print("sorted by face:", player_info["sortd_by_face"])
    #print("sorted by suit:", player_info["sorted_by_suit"])
    # Call the function to print suits
    suits_count=getsuits(player_info)
    faces=getfaces(player_info)

    #利用副程式判斷牌型，並存於玩家資料中
    #player_info["卡牌數值"] 紀錄最大牌面、player_info["卡牌數值2"]紀錄第二大牌面
    if  is_straight_flush(faces, suits_count):
        print('straight flush') #12345
        player_info["牌型數值"] = 5
        player_info["牌型"] = "同花順"
        player_info["卡牌數值"] =faces[-1]
        player_info["卡牌數值2"] = faces[-2]
    elif isflush(player_info):
        print('flush')
        player_info["牌型數值"] = 3.4
        player_info["牌型"] = "同花"
        player_info["卡牌數值"] =faces[-1]
        player_info["卡牌數值2"] = faces[-2]
    elif is_straight(faces):
        print('straight') #12345
        player_info["牌型數值"] = 3.2
        player_info["牌型"] = "順子"
        player_info["卡牌數值"] =faces[-1]
        player_info["卡牌數值2"] = faces[-2]
    else: #處理其他牌型
        key, _, _ = of_a_kind(faces)
        _, maxi_faces, _ = of_a_kind(faces)
        _, _, secondmaxi_faces = of_a_kind(faces)
        player_info["卡牌數值"] = maxi_faces #紀錄最大牌面
        player_info["卡牌數值2"] = secondmaxi_faces #紀錄第二大牌面
        #為了方便檢查、印出玩家卡牌資訊
        print("maxi1st:", maxi_faces,end="\t")
        print("maxi2nd:", secondmaxi_faces)
        print("牌型:",end="")
        if key== 4:
            print('four of a kind') #4444
            player_info["牌型數值"] = 4
            player_info["牌型"] = "鐵支"
        elif key== 3.5:
            print('full house') #33322
            player_info["牌型數值"] = 3.5
            player_info["牌型"] = "葫蘆"
        elif key== 3:
            print('three of a kind') #333
            player_info["牌型數值"] = 3
            player_info["牌型"] = "三條"
        elif key== 2.5:
            print('two pairs') #6677
            player_info["牌型數值"] = 2.5
            player_info["牌型"] = "兩對"
        elif key== 2:
            print('one pair')
            player_info["牌型數值"] = 2
            player_info["牌型"] = "一對"
        else:
            print('highcard')
            player_info["牌型數值"] = 1
            player_info["牌型"] = "單張"
        print("")
"""
for player_info in players_cards:
    print("Player Number:", player_info["player_number"])
    print("Hand Cards:", player_info["hand_cards"])
    print("Sorted by Face:", player_info["sorted_by_face"])
    print("Sorted by Suit:", player_info["sorted_by_suit"])
    print("牌型數值:", player_info["牌型數值"])
    print("牌型:", player_info["牌型"])
    print("卡牌數值:", player_info["卡牌數值"])
    print(type(player_info["卡牌數值"]))
    print("卡牌數值2:", player_info["卡牌數值2"])
    print("----------------------------------")
"""

#將第一、二牌面資料統一轉為字串str
def convert_to_string(value):
    if isinstance(value, np.str_):
        return str(value)
    elif isinstance(value, list) and len(value) > 0:
        return str(value[0])
    else:
        return None
    
# 將牌數字依據FACES[]轉成大小順序
face_to_rank = {face: i for i, face in enumerate(FACES)}

def get_rank(card_value):
    string_value = convert_to_string(card_value)
    return face_to_rank[string_value] if string_value is not None else -1

#排序玩家排名
sorted_players = sorted(players_cards, key=lambda x: (x["牌型數值"], get_rank(x["卡牌數值"]), get_rank(x["卡牌數值2"])), reverse=True)

print("-----------------------------------------------")

# 印出排名
for i,player_info in enumerate(sorted_players):
    print("第", i + 1, "名: 玩家",player_info["player_number"],"，牌型---", player_info["牌型"],player_info["卡牌數值"][0],"\t","第二大牌面：",player_info["卡牌數值2"])




