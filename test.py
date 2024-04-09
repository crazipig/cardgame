"""
def to_uniqui_array(array):
    uniqui_array=[]
    for item in array:
        if item not in uniqui_array:
            uniqui_array.append(item)
    return uniqui_array

array=[1,2,3,3,4,4,5]
print(to_uniqui_array(array))
"""

"""
while True:
    value = input('Value between 0 and 100:')
    try:
       value = int(value)
    except ValueError:
       print("Valid number, please")
       continue
    if 0 <= value <= 100:
       break
    else:
       print('Valid range, please: 0-100')
"""

list=['a','b','c','d','e']
for i,word in enumerate(list):
    print(i+1,word)