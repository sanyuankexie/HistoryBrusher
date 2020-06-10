import re

import requests, json
import pandas as pd
from pandas import DataFrame

COOKIE = "ARK_ID=JSc39d609c5ed9e7252fea7cb0aa76d323c39d; gr_user_id=ad346c42-17f3-4e34-83b5-84e35fae592c; grwng_uid=4c759288-9d29-4468-94cf-a6c8f6d92bf1; ketangpai_home_remember=think%3A%7B%22username%22%3A%22MDAwMDAwMDAwMMdlttuGqa-whah2l7HPjZWD2m-h%22%2C%22expire%22%3A%22MDAwMDAwMDAwMLOGuZmGqb-xhc6g3LKmdZ4%22%2C%22token%22%3A%22MDAwMDAwMDAwMMurrpWavLehhs1-lLGpm9uDp4OZepuomcWmmqaMiHtnr5ylzYWosKKZq6HQxtOK0ZCme5p-q6iZu2yrn4uNhJ3KedDYk7ivboS4ipmxqZHahM2d3H96YW0%22%2C%22sign%22%3A%22e19450ca20d9c9122d62f1f6158e9c47%22%7D; PHPSESSID=nn7smcefd7nstn3olutlcu6ak0; ketangpai_home_slb=54803d03eda35e5b7af37c2f4503c680"

URL = "https://www.ketangpai.com/TestpaperApi/doSubjectList?testpaperid=MDAwMDAwMDAwMLScuZaGz79s"

FILE_NAME = "中篇测试1.csv"


def replaceOtherChar(str):
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
