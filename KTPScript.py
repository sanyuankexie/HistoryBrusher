import re

import requests, json
import pandas as pd
from pandas import DataFrame

COOKIE = "XXXX"
URL = "https://www.ketangpai.com/TestpaperApi/doSubjectList?testpaperid=XXXX"
FILE_NAME = "XXXX.csv"


def replaceOtherChar(str):
    """
    过滤杂余字符
    :param str:
    :return:
    """
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', str)

    return dd.replace("&nbsp;", " ")


def writeInToExecl(title, theType, answer, optionList):
    title = replaceOtherChar(title)
    if theType == '4':
        return

    answerList = list()
    # 单选
    if theType == '2':
        theType = '单选'
        for i in range(0, 4):
            option = optionList[i]
            answerList.append(replaceOtherChar(option['title']))
            if option['id'] == answer:
                answer = chr(65 + i)

    # 多选

    if theType == '3':
        theType = '多选'
        correctList = answer.split('|')
        for i in range(0, 4):
            option = optionList[i]
            answerList.append(replaceOtherChar(option['title']))

        answer = ''
        for correct in correctList:
            for i in range(0, 4):
                if correct == optionList[i]['id']:
                    # answer = answer.join(chr(65 + i))
                    answer = answer + chr(65 + i)

    theDict = {'题目': title, '类型': theType, '答案': answer, '选项A': answerList[0], '选项B': answerList[1],
               '选项C': answerList[2], '选项D': answerList[3], }
    df = pd.DataFrame(theDict, index=[0])
    df.to_csv(FILE_NAME, index=False, header=0, mode='a', encoding="utf_8_sig")

    def Compare():
        pass


if __name__ == '__main__':
    try:
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        cookie = {'key': 'value'}

        the = COOKIE.split('; ', 4)
        for i in the:
            thec = i.split("=", 2)
            cookie[thec[0]] = thec[1]

        r = requests.get(URL, headers=header, cookies=cookie)
        subjectList = json.loads(r.text)['lists']
        for subject in subjectList:
            # print(subject)
            writeInToExecl(subject['title'], subject['type'], subject['answer'], subject['optionList'])
    except Exception as e:
        print("有问题请及时联系某某某")
        print(e)

