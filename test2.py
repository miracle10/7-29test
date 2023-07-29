import pandas as pd

# 读取数据文件
data = pd.read_csv("fyx_chinamoney.csv",header=None)

# 获取数据列表
code_list = data[0].tolist()
print(len(code_list))

batch_size = 80

for i in range(0, len(code_list), batch_size):
    batch = code_list[i:i+batch_size]
    print(batch)



