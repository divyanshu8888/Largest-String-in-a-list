list1 = [item for item in range(int(input('Enter the size of list:--  '))) for item in str(input('Enter the element you want:--  ')).split()]

list1.sort(key=len)

list2 = []
for _ in range(len(list1)):
    list2.append(len(list1[_]))

def match():
    list3 = []
    for _ in range(len(list2)):
        if list2[_] == list2[-1]:
            list3.append(list1[_])
    return list3

for _ in range(len(list1)):
    if list2[_] == list2[-1]:
        pass
    a = match()

print(f'Outcomes i.e., {a}')