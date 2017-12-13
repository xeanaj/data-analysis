from collections import Counter
from konlpy.tag import Twitter
import pytagcloud

removeNounList = ['오늘', '우리', '지금', '저희', '당시', '모두', '이번', '기사']
# 단어 제외 및 글자 길이 1이상만 
def removeNounsInTheList(countData) :
	resultList = []
	for item in countData :
		if (item not in removeNounList and len(item) > 1) :
			resultList.append(item)
	return resultList


FileName = "jtbcnews_message_2017-12-06_2016-12-08.txt"
data = open(FileName, 'r').read()
nlp = Twitter()
nouns = nlp.nouns(data)
removedNouns = removeNounsInTheList(nouns)

count = Counter(removedNouns)

common_nouns = count.most_common(200)

print(common_nouns)

#maxsize는 글자크기 옵션
taglist = pytagcloud.make_tags(common_nouns, maxsize=100)
pytagcloud.create_tag_image(taglist, 'jtbcnews_wordcloud.jpg', size=(600,600), fontname="korean", rectangular=False)

