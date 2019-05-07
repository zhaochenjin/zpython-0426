# # 1.读取一个文本文件的前 N 行
with open('d:/新建文本文档.txt', encoding='utf-8') as f:
    for line in range(5):
        print(f.readline().strip())
print(".........................")

# 2.按行读取一个文件，把每行内容存入一个 list
result=[]
with open('d:/新建文本文档.txt', encoding='utf-8') as f:
    for line in f:
        result.append(list(line.strip('\n').split(',')))
print(result)

# with open('d:/新建文本文档.txt', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line.strip())
print(".........................")

# 3. 查询一篇英文文章的最长单词
lst=['hello','hi','interent','boring']
w=sorted(lst, key=lambda x: len(x))[-1]
print(w)
print(".........................")

# 4. 找出一片英文文章的最高频单词
d={'hello': 2, 'hi': 4, 'interesting': 1, 'love' : 3}
p={key:d[key] for key in sorted(d,key=lambda x:d[x],reverse=True)[:1]}
print(p)