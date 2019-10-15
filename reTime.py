###
 匹配字符串中所有时间格式的子串
  input："2lo3j4hoqilu234hpq324po2019-01-01T10:10:102ioup34ypoquhi23rp"
  output:"2019-01-01T10:10:10"
###

import re
line = "12342019-01-01T10:10:1091832yaojkwsfifh2015-12-12T23:23:23uiouewory982374uiqwhelkn,.mxcvnljhla;kdsfj;laskdjf13:05 10/14/2019ls9iwejroiu"


res2c = re.compile('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')
reslist = res2c.findall(line)
for i in reslist:
        print i
