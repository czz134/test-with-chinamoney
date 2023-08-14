import requests
import pandas as pd
##测试1
# 定义函数以获取中国货币网站上的债券信息
def fetch_chinamoney_data(page):
    # 请求的 URL
    url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
    # 请求头
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Cache-Control': 'no-cache',
               'Connection': 'keep-alive', 'Content-Length': '119',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Cookie': 'apache=bbfde8c184f3e1c6074ffab28a313c87; _ulta_id.ECM-Prod.ccc4=239c8a7687969c49; _ulta_ses.ECM-Prod.ccc4=0af4a16f13049b17; AlteonP10=ARzTSSw/F6ys3TYpPRm3aQ$$',
               'Host': 'iftp.chinamoney.com.cn', 'Origin': 'https://iftp.chinamoney.com.cn', 'Pragma': 'no-cache',
               'Referer': 'https://iftp.chinamoney.com.cn/english/bdInfo/', 'Sec-Fetch-Dest': 'empty',
               'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.28',
               'X-Requested-With': 'XMLHttpRequest',
               'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
               'sec-ch-ua-mobile': '?0'}
    # 请求的数据
    data = {'pageNo': str(page), 'pageSize': '15', 'isin': '', 'bondCode': '', 'issueEnty': '', 'bondType': '100001',
            'couponType': '', 'issueYear': '2023', 'rtngShrt': '', 'bondSpclPrjctVrty': ''}

    # 发出请求
    res = requests.post(url, headers=headers, data=data)
    # 处理响应的结果
    result = []
    for item in res.json()['data']['resultList']:
        item_dict = {
            'ISIN': item['isin'],
            'Bond Code': item['bondCode'],
            'Issuer': item['entyFullName'],
            'Bond Type': item['bondType'],
            'Issue Date': item['issueEndDate'],
            'Latest Rating': item['debtRtng'],
        }
        result.append(item_dict)
    # 返回结果
    return result

# 主函数
if __name__ == '__main__':
    data_list = []
    # 遍历五页数据
    for page in range(1, 6):
        print(f"正在获取第 {page} 页数据")
        data_list.extend(fetch_chinamoney_data(page))
        print(f"第 {page} 页数据获取完毕")
    # 转换为 pandas DataFrame
    df = pd.DataFrame(data_list)
    # 将 DataFrame 写入 CSV 文件
    df.to_csv('output.csv', index=False)
    
    ##测试2
    import pandas as pd

    data = pd.read_csv('D:/BaiduNetdiskDownload/google/fyx_chinamoney.csv')
    batch_size = 80
    data_batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

    # 打印输出每个批次的数据数组
    for idx, batch in enumerate(data_batches):
        print(f"Batch {idx + 1}:")
        print(batch)
        print("-" * 40)
