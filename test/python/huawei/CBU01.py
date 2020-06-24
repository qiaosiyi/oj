#1
#12 3
#10 25 9 9 9 3 4 5 3 1 3 2


order_list = []
match_table = {}
C = 0
def lru_set(key, value): #num, num
  c_tmp = len(order_list)
  if key in match_table:
    order_list.remove(key)
  elif c_tmp == C:
    rm_key = order_list.pop()
    match_table.pop(rm_key)
    print rm_key,

  match_table[key] = value
  order_list.insert(0,key)

def lru_get(key):
  if key not in match_table:
    return None
  else:
    order_list.remove(key)
    order_list.insert(0,key)
    return match_table[key]

T = input()
for i in range(T):
  m = 0
  n = 0
  tmp = raw_input()
  tmp = tmp.split()
  m = tmp[0]
  n = tmp[1]
  tmp = raw_input()
  page_num = tmp.split()
  C = int(n) #set capacity
  order_list = [] #reset
  match_table = {} #reset
  for j in page_num:
    if lru_get(j) == None:
      lru_set(j,1)
  print












