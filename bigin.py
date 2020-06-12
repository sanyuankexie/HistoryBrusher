import pandas as pd
import numpy as np
import random
import os


def recode_num(a, fileName):
    with open(fileName, "w", encoding="gb18030") as file:
        file.write(str(a))


def read_scores(fileName):
    with open(fileName, "r", encoding="gb18030") as file:
        a = file.read()
        return a
# 获得答案
def get_answer(answer, choose_index):
    result = ""
    answer_ = {"A": 3, "B": 4, "C": 5, "D": 6}
    ture_answer = {"0": "A", "1": "B", "2": "C", "3": "D"}
    for i in answer:
        index = answer_[i]
        result += ture_answer[str(choose_index.index(index))]
    list_result = list(result)
    list_result.sort()
    result = "".join(list_result)
    return result
    
def writeInToExecl(title, theType, answer, optionList):
    theDict = {'题目': title, '类型': theType, '答案': answer, '选项A': optionList[0], '选项B': optionList[1],
               '选项C': optionList[2], '选项D': optionList[3], }
    df = pd.DataFrame(theDict, index=[0])
    df.to_csv('错题.csv', index=False, header=0, mode='a', encoding="utf_8_sig")


# 是否记录做题次序,如果想要记录做题次序就改为True
is_recode = True
# m是做题次数，如果作对这题m次就跳过这题，默认为3（作对是指在作答6次内回答正确）
m = 3
chooses = ["A", "B", "C", "D"]
names = ['近代史上篇测试1.csv', '近代史上篇测试2.csv', '近代史中篇测试2.csv', '近代史期中测试1.csv', '近代史期中测试2.csv', '近代史第一次平时练习.csv'
    , '1920215-202001.csv', '1920215-202002.csv', '1920215-下篇1.csv', '1920215-下篇2.csv', '1920215-中篇测试1.csv',
         '1920215-中篇测试2.csv', '1920217-期中测试1.csv', '1920217-中篇测试.csv']
         
mode = input("""
####################################################
                                                                +          
        +++  欢迎来到近代史无限刷  +++                    +   ++++++                                               
        +++  请选择模式:         +++                    +++     +            
        +++  1. 闯关模式         +++                      +  +  +          
        +++  2. 复习错题模式      +++                     +     +
                                                        ++++++++++++++++                   
####################################################

""")

if mode == '1':
    names = ['近代史上篇测试1.csv', '近代史上篇测试2.csv', '近代史中篇测试2.csv', '近代史期中测试1.csv', '近代史期中测试2.csv', '近代史第一次平时练习.csv'
        , '1920215-202001.csv', '1920215-202002.csv', '1920215-下篇1.csv', '1920215-下篇2.csv', '1920215-中篇测试1.csv',
             '1920215-中篇测试2.csv', '1920217-期中测试1.csv']
elif mode == '2':
    names = ['错题.csv']
os.system('cls')
print("""
        +++  开启你的刷题生涯吧！  +++
    """)
if os.path.exists("score.txt"):
    scores = int(read_scores("score.txt"))
else:
    file = open("score.txt", "w")
    file.write("0")
    scores = 0
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
    # 随机打乱选项
    chooses_index = [3, 4, 5, 6]
    random.shuffle(chooses_index)
    answer = get_answer(answer, chooses_index)
    # 加了括号
    for i, j in zip(chooses_index, chooses):
        print("【", j, "】" + q[i].strip())
        k = 0
    flag = 0
    while True:
        a = input("请输入你的选择：").upper()
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
            if err >= 4:
                print(answer)
                print("\n")
                break
        k += 1
        if k >= 3 and flag == 0:
            answer_list = [q[3].strip(), q[4].strip(), q[5].strip(), q[6].strip()]
            writeInToExecl(q[0].strip(), q[1].strip(), answer, answer_list)
            flag = 1
    count += 1
    if count%3 == 0:
        os.system('pause')
        os.system('cls')
