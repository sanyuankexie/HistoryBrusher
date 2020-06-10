import pandas as pd
import numpy as np


def recode_num(a, fileName):
    a += 1
    with open(fileName, "w", encoding="gb18030") as file:
        file.write(str(a))


def read_scores(fileName):
    with open(fileName, "r", encoding="gb18030") as file:
        a = file.read()
        return a


chooses = ["A", "B", "C", "D"]
names = ['近代史上篇测试1.csv', '近代史上篇测试2.csv', '近代史中篇测试2.csv', '近代史期中测试1.csv', '近代史期中测试2.csv', '近代史第一次平时练习.csv'
         ,'1920215-202001.csv','1920215-202002.csv','1920215-下篇1.csv','1920215-下篇2.csv', '1920215-中篇测试1.csv', '1920215-中篇测试2.csv', '1920217-期中测试1.csv']
data = pd.read_csv(names[0], header=None)
for name in names:
    temp = pd.read_csv(name, header=None)
    data = data.append(temp)
data.index = range(data.shape[0])
scores = int(read_scores("score.txt"))
while 1:
    index = np.random.randint(data.shape[0])
    err = 0
    q = data.iloc[index, :]
    answer = q[2]
    print("你的分数为：",scores)
    print(q[0].strip() + q[1].strip())
    for i in range(3, 7):
        print(chooses[i - 3] + "、" + q[i].strip())
    while 1:
        a = input("请输入你的选择：")
        if a == answer:
            print("yes!")
            scores += 1
            print("\n")
            recode_num(scores, "score.txt")
            break
        else:
            err += 1
            if err > 5:
                print(answer)
                print("\n")
                break
