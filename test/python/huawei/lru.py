# coding=UTF-8
# 实现LRU算法，设置list 和 dict， list中存储key，按照最近使用的顺序从0到高位排序，
# dict中存储 key value 查找表， 
# 插入key value，包括更新和重置
# 查询key

order_list = []
match_table = {}
C = 5

def lru_set(key, value): #num, num
  c_tmp = len(order_list)

  if key in match_table:
    order_list.remove(key)
  elif c_tmp == C:
    rm_key = order_list.pop()
    match_table.pop(rm_key)
  
  match_table[key] = value
  order_list.insert(0,key)


def lru_get(key):
  if key not in match_table:
    return None
  else:
    order_list.remove(key)
    order_list.insert(0,key)
    return match_table[key]


for i in range(5,10):
    lru_set(i,10*i)

print match_table, order_list 

lru_get(5)
lru_get(7)

print match_table, order_list

lru_set(10,100)
print match_table, order_list

lru_set(9,44)
print match_table, order_list