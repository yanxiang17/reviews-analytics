# 留言分析

import time
import progressbar

data = []
count1 = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip()) #每個清單元素(line)是字串，含有空白，去掉'\n'字元        
        count1 += 1
        bar.update(count1)        
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

# 文字計數

start_time = time.time()
wc = {}
count2 = 0
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    count2 += 1
    bar.update(count2)

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word] )
end_time = time.time()

print('花了', end_time - start_time, 'seconds')
print(len(wc))

while(True):
    word = input('請問你想查什麼字： ')
    if word == 'q':        
        break
    elif word in wc:
        print(word, '出現的次數為： ', wc[word])
    else:
        print(word, '這個字沒有出現過喔!')
print('感謝使用本產品!')
