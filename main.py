import requests

def main():
	url = 'https://w1.v2free.top/user/checkin'

	# headers = {
	#   'Connection': 'keep-alive',
	#   'Content-Length': '0',
	#   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
	#   'Accept': 'application/json, text/javascript, */*; q=0.01',
	#   'X-Requested-With': 'XMLHttpRequest',
	#   'sec-ch-ua-mobile': '?0',
	#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
	#   'Origin': 'https://w1.v2free.xyz',
	#   'Sec-Fetch-Site': 'same-origin',
	#   'Sec-Fetch-Mode': 'cors',
	#   'Sec-Fetch-Dest': 'empty',
	#   'Referer': 'https://w1.v2free.xyz/user',
	#   'Accept-Language': 'zh-CN,zh;q=0.9',
	#   'Cookie': '_ga=GA1.1.1097224415.1644561485; _gcl_au=1.1.1299104476.1644561485; uid=31219; email=shenjie8278%40126.com; key=772b4f245432c928abc93ac4257dbcb1b486aa43ba89d; ip=873971ac1430cbeeed56b9b0a3781c88; expire_in=1676105429; _ga_NC10VPE6SR=GS1.1.1644803702.3.0.1644803704.0; crisp-client%2Fsession%2Fa47ae3dd-53d8-4b15-afae-fb4577f7bcd0=session_625114a8-61e3-4a99-a820-2d65e0b44b67; crisp-client%2Fsocket%2Fa47ae3dd-53d8-4b15-afae-fb4577f7bcd0=0'
	# }

	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Cookie': '_ga=GA1.1.1798402011.1684397932; uid=180049; email=delawinema4664@outlook.com; key=65f45aa059d9632108f37a22d7ddb95333369afadf470; ip=1c3a096d509deaa0f16fe4f860090e9a; expire_in=1686990099; _gcl_au=1.1.118167882.1684398102; crisp-client/session/a47ae3dd-53d8-4b15-afae-fb4577f7bcd0=session_46d193e7-955e-41d3-bad6-a9c12984d2f9; _ga_NC10VPE6SR=GS1.1.1685692917.7.1.1685693752.0.0.0',
		'Host': 'w1.v2free.top',
		'Origin': 'https://w1.v2free.top/',
		'Referer': 'https://w1.v2free.top/user',
		'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'Sec-Fetch-Dest': 'document',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-Site': 'none',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
	}

	response = requests.post(url=url, data={}, headers=headers).json()
	# print(response)

	msg = response['msg']
	if response['ret'] == 1:
		msg += '剩余流量: '+str(response['trafficInfo']['unUsedTraffic'])+'.'

	return msg

def ftqq(push_message):
    requests.post(
        url="https://sctapi.ftqq.com/SCT210455TntlKaRrrnVq13rQTE5XQ8xCp.send",
        data={
            "title": "V2free自动签到脚本已执行！",
            "desp": push_message
        }
    )

if __name__ == "__main__":
	msg = main()
	# print(msg)
	ftqq(msg)
pass