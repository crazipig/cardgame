import numpy as np

card=[('3', '♠'), ('3', '♥'), ('5', '♠'), ('3', '♦'), ('4', '♥')]
FACES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']    # 定義撲克牌的點數
SUITS = ['♥', '♦', '♣', '♠'] 

faces, counts = np.unique(card, return_counts=True)   #  np.unique()：去除重複的數字
sorted_counts = sorted(counts, reverse=True)
#計算手牌中每種點數出現的次數，並返回點數列表和對應的出現次數
maximum_count = sorted_counts[0] #最多相同牌數
second_max_count=sorted_counts[1] #第二多相同牌數
maxi_faces = [card[i] for i, count in enumerate(counts) if count == maximum_count] #最多相同牌數的牌面g
maxi_faces.sort(key=lambda x: FACES.index(x[0]))
secondmaxi_faces = [card[i] for i, count in enumerate(counts) if count == second_max_count] #第二多相同牌數的牌面
secondmaxi_faces.sort(key=lambda x: FACES.index(x[0]))
print(maxi_faces)
print(second_max_count)
if maximum_count == 3 and second_max_count == 1:
    key=3.5  # 葫蘆
    print("葫蘆")
elif maximum_count == 4:
    key=4  # 四條
elif maximum_count == 3:
    key=3  # 三條
    print("三條")
elif maximum_count == 2 and second_max_count == 2:
    key=2.5  # 兩對
    secondmaxi_faces=maxi_faces[0]
    maxi_faces=maxi_faces[1]
elif maximum_count == 2:
    key=2  # 一對
else:
    key=1  # 無
    maxi_faces=maxi_faces[-1]
