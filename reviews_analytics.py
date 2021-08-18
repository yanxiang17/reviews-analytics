# 留言分析

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip()) 
		#每個清單元素(line)是字串，含有空白，去掉'\n'字元
		count += 1
		if count % 100000  == 0:
			print(len(data))
print('總共有', len(data), '筆留言。')

sum_len = 0			
for d in data:
	sum_len += len(d)
print('留言的總長度有', sum_len, '個字元(含空白)。')
print('每筆留言的平均長度是', sum_len/len(data), '。')

small_100 = []
for d in data:
	if len(d) < 100:
		small_100.append(d)
print('一共有',len(small_100), '筆留言長度小於100個字元。')
print(small_100[0])