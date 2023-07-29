import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://iftp.chinamoney.com.cn/english/bdInfo/"

# 发起网络请求
response = requests.get(url)
if response.status_code != 200:
    print("无法访问链接页面")
    exit()

# 解析HTML数据
soup = BeautifulSoup(response.content, 'html.parser')

# 筛选满足条件的数据并提取所需的列
data = {
    'ISIN': [],
    'Bond Code': [],
    'Issuer': [],
    'Bond Type': [],
    'Issue Date': [],
    'Latest Rating': []
}

table = soup.find('table')
if table is not None:
    rows = table.find_all('tr')
    for row in rows[1:]:  # 跳过表头
        columns = row.find_all('td')
        if len(columns) == 6:
            isin = columns[0].text.strip()
            bond_code = columns[1].text.strip()
            issuer = columns[2].text.strip()
            bond_type = columns[3].text.strip()
            issue_date = columns[4].text.strip()
            latest_rating = columns[5].text.strip()

            if bond_type == "Treasury Bond" and "2023" in issue_date:
                data['ISIN'].append(isin)
                data['Bond Code'].append(bond_code)
                data['Issuer'].append(issuer)
                data['Bond Type'].append(bond_type)
                data['Issue Date'].append(issue_date)
                data['Latest Rating'].append(latest_rating)

# 将数据保存为CSV文件
df = pd.DataFrame(data)
df.to_csv('treasury_bonds_2023.csv', index=False, encoding='utf-8')
