import pandas as pd
import numpy as np
import os

def recode_num(a, fileName):
    with open(fileName, "w", encoding="gb18030") as file:
        file.write(str(a))


def read_scores(fileName):
    with open(fileName, "r", encoding="gb18030") as file:
        a = file.read()
        return a


# 是否记录做题次序,如果想要记录做题次序就改为True
is_recode = True
# m是做题次数，如果作对这题m次就跳过这题，默认为3（作对是指在作答6次内回答正确）
m = 3
chooses = ["A", "B", "C", "D"]
names = ['近代史上篇测试1.csv', '近代史上篇测试2.csv', '近代史中篇测试2.csv', '近代史期中测试1.csv', '近代史期中测试2.csv', '近代史第一次平时练习.csv'
    , '1920215-202001.csv', '1920215-202002.csv', '1920215-下篇1.csv', '1920215-下篇2.csv', '1920215-中篇测试1.csv',
         '1920215-中篇测试2.csv', '1920217-期中测试1.csv', '1920217-中篇测试.csv']
if os.path.exists("score.txt"):
    scores = int(read_scores("score.txt"))
else:
    file = open("score.txt", "w")
    file.write("0")
    scores = int(read_scores("score.txt"))
data = pd.read_csv('test/' + names[0], header=None)
for name in names:
    temp = pd.read_csv('test/' + name, header=None)
    data = data.append(temp)
if is_recode:
    data["recode"] = 0
data.index = range(data.shape[0])

count = 0
while True:
    index = np.random.randint(data.shape[0])
    # 随机打乱
    data = data.sample(frac=1)
    # 做题正确超过m次就跳过
    if is_recode:
        if data.iloc[index, -1] > m:
            continue
    err = 0
    q = data.iloc[index, :]
    answer = q[2]
    print("你的分数为：", scores)
    print(q[0].strip() + q[1].strip())
    for i in range(3, 7):
        print(chooses[i - 3] + "、" + q[i].strip())
    while True:
        a = input("请输入你的选择：").upper()  # 大小写皆可
        if a == answer:
            print("yes!")
            if is_recode:
                data.iloc[index, -1] += 1
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
    count += 1
    if count%3 == 0:
        os.system('cls')
