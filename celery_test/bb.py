import sys
import os
# 得到当前根目录
o_path = os.getcwd()
sys.path.append(o_path)
print(o_path)
from base import aa
aa.nihao()


