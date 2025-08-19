import requests

cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'www.roblox.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/id/NewLogin',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'identifier': 'Ermomhot',
}

response = requests.get(
    'https://www.roblox.com/login/forgot-password-or-username',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'RBXcb': 'RBXViralAcquisition%3Dtrue%26RBXSource%3Dtrue%26GoogleAnalytics%3Dtrue',
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'www.roblox.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'RBXcb=RBXViralAcquisition%3Dtrue%26RBXSource%3Dtrue%26GoogleAnalytics%3Dtrue; rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/id/NewLogin',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'identifier': 'Ermomhot',
}

response = requests.get(
    'https://www.roblox.com/id/login/forgot-password-or-username',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'pageHeartbeat',
    'ctx': 'heartbeat2',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:03.422Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'pageHeartbeat',
    'ctx': 'heartbeat3',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:23.443Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'username',
    'aType': 'focus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:40.579Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'username',
    'aType': 'offFocus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:46.925Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'password',
    'aType': 'focus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:46.934Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'WebsiteLogin_Attempt',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'WebsiteLogin_FirstAttempt',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'password',
    'aType': 'offFocus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:48.255Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'loginSubmit',
    'aType': 'click',
    'evt': 'formInteraction',
    'ctx': 'loginPage',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:48.269Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'WebsiteLogin_Attempt',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'WebsiteLogin_FirstAttempt',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/rotating-client-service/v1/metadata', cookies=cookies, headers=headers)


headers = {
    'authority': 'images.rbxcdn.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://css.rbxcdn.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://images.rbxcdn.com/059b09408c6b199c.gif', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/hba-service/v1/getServerNonce', cookies=cookies, headers=headers)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'open-connection',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"open-connection"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'transaction-upgrade-objstore-creation',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"transaction-upgrade-objstore-creation"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'connection-initial-transaction',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"connection-initial-transaction"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'connection',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"connection"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'transaction-get',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"transaction-get"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'transaction-get-complete',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"transaction-get-complete"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'transaction-put',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"transaction-put"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'auth.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'content-type,x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options('https://auth.roblox.com/v2/login', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'saiCreated',
    'ctx': 'hba',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:49.531Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'ctype': 'Username',
    'cvalue': 'LfsmmsfL',
    'password': 'dfsm230203',
    'secureAuthenticationIntent': {
        'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==',
        'clientEpochTimestamp': 1755625009,
        'serverNonce': 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTMxMCwiaWF0IjoxNzU1NjI1MDEwLCJuYmYiOjE3NTU2MjUwMTAsIm5vbmNlIjoiSzNIVEQ3S000RjlZOVk3WCJ9.8bFgXgbBL_ib-bv93rCn-w1PqMS1OoCwwbxQySopaa0',
        'saiSignature': 'n474tTSf7ADCROdMdvP50JIdsAq7mPiaLA9hrrywSD/ELcmIX0bHIKGObAT7FLzwyMVLNnaBA8lGGDoGjU9ljg==',
    },
}

response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"ctype":"Username","cvalue":"LfsmmsfL","password":"dfsm230203","secureAuthenticationIntent":{"clientPublicKey":"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==","clientEpochTimestamp":1755625009,"serverNonce":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTMxMCwiaWF0IjoxNzU1NjI1MDEwLCJuYmYiOjE3NTU2MjUwMTAsIm5vbmNlIjoiSzNIVEQ3S000RjlZOVk3WCJ9.8bFgXgbBL_ib-bv93rCn-w1PqMS1OoCwwbxQySopaa0","saiSignature":"n474tTSf7ADCROdMdvP50JIdsAq7mPiaLA9hrrywSD/ELcmIX0bHIKGObAT7FLzwyMVLNnaBA8lGGDoGjU9ljg=="}}'
#response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'transaction-put-complete',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"transaction-put-complete"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.rbxcdn.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.rbxcdn.com/captcha/v1/metadata', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'name': 'event_generic',
    'value': 1,
    'labelValues': {
        'event_type': 'Success',
        'challenge_type': 'captcha',
    },
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_generic","value":1,"labelValues":{"event_type":"Success","challenge_type":"captcha"}}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'LoginFunCaptcha_Triggered',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2//api.js', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Triggered',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Triggered',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Triggered","application_type":"unknown","version":"UseLightboxModal"},"identifier":"b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/api.js',
    cookies=cookies,
    headers=headers,
)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/settings', headers=headers)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

data = '{"id":"fa301511-2551-4bf9-b8c0-acc0b31bafcc","publicKey":"476068BF-9607-4799-B53D-966BE98E2B81","isKeyless":false,"capiVersion":"3.7.0","mode":"lightbox","suppressed":false,"device":{"platform":"Linux armv81","language":"id-ID","connection":{"effectiveType":"3g","rtt":450,"downlink":1.35}},"error":{},"windowError":{},"sessionId":null,"performance":{"error":"Cannot read properties of undefined (reading \'duration\')"},"locationOrigin":"https://www.roblox.com","locationPathname":"/id/NewLogin","timers":{"onReady":{"start":1755625012078,"end":1755625012734,"diff":656,"metrics":{"apiExecute":{"start":1755625012072,"end":1755625012075,"diff":3},"settingsLoad":{"start":1755625012081,"end":1755625012728,"diff":647,"info":{"requestId":null}},"initFPCollection":{"start":1755625012089,"end":1755625012733,"diff":644},"fpProcessing":{"start":1755625012733,"end":1755625012734,"diff":1}}}},"sampled":true}'

response = requests.post('https://arkoselabs.roblox.com/metrics/ui', headers=headers, data=data)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'LoginFunCaptcha_Initialized',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Initialized',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Initialized',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Initialized","application_type":"unknown","version":"UseLightboxModal"},"identifier":"b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-ark-esync-value',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options(
    'https://arkoselabs.roblox.com/fc/gt2/public_key/476068BF-9607-4799-B53D-966BE98E2B81',
    headers=headers,
)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-ark-esync-value': '1755604800',
}

data = 'public_key=476068BF-9607-4799-B53D-966BE98E2B81&capi_version=3.7.0&capi_mode=lightbox&style_theme=default&rnd=0.9489139684461205&bda=eyJjdCI6IjBUTitLNnZsSmhhbmw3VzA2RmVUS2FITnFxN09XR3BjSmZZM2J5eEYyWXJBbkRTZGlWWm5HaUJ0Z0djVzhaVDZVeDMrQ0l5elNQS0RkdnpvZUdhZ283REJwM0M2M09VdlNkN3c2Q0hPTW01Z0RzbjdFczVZditwVzVIVTdQN3BHVkl5VzBiSEovT2xsMUlxVGZ0ZkxGaGVXVG10aFdZSlFod1dIK0VOcmdoTEsyQ2c3a2JRZ3h3SkxNank3S2FuK3l5RnY1Z1VXM05tSG5XaGpGV3AwUi9RZTBVaGMxaE9rdE5NMWw4bjdzQjRTUEtPUXRaL3BpN0cxcTVmVVZzbEpIUm92MmpRU0NRbmtnUkdlWnlOeWp6UkpBMXByYlNpZ2VnazFtVFpwaVhKSHJkdW55NGZRdHBySHhhblhCTGNXcDV5M2lwcStscDZmYkpKRXJYeXBzWS8wZXJoQzBYNU9LOFFWaTNVdGQxV2thY3VPb2VkNXdrZzViREVpWWQvNW5EUnNsQ1RMVlgxM3hLdVFjdmxRblhETmtIMTJPUkp3S2xpRG1LaHRpb3NIbGVzL0xkcGVTbFFQdDFYbWl5R2dkUkhkaVk3YnA3dDNRTXFja054LzlIdXNPb0E2SXFHYThVWG9mNlR4M1ZhY1pXcUZjOE4xRnl3dGZzM0k0VXNQeTVsOTRUejc5NEh5c1pwZHFDSEtQU0pWcDFzcW81SWpiK2lnZk5OZHZoVUJacHBIMXBGc3VCZTZVMFlrdEp3NHdKS1hPZ3k5UDdaWE94Zzl1TWpzMyt3eUwrczk5OWNnTi9mR1FBbGNHVldNWGFPM1UvVWdnWmE2anlUQnZ0QXkyZWhtWHR5aDNudHZoT1gzNHdZYzB2UWtFL1RnT3c1TUxjOVV0ZTNETUc1QWEyWTV6VWxpM1JEdkpWc3J6UW5MempHQUt0UkVzMm1XSTAyMHJ0a05ZQ0pFSnpWbHd3WFh6YzdUNUhNNnFBQmFxVVEzKytwTHliSXAwaFh5MnZHWUZsTDhST3c4YkVrcG1WRWFORCt4eHF5c3VPU05HOUR3aXBuTTBEMHN4VlJEYklQSVdxM1dxelphcisyU3JwdTZaUVhpM04vMHMraDR3NHlvOC9wYzNYUTdUdHZWa1ZMM1p1ejVzRktlQzRIMTFnWFI1Vmo1ekFCb25Nd2pJRmw1d1A4UWRENXc2aW9NMUdFOHlrZlBOMUd0SmcxSnk0UzlnV05XUkh2cFFoWllYQlkyU2tNSlltM1doaDZ5T25oRVo5RDNQc1hoVXYyd1BxS3VDMSsxTmhkdmx4OUZYc3hzVUJDZjAxdEREWk1YYVU2cFZxWGhmVElleVB3bG1rb3RSaDlVcXYrWE5tWGR2czQrT0VYckEyeG40N25lZHFsVmlNbjlWelVpY3Q2L0ROdnoxZk10aXNDZVBBZmliMmNncmRMcnNySnpqcXBvZnZzZTJ2M0I1ekVvYUw0RFRhdW54TVR4b3hvamNCc2IvbFZvQmlzWEluTjkrQW9lV3ArSTNNSTBOblhSd0FvdzlKZk5YeHl0cC9TQkVmbnpVaU9WbjlyQjZtRVFUejNzbGE0Q3prTzFic3JuY2tqQjFIZGFEa0U1a3FXYXEzYXJ1N2s4bVZ1QUhXbzU4YW5JTFk0VVl4VkM2SkJaUzFNdlhGOEN6cm9kNlg1c2ozcGFmT3MxWDR1M2RBVlM4VERNejFNVmZwTXk4dXBmVGUvUzZyN3JmeHdDdnIrNld5N0h1ZmZ6b1dQV1FEbFREVDRKeVUyWDYrelcvemhwZWRXQ1c2UGFvb0hBRUl0Zy9qTDBzZytSbnZGVy9mTkZmT1JnNERYbk80TndFdC8zZzY2VFIvemx6aUFWcktmM1hIRXJvVHJBRWt1WjdJSEE1TXV6R1puSEVoeE1wY2diSjltekJ3UElHZmRJZUVjc3Zib3JwcTRRc0VucU5vcks4ZDd3STJHV2JZNEY5WWFRc3NtRGFIakhFcy9WZE1NT1I0TldOODJzYnlVOW9YT3lCKzI3eXdvbG1ZZzdjWlJiTFBBN0l1RWMwa0k2ZmRWcVBSMytWSnV5ZUR4SFJZekRmazRKb2NheVlTMGRTZlJGaDBqSnJLaVViODhzN09IOHI2V3AzclREOTg0VG5mcTBpTXdnUGFxSDZvVXArckdzTnpsbXRHTExEWnVZOHEzL0k0OGJCT295OHpRRzhDRXJITC9EVG9RTHNSZW5wSmxDaDVCbHdpRjRjbnlrdm5BVDZVNWtyd3pSei9EZjVRajFCWWpuR2M3TlA1K1Zhd2lIaHZwNzcxMi82dVE5L2crTXJBVXpBRzU1VTlHOEphb0dPTFF5R3BJTlcwdm1LZnlYY3dVZytVek16Y3gvT1FwNXBwRjdrZTA4OHBjc0pIYmdvS1Z6dmdwUDZ2YWxFUXcxeFBPRVJRckp0bkQvczlVRTM4K2tmbUlVTTZYcWxmU3lrS0hZUHNCQ2lEbUFqRkt4SlpXOERRTjhKMHJzRTM2eXRXMm45Q2FBa3VTL1JUSlR3N05KYmZtRFBjb0ViL3gwR244Nm81QlNyd3FTVTZtSFdlK2RiTkVjVEVOc1Q1ckxZMGoyNHlIQ1J1M25tbCtjNXRhcHc2Sjd6MU9sWkpXWld6YWN6VmNqTDFnVmRtTzMzb3JqVVNyN2FHVmpwOGFUU25pYkVWeVpJcldGVEpjSEJsbnJkRkpjdGlFNHRiZFF3OVlKOEVHeE5xNVhCVlY1dDF4WTZzT3RGMjV0ZkxDeU9NMmJzbzFHOXFDUWpNUWMxL25EMC9pb0lqNmxRK3ZQQkpEeTBKeTM0ZzNTZzkydVkxRFo0NFZCUFM5bjlQcHRoT00rWFk5OGlZVyt6SWdEMzVNbmkyb2M1VEEvQXhVYTNIU1pNY2ttTnJhZzZNaGc5RzFVQ0cvYU94aHE5dEI0M0VDdmE4dkZGODkrUUxZU2tsNG4ybFZaR09EaSs2SksxcUdITHFnU05KWlFLVkRLVElQakM5RkVpWjhyTElMdVBLTlJqb0I5Z01ZaU1CR1N2aUhMbDhlektneE9EYkVCN25MUUwzbjJwTE9idWN4Y0xTc0Z5aU1VdHc2UlZkTXhDNk9WbkMwcDRmT0dubVo4Z0thclJQUjM1ck91LytNZUhvUDlVNitMYm5BTXJJWlE0NW1vRjJWM0JqK3hQcFJqckFib0VMaW5ZZ1dsVFhKY2trMktGemY5Q0R0YVVqeXZIQXUrVlRJZytjYzJiTG1ubWFkK21VY0htTktjbmRYVkRwVTE1clBPM2NyZVZDYjA1WE9IWTAyUng0QVlrcG1OSmcwSGZKSjcyTG0wU2dOWmdTQWYrM1UzMTkxRnVzMFhLWG9UU2lEcC9WWnUvano4UUpwRytYVnRJeU5kM2tnVXFrY0hQZXJLcHA4czJ5Rlg5b3ZrNk9FVGJ4SVdOZ3dialZwVUFxM1ZycDBxSUdqVGhHQlNhYncwaTdONXNBWkhOQ0tzWmxKUTBuc29hVUQ3YkxNRmh1U2tZQVVaTmZOSUpJVUMrMVUvWkdzOFRXYWVJekhFZGZUT1ZRcjRhcGxJWWM0NlVabzhnVVVnL1l6NGw4bThDSWJoRnZqOEV6RERBSXNzMUV4U05KdkRQZzc5MjR5dXo0bkp2QjNLOXhBczQwdTArYzNEM3dNSWN3TklsbjVaN0I4QUp3M3VWZzRHcEI0VW5oRjZ2N2xpSFBnV3dBbFhIUno4T0szdXVRaFFOclVwYTFjZUltdm50NlkwNFNLZ0RwVi8vbS9pMm93WGJkZTAwRUhrS0VlWkdjbWpnQzRmd2ROcmhvd0xPWXdGWmtuTlc3TmI3S0htL29KTFM2dlAxOWFVMThDNTh4NmVHOUhtYlNsRXZjK2JXUzBOU0xERXRnOURRK3VPTFJOQWUzY1dQaFU1cHhMd3VmNGV1ZlRKaVhTbzI3MlVKVnhSS3R3TUNFSVkySWtkWkJyNW1yQUJPVWpaRmt6Z2ZFTkp2bTM3Z0ZoV3piNTVQOXhmZ0kvZUJQOEgrZUpNNXlIZ3pndGdIOWRqSEFscFFKVFdYbldwZXNDcDR6OThvdjJZNEdXZTBpS3paVjNoZDBQNUF3eGRPY1hYVFNHRzcvNnlEWEU2SXltS3diS09XaWdZQ0ZKcytaNGJXem1Xb3ZBcytoOG5Ca3lsVFRlOWVrdGl2OUxFTmJvOEJlaTBsQXRmeDZWdFp2T21xSjNydlNMaVlEZHkvR0xuZ1AvN1g2Z1R6dXRVMmdXVzVmNDdqb2JpMDV3YS83d0NNWGZhNkRaWVh1cExleVppLzVNR0d3MGMrc3pYY3hsVUZlaHBhOFA5ZC82YVBDVjBMTjY0ZzlBQWFNRThZb09LQWlWYjFPcUxTVFpoK21OR1ByVHdadlFUYzFUWG5jZFltTWN1Q3FiWmNoMWx2T2xGdjV4S2N1YTlOMTRqNlRQRTRWeEFSajd1S3N4UEVvQ01hSXdWbkRUOHFOZjlKaStuaHd1eU9QbU41NHdpdm1JempyQ3Rrd2lYTHlSVkJwOEV0R0oxekpJVVJFR25FNGhiSEhXNlFjS3ZNZ1J3TTZMYTVJa0dnWUVOTjVHL3VjWFd1QXJ1NzhYUVhEeUNsQ1NURGVLYno1MERSdnFOUHpyZzZSZTAvdEJUR25MS0o4UkZmMHFJdmR1UVVVcE8rUXR0MVZDbzFaZXFHRkYzRHVsSHdZUHZTZUhRTW1ZVzhXSkdEQ3FoWjZJaUhjTThINzdmanBPNCtoS2Rsc3plZGs2dy9QdWtMYVNBeDltZVdqaVlHeEJBay9qOGpubmo1U3ltNUxzdkVsU2RxenlmdDZCdTZ3OVh3N3BjdHNEb2RoOFgzV2g1SG54L1h4d3pRQmpoUytnc3U3bGVlSUNUd0xLRWFra1lUck1FN1A1QzFTdENLeDhUeEltWEkxUW00bUZoNC9xdmhnMWN2NWhCTDEyYnVkaFZaZXlIQkhxK3ZkbGVPTlpDazQ4SjlxWGVSRUlHY1FISVdtZ2prRlN5VSt6MDkvVVVNVUk3bThuUS80dzdqdGl1ajQwNlNUUjF2WWxrcXNEUVQwOHBtdkF1RllJNHlrdURIL1NMcVo2N3lyQzZEdkJWc2Z6SnlTUjN5cmhGVHRDc2VtN2srNUFYejVRUlJ1VFVFMlhMQmlkdjRkQStUUHAxTEFrVTkreWtkdFdJVnh1dW9janNFVkliZmhIdGxTME1zUEtvY3lmdGtmWll0cVV2SjhXSnJrWDVmRzRvRmppUDdIVnNxclpMc0RBeDRreDBtT0VQeHVJTUJON3lCRUIxbWxCR2dUSjJYVE5IbkNPMG93dWxBL2RBbENHcTQzOTVOT2NFZm91TTNHQUFxNytPdnlIRytmaDJmQXh6TWQ4Yi9pdzBzQmE1cStOa2RmQ25FQUR3dmt4b2p1NnFMNXlRakhyQmFOcFFnN2RFN0JpQ1BQS1RsRk1KeUxkYmRvaWluNFR4Sy9mQks0bHhVQk5GVkEvVitrNldCMGZFSkI3cHduRFF3eXB5eHVsT28zNnUwejFtaXE2MGVmQktHaFpvVWpUYUdwSzU3Y3gzZkpPd0t2K2liRURDQW9HVFk2UkVhVThKNk96MmdRQW9hV1NsdUl1T09DdVBEejFPZUdDZFNGVXIwQVBjbFdObzNIVFAwcld1RFdMVzNwaS8xWmRGR2piSmYvMFlHdVZHOGNQYlZHUmxadmVLc1pMQTQrcUhhVDVFTlViaVhhUnhXODA3MG9UUVBYcVYrbnZCMmtuT1h6dDMzYzlCenI0UVRmWFNFQXZ5ckVEK0twZVpBSFRnRXF1bnhhOW0wcDZWejlZNlhqdHc3Q2RRbWhDR2pCTUpNcjhRSlBGY293TitvVDBMdjlDcmFaVnp5c0M1Z2RyMjNBY1p6cGRIdXBpOVpRejRJSTBXRE1wQlZGb0UvQ0pvb1hIUnE1Y3ZscVhIOU16dTNEVWpxbHp4S3k3bHhvUHlJSGo0NnU5cERMOUsrdDR5SHFabjBwWmhwTy9kQjJtREIzZUhmb0o5STVtV3NuWExlK3FOUE5ZZ1pZUzhlTjZXK2hDRWgwc0hrUi9zWHhoVUN1cHNSYjdyNDdEY2ZBcXFsb012eTZMSklxYlpNUzNlTnhWUHVGTmNkQTBjV2lmWTdibnlpWWREeTFSTG9mQlpsN2FEejF5T2pmd0Vwb1NqUUxKWUpTUy9BdVd3OS9LeVpINlhwbGJVN0lGK3J5anZ2YlBwa0NIWkF0WUFBZHlhdlV2MXZSRWJTZGVGd3RtNnlNVS9xRUxkMm1nQVBqKzljRlZTQk5STCtHSnBIbUsyNWR6Q0ErbCtESXlMTkxKVnVtR3hvOElnRllIS3FmRElqSDdRZTFzc2FVNitmZHA0QTROcEtDY0ViU3Z5SnlvVlRiRkdsalZRSW9DY1M0eU1lZjdxQitRYXdDVDA2ZGpEczJ3WFdqcHZTRHRIeHp4YTBKZmRCeG9ma0JZeUlaS1R6NXN1cG1NSkpwLzU2Yk41TFZPK2dSU05WVCtFU0JzRzRVTXhlTW5KT1FIelphR0pwR0VzeVh1cFZXZjJLT0VvR1Z1cWdFR21zK3MrRXJxYjNCalY0UFh6N205SFg4KytGQVowY1E2eHJrSXU4OWp0UWJMdlRFK3RiOXJPYlpNRkluMmNZYVg3WHNhMDR3R05zVUIzQ3RFRkd2bEJOTGhIanpsNDZ0cUJMRWdvUWVMNHM2dVg3Y2E4Vld1bDJaQTBPMEVlSFNiMXlxamc3VlgvMEoxcy9jblppRFZ0MU1oMisxS09qbU10dVRvUTlYZWJ4WkhXZlJQWG5WTzhCaTN2ZTB0dm1VNG85dC9MM2c1b2tjS0liUWVUVjc3bXhSN3QwZVFIaHZOQXc0OTUvbldtMUYvZExJR1ZTQjBiYjcycHl4SzZUNklla1RLMlcrTWF0YkJOWEU4SUZoNWVIR3NTdHVWTlg5UUlVTHA0QkhnTWV3SUsrb09kOTZRTlV4YWRoanpsOFFwS3daWDJYTWFCekYzVU10MlNzQzBjMnpHNjBaV0Z5alZtM01tWndRWVh2NGR0b1UwUC9uWjUyd1NXYWxuR3hCVEhyQ0syei9lRVJlUlBqakIyWlhxVkFFK2VoS0s5MkpsUm1vS1g0K3hJVWVTLzRwdnJzTWIzWlB1bUlSUGdmWDRzcS9WbGZnQzMwYk92MlV1d25lTkJxNnRoVGdCQTZrT2haNmExSVZxb1ZiMFBuK2FnZGJiYTFFbFhZQnJaNlJEQ3RRZXEvMVYzb2t5OTUxTFEzRW1HSnRTWEVmS0sxUkdYems3QnJ3eWRWSS84cGllbUtNdlRMN21GWnVwNzgrV05ORkN4YldEVGFwUmdObXZNVGNlK1o1d3lKeVJrV2plMDNJazZQWkhndmt4ZVR1N3NWalorZzJxZmhXUlJDNTlKMHAvL3p3TzZwM080K2NKN21jK2JmOUxDcEFOWDZ5YmtKZFEyc0xscXMxMnk2a0NDUmdkMU9LQmx5b0ZRR3o3eStuRURXWUpCYjRnRkJ1anFvaFpYV3g5MjljQVp1UXdlV1R5SERFNVJmQ3dMbXFXTkQ1TXRYS050bGYyRWNEeTZiQm95S0cxaDVLS1h1bXJVVjF0TWNWVzkxNUZ5aENTTEZxQlhlZ1hCYkEzUUhtc3dveGZBY0VDRzk3UFBKSXlWNTJ3TlYxQU1MNGpwVW0xcnlVL1hudVdicEgvRFkrOUVHSHJmVGdseWFrLzZKaWN2V0M5RGRFQmRBSzhkMjkyeWZYbmdlVmczamNiays5NGdkRlFZc2FUdXNNbFJ1SDdxWVVIR1RoN09QVGNpcHZab2RVTlM5bFd4c3I0SkdJS01UWUY0SnJENXB1enU1aDF6RngrQUlOa2M2Y2d1Z0tJRnJmdm9uTnlEVmpWMXlSNWw1RGJlL1JYVVVJZ0l5WWpETDQrbmdna2QwUDZMQm8yeXd4Rk1LMFZvTHdxak1Wb0Z3ZEFGWllWdS8yUWtmRzJzYUc3dDJzWEFGSTJ6cUtpc05MUmtLV01mcHBiNVVQbEZ2VlZtdkxVZWgzSklnUnpXSFVZa0QvWFlCOWFRbG5SNmU1UVNqblRDVGNINk5POGtHc2JFWC9CUjVreVBYeG5GWFEwQTM2M2dBSlluU3lMSjJxY1B1ZHZQK2JyTGcwdUpreHFPT2l3WEVDdndhQ2RZZUJhTGlDMDZDaGhYZG80aG9Lc3AvaG5VdzJXZ3YvNW9OUlBxSHFneVNVOVpHQWdxN3ZPekcwTTZKODNRN3MzT21EZHZVNWpxNUNPVVQxNzlsMWN4dzdBalBZUWVMZU4zWURFdjRydG9IRVZQazYwaWxHcE1wdmhQUjlia05Cd0dvM1JRV1pMWXdVbTJUa1oxSDQxQ21Kc0ZIM2x5b0dCSEVpWXNGT1NycjZraFZxdlAwZmlQdjhKL2cwQzQ4eU9mSG5uZU0ycXNHcXFlUGR1ZzdCQUdjZm9jdVNMQldMdWRvSlRlQ21qQzhia1VDbndLWXB0elJCaXpWbmpqOS8zSFNRbk1QTHNUdW5NeVcrUHAxVWhOa0JGMmFITDFnTmtEaXJCWTUvaW5KOWtrbGo2eGY0WFc4QVRSeExYa1p2QnV6TTN3NkdHYXNkdThDV25QN2k4MWIwMDBCQVpSUzBrS2JCY1IyZEUxMThEVGNCek5zQ2Z4cnpxekpBYUhhT1FNNFVnejczUWl0SDRVcVc1ek9ET1FrWGZSakJBTGFGTVI5c0dNU3ZlazUweDlHVlh1RGlBRXdzNUpweCtUVVdPSzNGYk1ZRkd1TWZaT0NJWW05UlROQy9GZHFxalN3TFhDUHIweXljdnJNUm1scXZYUjRKS09wYlRpeVRuTjlCb2tObTk3Y2tqV3hZcktMUjFwdllsWmxpY0t0c1hpd2lDTVRuS2pmbnZmZ3lmMzl3b0V6R0xJb3pwbElRVFNSQVIxaENqRzNkT1dlZ3BZK3QrTlEvQ0IwbVpMMjhlVEZNemNOWkNBZ25nZUNLMldVaHZTb3M5L0VKYVo3eitzSUpVM3dFRG1VN0xIUE0wSThBcDg3WUZhbkdxdWYvSjBITHRhVjZIam4xVGFLUVJNL3A0Wm56M3djN0x5eVMvSm9aVDN5WGE0ZkFsQUJmalNCcU9NenJVQ1hnMDJJZllEUGQrZlZkeFB6VWNvVWM1OFpjaHk0eldPVi95eDRjOUE2RlgzVzJvUWpKRjUxdWpwWDg4UEt3SE93VVRRdmw2OEJMcklIWVloNjBOalNNVFJRQ21TNFE0aTNENnJmN0ZkWE1UQWs4S3NZemZCclNTd2NGTmoyR3crY0gvd3FJUUI5RVlDVkYwK3VxSWUxeGx3N3p2Sks5TERzaTB6N3I4OE9vMzJqV1lOQUtUS25TemNMOFEyVFFTVk5JMGpxWUJyRjBQRWJROTRvdmlORlpDaXZKTWZmTHNlcHJzTmVLSVEvNXIrRWgxQmxJL0ZEcFJDVGhubmdVMk1tYW5ZdFdEMk16cXRNT21pSUtrbWFWdHR6cFMvVW5tWmNUOTVBYWQwUjNDMEJCbHhvQmtObmJDVEFoRVJTanZDVFRXa1pMS1dWU1JHVng3Y0d4ZjRVcy9uWXE3bzJPRVZlSFVQYnFyWHhLRXBobXUrcHZtcHZINmRxSGlxUUZVQzdyb0RHazNubHZCM1ZrR1RPNWJoR25ZT1NXa2s2WThLVTUydUhydFFqcmxYSzJKTU0yMHVWc25xMHVsM2RNLzRFOThqajVBUEhBaFQ1cndobmdWVVZBMjh1ajJkQVdmVUQrU3VpYlNOZDlqMTkyZjNFdVVKaXZIYWd0SzRKeHpiTWF6ajRscTF3NUhEb25Zb0NyQWNGTFJ6VWxxN1E5SVg2SVNOSTZSZDhmLzhRVTNQMWN4Q1F1S3lGUlNHOGM2SU04WUcweFNyWFJWNiswOWd6elJhNWppbkVYc0czNkY4a3FRZy9LVEtqNDJJQWdEVEZiQWFKZHlRSjlTZVpWY2JRd2cvSHpWVlF6WWpzY1VUR0gxbjl5eWZ3THBheERwT2xNM2FRcWt5ZTBVV2lMQmJmdytpbkdVNS9wNnZMS3hhbEVFZkVOM1JBTDhIWXpYV096MDM1WmtuaElnZU9hMmdNNXFhT3hiNnIxdUQ0bkFEaFE0dGVlMGptRWNVd1FSdFZzbkVNV0x5VjcwQkZVVFhoQm9Ea3RiWWlUcnNDZU84WWhPVWxYbkVtRk83anZ1QjBSMEszdXRXWFRHcHZQQ2d0R0VQeVRNRGlXRUpBeVB6cTFJM0gvZGg3YXNLZXlqcmVPTFRJOUVsNlBUd3k1SmtVNmdKa3NBaU1ocGYyWmdTOHpiU2NWQkdaK1I4V0QwM2pOL2p2OEx4NDNxdCt5d3FkVTFKclRyOW1VUkFEMjAzcG1qWDNGd3c4Z0FoZnhTY0JRN2RzS09YMGRLWlg4V3c0TW9NRXV6WXFnYlVTOElYTzFZOXd0WGJQTnB1SEtmSVNNRmhydnlYV0ZZRFl3SUlDVWZNYW9TUFNqMW9mN1dTZWVYYk00SFl4Rkh0czVPNmpCL0pqeThRZlJMNnJETFAvN0Fqb0cvb0lJZGx1VWg3c3V5Y0dUOG1NUEZ6ejlCRGlBc0llSkE1ckVISGs0aUdPLzhJMk1GRVlQUVZEY013ZnMzRWMvQTc5STVCRjdnVndKWll3cys4aGpwS29zVG5ZVEN1aFFQS0k1WVBVS0lTNXhlYitUMnB5ZUZHVVk5dFVMem81SzJZZDErWmYyWldMNnJrUzAxbGVQaUtMY1FkZmxEN3dqaGVURGxlbm9CVmRPc3VTdFl0QWg4OE5sWmFUWWt2WVRTWGlJbFdZdDFXR1FJV1loMEJQRDEranFNWlF2UU1Bdz09IiwicyI6ImU1NmU0ZjNmMDcyOWIzNGMiLCJpdiI6Ijk2ZjQzZjc5NGVkZGQ1ODEyNWEyMzZmNDkyODUyNWZiIn0%3D&site=https%3A%2F%2Fwww.roblox.com&userbrowser=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36&data[blob]=GF07pZE4TZ6vu%2Bzo.0rmSu1v9jut6P%2B5v%2BQqHlOq1rvK0qso9gKfo%2BWUqDOT%2FTVsEWSAmMP7K5WoREuWY1DRpZfjqH0L%2B6kn2NDz9GUCPGbTx19IdD9AEvGUSnbdlix6VEZwo9BhIwRR0qnliRKzo8x2YpPtK1oJ%2FQ2NPaUHKKN6S385KYho%2Fhcl22LQ%2FVICTEL22pyobH510E1mKSBZoR5fmTV80uCIcNzQNUbm3wFNLZ0Dr0ltbyLt9Y4rDXmeYHwvTk%2F%2B9%2FTkPg9S%2Bh6VlOTEJMrCj1itB7wQqlKFX7OGxy1lgARQsZ3ttsaSdf0z18Iqm7cdtNPt%2F0x7rXLYBhsCEJ%2FusjLPG%2Fr5utV%2FKv30p3Jvx7iyyet%2ByhzvFbWEuSnVikGHEwGidipd%2BU56zdNK9Sh%2BUa%2FMetW7ottI7uXdMzxSwxdhIDohlCAWDshslpVlipLYJF9IA4pEnIhEtWKeRGY%2BmXwxlm05%2Blyic%2Fm7Fa4qPd1jk3vo3G%2FCX3kOS5z1pXdQ8MjVhremA8v64192tIfzoeFA1ML8pK%2FhscYQSq1toUXZLYYp%2FVeer4%2FaIndI%3D'

response = requests.post(
    'https://arkoselabs.roblox.com/fc/gt2/public_key/476068BF-9607-4799-B53D-966BE98E2B81',
    cookies=cookies,
    headers=headers,
    data=data,
)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

data = '{"id":"fa301511-2551-4bf9-b8c0-acc0b31bafcc","publicKey":"476068BF-9607-4799-B53D-966BE98E2B81","isKeyless":false,"capiVersion":"3.7.0","mode":"lightbox","suppressed":true,"device":{"platform":"Linux armv81","language":"id-ID","connection":{"effectiveType":"3g","rtt":450,"downlink":1.35}},"error":{},"windowError":{},"sessionId":"440185d3ba67cf656.9457285904","performance":{"error":"Cannot read properties of undefined (reading \'duration\')"},"locationOrigin":"https://www.roblox.com","locationPathname":"/id/NewLogin","timers":{"onShown":{"start":1755625012743,"end":1755625013839,"diff":1096,"metrics":{"setupSession":{"start":1755625012867,"end":1755625013833,"diff":966,"info":{"requestId":"Dd9aP6nGJmfu4lI80CIFUSXNOpX0qlH5tPRQeyzQEiOdXNaX4a3dDQ=="}}}}},"sampled":true}'

response = requests.post('https://arkoselabs.roblox.com/metrics/ui', headers=headers, data=data)


cookies = {
    'ARID': 'pukPiDvjLoj1DPMTg3EV6+tvP6kn0Sbb+0GY7IgCHuai+kaN7DgTZPGq3XrY5yXKREHoqFQYkLqf8Tr+RlGP6rrqRjtGvrGPAMG1whcvbc0AtJsd/QLe1/TsUk18412/0q9eS1BWgsdqfvOWNacM42QUTwpkEsQ=**GHpLQAv5YT8oszlr',
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'ARID=pukPiDvjLoj1DPMTg3EV6+tvP6kn0Sbb+0GY7IgCHuai+kaN7DgTZPGq3XrY5yXKREHoqFQYkLqf8Tr+RlGP6rrqRjtGvrGPAMG1whcvbc0AtJsd/QLe1/TsUk18412/0q9eS1BWgsdqfvOWNacM42QUTwpkEsQ=**GHpLQAv5YT8oszlr; rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'callback': '__jsonp_1755625013868',
    'category': 'loaded',
    'action': 'game loaded',
    'session_token': '440185d3ba67cf656.9457285904',
    'data[public_key]': '476068BF-9607-4799-B53D-966BE98E2B81',
    'data[site]': 'https%3A%2F%2Fwww.roblox.com',
}

response = requests.get('https://arkoselabs.roblox.com/fc/a/', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

data = '{"id":"fa301511-2551-4bf9-b8c0-acc0b31bafcc","publicKey":"476068BF-9607-4799-B53D-966BE98E2B81","isKeyless":false,"capiVersion":"3.7.0","mode":"lightbox","suppressed":true,"device":{"platform":"Linux armv81","language":"id-ID","connection":{"effectiveType":"3g","rtt":450,"downlink":1.35}},"error":{},"windowError":{},"sessionId":"440185d3ba67cf656.9457285904","locationOrigin":"https://www.roblox.com","locationPathname":"/id/NewLogin","timers":{"onComplete":{"start":1755625012743,"end":1755625013874,"diff":1131,"metrics":{}}},"sampled":true}'

response = requests.post('https://arkoselabs.roblox.com/metrics/ui', headers=headers, data=data)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 03 Apr 2025 01:20:14 GMT',
    'if-none-match': '"dbebb932424e9f7599691d0ae24897f7"',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/settings', headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'LoginFunCaptcha_Suppressed',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'LoginFunCaptcha_Success',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'LoginFunCaptcha_SolveTime_Success',
    'value': '2523',
}

response = requests.options('https://assetgame.roblox.com/game/report-stats', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'hidden',
    'provider': 'FunCaptcha',
    'ucid': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
    'session': '440185d3ba67cf656.9457285904|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=71|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
    'message': '',
    'providerVersion': 'V2',
    'evt': 'captchaInitiated',
    'ctx': 'Login',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:53.860Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'solveDuration': '0',
    'success': 'true',
    'provider': 'FunCaptcha',
    'session': '440185d3ba67cf656.9457285904|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=71|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
    'ucid': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
    'providerVersion': 'V2',
    'evt': 'captcha',
    'ctx': 'Login',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:36:53.896Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Suppressed',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Success',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_SolveTime_Success',
    'value': '2523',
}

response = requests.post('https://assetgame.roblox.com/game/report-stats', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Suppressed',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Suppressed","application_type":"unknown","version":"UseLightboxModal"},"identifier":"b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Success',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Success","application_type":"unknown","version":"UseLightboxModal"},"identifier":"b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'name': 'solve_time_captcha',
    'value': 2528,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Success',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"solve_time_captcha","value":2528,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Success","application_type":"unknown","version":"UseLightboxModal"}}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'challengeId': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
    'challengeType': 'captcha',
    'challengeMetadata': '{"unifiedCaptchaId":"b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf","captchaToken":"440185d3ba67cf656.9457285904|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=71|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager","actionType":"Login"}',
}

response = requests.post('https://apis.roblox.com/challenge/v1/continue', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"challengeId":"b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf","challengeType":"captcha","challengeMetadata":"{\\"unifiedCaptchaId\\":\\"b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf\\",\\"captchaToken\\":\\"440185d3ba67cf656.9457285904|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=71|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager\\",\\"actionType\\":\\"Login\\"}"}'
#response = requests.post('https://apis.roblox.com/challenge/v1/continue', cookies=cookies, headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'content-type,x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options('https://apis.roblox.com/challenge/v1/continue', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'rblx-challenge-id': 'b14d8825-1d9b-4f98-aa6a-3d2d61d3b6bf',
    'rblx-challenge-metadata': 'eyJ1bmlmaWVkQ2FwdGNoYUlkIjoiYjE0ZDg4MjUtMWQ5Yi00Zjk4LWFhNmEtM2QyZDYxZDNiNmJmIiwiY2FwdGNoYVRva2VuIjoiNDQwMTg1ZDNiYTY3Y2Y2NTYuOTQ1NzI4NTkwNHxyPWFwLXNvdXRoZWFzdC0xfG1ldGE9M3xtZXRhYmdjbHI9dHJhbnNwYXJlbnR8bWV0YWljb25jbHI9JTIzNzU3NTc1fG1haW50eHRjbHI9JTIzYjhiOGI4fGd1aXRleHRjb2xvcj0lMjM0NzQ3NDd8cGs9NDc2MDY4QkYtOTYwNy00Nzk5LUI1M0QtOTY2QkU5OEUyQjgxfGF0PTQwfHN1cD0xfHJpZD03MXxhZz0xMDF8Y2RuX3VybD1odHRwcyUzQSUyRiUyRmFya29zZWxhYnMucm9ibG94LmNvbSUyRmNkbiUyRmZjfHN1cmw9aHR0cHMlM0ElMkYlMkZhcmtvc2VsYWJzLnJvYmxveC5jb218c211cmw9aHR0cHMlM0ElMkYlMkZhcmtvc2VsYWJzLnJvYmxveC5jb20lMkZjZG4lMkZmYyUyRmFzc2V0cyUyRnN0eWxlLW1hbmFnZXIiLCJhY3Rpb25UeXBlIjoiTG9naW4ifQ==',
    'rblx-challenge-type': 'captcha',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
    'x-retry-attempt': '1',
}

json_data = {
    'ctype': 'Username',
    'cvalue': 'LfsmmsfL',
    'password': 'dfsm230203',
    'secureAuthenticationIntent': {
        'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==',
        'clientEpochTimestamp': 1755625009,
        'serverNonce': 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTMxMCwiaWF0IjoxNzU1NjI1MDEwLCJuYmYiOjE3NTU2MjUwMTAsIm5vbmNlIjoiSzNIVEQ3S000RjlZOVk3WCJ9.8bFgXgbBL_ib-bv93rCn-w1PqMS1OoCwwbxQySopaa0',
        'saiSignature': 'n474tTSf7ADCROdMdvP50JIdsAq7mPiaLA9hrrywSD/ELcmIX0bHIKGObAT7FLzwyMVLNnaBA8lGGDoGjU9ljg==',
    },
}

response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"ctype":"Username","cvalue":"LfsmmsfL","password":"dfsm230203","secureAuthenticationIntent":{"clientPublicKey":"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==","clientEpochTimestamp":1755625009,"serverNonce":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTMxMCwiaWF0IjoxNzU1NjI1MDEwLCJuYmYiOjE3NTU2MjUwMTAsIm5vbmNlIjoiSzNIVEQ3S000RjlZOVk3WCJ9.8bFgXgbBL_ib-bv93rCn-w1PqMS1OoCwwbxQySopaa0","saiSignature":"n474tTSf7ADCROdMdvP50JIdsAq7mPiaLA9hrrywSD/ELcmIX0bHIKGObAT7FLzwyMVLNnaBA8lGGDoGjU9ljg=="}}'
#response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, data=data)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'WebsiteLogin_InvalidCredentials',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'WebsiteLogin_InvalidCredentials',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'o293668.ingest.us.sentry.io',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_version': '7',
    'sentry_key': '24df60727c94bd0aa14ab1269d104a21',
    'sentry_client': 'sentry.javascript.browser/9.13.0',
}

data = '{}\n{"type":"client_report"}\n{"timestamp":1755625018.308,"discarded_events":[{"reason":"sample_rate","category":"error","quantity":1}]}'

response = requests.post(
    'https://o293668.ingest.us.sentry.io/api/4509158985826304/envelope/',
    params=params,
    headers=headers,
    data=data,
)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'pageHeartbeat',
    'ctx': 'heartbeat4',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:37:23.700Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'username',
    'aType': 'focus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:38:55.696Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'username',
    'aType': 'offFocus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:39:03.907Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'password',
    'aType': 'focus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:39:03.940Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'password',
    'aType': 'offFocus',
    'evt': 'formInteraction',
    'ctx': 'LoginForm',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:39:06.221Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'field': 'loginSubmit',
    'aType': 'click',
    'evt': 'formInteraction',
    'ctx': 'loginPage',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:39:06.235Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'WebsiteLogin_Attempt',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'WebsiteLogin_FirstAttempt',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/rotating-client-service/v1/metadata', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/hba-service/v1/getServerNonce', cookies=cookies, headers=headers)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'open-connection',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"open-connection"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'connection',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"connection"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'transaction-get',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"transaction-get"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'saiCreated',
    'ctx': 'hba',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:39:07.371Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

json_data = {
    'ctype': 'Username',
    'cvalue': 'Ermomhot',
    'password': 'Fuck2020',
    'secureAuthenticationIntent': {
        'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==',
        'clientEpochTimestamp': 1755625147,
        'serverNonce': 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTQ0OCwiaWF0IjoxNzU1NjI1MTQ4LCJuYmYiOjE3NTU2MjUxNDgsIm5vbmNlIjoiRlRDOTlHUFdDSDk5S0Q2TSJ9.GMC4sp1mytWN8-iY-90Q4qonw57CRLaPweU-gMjuKJk',
        'saiSignature': 'P5JZ7D4TNdym0Yd2SPFis4xEHB9xfkuoqQ4sYHm/7KcCBPac6xepnRaii+LY8HZ4rtr/PuqbNVovYmgnXLRbkw==',
    },
}

response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"ctype":"Username","cvalue":"Ermomhot","password":"Fuck2020","secureAuthenticationIntent":{"clientPublicKey":"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==","clientEpochTimestamp":1755625147,"serverNonce":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTQ0OCwiaWF0IjoxNzU1NjI1MTQ4LCJuYmYiOjE3NTU2MjUxNDgsIm5vbmNlIjoiRlRDOTlHUFdDSDk5S0Q2TSJ9.GMC4sp1mytWN8-iY-90Q4qonw57CRLaPweU-gMjuKJk","saiSignature":"P5JZ7D4TNdym0Yd2SPFis4xEHB9xfkuoqQ4sYHm/7KcCBPac6xepnRaii+LY8HZ4rtr/PuqbNVovYmgnXLRbkw=="}}'
#response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'identifier': '1755624948360002',
    'name': 'saiIndexedDb',
    'labelValues': {
        'success': 'true',
        'arm': 'transaction-get-complete',
    },
    'value': 1,
}

response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","name":"saiIndexedDb","labelValues":{"success":"true","arm":"transaction-get-complete"},"value":1}'
#response = requests.post('https://apis.roblox.com/account-security-service/v1/metrics/record', headers=headers, data=data)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'ctype': 'Username',
    'cvalue': 'Ermomhot',
    'password': 'Fuck2020',
    'secureAuthenticationIntent': {
        'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==',
        'clientEpochTimestamp': 1755625147,
        'serverNonce': 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTQ0OCwiaWF0IjoxNzU1NjI1MTQ4LCJuYmYiOjE3NTU2MjUxNDgsIm5vbmNlIjoiRlRDOTlHUFdDSDk5S0Q2TSJ9.GMC4sp1mytWN8-iY-90Q4qonw57CRLaPweU-gMjuKJk',
        'saiSignature': 'P5JZ7D4TNdym0Yd2SPFis4xEHB9xfkuoqQ4sYHm/7KcCBPac6xepnRaii+LY8HZ4rtr/PuqbNVovYmgnXLRbkw==',
    },
}

response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"ctype":"Username","cvalue":"Ermomhot","password":"Fuck2020","secureAuthenticationIntent":{"clientPublicKey":"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==","clientEpochTimestamp":1755625147,"serverNonce":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTQ0OCwiaWF0IjoxNzU1NjI1MTQ4LCJuYmYiOjE3NTU2MjUxNDgsIm5vbmNlIjoiRlRDOTlHUFdDSDk5S0Q2TSJ9.GMC4sp1mytWN8-iY-90Q4qonw57CRLaPweU-gMjuKJk","saiSignature":"P5JZ7D4TNdym0Yd2SPFis4xEHB9xfkuoqQ4sYHm/7KcCBPac6xepnRaii+LY8HZ4rtr/PuqbNVovYmgnXLRbkw=="}}'
#response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, data=data)


headers = {
    'authority': 'apis.rbxcdn.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.rbxcdn.com/captcha/v1/metadata', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'name': 'event_generic',
    'value': 1,
    'labelValues': {
        'event_type': 'Success',
        'challenge_type': 'captcha',
    },
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_generic","value":1,"labelValues":{"event_type":"Success","challenge_type":"captcha"}}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'if-modified-since': 'Tue, 05 Aug 2025 03:34:49 GMT',
    'if-none-match': 'W/"232a87d38e07cd994738a31a347739ff"',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2//api.js', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Triggered',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Triggered',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Triggered","application_type":"unknown","version":"UseLightboxModal"},"identifier":"2ab46d47-059e-47b7-8a67-e61a6d98c2b2"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'if-modified-since': 'Tue, 05 Aug 2025 03:37:19 GMT',
    'if-none-match': 'W/"ca28baf2d673aafd262a5bb8fd90b65c"',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/api.js',
    cookies=cookies,
    headers=headers,
)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 03 Apr 2025 01:20:14 GMT',
    'if-none-match': '"dbebb932424e9f7599691d0ae24897f7"',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/settings', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Initialized',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Initialized',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Initialized","application_type":"unknown","version":"UseLightboxModal"},"identifier":"2ab46d47-059e-47b7-8a67-e61a6d98c2b2"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-ark-arid,x-ark-esync-value',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options(
    'https://arkoselabs.roblox.com/fc/gt2/public_key/476068BF-9607-4799-B53D-966BE98E2B81',
    headers=headers,
)


cookies = {
    'ARID': 'pukPiDvjLoj1DPMTg3EV6+tvP6kn0Sbb+0GY7IgCHuai+kaN7DgTZPGq3XrY5yXKREHoqFQYkLqf8Tr+RlGP6rrqRjtGvrGPAMG1whcvbc0AtJsd/QLe1/TsUk18412/0q9eS1BWgsdqfvOWNacM42QUTwpkEsQ=**GHpLQAv5YT8oszlr',
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ARID=pukPiDvjLoj1DPMTg3EV6+tvP6kn0Sbb+0GY7IgCHuai+kaN7DgTZPGq3XrY5yXKREHoqFQYkLqf8Tr+RlGP6rrqRjtGvrGPAMG1whcvbc0AtJsd/QLe1/TsUk18412/0q9eS1BWgsdqfvOWNacM42QUTwpkEsQ=**GHpLQAv5YT8oszlr; rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-ark-arid': '{"ls":"pukPiDvjLoj1DPMTg3EV6+tvP6kn0Sbb+0GY7IgCHuai+kaN7DgTZPGq3XrY5yXKREHoqFQYkLqf8Tr+RlGP6rrqRjtGvrGPAMG1whcvbc0AtJsd/QLe1/TsUk18412/0q9eS1BWgsdqfvOWNacM42QUTwpkEsQ=**GHpLQAv5YT8oszlr","idb":"pukPiDvjLoj1DPMTg3EV6+tvP6kn0Sbb+0GY7IgCHuai+kaN7DgTZPGq3XrY5yXKREHoqFQYkLqf8Tr+RlGP6rrqRjtGvrGPAMG1whcvbc0AtJsd/QLe1/TsUk18412/0q9eS1BWgsdqfvOWNacM42QUTwpkEsQ=**GHpLQAv5YT8oszlr"}',
    'x-ark-esync-value': '1755604800',
}

data = 'public_key=476068BF-9607-4799-B53D-966BE98E2B81&capi_version=3.7.0&capi_mode=lightbox&style_theme=default&rnd=0.24512975284418959&bda=eyJjdCI6IkdKSWU1blNkUlFRWWVRVUtyNVJLS1RXSXdybk1aY3FoQi9BZDJPSmZuU3Q0aTVJUUZGMW1lRXBPcWF4R3ZUV2pneURsb1ZzNDVIcExOTTMvYmRGL0V1RGQ4MFd5WXRIY2NLUmR2bllVdkxnakh2a0pCbGI4dktYaGhGTTB1dzVQelc5UjZBNk5WYXVsZlVrUFhGajlzT2tJaXdNcWlEbEhVcW9sNm5OVGd2T1R3YkQwU3FQYzh5VlAvTkowUVpvQkNGQ3JxVG1zUjNqNkNmV3hrSGRkYU5VM0J3aDdsY2FRdE91TFloaWxPK2xtOFlHeWdBRThTTTNLajFScGZaYS8xdTViMlk4VldzUDIyd04rbU9MeWV0Q3JrMzFtakJXaUF6elI1V2tZM2UzajFEb3RRVHJwNVRrUW9vSGJ5WGhpNFlmcE5HQURlQkJ2SExUa3B4OFBMMkxySTZjQ1JPVjZ3MEFDYzBUOTlTL05rbzl4WW10VjhtSVdQVzJHSHphMEJWZ3BuWVY5Szl5Qk9JZU9zRi9MZ0o4RENVK0ZRZDdWVndWdEU4OVcyMlRCK3RVNXNLckJYMmtyR1dNTUJPOS8ycy9La1UyKzd1QklHaWVKQVIrSVBZVlNhU3NBM1p2TEVpTnArV0FuZXEySkk1MWdQdFFvYmVqUGtJdXpHWDI5UlVpZ0Y4ZHp3bnVzZHZoSWJ1MFJNajBrSWZvUnd1QXZPOWlhYWpzajNoQ2hoR2NCZTFGaTgyWkQ0T0tWaVR1RklPZkZBSDl4YXB3UzUwZ2hXeHljeEc5Ni9ibWdEc1gwNFRXY0lTN25VR1JKZE5tWFI0RENSM1FsazlrdG43aTlVV2h6czFXSHRzQVd6Ymg0YU0rRUZJbXFlakp3a3Bnc1Q1Y3ZudmM3SzFIV2lNS05xZjB2cTZPdlZ2NjljOGMyTUFvYVFtdE0xait0Y01JT0w2WVFoRVBsazBZbXg4MERuTGd0d1VWTnExQjNkcEs1dlo0NUlvSHBDMWUwK1pxNkNweW13aG1heDJFazl6TXY1VVdOV2lPZmNkY2xnZUFDVzQ3VmQ5YnlRZzl5Y1VJc25Jc1Fyc3cyTFhOVXlFUkc3Yy9IaUcyS0xPSU5SNlRQOWpXSzFFYWFrU0duNWsyT3NCcCtMM1BhaE9nSlZJcDZ4RkZvMnFyQU5vS1hsTnBlK1MvNTFmMlZWQ1E4WWVaQWxGd0RrdFlKSHdtYzA4NmhJMEdzVXM2TzlLb2xmTUxLK2F1MDZOb2k0NWF6OTMvYzJsbml5cW1sS3VkZWU0emtiZmJPQWRjYzQ2S3l4UEd2bGRwTisybHRDeDl5VlpzQ0FGaHVxbkYxY1JyYVhMMVo3VllUMnVsd0c5RVVmN01iSEVrcGdvUHJNeTBzRlhOeGxBQXI3cERPTFNnN3lnZzE3L3hwd2g3cFdvdERybEt0NXhWcGcvblVSbGdwY2ZmOHI5YjIzeHFWMEJFNGRNa0VqU05BQzROdTZWOEFnSTFMR0VVZFVzYlBONnpxcnliR0tneXQwbW15RGVWYVpqZHM4MVgvSDJwOUg4ckFSKzhMaUNvbnd1cXptS2pmQ0h0MytjWGM3WldvTjJGaFI0T0wwY1NLMlNvTjJtcmhhT3BVK2N5dk02a05XVDh3anBucEx0b3VoRW5MQUtIc0UvNnZQWkgwUmxaM2czV0h4VkR2SnU4M3FBU3V1V2VkWUltWXd2aUpBVE1ndHQ4aDM2eVZzVHhmam1GZ2tCT1JMY3YxdzFYaVdld0FDaDdxTFFsRzNtZVMyTzJUY3VWU0dFbXlxRVJNNmNXN1lNeXhUUFUzYjNZNVpIT2llcW8xaWtsTkxPcjVQSHRlRUdncXdZTHlIbERVTjRxWVB1VGFPU1VyVldQZzZSMlQ3K3lSM0FOcFFMSlFoc2VydVRJTUdhZFR4VmIrRUQzcFRCSGJzQlpqTC9MU0FtRFBlMFVPenVybW9FdHl5WVN5MURGS2w5R0JRdXczaHVpbjhXTWdqc3pZdVN0Y1NybTZ1SVVqb1JjbEhrUnVLOXpUYTVOOUhGcG1TTk05cU1GOE9EUnFoMmlnb3lSNjJwc1hBZGZ1OFJ0cGxKMEJNVitZbC9pMERsMUtrc1EvQ3JyeG1GbkF1MnJvSDhiZDd1MFdEMFZFTVlmMTdkQ3d4SGp2RGdRcXdnM2RXYXlXRU5VNERQOU51QkFWQmZHaVlXN0VmSWI1czM0QkV0anVkbExvVEQ0eThXd1ozQk5FVTlxZUhtSUtuRFJjMlhTdjVweER3aXRqWnp1Q0JidlRUYnRxYVdIemFHM3JMdlZrSjFYRG1ZQklhdHRhQTRDN252Z2J0bndQeTlxaEp2NTF6TkZ3QkZKc0pkQ0pOa3NWbDg0T0JOcVFCcnNFUFFhUGt5ajhYaUlJWmJxRGJmQStUYzhZbzdTY2ttZEhOcGMrSEpHVTBxMm92TGxHaVAraXJWOCtNdlhqSDFod3htS2EyU0p3ZkxBc2poUk5ldVcrTk1BNWgrSGdsY3l1NXBRMjVkWWR4Uk1lSVNURG5SUlFycGJ4ckRGTnZEclJ3T0ZPZ1VBL0VmM0tyTWhGN2ZpYVFJS0hwY3JTbURSUHVYM0pXTENadnJEcHRNVS9PbzdrUkhHSkhKZXY3d1I5eG8vb0FqZmh4QWphRTUxVEgweFBqOXF0bXoxSTJQSGUvdXpMMEw5MjdBbG5HZjI5TkhaaEdkUkVVdmpiVW0zK1lrV01MRzN6Q25CTXhwSTFvYldtb1BlYm8vU1FuZlBYbkNTM095K25ZZjZ4WFFNckxBbGI5Z2VwakpQRUpGTDFZVEttYWFPdmY1YU9WZWFPZitPWTU2M1R5ZG1VSEtsNVJZRUdldEdwekhnU2lGZXhtOU1QZHBiMG5yOXJzTFJPdnorRlF1NGZ4VmpIK2JFWjg1N1UrL3gxSTh4ODRuQXovM2oyam8yeWIzbW9EU1hDd04rSDZkZEYyeGpUTXVKcmFpSjFRWGNGU2pmbStwd05VTjdETzZnRnZzaEw2YlBFYlY1WXoxN3QrL3hWSTUxdlVSYkhKMy8xc3dvc3h4bGhHTnNhcEFhVURwMnRZVUptZE0vdzdsbDdLV2ZYSTFYK1lIRjlqYU4xdHRlczBYdXc2dVFpTG13U044VXlQemtBOWJsNGN4Q1lHQndkUjRGQktFKzFJdFZ1NWlTRUtvVmJQaGVHME95UFB6WktJdUxvVEQ2Qm9uM21DR1hEeW14bzNDZ0FVWTVIWEI5Z1hqOG9VOXp5dmwyUm5icGs4UWtnWG8yTEdVdTNMa0RzZFRzNHhwRVNwN1dSMHRFamdnSy9GZXYxOG1MdkpNRXdSaUIxWmxsVGdjaDYwQ25qODZpQ3NIdi9pUERRNnBHQ3JkNjB0UDVTZDBtT2cycFN0MlRFdUtjTDNsa054VFBFSzQxdUhGeXVad2FHV2wvRkhKODhiWk9xWi9kbFlVNDFJTmo2K2UvT0E3S0xzOFJFaTRkZXlYZFoyTDYybHFwMnhqcWxzNHFZNWFlY3d0aU1vTktqY0t2dGdqMW5hWDBIcUEwTFNzcy9SS2UwTHl0VkRQNkFFWmVDS2V5WlVhMnIzWkhYVFJWNXJ0S2hlSEZ1YnhTS1RjODdpUFMxRC9SQmRjZ0tEWVh1S3lPMVZvOWFhM0ZVcURiWHkxeGRxVklrc3VVMkxVcFFpaVlSMWVkdVFIVTVvRTloc2NSTSsrMURVQ0FrK0NicUg5K05pdXRINE12T0lxNHc5U2hFNkUyY3huYUlSeDFKQ0dRdlQ3ZkFQZnZzdGFWbFFYTjU1S1k2K2gxOUk0b3VBRkkzaGIvZlVWWFplRXlGZGxPNVBtTjlOYm1qYkVEYnlMSHJZQjBUSmhOOVlzdTJRejRlMEVmaGljckN0NEJEbTd0Rkk1OHFBTDhCWEppeTBpVThxMXJVRWVZdE5BNndRSGtMYzhrcEkyQlk5b0l4b3lFcDBqSUk5ZXRNY3JqVmZNVmR6ZW00TGgwaG5saDNDZ3RXcU9TSWdQWGRxU2x4K2NjWEhmY1BYWWlndEN0RnRudDJXY2dJdzhjWUYzTFMrOFBsSWZiOW9BbzRwODNCUnVCS2t5c0h0MXhKZjJPQms5WTR6VHhRblg1UFduOCtwM0ViNnE0MG4xU3pWc2RxeXhvOFhmZ2d0bDdaRTg1VG5EUk1RNDZTWG10TTdnYWg0QmpXYmtFd3d2WVBhbmZKNTFlUVJ3NnphZkFTeWJsSFFYVVI2eEFmZHVlaVV3Y3NJZm5qYmhpZ2tscGZ3QXhCRnRVdmRHMGcwRldZOGdTWEJVZEkxYVlrRlRUbFQwem5OTndwMzErZkZIcTZzWkk4cHJMdE9HVGEyK2pYY0g5OVJBa0hsbVVtaHlEUUk4dXVQcVRZaHhxRnF4S3prd1dBZDBvNy9vTUE5UGJyMmhPRXVYdUR4empmeVp3d3FqQkdkb0RtaEtKRkdaOTlReFFzekpCbzVFLzlLdU90dkhNMFhWVGUzY2lCWmFxdkdmZXMvSXRuaTd1M2JiakdUTitPaXhabGpiaVl5Y2hUQ0YwVzVZVGxrLzNSUWlHU0cyVVZIYytOK2tyam50TGp5ZTcrSkh3cEdpZm5qMTZSK2N2NkxHOUt4QktlOVhDOS9oVk9YK2I1cUwxcmpOZVhJbXRHNlh5WklzN1VGTjh2NUpLQkhaVW9qWmZWcGp2S3ZmcXZNTXhHVWdxYzFLblpqbVRBbjNNaUFkVmhHMStZcDBXNk0xQlhCZkUzTllRUHlTd0RaamVUYWVyY2pVWU5qSGtSTlFkVG9iNlZBSllSd1BHM3lNdm9ZRW5YWldjSldJTlNjQ25Na2JBSVdSVmhKV3d5TnJEdTJEN3lqTFh1SnFjeUZVVTduOVJnYXRWVFVLb3dhQ3A0d0l0Yk53L2E2b1B1Vk5Dd2JJYmM5UjlPUWJDa0dpUXlVWExtb0FWT1B2UTBSZ3gza1RTeEZHK3NWcHY0cG9zMzNZaEJMSFNibVFtSjR0UHBGSFNJVDJuRVZ1Y0IxU05kdFdsdXA4ZHZXaXREUWJSM3l2eVNoWUovWlhGa08vZExSdEJudk1SYXpXdkpubi8vcGdYczJCRGc5T09hVlRKYUJTV205YmxlekNZYWJiZm5MVDBQcEtuUElFSjcyandrYXBnbmdCRDhJRndsaXRtT0FCN3gzR1VaOHl5S0h6OUlnNFRuOWxYT2JEYkJodGVXOFF2VHJVR0wvRDhmbC9WTG5BdSt3NmRHWVhJTVluWUNLNjlqNDFabUVJbzA3cVJrc2lHdXZFempwbll1NEF1NExQb3VOYjlQeThhYlRNdmU1VXdCcWZLZ2hyNGZFM3ZBdUVlYmthRWFEcnhFTGJDcDM3UHM3THQ0NEVETkQ1ZXRORFl0MlJGQkFDM2xZSytHSDMyQXYwMGtXblB1VkFzL1FIU2QvOHNNcmluNFFFUm5DcFBVUlV4bWNJS0xDakNZRkM1cUlqd2IxNWxFNVNMbm91KzJzNnJBWXZuYTlvSWIzQzlnZmdmSFFxb1UyaWZZai9NMXdVdXdMck5ub1J3YVNHbmNwbEtQVU85M0xQNy9FODlCNE1mbzA4UmtVTjVpVy9rY010U2NmTjE3Rjgyd2FJWUkxN3NGU1VGemphN0xwUlFhaGl4S0d2UGpWRFJEa1RuNkJmTnZnZzkrWWttODY5eUpxZGwwcFNGcGRPL2hZazBOaXZJaStlcGNUd1hXeXJnNXpnS2dOTU93SkNTVGVNTG00QjVsYnNYMnE2cURvcFRSMjBYSmp1YTFyRlowdmtPaWxDeE50OE5sQmdGRFI5eTdxSjU5MGZvZ1RWSnJkS3llaXpxY3p1NTF3RHEycHVpd3VWUlU3ZDhaTEk0TEh5VnhzTWFaVWtJT0F5bGNQdWJOcElNNVVLbEt1aFh2dDZsWGYrUmErRkMyRGNUY3RieDE2NGd3SGNpYXZUZjlwaFNxZW5QRm1RUnBVOXBwaHhmRzM5ZFhtZTlHWjhLd1EzY2tIb1FFZzkrQyt5R2x3cUtYejdDc1h2N3hFd0c3SFluYUNVc0xsTjVob0lwQTE4bmoyUUxNZkMrU1ZjQlJteGk3cDZYQ29nNmZwVThaVkwvT0JMSWN5TEhkRWRmU2lWa3d4RUZPbDVYMU5nMjB5dWdxdFNkSW5GSGl1YTlLOERqQnZCc01tQjF6OUVYV1E0ZVJyalRSUEZMVE9aU1dzeXladE80VXVXd1BPcis0a0xzRWtWL2JBQm5FckxNdTl1cE5mVXBHV1JwcTFJNHNFSGh3YjZtTXUrV0c1amRxT3MxdmlBMDJVZ203VkgxcE44T3BXdFNZbU93ZDFqc0N3L3ZHMVYvSit6L1ZOanBRbkNFSUxnYmswTmNyNmZqSFN1S2dEbzNiejJ2L3dUZ20wTzRkUE5mazJ4NjB1MXVTOUFZVDlNMm5nVC9jYTRMcXA3dDBTN2kyeUs0OXBYUHRLcDV2V2ZsTW80emdRVnJicTBaMHVTbkYzUUljdlArMWRKd0t6ODhNUVI4QlhBNjdPcGhHaDdwTE9iS0NSajQ3eUVSNVNzVVlUeDlmblo1UGU3dUZBcksyTm1yZXZwSkZ0bUY2SldXdEI3a2l3Z0ZvVmJiMnJjNmt0Y0lsYzNSRnA0blNrMnBNNmJhU1FhcjF2VkFQaWszL2xLM3lETHFoVGhFMnhxMXd5NGlrLzhvSHFlQytxUjJRRWZBT1VGZkl2YitIRXlrdjc2VFo0emdxenF2VGtqd3F3NEJqTjBKZkZ1WlNnR0pVT3U3eXBqU0JvL2U2ZjBHK1B2VE9Eb1JrNWtHWFFIOGZZNWtWamlURHRkenJNaytoOWhCbXQya0dLT0hRZ2ZDS1p2Z2pIMnNqTzZYYXBCVUwwZ3dqRTg2Tnc5N05LRVl6UTdLQ1h0VFdqVG5XVzhnYTZGaEI4N1pTc1dCWkV3ODJES0ZVZXN3L09tOUl3Y2lGQzQyOEM5bU5DVDVKVUZWSEZybnU3bHZJZmlrMXdVT1NuSW9wajVKS1BYcGJxRXR0NnZSU0ZtRjQvSDR1TDQvQjRsWXpWL2pkYlpUY1BkQjFjTDRzM1B1dTB1MVZPUVBDRXh3SlFkc21Rd2FKRm40aU02d1FsZFUrMkhBd2I0a0JkcFhaeElGUlBycHc0VE5kSmgwdnhmNFdITFh2SG0zZUQyaHJuUlhicFBWM3haMW1XRXZUazJoRG5ZN2M0N3dtWW9pSGZFSUlFeTJzYXVUK29ab1NDYmwra2tyTDJDL2RWTFdKSFpld25GMUd4TVNjclJVQVZhVCtmbUdNdXdBZHk0cHVDSDZ1allNOUdLWlJKaTkwUEVHUVkzUXI0QUxaa1hHS1NWMVI5YWFCaHZyRGJkMlBaRzZZU29WOXRqRXBsWUdGWnNodDJsMS9CR3JLNEcraEhUUjUwa3NmS0Yrb3ZMeVNLTDN2bkJDM3ArZ240b2MyV2xqeURUbnBOYUpMLzBQMEwzY1lOS3Jkbm1TZmdYTkNIZS9Mb0RNWkU5R2NXNDg4VCtIdFBtSDZ5a1ZDMDZNcHdENU5KT1hMc0Y2YTh4VmIwTUdqUkQ4dVNTclZsckdHcTZsUVNLOFVRVkRtWU9hYnhZMkVzcnNTc3ZjNy9wSmd1bHQzSS9pdit6VE5JaWt6NHRCaHNaZFlNRVF6ZE1OMnFBVmdTbmdkcUR0VFpNVFBMM3dkR05SUUpvRUFpOVpzSFB3eWRWQlJDU2xmdnhvVGIxbUZHV3hxb0l1ZVVrSUx1c09HZk8rUGZTQlVaNGg0YmN0MWQ4SFBzM2RCV0o1Q3Z5OFNUZnBMbzNSb1NaVUpvNjRFY3NVRW9abS9ra1JyVGRxcnR0Uy8wUTJIV3NPelJrWVh0RW53Ny9YNWViNDYxVFU4OUxsK2FGc2VEcnZtalFBUzN4ZHp2dFFjV0tqZ3FTemhlVS9kZ1p6T1JQajViM1ZhSEVxeFY1Nno2MXFnR2hKL1d1OGwwaklhSjZpbTdvNCtZbW9FelVnQWtuUHRTamVOTjF5dzJ4M25wbHF3RnNaR0tUbjlUR1hDNVl1S2lXaW50dU1vL0YxWng1TUdYM05iTnJNRk9qa1JhNXRiMlJiSjhybjk1ZENTTnVTdXBOdUx0OXFBTWhHalNqVVFMZ21yS3QyZGFTeEN2SVFBWUMyRHhRUVMweXcwaW9xQkZhZFV4TWJTRENBK3VZSU1qaStxL3ZVUUlsRW40V1RrVS9reXhjTGNyYVcvYjROVExmWFowZlp2K1hEcFRCbzV2TmhGSjE1RkJyU3VDNjNFTmVUR25YWE5kdVpwSUZPNm1xd2ZpSGlHNzBtVGRBRXU1RlJqYnVSYVdqYXpTcWRDMXFOT2RhL2V4ODROeTNOQnd1QkNySEhaMUpNVjlXQWx6TW9jdlBSZjc2MzdUYmtiMzBUeXhMeThvUGpvRU5ZaHdoQXNWSkpqN0NHN1V3SzFIRXFVSkxqcnRoaFdBbCs4L3JQQ01DVEhNOWJONS90Q24vU2ZsMm1oMGh0R04yYUZONGVOU1YyYWhDNzMzRlVSOVBHV28ydS9rRVJKNFNKNHJRQVRHSDRpUCtOc1pEc0hQZjEza1B1VW90dnZzL1dKOTJwSitnQkt6K05EZW1mQjVuTlhYVjhXWFRRenJvREJVNFhZa1hpdlJyMkJmNTFRcklpTFRJV21tV1VEdjZ4bEhEQjFTUTZKbnA5VW5JamExeGdTMWxQc0E4N0tyUTEwc3hFMkdiTlRIZHBXRHp5akhZQ2NuVmphZjNkcGZHYVZVbGFoWU5JTjl0YWNtTkFac1RRYVVuUFJmbjZwcFhESUdQRlF2MElObEhXWnhxZHB1bUlTbVIyRnMwZFhWWTVZT1FONFgwMVR2MzZyUWd5dWRrZEhoVTNDMXV1REhHUzNmYXUrektrdSs3NURtaTBWSjYwRDdTT0I4M3d6bmRFMnRCTXYzNmR0c0hEUjN1ci95bHkzdmNXcXp0QnpCdERiYTNIbVE0NjFpZ2FXM0Q0N3NjNTJCRlVtenBBS3dTaUR1aVNBeFJxVWhreU1jK2UxRllzcEQzZkFFQUNtdjVkTitoL1R2dXp6eGZFTktLS2FHUUlpSTlNOWdPbEY1UjFwT2pabnh3bnVZV3V4cFJSdS9CVEF5N1RXYUxGZGI5bnN6RStEcFpLTk1XVjlCZ1Y4NTdEaVRDNkRhUUtSeCtqTU56cVJhZmJib1h3T3c3OVhzaUJtODhOeHBLcDE2eTNYSVMvU0lHM09rbC8wZ0pBZWFZWjBQVWJVandVckkrR3BEUmd5K0xrNkZ3eDRpaG5mS1M4Rm00djIxc0p3Y0t4Q29iMTVqbE9aUkNWZEJRTmY3bndxdkMzSG0yOHl4MVh6aTd3anBjb1E0cy9FMXNpZFVtbVkrWnQ4M0lTdGVlZUJmMkxNT1hrUHhTYU9KaU1Benh0S3Q3V2tpSVdaVUprajlGOW1lUVdEZUVMdFUvSk1STW14Y1AwN0t5VlhvMW5QYnpsOU11L25GNytsUlhEcksrT1FSYzBHZTZ0bkdVdXNGV3lMRWFWNm41R2xWRlEzaDBvZEEwZ2tMcmZ0VFpwR3p5aGh0NzdNNWRrbVBKa0FkZGVVRCt3dksydzBDM0FUSHFKSWVGckF2NkdsMno5TnQ1WGNWdDZkaEFXeTV3eGszdlVPZ2hxMDZwem5NYjRmMVhoajgrcEw1K2N1SmFPL1U5QmF3Vk5RV1RPZnl6MVVCNzZ0U0grOGpqNHFpQjNBN0YzV0RSNWtnMDlTWlRZQ1o2eTVIbmxyeHh4WWxGS2txanlpVzhkdnJpVlovYWhnUzZwSGNRWUZDVzRodndWWFhlVzRIdTNxQm5EeVRlYnZJOWNLcHp5a254L0MyWkRYeDJLQVJ0OXlWRjV6L1VFNmZ0eVd6ODdpNC9rd0dsOU9iZHp0cTAxT2p6OERma2dQSkZyZU0yVnRoWE1JSFFmajBjTXB3SWVUWlR2czlFWmNTR1h3ckFkR3g5ZnhXa0I5WnV1cUdTTUFJdW81YmY4QnNxVFNUaGxXeXlVcVQzRGtkNEZQcHU5TWhFUmdUQ1pWRVU5QjJlMzB6WlpnYXcyTmpiNTdBVC9ma2tON0NkYlJ3V2UxaEdEeFZ5Q1VONHZZUUJjT0IwSS85QXAxRktheEM4MkpXVXNEM0JQU1hwQUJqUkk4WGZBV1pOWEtXd2p3a3pKdkx3NEZvVEM5TGJDTk5yNElrRk9xTXBJc0libHZzaHhNRG16eXFCOWtKQ1Q5NVlYTWNaNy9MS2UxSmxhcFp1TFd5R0hCTGJ1U3BrK25waTFKdXdTWTltRUJXNnhITTh6SGNnendJL09JcVEzRXdBaVhDWXAvalVzUk0wYk9tbmpybDM2YUcyRHpjMkxNMHE1d1NsRDZDckxNRmxmL295bUsvZ1kzVHI0cC9uN3ora081cXZGVjREd0MyTmJoRTlGQ01PODhWTHk0eHFrTEg5L1ZlUElTS3ZVNWtqV1pNYzlzbVJCam1CSk1BRlpiOEpMZExTT1JBUUFRYkpkYjI1RGN5V1p1d2ZQOXZUMFl0eUtGYkhWZFpkYkRYQ3kya2dWSEppNVc1Qk12cERBTGlaSXl2RllLSkkrN1FUZ2lRaExtUmV5VVJGd2tVclkyY1FKbExSR0RRR09QMm1KeXJwdjZTaEtlYTUxU21WLyt0dVFnK1Z2NEZGblNtLzFqQ0VGVWRTdVEzZDV3ZHlNeTZTeGVBMUVNYnFReGkvZVA4MmNrTUtweHNvWGNxMzYyWFBqVGY3SVJMbGNkOFl4MFZxelRmc25LcW1yQjVuRjJKRmJBZHJ3cDNibWo0SDU2ZkZ6ZjZnR2gwWEl1MzdWUDJqN2d3T1ZLcStmc1ZIenFMbFgyWGxTWk9DNVF5UXdobCtOalJMeVg0b1JSRUhTYnRvbU5vRzF2cm4zM3ZlcUNKR0RQRXVHUEYzdGlpcktMSHBmSlNHUzRTekZ2QXUySlh3MHRsc1p0L0xsb1p4bDdIRjVCNE5vNi9Kb1ciLCJzIjoiYzk5MzVhMzA4YjZlYTk2NCIsIml2IjoiNTA1OTlhNjNkNmI4MjU2OGMyOWFhMDRkYTI0MTllYTcifQ%3D%3D&site=https%3A%2F%2Fwww.roblox.com&userbrowser=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36&data[blob]=GF07xZal7Ax108WK.KvSZnSndLxeKYceQwNjjMMu4NYxuZyycKh3m3vcKY01kac5UhxTgc2dEV4c%2F0x7HpX07jL30820qqX5Dy5RSMvUJKUcaaLB5tvWi8XsGc%2FrwnGnTlqUcyB%2FHfICaJdQdPGoFTPjSfw1tEYSIvz8K5cmnEV6hgomSYfFpGkuyEZzU1dfRnPnJLrD2YLu6%2B8Kw0wUUGlv4vk%2Bhq5spPh95pI8bAMz6RXuPkl99uCdDrtV2fKQM0lGfZ1hRV7lOEuX%2BOJE5%2BIdz8NUXZMzOs091aeoYRn7clrPvm2iq8be1sgoxipGvEX0mnhNYWhplQwlKgCFlcorHNGiQKRbZq5lRKtfmykkYWCDiDBCVzcxwOl9zOxF0dl0i%2B64CK6iV4fwJLGhjY3Kyeoly0xDvsS6VRM%2F0%2F3zduxOH99XRHspYUyTW6wTPHGuKDrESHchzdRqBeGqXfjgWXx%2FwkPunTWaNfogyjKB7TXy3E2d9dJzxrDODMORBb6V0LeTBKvo4BM4%2FONXq6I5w19ZpclmYWqkdbYUOio2B3Ymx0XAcxiAPeAYA%2B6BNrpc%3D'

response = requests.post(
    'https://arkoselabs.roblox.com/fc/gt2/public_key/476068BF-9607-4799-B53D-966BE98E2B81',
    cookies=cookies,
    headers=headers,
    data=data,
)


cookies = {
    'ARID': 'U2jMlVBbA6Wd1hT4QvkF1y4FgTsULIgo/l/QhYeUPESvFc8gfnbBQSom1ehkvER+W6si9e+2UpRPqCBoedSIrqoYQ32L01yz8vkR71yW8EZzKU9pKVcH5ugap4BKhlQEjZvxsy1zpUNj2qnpxQk/1axNjybqeZE=**bk1VwwHZBafIVVQP',
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'ARID=U2jMlVBbA6Wd1hT4QvkF1y4FgTsULIgo/l/QhYeUPESvFc8gfnbBQSom1ehkvER+W6si9e+2UpRPqCBoedSIrqoYQ32L01yz8vkR71yW8EZzKU9pKVcH5ugap4BKhlQEjZvxsy1zpUNj2qnpxQk/1axNjybqeZE=**bk1VwwHZBafIVVQP; rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'callback': '__jsonp_1755625150229',
    'category': 'loaded',
    'action': 'game loaded',
    'session_token': '181185d3bc634c9e6.6684639404',
    'data[public_key]': '476068BF-9607-4799-B53D-966BE98E2B81',
    'data[site]': 'https%3A%2F%2Fwww.roblox.com',
}

response = requests.get('https://arkoselabs.roblox.com/fc/a/', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 03 Apr 2025 01:20:14 GMT',
    'if-none-match': '"dbebb932424e9f7599691d0ae24897f7"',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/settings', headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'LoginFunCaptcha_SolveTime_Success',
    'value': '1361',
}

response = requests.options('https://assetgame.roblox.com/game/report-stats', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'hidden',
    'provider': 'FunCaptcha',
    'ucid': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
    'session': '181185d3bc634c9e6.6684639404|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=12|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
    'message': '',
    'providerVersion': 'V2',
    'evt': 'captchaInitiated',
    'ctx': 'Login',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:39:10.220Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'solveDuration': '0',
    'success': 'true',
    'provider': 'FunCaptcha',
    'session': '181185d3bc634c9e6.6684639404|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=12|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
    'ucid': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
    'providerVersion': 'V2',
    'evt': 'captcha',
    'ctx': 'Login',
    'url': 'https://www.roblox.com/NewLogin',
    'lt': '2025-08-19T17:39:10.244Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Suppressed',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_Success',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'LoginFunCaptcha_SolveTime_Success',
    'value': '1361',
}

response = requests.post('https://assetgame.roblox.com/game/report-stats', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Suppressed',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Suppressed","application_type":"unknown","version":"UseLightboxModal"},"identifier":"2ab46d47-059e-47b7-8a67-e61a6d98c2b2"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Success',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Success","application_type":"unknown","version":"UseLightboxModal"},"identifier":"2ab46d47-059e-47b7-8a67-e61a6d98c2b2"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'name': 'solve_time_captcha',
    'value': 1365,
    'labelValues': {
        'action_type': 'Login',
        'event_type': 'FunCaptcha_Success',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"solve_time_captcha","value":1365,"labelValues":{"action_type":"Login","event_type":"FunCaptcha_Success","application_type":"unknown","version":"UseLightboxModal"}}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
}

json_data = {
    'challengeId': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
    'challengeType': 'captcha',
    'challengeMetadata': '{"unifiedCaptchaId":"2ab46d47-059e-47b7-8a67-e61a6d98c2b2","captchaToken":"181185d3bc634c9e6.6684639404|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=12|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager","actionType":"Login"}',
}

response = requests.post('https://apis.roblox.com/challenge/v1/continue', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"challengeId":"2ab46d47-059e-47b7-8a67-e61a6d98c2b2","challengeType":"captcha","challengeMetadata":"{\\"unifiedCaptchaId\\":\\"2ab46d47-059e-47b7-8a67-e61a6d98c2b2\\",\\"captchaToken\\":\\"181185d3bc634c9e6.6684639404|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=12|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager\\",\\"actionType\\":\\"Login\\"}"}'
#response = requests.post('https://apis.roblox.com/challenge/v1/continue', cookies=cookies, headers=headers, data=data)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'rblx-challenge-id': '2ab46d47-059e-47b7-8a67-e61a6d98c2b2',
    'rblx-challenge-metadata': 'eyJ1bmlmaWVkQ2FwdGNoYUlkIjoiMmFiNDZkNDctMDU5ZS00N2I3LThhNjctZTYxYTZkOThjMmIyIiwiY2FwdGNoYVRva2VuIjoiMTgxMTg1ZDNiYzYzNGM5ZTYuNjY4NDYzOTQwNHxyPWFwLXNvdXRoZWFzdC0xfG1ldGE9M3xtZXRhYmdjbHI9dHJhbnNwYXJlbnR8bWV0YWljb25jbHI9JTIzNzU3NTc1fG1haW50eHRjbHI9JTIzYjhiOGI4fGd1aXRleHRjb2xvcj0lMjM0NzQ3NDd8cGs9NDc2MDY4QkYtOTYwNy00Nzk5LUI1M0QtOTY2QkU5OEUyQjgxfGF0PTQwfHN1cD0xfHJpZD0xMnxhZz0xMDF8Y2RuX3VybD1odHRwcyUzQSUyRiUyRmFya29zZWxhYnMucm9ibG94LmNvbSUyRmNkbiUyRmZjfHN1cmw9aHR0cHMlM0ElMkYlMkZhcmtvc2VsYWJzLnJvYmxveC5jb218c211cmw9aHR0cHMlM0ElMkYlMkZhcmtvc2VsYWJzLnJvYmxveC5jb20lMkZjZG4lMkZmYyUyRmFzc2V0cyUyRnN0eWxlLW1hbmFnZXIiLCJhY3Rpb25UeXBlIjoiTG9naW4ifQ==',
    'rblx-challenge-type': 'captcha',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'EceJ2evvGWuh',
    'x-retry-attempt': '1',
}

json_data = {
    'ctype': 'Username',
    'cvalue': 'Ermomhot',
    'password': 'Fuck2020',
    'secureAuthenticationIntent': {
        'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==',
        'clientEpochTimestamp': 1755625147,
        'serverNonce': 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTQ0OCwiaWF0IjoxNzU1NjI1MTQ4LCJuYmYiOjE3NTU2MjUxNDgsIm5vbmNlIjoiRlRDOTlHUFdDSDk5S0Q2TSJ9.GMC4sp1mytWN8-iY-90Q4qonw57CRLaPweU-gMjuKJk',
        'saiSignature': 'P5JZ7D4TNdym0Yd2SPFis4xEHB9xfkuoqQ4sYHm/7KcCBPac6xepnRaii+LY8HZ4rtr/PuqbNVovYmgnXLRbkw==',
    },
}

response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"ctype":"Username","cvalue":"Ermomhot","password":"Fuck2020","secureAuthenticationIntent":{"clientPublicKey":"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Mj50z5fi6x+YWYltJVPpl1Ky+0N1eD/sNgli0/UACv6+O0IX4A5jQdpAStmMQ61VfJ1CM5tFZFoK9ZjdVXYjw==","clientEpochTimestamp":1755625147,"serverNonce":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJoYmEtc2VydmljZSIsImV4cCI6MTc1NTYyNTQ0OCwiaWF0IjoxNzU1NjI1MTQ4LCJuYmYiOjE3NTU2MjUxNDgsIm5vbmNlIjoiRlRDOTlHUFdDSDk5S0Q2TSJ9.GMC4sp1mytWN8-iY-90Q4qonw57CRLaPweU-gMjuKJk","saiSignature":"P5JZ7D4TNdym0Yd2SPFis4xEHB9xfkuoqQ4sYHm/7KcCBPac6xepnRaii+LY8HZ4rtr/PuqbNVovYmgnXLRbkw=="}}'
#response = requests.post('https://auth.roblox.com/v2/login', cookies=cookies, headers=headers, data=data)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'nn35J1ecyP2P',
}

params = {
    'name': 'WebsiteLogin_PasswordResetRequired',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'WebsiteLogin_PasswordResetRequired',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


headers = {
    'authority': 'o293668.ingest.us.sentry.io',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_version': '7',
    'sentry_key': '24df60727c94bd0aa14ab1269d104a21',
    'sentry_client': 'sentry.javascript.browser/9.13.0',
}

data = '{}\n{"type":"client_report"}\n{"timestamp":1755625159.333,"discarded_events":[{"reason":"sample_rate","category":"error","quantity":1},{"reason":"sample_rate","category":"transaction","quantity":1},{"reason":"sample_rate","category":"span","quantity":1}]}'

response = requests.post(
    'https://o293668.ingest.us.sentry.io/api/4509158985826304/envelope/',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/id/login/forgot-password-or-username?identifier=Ermomhot',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'v': '2f89a5fa99eb4cb3591ea59b884e458d',
}

response = requests.get('https://www.roblox.com/js/utilities/bundleVerifier.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/c9148a155e1528ea3ba446d56888266c7556ca38fcad0ca830d9a4c5d8a2d409.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/fd96125f67edabf301d44c9868ab5abbbfa4004ac4465c2e58635cb5912362d6.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/7fc67d38cfc34042bc251805f872ff5be8cb502859e943e5dda46fc3907375c6.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/28d3da7c913edb3c5dfb82f72058178c9ba2c6fb9876b08d73677160922ab903.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/b8f8f15a57a66e73469ae72eea7d8905346afa78b9f2397627cd099f7dcc779a.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/66b2fd496e668938e3b0e2d9a0c12f9f88c3a1a4974608f69059d8061fc0141f.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/99bc7bc872c39ffa5d2bbb936a006c28d743808ba187f992ad896a31618c17cf.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/f77e16b9fa5823882aaa0cdabade9706b9ba2b7e050d23d2831da138a58e5f7f.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/b2cff71de0c286e8f85b1a26a8b87a8cd7f77422c592849ad5114ac5d929c575.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/49fff8dad77e5262087267ee2e8fda1607525506c4a1ca20af60f9757684e980.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/9bfc48ea40a698035ea8cbe3d3e94bd06d3aac48969bedceb6d8ba5ff17ff84d.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/34b79279d9cb0428d155418f3035def3b8d2d3f952fd6dabe06ae28b2eb32afc.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/c82fb4a6d899cf9d43b206512682eaad7feba6102f795b5450923a3d2a2c8f7f.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/7e348738266e9ea2bae9314a2d26b33618c6f4cf3c527b11023620d973c6e7fc.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/945686c706d827658e2e4dee3009559078256e204bb42a3f02fdc6c9552cc7f7.css',
    headers=headers,
)


headers = {
    'authority': 'static.rbxcdn.com',
    'accept': 'text/css,*/*;q=0.1',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'style',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://static.rbxcdn.com/css/leanbase___fb0c7d1e28371fc5e8367ce241b98d69_m.css/fetch',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/d777254408347583551beea274411ceed572e3b23f4b31a2fbf3044bbc672897.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/bc981bafa6b0a52c86d071d1f81b24168a8dd92e72b8ac52d37cb46bf8bd8c42.css',
    headers=headers,
)


headers = {
    'authority': 'css.rbxcdn.com',
    'accept': 'text/css,*/*;q=0.1',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'style',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://css.rbxcdn.com/54928caba64d7d940b99ad67a1cda94892b6d8d9b2f51bba02727df9e1df80b2.css',
    headers=headers,
)


headers = {
    'authority': 'css.rbxcdn.com',
    'accept': 'text/css,*/*;q=0.1',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'style',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://css.rbxcdn.com/2d1c79c2b78e53a2840b1b9a3bc8227a6b0b8dca908068443269b5b3a36ee744.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/7dfc7837b5da6850e13413c630b37da7e88aeb610ca2c7d4e8b71b02cbdc6ba6.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/3c4bd9b17b9020d9ebc87d4542a68a949a9de6150a55a92f0e65514520ee777e.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/1b6cc6d0699561a61e37bae3b8fa07ac5698c5c41c8375ac4f907e189be90232.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/3bca47a98d58fdf98a7063c4f3b390671e5326ed559813887f3945876c997da6.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/d45e200658a1343116bbf4a88c367d093758085e7d001918d641c85b2143468f.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/c5373f0dced8d7be7bb3ad1b978fb8af776157fcc41ad3d5c92d725063c2e6e1.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/d5a3728b78be729b693aadf79a1f45f0fa49c15fe863a0d7dd631b75f9e82207.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://css.rbxcdn.com/c08cc90b15de2ce9073dfcb9c8c3c1facc34dc33b42e94010570dbbb470f9f83.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/fc5032e013a877ae8dfdaf16e906375fc2d37781f22ca2908ee39b163d5e6269.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://js.rbxcdn.com/6f8bcfd33c17e884e38a8dcb89b5da42.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5c8a2ba3737908f693394045e81ebd71c77cde6f87550ea51f7833e8c98200ae.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/2f0fd0c2760ff1898187af6df3b764f4b08f77a315d0a33654f105f61b0ea6d0.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/dd0d34c6d7afd472e5636ca7645e703dd18502fc01c8211279879f64c847dee4.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/f85ce090699c1c3962762b8a2f8b252f0f2a7d0424c146f41d6c5abbf0147a57.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/02a63ed03498b17dc2e133716717d996d9be5ab25ae788ee1234d40267fc2d2b.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'v': '3',
}

response = requests.get('https://roblox.com/js/hsts.js', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c0b9b674b2a87f0aa6358830e63fa62841ce9a3e24f065c5fd33b7e73f22ffa6.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://js.rbxcdn.com/00e1d37a965af4242dc6b296d6c883f0.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://images.rbxcdn.com/4bed93c91f909002b1f17f05c0ce13d1.gif', headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://js.rbxcdn.com/4bae454bf5dab3028073fea1e91b6f19.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/730a5206adda5785166891801b1e0f9ae622a95558b260a144db60278b243f5f.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8c1eaf614415a40296956e4691eaec91600ffb92ef6216d2ac9e92a971d6e3ea.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://js.rbxcdn.com/748a01cf097480a4697d1444783def09.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/bfb3e7a7efed2f8ba4d12dc9fdb70dce1ff97ee13e988833a8638cf3ed8fd7f8.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5a0d69482e170c2b7377a03d75c1c128ce14136f9225520203007e8122d4da2c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/41bd9f2b3a9485661a0c9637526141c355311899d473b7a4ad2cca837f5e47f0.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c27f57f4a397dabc2fe3b74fec93c2401913bdf49373f9339c00b6f18b32d2ac.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/63b59480fef503ff6648900d1051bae7531757a38ce24f77587552fca279d16c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/30a799d27fa08973f1d5b1674a95750924cbdac1ccc76ca27817361001d54bb4.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/d8ebdb41a9d5df4ee618138bca4e1663975b7134d68c138418ad9a76cd031a2a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/2c21e9e061930ad208faef91747c11dc3ceb3115fa75b9e9a0f5b037409cde72.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/f237746d0aea12de9860040043f8d9bee7dab0baf4a87bb6fc87de6d160c4000.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://js.rbxcdn.com/3756ad214dde52cb58a1300177547475.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/94039c6a18f1d31aad2d345a095ac9b7668a378ea4dcadaf5c88f76ec321255d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/47aa20a4d7ec095fabb9db116c99c5c798b2fa37161a5f59a340cb352279596f.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8dfa98e98ef853c2798f8ea8a1f486c63bb5fd40cbd636f7af9d22888c0d5ca8.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/4972161ae75116f48680ae3b6137c1683794a4d48e7f0b9f8443326bffc553d9.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/d9b4f8626ba6e9c4a9b6f84527e222dbb214a0e61e1e43adcc8d71082413d667.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/0dcf101f1c9263155e09e1b1012bd70040ac00d34a6b01d54d0fc3b0eacf1c9c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/215fe9b0fe92491f665645f65f57db6668d716af72e02465db259b715f061118.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/1e979a52d80126c2447674c17604baf65f73183fd44df1e6cd862feb441bdcc5.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/1c8bc37109fd84f255ebad8b6f2edbbc9f0d2b97ef180131d9856ab1852b48c0.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/02ed13a20a4a50ef26468bad76b51aedd8ef9812d5881e9838f870d0a2d4e579.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/7e7e254777b3297ad861dfaae26e13ca6cd0efa8586fd5dd375e32ef0a415a19.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/67eb3a1bc1b5f6968e780734ccb0d41ca6100ed33bdece52792718166967d6a5.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/51c4f4bd1e92885b4faeb2216cd1a0340db56eca4ff990ba495eed0a2ca43d50.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/654ef13ab955a51b3d90e44a1f0c3d911524409fc477f9b4c4985132bfc5c9e1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/81791d9d9f3c1fd273b7d1179ce60bea44c4d2211ba4d784347ee9535ef6499a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c0ad58d64ca1d8f9b43376b105b0889d048f41b26e0a52dc4fc06dd61474c199.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5ed3cf7853ea3f823aaad8bee17c082b64a4b4de2b4916c6b20d5985fbb8ca1c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/dc2cf2e13daeb298bb874d126d8b067c2863c6a8978b4d5046e600e4b598578a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/fe3b45517c518cda98809c915b1ae9575ea97ccff4c05be8e68933e70b15751d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/a9267fa6d3440f80f8ded50aa4475f583c8fbd20df518927674cc92008cb3c73.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c851e5217187d0ef33b1834aad9be04520756a3e48cee5a15ebaa9aded7f46a0.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/7730fff4e1477239840256961802be137c8d5ce6723b0889ac525bfe58a74003.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/2d0a39178b783d4e09a426a042a826da646b1fc91f581c3aaaf26462da283d18.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/995b8771a95f0e5cd5d8cfa1984c78bcb7f8ca9c2472e1cf3253cf913d6ba4ba.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/541a2c06b0dcbe1e2b287c07c1cac903dfffaa0103d4dbed4c96ee990700b5d7.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/6c39ea60ec56be5df71389cf107745e34be8f3b84694cb25d5feb6dc234203a0.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/bd15b4a89fba2137a52116e947e7ad4129e8e3496c63331fcd85d4db733a4cbe.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/d16bb56a77b8920f38b6ed47489d672663cc2178111d6e706fc3a13b33cabcba.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/3a08fa760f713b9a813fd3dd9a287c4a884d420ba55569d691abb51f5d0607ef.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/3668b85e1fa275c3fbdac445d65540631122c3cace07409d57f1fd4b32c9818d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5699f030466d49a7ffaa49f4780409e9f2c4fe7cc6f9801204af0271ac364da9.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/9f93ecf74c3e1644357b3aa7db17bb1dbd2e86da0bab4cd116b9227bae9000a9.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/955567fcee625c9235aea26b45e9b137de9ab1340f359f7b2890c0589415137c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/692e5defd689fa4a13441dccd1f85149097f561bd11743fe46e349e07b384c63.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/45dd9a6e8e3dbdfc18153719b293eff8cbfd32e05b8186a5ed3f15a95f1ecb64.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/b0dc5ac0c220a69861853f497f5e7f690dc4a768b460bbd18bcdb6cc6f08cf22.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/ed49522fd0b1b617240fb3c3cffc90e86c867ddadfb863283393143e84cc2933.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5dd353d7403bdca0ab15e23c428b3ce38691a507ec9bf7773f80c84dd9149770.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/06ad3970b5febcc0e936dea943d90d2adbdf81d11b2faa29dedefd95ec3ff899.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/08d04a5eab233e8d3b2dadae10a9cf394557724da8d5a95a91ff43b9e1a276cd.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/d33ce74e1b98bc070ed4542a3ac39318489a693cd98ce6725624311fd83617e1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/3404f4cd27a8f670cdc434a028a9e7b08deae73bdf89bacd3fdfe469f7da4a4b.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/521820ee43424a5846d5aa06ac88bbc4cb8fc05419dcdb8b3dff29cdb3b74858.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/f6d7d1a6cf6c40a6fb6fb8349d77485ab248475eacfb1864dfbfc512627669d9.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/2df47c668b6a2a7e3b7de775aa9cc6a3e0ca5d755c5970440b0943449b5838ce.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c4b0a446b38285f3db5472340f4ef27d737c87b78348e36dc7acbcfec89d70bf.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/0fda9cfd273e3b66911be0ddc95122a72afdd394fd9d0f3b61f73bea3dbea606.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8889de1e23be3333741bd33377c89e88aeab7998ebf4ced2ea65a96d770af729.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/94f5c1157e96c6895ed1fcdbc03ba1c76d41b1dddc3ff2f5faf31892128244be.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/1fb472f4ffb7f82b3d4fa7df3938a70b5021eb457e187ccca1315181c0f7d705.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/3e7ac6c523a5b50ac227a665953471059676c5bf7daa74ca3799d63b508fbace.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/a97f87397f140a885625b615835376bdfdc14f4f271ac80ca36137c15b34adee.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/60ddd2e451fd1bb0df64b78e010f486ecdc9a94ef809f56e9e327acb537d9cab.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/0df8cd9671f7491ebfabcad568413ac5fa22f22c299ef9e8c505f18fa1bdde1a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/cd456bb506f1b0b06a2eb645ca018d367185ca84725ec00d524e35ce431f4a8c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5b83c64f03d78f7dda0146e136bbd3e077eeb8e93f72cb34696e1efc6d2c6a06.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/a35b5342ceeb69aca44f03fd05d6cf49d8c2ca296170db4e62411a64292b3219.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/90b55ce1b893fce48f63c6321a37dbf97289c65d3a834fa2432369459f3ad519.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/b1f1bf29aeded8f428f8129befa3a5f6a0740858622c07e71496a1939cab7b63.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/26fe7ff8082301c55ee0a9f0412aedaeca56aa7752fdb99bd3cb55508e4e3185.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/378c36d691686a26d3f0d8b0d3bb92a228cd9aa7ffead2c4a0e8d9e330fa0cfd.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8f2404ea3cd842c0d1ffd9bebf673b8572a2935243f7e054eef8fcc7a898f48d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/0f4fec08343bc2e270188e71a54dda56939164b70a17a9fb0655989603c8a89a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/dc442d3486e4f93a4b0e4ffd38f75cb3edc2023aa2b64e13fae8b8d1f3d24431.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/3018b4b81a2b9aa77105c9faf3a33a1d3fc763d0cad86214973cbdab5af3a017.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/6fac7d9e4c52d1abe61e4b00c1d407fecc2bd9698de0b3a781b1f84a8af45943.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/ba2ddb1364a45345d20316073a7bb2a20f942445ac526977a1ab681acaa10cda.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/689e92f57ee764a513aa683f677071ebb20bf3eefbfe1cd95bd9667bfee198cf.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8a0c4978d0e4b101616ae2d19e886d756fabd2ef3ace148eb53abbbf0107128d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/a3cc7f32b1fe5728cb269f944588f14aa3dd42814c98f5ee5967961960297ef4.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/fb311077af827b98eb07e72c4741b4d1a07fe56443d9568a80416fd02d740cf8.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/4c84b332c5a6495043c9bb6db71f2d237083bcfbdb2200d82a3455930f745100.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/98806d314b9f870c03c532361024415ff965072f1bfba496a44bc1d9aa04bfde.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://js.rbxcdn.com/bd55486501ae330c5d4d3df5087ccf59.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/a43e9b89014dcf0cf88d3d3ef1fb2e770eeed0d281dded99fde8ee7262a483b3.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/d89d8f18191398b5eb1d491787e10c4913d8704ce12c032916499071d36ac365.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/dc7856c3e3566054f9b45f915ce7f6b8631f2dac986fd51ef290753688c9251a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5418f00c73c08d3b23c21e9486aaf8de16ee77af85d668428bf542a636103a63.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5e078dbb38a77f6840262e5ba181b8cd4633650a9c92e6b7c36b07d7db32dbb4.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c9ce6459bd9a4ed04a23d157be6365ef74c4993e0756008fcfa0f93fdb20dbbd.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/0821c494a79ed7cbf02c0ec27d680ede7a27efc006f90d6ba6498334d9361b80.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/15a79b2dc71932e749aa68dede97795d296161fb62525a8bbfa9ca9bc42d21c1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/dbc7f7ae0cd8b83ada2cd1ab4642dd9d83a65059db880f4e55981f46910c4921.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/edadb62c4464e0730296467df929e577d274ef9a9793fce59a5007ec3b8c202b.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/cbead6e228035d2c21e48db603d9c9980a99ef5f21b0bc3cceb566787b2a7968.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c369044ce9b2a60366777c8cc797e67b2ddde949e43dd166085603940bd1131d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8b8f62c93ba1f851f40cb89cde8ed4b44cc0f892f0fde805b4243f9fb8b8f6f1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/36126f2c49b9c9ebd1f71b52dcadce2961d90a7eb7203f0c72f2826f365f0603.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/43c65eb03c2fddfb7aa81e4e92eb4fad0d302d328205a1c6e64d8dca3457a421.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/b61c496ad0f03022ec048a17b56773d748d3b5ab8770c9abf42f9d79d23fff9d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/ef0d5bf50bd1c7c225e07156087085a29bb9b23ee09368dee2338a64fe9a7745.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/3f8e434434483277444be52271f30d7e3d83ce0e00218e309bb202c7aaf78502.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/f3864eb4e31b54ec164213463e8c438457336e4db0acf816c645c426f11f9718.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/05355f4f42e31d8469852179b730ec7f252467eb07a3139c9f3c2551f378bb9c.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/a9987af2ed8903db214ccc2cee2749e962bf8aa5c0be8a827af6546e54e04a32.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/814b1df345403bf644b6807b70005fdc67c7ae6eb072a446c1aa95c2226c3672.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/305e90f47e80cf03c8571c8e69c9ef0ec246a4f2f486e83d68c2d5c2c15b378e.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/225bed6650e88e329083fc7ca2674ab5afdac4c70d7cdd8cf877ae985946d82c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/d4b315e3bee4f66ae47fa9bc6b886f0c4ced6cd275176f1ba44acda156f436e3.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/5232cd46bd6ba8ca852187eb998838a2b2ebb307827376c3610074e306622005.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/3b3d5c0a4f69f72d9b42c4668ea9392b1539da869b506fb4670c2d08470712a0.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://js.rbxcdn.com/39021938acae6daa93401fb08570edc575e92b666de335ea2901f7ae58624cab.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/17ff856cc744d543cfd56aa13d5c31a29a19bfc5ff4f5524bccca6f7ae86f97d.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/7ef82dbd60489bc7f46db596141ebf505dfba9b86f97163dbbbcec65728e6c90.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/2d86a5d66f7a4ff56a0ee438807ec1464d3fe4e624aa438bbc01e5f917ee9602.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8016323dc3a7c9f4855285d5b472a7f18124fd1a4f51fad4943ef0ff9626a330.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/652f6e98a4312287b0085945ba8763acbc91da6250b5a76f20284a6165ba12f1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/fb8de862b7fa51dc12e96800cbc339d4eac4131fc0e7834e860e418515687da2.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/426714c4e3ef9aca416ef233c11eea04e1800ecbc5f05b3c64a299fd87e18dbb.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/dda8c538a8ebec4ff978f30540f47d08d2a68424b7e0a41a1b8a1bf633b25066.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c2417a2ce3929d06b61328208953f780fe36dd69f07404e111096c9895b6d27a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/9ccf93e65568293a9d6d037257f446e7f26c3a5cc764663620e3cb3162f7e92e.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/660e0e2b5c3e420c62d740726e7cfc04d1279e8a13cb924f0e7649a4942498bc.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/bd18305af9e4ce41099df37e554eeb1bf2cc139ffba636e356666ccd9d07481c.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/f97eb41a12dc145846afb2e40be96dc9dd4424a5e6e8ca5609e0b1076011675b.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/f579595528e9a1b33d70420581f61fb28d9d96637c37947fc2e07c135a21c928.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/e778966a23e02f475d8725623a8dc21579b54a939c52738ec1b6565dc15be9bc.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/21da704c9991acacddba190a2583329bd2978a35782ebbdc104048aa50d1f2e7.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/1005ee0fb5cbfd9e99d5575c59681fc24aef60ffed860f52b98dc7547f40c496.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/cdd3e1a874aa8ea12dbf80a827a5ef24ff9117149b4bb43cf9b244bd71026c40.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/27b36084b8e8a2834980847abbc534a171f6d3dd846032932aa2c6ebd9ed190a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/fa49b46728d627484c60dc5c5692168826333b0e4fb8cdf0ee0f131dfc0067d8.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/2d85da4f9d2a484be909587bb1490c109d0e2657b9da180d1f0d2bffce8c8508.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/936e553581c22844cdd2c960816ae799225a4a981a7a06fca90995d0aceca5d7.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/c874c33284a7837876f9f02267d7dab86a6a165e1e75534dd5a7491b39a672e8.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/50f891b4a11cfc38b3f5e71ac32d3ae63d0159be98565183e182d85083cef9e8.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8e2f0b0f8947fed790611d72b5888cfc147dc122f6490f97b3222dbf1b8708b3.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/232dd8f620d636a0644040e5863ec1404bcd439bfb27da579770fc9914c14e4a.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/8039fb52ccbc024ef9fa99cf547d4317d584c791675835c7b056a2bbba7f2682.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/18a39f1adad50fcd69442f5ddd58c68c80ee0ff59fadc808ffda3195ceb492a8.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/56728bee27a8608f7bbd04016bc65d1b97165cdd2db169a8fd975dc92ffbb09b.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get(
    'https://js.rbxcdn.com/94386fe7694e4843f7c5884e9b19763c279b340daeb6e2c6c6fa1e6518bbc966.js',
    headers=headers,
)


headers = {
    'authority': 'js.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://js.rbxcdn.com/fbeb250de5f071bcf9dc01d5618097a7.js', headers=headers)


headers = {
    'authority': 'ssl.google-analytics.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://ssl.google-analytics.com/ga.js', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://images.rbxcdn.com/8894c545f59a9020.svg', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get(
    'http://data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYiIGhlaWdodD0iNTYiIHZpZXdCb3g9IjAgMCA1NiA1NiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTExLjY3NjMgMEwwIDQ0LjE2NTlMNDMuNTc3MSA1Nkw1NS4yNTMzIDExLjgzNDFMMTEuNjc2MyAwWk0zMi4wODQ5IDM1LjgyN0wxOS45MDc5IDMyLjUxODVMMjMuMTcyMyAyMC4xNzY5TDM1LjM1NDIgMjMuNDg1NUwzMi4wODQ5IDM1LjgyN1oiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=',
    headers=headers,
)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
}

headers = {
    'authority': 'metrics.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://metrics.roblox.com/v1/thumbnails/metadata', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/rotating-client-service/v1/prelude/latest', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/rotating-client-service/v1/metadata', cookies=cookies, headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'pageHeartbeat',
    'ctx': 'heartbeat1',
    'url': 'https://www.roblox.com/login/forgot-password-or-username?identifier=Ermomhot',
    'lt': '2025-08-19T17:40:27.584Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json-patch+json',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

data = '{"identifier":"e8555554-5d79-4738-a002-409dc74464e0","key":"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEfd4vR5Ho0McD4FcwqkR2/GhpFPjpV1aOz7wWdtqTkVesxKLMTc3JhYZgFTPoalLUhVcUpS43pnQ9CGX4xxItXw=="}'

response = requests.post(
    'https://apis.roblox.com/rotating-client-service/v1/register',
    cookies=cookies,
    headers=headers,
    data=data,
)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/guac-v2/v1/bundles/user-heartbeats', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json-patch+json',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

data = '{"identifier":"e8555554-5d79-4738-a002-409dc74464e0","key":"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEfd4vR5Ho0McD4FcwqkR2/GhpFPjpV1aOz7wWdtqTkVesxKLMTc3JhYZgFTPoalLUhVcUpS43pnQ9CGX4xxItXw=="}'

response = requests.post(
    'https://apis.roblox.com/rotating-client-service/v1/register',
    cookies=cookies,
    headers=headers,
    data=data,
)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'btn': 'GuacMigration',
    'ctx': 'guac_migration',
    'url': 'https://apis.roblox.com/guac-v2/v1/bundles/user-heartbeats',
    'latency': '304',
    'version': 'v2',
    'status': 'success',
    'error': '',
    'errordetails': '',
    'evt': 'guac_migration',
    'lt': '2025-08-19T17:40:28.285Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'identifier': '1755624948360002',
    'labelValues': {
        'l': 'go/at-playbook',
    },
    'name': 'foo',
    'value': 1,
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"1755624948360002","labelValues":{"l":"go/at-playbook"},"name":"foo","value":1}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'authority': 'apis.rbxcdn.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.rbxcdn.com/captcha/v1/metadata', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

json_data = {
    'layers': {
        'AccountSecurity.SelfRecovery.RecoveryUI': {},
    },
}

response = requests.post(
    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"layers":{"AccountSecurity.SelfRecovery.RecoveryUI":{}}}'
#response = requests.post(
#    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

json_data = {
    'layers': {
        'Website.DownloadFlow': {},
    },
}

response = requests.post(
    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"layers":{"Website.DownloadFlow":{}}}'
#response = requests.post(
#    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

json_data = {
    'layers': {
        'Website.LandingPage': {},
    },
}

response = requests.post(
    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"layers":{"Website.LandingPage":{}}}'
#response = requests.post(
#    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://images.rbxcdn.com/dbc562edb12e2e68.webp', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/guac-v2/v1/bundles/cookie-policy', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

json_data = {
    'layers': {
        'AccountManagement.VerifiedParentalConsent.ChildExperience': {},
    },
}

response = requests.post(
    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"layers":{"AccountManagement.VerifiedParentalConsent.ChildExperience":{}}}'
#response = requests.post(
#    'https://apis.roblox.com/product-experimentation-platform/v1/projects/1/values',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'Referer': '',
}

response = requests.get('https://images.rbxcdn.com/8894c545f59a9020.svg', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://images.rbxcdn.com/5a636d4244a1f70a.png', headers=headers)


headers = {
    'Referer': '',
    'Origin': 'https://www.roblox.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    "http://data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' width='32' height='32'%3E%3Cpath d='M7.29289 8.70711C6.90237 8.31658 6.90237 7.68342 7.29289 7.29289C7.68342 6.90237 8.31658 6.90237 8.70711 7.29289L16 14.5858L23.2929 7.29289C23.6834 6.90237 24.3166 6.90237 24.7071 7.29289C25.0976 7.68342 25.0976 8.31658 24.7071 8.70711L17.4142 16L24.7071 23.2929C25.0976 23.6834 25.0976 24.3166 24.7071 24.7071C24.3166 25.0976 23.6834 25.0976 23.2929 24.7071L16 17.4142L8.70711 24.7071C8.31658 25.0976 7.68342 25.0976 7.29289 24.7071C6.90237 24.3166 6.90237 23.6834 7.29289 23.2929L14.5858 16L7.29289 8.70711Z' fill='black'/%3E%3C/svg%3E",
    headers=headers,
)


headers = {
    'Referer': '',
}

response = requests.get(
    'http://data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2aWV3Qm94PSIwIDAgMTAyNCAxMDI0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMCA1MTJDMCAyMjkuMjMgMjI5LjIzIDAgNTEyIDBWMEM3OTQuNzcgMCAxMDI0IDIyOS4yMyAxMDI0IDUxMlY1MTJDMTAyNCA3OTQuNzcgNzk0Ljc3IDEwMjQgNTEyIDEwMjRWMTAyNEMyMjkuMjMgMTAyNCAwIDc5NC43NyAwIDUxMlY1MTJaIiBmaWxsPSIjMzM1RkZGIi8+CjxwYXRoIGQ9Ik0zMzYuMTczIDIwNy40NjFMMjA3LjQ2MSA2ODcuODI3TDY4Ny44MjcgODE2LjUzOUw4MTYuNTM5IDMzNi4xNzNMMzM2LjE3MyAyMDcuNDYxWk01NjEuMTQ1IDU5Ny4xM0w0MjYuOTEzIDU2MS4xNDVMNDYyLjg5OCA0MjYuOTEzTDU5Ny4xODMgNDYyLjg5OEw1NjEuMTQ1IDU5Ny4xM1oiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=',
    headers=headers,
)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://auth.roblox.com/v2/recovery/metadata', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://images.rbxcdn.com/e998fb4c03e8c2e30792f2f3436e9416.gif', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://images.rbxcdn.com/059b09408c6b199c.gif', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://ecsv2.roblox.com/www/e.png?sampleHash=1169.1656403562806&oscillator=sine&maxChannels=1&channelCountMode=max&commonImageDataHash=6735748a8497bbdb12511d15137fe867&Courier=435.9375&Courier+New=435.9375&vendor=WebKit&renderer=WebKit+WebGL&version=132.0&shadingLanguageVersion=WebGL+GLSL+ES+1.0+(OpenGL+ES+GLSL+ES+1.0+Chromium)&architecture=127&deviceMemory=4&jsHeapSizeLimit=1098907648&languages=id-ID&timezone=Asia%2FJakarta&timeout=true&plugins=%7B%22plugins%22%3A%5B%5D%7D&is_touchscreen=true&maxTouchPoints=5&colorDepth=24&mediaMatches=%5B%22prefers-contrast%3A+no-preference%22%2C%22any-hover%3A+none%22%2C%22any-pointer%3A+coarse%22%2C%22pointer%3A+coarse%22%2C%22hover%3A+none%22%2C%22update%3A+fast%22%2C%22prefers-reduced-motion%3A+no-preference%22%2C%22forced-colors%3A+none%22%5D&platform=Linux+armv81&cookieEnabled=true&productSub=20030107&product=Gecko&useragent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F132.0.0.0+Mobile+Safari%2F537.36&hardwareConcurrency=8&name=Chrome&applePayVersion=0&commonImageHash=8237f84114c66a23e106264a76649c4e&acos=1.0471975511965979&asin=-9.614302481290016e-17&atan=4.578239276804769e-17&cos=-4.854249971455313e-16&cosh=1.9468519159297506&e=2.718281828459045&largeCos=0.7639704044417283&largeSin=-0.6452512852657808&largeTan=-0.8446024630198843&log=6.907755278982137&pi=3.141592653589793&sin=-1.9461946644816207e-16&sinh=-0.6288121810679035&sqrt=1.4142135623730951&tan=6.980860926542689e-14&tanh=-0.39008295789884684&fonts=%7B%22Courier%22%3A435.9375%2C%22Courier+New%22%3A435.9375%7D&dataLatency=1881.2000000029802&evt=thumbmarkjsFingerprint&ctx=prelude&url=https%3A%2F%2Fwww.roblox.com%2Flogin%2Fforgot-password-or-username%3Fidentifier%3DErmomhot&lt=2025-08-19T17%3A40%3A30.196Z&gid=-53795620',
    cookies=cookies,
    headers=headers,
)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'content-type,x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options('https://apis.roblox.com/user-profile-api/v1/user/profiles/get-profiles', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

json_data = {
    'userIds': [
        0,
    ],
    'fields': [
        'names.combinedName',
        'names.username',
        'names.displayName',
        'names.alias',
    ],
}

response = requests.post(
    'https://apis.roblox.com/user-profile-api/v1/user/profiles/get-profiles',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"userIds":[0],"fields":["names.combinedName","names.username","names.displayName","names.alias"]}'
#response = requests.post(
#    'https://apis.roblox.com/user-profile-api/v1/user/profiles/get-profiles',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'accountSecurityFrontendAccountRecoveryEvent',
    'ctx': 'pageLoad',
    'url': 'https://www.roblox.com/login/forgot-password-or-username?identifier=Ermomhot',
    'lt': '2025-08-19T17:40:30.238Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/phone-number-api/v1/phone-prefix-list', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.roblox.com/guac-v2/v1/bundles/intl-auth-compliance', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'btn': 'GuacMigration',
    'ctx': 'guac_migration',
    'url': 'https://apis.roblox.com/guac-v2/v1/bundles/cookie-policy',
    'latency': '357',
    'version': 'v2',
    'status': 'success',
    'error': '',
    'errordetails': '',
    'evt': 'guac_migration',
    'lt': '2025-08-19T17:40:30.314Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'showAllPrefixes': 'true',
}

response = requests.get(
    'https://apis.roblox.com/phone-number-api/v1/phone-prefix-list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'btn': 'GuacMigration',
    'ctx': 'guac_migration',
    'url': 'https://apis.roblox.com/guac-v2/v1/bundles/intl-auth-compliance',
    'latency': '305',
    'version': 'v2',
    'status': 'success',
    'error': '',
    'errordetails': '',
    'evt': 'guac_migration',
    'lt': '2025-08-19T17:40:30.602Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

json_data = {
    'identifier': 'Ermomhot',
    'identifierType': 'username',
    'recoverySessionId': '',
}

response = requests.post('https://apis.roblox.com/account-recovery-service/v1/request-recovery', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"Ermomhot","identifierType":"username","recoverySessionId":""}'
#response = requests.post('https://apis.roblox.com/account-recovery-service/v1/request-recovery', headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'content-type,x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options('https://apis.roblox.com/account-recovery-service/v1/request-recovery', headers=headers)


headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'identifier': 'Ermomhot',
    'identifierType': 'username',
    'recoverySessionId': '',
}

response = requests.post('https://apis.roblox.com/account-recovery-service/v1/request-recovery', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"Ermomhot","identifierType":"username","recoverySessionId":""}'
#response = requests.post('https://apis.roblox.com/account-recovery-service/v1/request-recovery', headers=headers, data=data)


headers = {
    'authority': 'apis.rbxcdn.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://apis.rbxcdn.com/captcha/v1/metadata', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'name': 'event_generic',
    'value': 1,
    'labelValues': {
        'event_type': 'Success',
        'challenge_type': 'captcha',
    },
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_generic","value":1,"labelValues":{"event_type":"Success","challenge_type":"captcha"}}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Triggered',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'if-modified-since': 'Tue, 05 Aug 2025 03:34:49 GMT',
    'if-none-match': 'W/"232a87d38e07cd994738a31a347739ff"',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2//api.js', cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Triggered',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'ResetPassword',
        'event_type': 'FunCaptcha_Triggered',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '57f1f859-fb1a-4b5d-be9e-641791b78108',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"ResetPassword","event_type":"FunCaptcha_Triggered","application_type":"unknown","version":"UseLightboxModal"},"identifier":"57f1f859-fb1a-4b5d-be9e-641791b78108"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'if-modified-since': 'Tue, 05 Aug 2025 03:37:19 GMT',
    'if-none-match': 'W/"ca28baf2d673aafd262a5bb8fd90b65c"',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/api.js',
    cookies=cookies,
    headers=headers,
)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 03 Apr 2025 01:20:14 GMT',
    'if-none-match': '"dbebb932424e9f7599691d0ae24897f7"',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/settings', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Initialized',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Initialized',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'ResetPassword',
        'event_type': 'FunCaptcha_Initialized',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '57f1f859-fb1a-4b5d-be9e-641791b78108',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"ResetPassword","event_type":"FunCaptcha_Initialized","application_type":"unknown","version":"UseLightboxModal"},"identifier":"57f1f859-fb1a-4b5d-be9e-641791b78108"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'ARID': 'U2jMlVBbA6Wd1hT4QvkF1y4FgTsULIgo/l/QhYeUPESvFc8gfnbBQSom1ehkvER+W6si9e+2UpRPqCBoedSIrqoYQ32L01yz8vkR71yW8EZzKU9pKVcH5ugap4BKhlQEjZvxsy1zpUNj2qnpxQk/1axNjybqeZE=**bk1VwwHZBafIVVQP',
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ARID=U2jMlVBbA6Wd1hT4QvkF1y4FgTsULIgo/l/QhYeUPESvFc8gfnbBQSom1ehkvER+W6si9e+2UpRPqCBoedSIrqoYQ32L01yz8vkR71yW8EZzKU9pKVcH5ugap4BKhlQEjZvxsy1zpUNj2qnpxQk/1axNjybqeZE=**bk1VwwHZBafIVVQP; rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-ark-arid': '{"ls":"U2jMlVBbA6Wd1hT4QvkF1y4FgTsULIgo/l/QhYeUPESvFc8gfnbBQSom1ehkvER+W6si9e+2UpRPqCBoedSIrqoYQ32L01yz8vkR71yW8EZzKU9pKVcH5ugap4BKhlQEjZvxsy1zpUNj2qnpxQk/1axNjybqeZE=**bk1VwwHZBafIVVQP","idb":"U2jMlVBbA6Wd1hT4QvkF1y4FgTsULIgo/l/QhYeUPESvFc8gfnbBQSom1ehkvER+W6si9e+2UpRPqCBoedSIrqoYQ32L01yz8vkR71yW8EZzKU9pKVcH5ugap4BKhlQEjZvxsy1zpUNj2qnpxQk/1axNjybqeZE=**bk1VwwHZBafIVVQP"}',
    'x-ark-esync-value': '1755604800',
}

data = 'public_key=476068BF-9607-4799-B53D-966BE98E2B81&capi_version=3.7.0&capi_mode=lightbox&style_theme=default&rnd=0.6986439453968671&bda=eyJjdCI6Ijc5YXBnRmtpbEU2cXU0L21zUGtBSTA3aVJnN3QxdURTZkpnNWZZMng1ZkVMZytDWTNEbDcxOWtDUHpnN0xhK3hsT3l2RGZsaWFjOHRDNFdqUkU0Uk44YjFvKzVtMi82KzlwRWZPeGJLcVVxWEZtUVNDMDF0Q1VoSm9jRTRtSWxodjEzZkNiSzJ6UjJjZXA3NmNPTHE3YzJWd0x4SG9FVkNXSnFPaHhLL3laTlRyUjYrckdVbWpWYnVvblFDOXg1L3VDWFdMbS9HSkhadlNXQzF6b2F2V1BTSGhnMzg5SXRpM1pWVE5KSkhlT01waGtEbC9SSk5WTWlOa1VTck53Q3FjSE56QWxLVXE0eXFSZzhmbktzSm8vbUxPa05vQWpyeDNyYVNGOVZNbCsrNjY5bDVkdnJBSFZVUDJEcDdwQUN4NmxhOWZMUlE4clFOMk5VYkVOR0hPL29ydlduYXZFRWpIbUtnKzlMYzY3SExJWDVvRVNwK29WM3VFcUNVRmVOM2Y4elpXZUNScDJlU05Ec1VNTHc1OFZpUjBkbVY1QmxRMGNKeVRZMjFXbU81QVQzK1Z1MDBJLzR3dlltYkJBamh2NXlGNjgxM1FyZlE5SHU4eHNzRHZLZDF4alAvNm16WWxUYVZsbjkrVWE4VnJWM3V1K3JBT081R1ltU3BSMllOVTR4UVJlYnhsdm1pQm5pK1BpUHAzQTlVdEdzQ3gvVjRpanhiQ001dGsreWY2aFRmTXFKUmwyNE9TSFdRa0NqaHc0Q1Q1cC9GRDJBQ2dtQ1BMdy9tM2dkSUxORlZmTWlZQ2Q0SWZBd3U2ZUJXNVNhNHFFWTY1REw0MUh4OTJmMU5KcnJnNTdhMFExZFNyaWhqN2JkVHVKNmVUbnZRbzYrWEwzREZRMEFHVzFHcFhza1JMbHVXdHNHb3EvZXQrUGpwS2V0V2FzS3UxWEpiWXJLaUJIWFUzRnJlRlhRdXNTdHNSaUUrbEt2dTlTK25lV3RIdmJCdGtvdGdDYWpUaVp5SVpHVytVNmNYM0o3Z2xyc3NFLzNhdERseGduV2pFaUZUOTVhRFFTK3g5Y3NjemFZemozeFBpUSsvZ1BBcjFaRC9MQlg2SnJHMmhmaE5lUFhhcXpSSGtjU3ZSaDFxOXY5V2NGQ2ppQ3g3UXYrenBJY0xlSjM1Wkk1WXhLK0Q0TEJjZjYxQ1ZhSytYLzF4Q1NRak9zSlFxRUg5c2FLZWxURUhnc084SkdRL1d6bk9YVklNQytGTXY2WUtJVjZKTUZ5c3o0MEpYK2JZWlY3TmJScmk5ZzUybnFzd0FuLzdtS2U5bm1kTFoyVDdzNmJkNlYrTHVKS3VPL3NyUHhWTW04VVZvdFpaU29MeDBXZHh2K2piWHVqTThqK0hJWmlFdjVsMlUrM2JxWmR0bTl3TXpwaDZWVDVNaTRKVy9WVU1GcTh0UFhjMWx0QjdtS2JRL1l5UW9yOTdFMlh5SUtDbGx4Q3VBcXQ1Wk1uQmgwaGdpYzBZaXR3TnI0dXRCeDVIMGlYZG5LMTk0QzBJTE1HWlZ3MElPbTRsSWhHbDFJNmhScGdNTFU1VXJmdCt4YTdBYXR4emR1dWtsYjFTRmZ3U1pqWSt6VG1JdVpMeGx4U3g2bnR1SjRGNVNnS2I1S05EVHVwWDZEVTQ5WjlTZEhoWUVFT0VFWnorQXJobkczeVBrUlVvVnk3akFDZXVTRXZWNGp6aTNFLzNDMW10MXRYLzA3OHFqeHZvUEU0NXE2WjhQZ1dBeUVDOWlzNjgxK0FyWllOYTdXcVNWd3dwWGhoWWZMMjNkaG9KOTdlbWpCWU9ic3p4NE5qWDNCMTM3Y2owSG1CVE9VUkRwZFRSM1l5Q2dmcnN3L1VBMjlpdUw5NUIydENNN2xqNUpaYzlEajlwUngrWEtSSHBOd0IzZmlHMGZzVXhXbFBtRkxtYVZLbEp1S1RraG1iR0JLeUwxYlFlRXdYZUo2ZlYxRGVRMlB2Ky9ENFhjYllHd1NnTTdXMFVTTnhHR3RoaVJSUTJJeWdKUlZVSUExWm1GZVk4My9jbkowRlZSRCtLNkt6alJVOTlkOFllR0RsSmRXZHUzaDVWSFU2UjNzbU1MVWVveGV3OS8zSVgxNDRiQ0huaDZWQldtVHl2cG4zWk5nL0NTVDFEUE1yVDg2cXNRbEdqdHY4Y3dmYXl2alpzeTZpQjZzV1VOc0xOWUY5TjIwVUN3cVlDNUtRNklqWDlXSFo1bGdyNTdUbGhVSkN0QVBTQ01VK1JSOU9JWXU0bURLQ1hySlF1bGtMOXRqYXYrME5WUGVwN2NPZGJOTzViS29DVkp1bDlCRXA0Tm54U0dFVTZ2ODZ1c1I4aWNDSlYrMlNSd1hnalpWQ0Q5Y0dNMzRCdFVwcTI5RFVvWS96dkM0S01xS3M1dnJnZEVjNTdkOXpzQTNDN1Joeng0cnFTOTN2djBNWEhDVHY2cHVpbHJnTlg2YXN3aGgrYUV3Nk04aHlPdEdPRldHYTFOZUY0UCtqelJkNVd4ZE44ek1xY1BRT2pDekpiN2NVSXFXeFNSNFBpR0dsekNTK0NOTm5QM2lsZG1YcXBsVDJSUEJmaXVYcWt0dVdWM2FsbXFibnZVVG1lUGhBOVkyRUlOUnI3bzRud1pqTENlSllsdHJ3UkdaL21sTzQ5TXpjcXhIWFNncXZmd0lCTkRjNWN5dnNROUhwb2NqZmNyQitZMUVpYnZRdHo4VXprRzc1NUtTVkVOcU9QbXdnaFF6SzhGVXlNZ1BUK2E0QzlMSnJWQ3BIRk91M3FMeFNScitPbjhZQk9RZ0NLYlVwR2M5SHpnK2hCQnMrTGZMN1ozTFV6dUJRaEtoTDM1YjJ6dkl6T05oUElZaVdrRjJuTkR5Y0kxMFRyL0pXcnRCTW9VRlg5YlNIMXVnOGNTMVZYSUo1cUlpNnJQTXBvZ2tiSnJ6YjRTZG12UjkrYlpCQnNQSHhUTkxUZHVXOTZTTUZOTjRFWHEzOVNMbG5jamJUTldYRTZ1amRJZ014eDY2cW9rOGc2eEQyTHZaZmljeVNqcFhHQXFYTWpxcDFnRUNrbDNOZTZEdE90aTBqNjUzcmZob01ET0Z1RzdURHlBUzRmNFZyUEFCTmdJZHpqditOZVAvYkQ5T2NKYUZHMGNFdWlFaEdFbDdpdXREWklhZGREekZNYzYxUitLSnJUQkRNOTF5dGhlWStHbFVMM2FYdnVvczEzV1cza015RjJYcDZpZWU0VXpCY1FhWVVBeHRkMEwvc0hUKzVmaFhKSTg1QSt6bko5N1lCUVgvM0h4S2g0V2w2U01rbDRlUkJqQzlOZzFGdVBRd2p4RTRYOXA0cU9tYjZwM1pxdDBLKytSY0F3bmJ1aFBhdDVMSUFTbDVVRkVDK2o0Q0NEUGV2SjNLWmZHZUJRM1FKV3BnbEhTY1FWN2o1ZzRqaVdua2VQSWc4MEp3Z3ROTkpuVmdWaitNVEZPNTFtcjhkckRpay9Ua1R5bFZ2TGJBN3hzZU5IN0VDOThVR0ZBVk0xUkIrdHFTL3I5aFplVUllSmovRFptT2hwT0k2MEpBc2tnM3RJYUNIcURUenlUUjJQQU1sS1dzaEltUjRnbjhSenVROFB5SWFyb0FlTUpHYjFrQ3BtNGk5KzFLWjV0TndQV09EeG5weUl4aUdlU053QUo2eWtCT3R1YWJhUWp0SlBXdlZqZE8rMWlrZjRvK0FvVmpjUnBHa3ZuQmY1ZlNzWWxRbTYzM2pYZTQyc0tLaXMyOUsydVUvWlE3aytMT0hhMFFrWXYzTXRIMTBLSFpLNHcxNlhQa3dkNExhbmN3TmZGaEE0aHhsdzRBQi95QmkwQURhQ1BLL0R6UEJ6QStmSytscTRjS2dLRHlaSU43ZHRzK2ZPdThHYXJQOEJEcG1yQkxKRzhoVmZCSWl5TmYrUk5hYnQ5WUtxTTVwV0Z0a01GU0VNZjBQaHlRK0RENE1EelA3VFBkYjFMMURGVXhJRmtobERXZFFMSVNaMHFhRlRNdU8yaFU5R2doT3FHbEhoSkZ0a2duZ0lGbHllak5YemdsMFVlT3czZEVJSjVwd1NLQVd2L3M4WGdQWFp4cXU3aGxOWjR2MXZSOWczOWMxQUF6cjZtcEtxUDFQT1gvSUwyWDR4TXBHNzA3aXFLRTl4Q2VDNG5OclIrbk1uTWFPMk84SUlZMytnRk5KMW5hWkZxaUVJTG5lSVY4K0dvWktJaUlDaWpwSGtsc1U0VHhCMWxzQng2NktRVE9LdHVta0hDMFIvWWQ2VXZHTzFzZGY2YTVCL3V5YkhOd0lDVklORStxZFkwREo4aStZVnF5WC9MUndtaEY4UWJxL3psWDlEMVJsNkYzaGZVeDZ3b3FmdDk2WFpxNWJNVTJrektrYnVQMlRKd0VpN0ZST0VpTjhLckJVUWV4K3g0djAwaXJWZFJpbHJiQ3oybmVOMURRLzhOdmlQdlF0dGZJV3JPVEp6bFZRTlF2RDMvT3AyeDRnNG16dlpIZW1EN1I2Q2UrV095YWE1OWJFSHRZNzF1QlhWUkNuZnhVYy9vUUFLdkVkZGRjNkNqVDltVTQ2Q0N3ditNTkNDeUN2a3lPcW1iRDRTZHVxVTZvbUxLR1Y5dVJXekRubUQwd3NGTkhrK2tleVZQbkJrMGIrSXJxQnE3Q3haK3pwU0pKaUtqUmN6TVNkcGZuNkgyd0xJdFpDTHVXSi9jeW12dmpOd2VlWnVxOXFSNUJ5QW1Ba3pOd29lSDdVMXdZWFNIOStoWVBZak1zL2JjblNITGo3a3g3OFNVUTd4NUtpOFZLV05qdWpwQzNQRVNJVm9sVkt1WFBNaEhsRkptcktBNjdlM0R5S3RpMS9xRHV4TlpKTnlGNFdGUUhRSk8rMUpPSlFNYXVBRUZSeDgrblI2WUY5S3BiU29FQnpRRUQycjhxMHpNUFFxZm1kVnJxeHB2NURkeTVSQ3ZLVG4vUVdRdmgvYzcwcmlDSEg0dWNuOURicXhoZUVtMVdORWpVQlhiQ1B6enlUeU1Cakl1Vnd1UThTeHlHV1JSdUJpN3NjV28yWmI0ZU1NdkwxMHFBYXptZGVCRnJzWXM0dTlNUEhDWUpoWXRsbXBUWlpqdlpjeU0wV3MybDRYWVA2dzVPN0Zac2V0YWNMUTk2QmdGNVhjYlJrRjBGTDNmSTVHdWRTQnhaZTFpNTBpZ1EvYnF1T0MybkRHMC9zUlord0lSRWJ5cnN3VXlFZnM4cFJ1Q1pXNWFGVVBvL2VCWlptTTB6bG42NDRxTkRZRCtOQU1VY0JsYWFBekFpVklPL2JEVXl0L1dvenQyUUpBNEZVejRZc051LzVzTjJibmJuMDA5WGFBdTN0MGtsQnBWcnE1TG1vVTM0Wm5hL01LQjFkVE9wdTArUmhrR2s0TTdpb0ZXam5HaStES244dDJ5WkliaXl4RmpVN1liSHRpMTFJQU96U1pGejd0bEJkMWg3OWFNdmpDSlhzczVQajlYNnBrSnJKcko1bjlBM01ibWk5b2FiTEN0Tk9YNnR6R3Mxd2hvdHZtNUZDZW9ZSkZCcmhoUWIxTm1CcVZwRnYvRldSY3M0NXMyTSt1RHkrK3N6M2s2VEZrVXlWVUljZzdUVm1NT2d4cHpxU1pHSzFrUzVvZ3M4OHZRaldwU3VTcjR2VnRTSkYwWWN3SUNRenlRK2l5b3pPMGdzK3c2aGErejZrWjBMT0xPOHhzNWdTNitIdXJvMnR0Ykh3aHY5RnZBcGUwOUNYRU9pL3pvUU1JRTA1eHNLcFFvaDRSR1IxUGJhaU1ONThjczh0REhqSytQTUo5a3I2dVkvR1hmbWhtdUtwOE1XWVZyb1dOcHc5YUg5MUlaK2VyY29ONklFR2RuSzExQXFBT1lMa2RudnRUUjdFcXdUdy9NV2hEK1dzZ1JsdnFvWTFVUTR3dUw0QnhTcVdveFFHUWFPZFBsSVlRUTB5dFlpaUN3RkZ6YndHSVZ6aXNoMzFOT2VaWjkreHJrNnY1QW80aVAxZEhkWWlxODRqMnR5REdwQVEvc2wvRmdwSHhLOXBXY2t3bU5FSmJETzZqTFEwaThobERqTzJlMHpMM2RkUmR4MlUwdUVIbjlrMkhUSklLK3lFa2NGeE55M1NuVGdHOEhwUkpJUFc5eU01NXpoS1ZLeVdSL0xBQVBtOUJPSlJBeFBreGpQZmFmeXkxd1d3MkhzK0tjSjlHOGx5RzQxNjdWc0YrNWx5TFc4WlN1eDBkdEpZQnJHVU5rOFFuY1RFdHhtWTE4ekVTd05YQzlQd0VNN3BpeTdjbXJGNEVsRkJVSC93NlluNytCNUxqTmNYdWxML0oxeXgvbGIrSE1EdmdwSFdlTHhma0hta0FKTmVSN2c1SzZjOXBYK3NmUWNsajNGSXhHck41OHU1aFBOclVBOG1od0hFTG1ITUk5TVcybGlBVndyNmR5L1FmU0IxaCtVNkVrVW1HclNZUFl6NlFZQUVROCtNUytMZ081eWZvZE9uTTJyR1h5SUl5OHFPQVFkZUhERFRtYXR3bGdvUWVVM2VJUk9Db3VSWXN5M0RlUlJoMjV4MlNDLzBYM2wrQzdHUkVWL0RDWVFYUHJqaTdEbEZjTXA1STl3L3BZUyttbUxndmF3Z3NtWlVVQkFVYnQwUTFuSnZGZ2l0UzJBTjFlSFZXb2U3cU1kc2UxclEwNVhVM3MyUXc2elNrQU5ZRDU1Q01UNUpHNjE1TDFFeDAybzBmZE8vR0hoT0NQWjhqZitqdCtKUjA1bk9sZlA0SmM0b1N5ejZ1ODJkV0ZqM09vaFBobENSTnN3UDJlU3lCN2JXdGFDVVVIOHFPcVBvRnpYMDlkRUNZb2IyZUNvTmlzdlo0WUZOWjhyeC9SQzc0WCtaaDJUVEJycVRmWmFjREFsQXRLK2k3S1ZOZW9vWTI4VS8wRm9ldFpZbU1kQ0wwMDEwR1JWVk92b0dYN3hCZXRrZlh1Zm1YSW1rR3R4bDdpditreGVoNVVzWnNHSU13SGs3ZlV4WloybTVqbXp4WlpkaGx6K292SnF5M0g4YUdaaFZVVVpRMWtJNk1wVHVmNHRZcVhXMG1Zc3hxcUI3VFNhcmlMYzFaaFNBYURpYlVZK0g1b244aC9JWEFNQUZ1Y1Nzd1ZrejFBWGxjd1BWN3ZMUHhuYnkxSDFZMWhCZ2k2b1JhRUZJYzVMbDFiSFdWWmpxSjYvbkcyTjFMOFdsaVplMGR1REtMc0tSU1hjWGVQV2w3R241SDBrVlI0T2tyZlFNbU1sZTVZeWJSQXVBdVB5bFE1ekp5ZnNhZXd2MWpueWt5eFhBTXUyUFh4T1c3SlJKT3NqSzJaM2I0Rlozdk5DeGh5R1hPNktRMEVnVjIwc0sxTDU0TzloajlCcGNHelYrQWdrSHlXK2VVUWdaMmJEVDlEWmNzWlJGTUZPVnNPNkdkU2NXVnFGZGpoZThjTGI3TUpMODdWZnNwVG1PaTJUeHRPSkw4bUkyUFNPV25lanJ4dDk4bHpvSnJ1eW4zeEEweUtudXlORFB2UFhSZmtYTDhjMkpFcXFhcGNqZ0lUSnIxUWVtRy9RcSs5TC9PNk5pWC9ybGFnWFNZRmp5MDlrRGNmdGJTV0lrRjAwQWFTTmNpallZN29sKzdKKzIweVhIcjF6MlNBOGJneGdScGlLTFR1elVsVWgvdnZqdnhwdWwvb3d2WHYyTE5BQStTUXFoS3lGRE83VWorL0JRVGZvTHY1bkhJRGQ3alplWjZQVENNUTZiU1oxcjN3OXNzSk1Fb2RjTzllaS9IRWZQUXRXbnZNbldnZUw4NklnaXB1a1kxUnVzbmJtQXJDNy9wZFlHQWdnLzRibG5JNFJzcTV1Mk9rdWdtajR2UTdUdlBieWZUdnhPSDIySXA1VnlkMHhKZkJoakhuWWVHSTFXZktHWDRCc1NmWjJCSEVuUWt0MG5Rc2tYanYwdVIrZk80Y0RSSXY2bG14VldRNTFrRlJJKzM3M3pHcXBwVEQzTmkzYUNFLzBEdEltS0hMMERYNmdIUlFZclBSZXRGZGJFbkI3S1dQOUxQMUxrUmNHZUxzSkZNaHMrUmNUN0ZRdWhFbUlDbWpCTURYZERMZnBaa3k3b2wzOG01c2VtUldDeHQvWGQxUGhuQ2VGNlBrbHVPeGFGYnlFWFdDVTR3Tmt6VTNPRVdsakdaUmNITjVtV3dsNXpJaGJjdjRVSWpmNTNFcmhZSXN4d2RuRlJuMWdIRU9YaDhpcFlMZ2NZMVMwRi9LZ0R6VzROZjQwVys5eEtiN0Ixcm83WVQxTHBmZEtYS1BqT1N4YWxqSHNWeXkxbXg5anRidklrWGY4LzRZY1NJTXY3NGJYRjJJTnNrTzdWVFBsNGRQbzBNWnF2WDg2T2dQc1ViTVlDQzhVMWtJbFdCRGpDUGxqbVJocXBEY2J3Q0dLS2xacE9JeUp4Y1ZrdkE4bGxxWVNuMlQyOEsyalBybkRKakEyaUJiOUdpeVNoVnBKbGZGQWVBTXNoWi9wQlFadVBrL3VpQUUzWS94MGIxYmpzZnhWbTZzaXJIZ056cFVGempFNU41ZVNldWRobExtQTlydHM0MG9CUDQra0FvaFVtZG5pTVVMdWF2aHNoQmd5UTR2cUU5L0tGNjRXRXJQbFQvOVVmUGo5QzF3VXhhN3ZqdGYrTXJOalFMYzJZZXp5dDhTNVJDOE8yL0FVQmlhOXRibUFrV040OGs0Qlc1RExtRzgxWlJmeG1vVnhCYnNWOStsR21HU1RzclpJbnJxbFZGbmJQR0dkeXlKaG1mQ3ExbkpnT24vOWdPUVUvazdRM3JjQXhhVzBMOVU0SzcwNFQyMjBpcis3WWVsUzZmekxacTBjMVhrTmpiVmI1NC83QjVxcFpVS2VwTlc5aFViSkN6RDdrbDFFNjd3UU1PdXVFaHovSVRQOGtHWU9IazErQ2MxdThWWmxVL3k2WFFGYVdpbEEweUgrc3BldWlnTGNlb015Y3NlWG5xZmR5Rjh5Q3hoaUN2aWFjdzFwMkRhMFRlVVJUV1BCNG1US05nWW9iOUxCNE5KRUR0Ty9abk5rQnAxM0I3aDNaZGFJYmF2SXRGeWJGc3VISGM1QUVzZzRwcnBxckhuallyT0dFaGJOZWZwTGFzVEFDMDUwLzczOHFZSTlleThNOWJzODE2OEpqV0xRNzNEcVhaM2VQTDBqanRzRGthQnovWWtOMU1WM2dtMWpNaCtYM2N6ZXByYjNPanUzNlNkaVBSS3FBbUF1YjRqZ3JDbWJoOEJWcGErRFEraGdrRjhFb3lGaW04WEpKVVF5U01mQnE1ZUtwVzQ4N2JMZm5Qb2hJd0QyamdmQTdZUVMzc3lNVDM5UkFTSmVQQ0dmSXcwMy9YM0RMTVE1VzNlNTlGTGZ4SmgzVG1zTkoyOFNOc1ZFcEZLdExTMmZtQ2s0SzF6YUltR1pCeTRPV2tvTXJvdDRkZlh2Tlc0eTlqNHo2WDBTWXBVOTNCeVR6bVBzQW5vZjNiUm5HZ0Z1VjluS2diMi9IV2FvNmVML2YrdFR1UVgrT09pQ21YUnp3WEpGdHJKbEJUNjNKWlcyTmdQcmFvdG5nMHZKYWw0UjVxdm1MWlhoYitpR1F3VEZCN05RbGsxRDVDbGFLUWpxR1pkeG5YZjRrNEVxRUZUMEJ5d29JWStNZ3BwT1BtRnJNSytkVWN2R3NQNE5scTVGU3BRck1meHd4blY1bk9HbVQ5V0VMZEp6NWRFdEVOV2lMR1UzeGt5ekI5TmdHb3Y5R1J4ZEx3OXV2MHlsVUlzb1ZDRm1LalNVMHZ1Y2ZZVXhjQnRuSDZzUTlGOW5oeVVRNXp2SnJLYW1qNHdINWtMT3phTTN1ZWE1dng3aUFJWWNFdlRwbVFGYXhFZHBRREl0U3BsZHAxQUdCTm8vTDJkdVhSV2tPcjhHdVgxSjVzNE44WWo1VmVJSHBPT3JZVnh2T2VaYitWWkJoOWs0bnN0Z0dqbmhzSEVQNWpQdnhCa2h3M1RrSE16Ym9qYWpWSVR5eDZUOE5MZ1ZWcnJNS1lPRFh4SlNLWVM4YmxnakVKK1R2Z1hDMWhpNDNWdUprVEtrK2hkcVV3NmJsQW9BTUtzOWVQOThUQlMyVVp1eHc5NmJKck10RFJ0NWNrUmhWSERmaVUwZlkyaS9YNFBKZGtDTXZncGFZQllOajJlUnJvcmhrSXhhS0MxNlFZNm1taGJpR2hPTHJzaXdyTVFrNWJXYkxWOS9iUW4xUzlWZnZTdlg2dnh0UmhBc3JBWDJMdFNqKzgwdWgxRFlDVm03bkVtc2FJbDhJZTVGS2VoUlVwWHhmVlRwL2t0TVdMbjl4YzFSbGl4eW5HOUd0dFdhTUNhNmRiZFBTOFdnb2dpekNZK210ZjhUWktNTHFNMmdqVzIwUEZ5dVJ1QVRDUkJYRi9qSkJZUkVMVW1GWjlaeTYydTJGcEU1L3ZJSk1CWFpDaUtCVm1LYlhSdmdKS3NRbHZVOTBYOU9QNzMxSndzZXRBUVZRQXVLellGRkpudmQ2WVZkTTZVYjlqVHo5ZVRqZ2FZck5zL2J2UnJJZzdxa2duNFMyZEJ2SVZoMEtKbFlIKzBZc1pBa0hZK0ZXbk5LODNSblFIZEJVS3ZnbXMyejhVNW9UajFvRWF6MS9sN0Y3dEs2OFFwTlFDY2lsRUNHSzZMYzY4TTlVYzZVS3VaOVpWN045R01rU2RNYUdvdmpGSFE3aWg5RFFCV09jK1pab1JFRExLVk1VL295V0l5aERMSlFrYXlYM1p5dmZic0NhVW5NbTV1NGpxelFSVlBSMVVNMXlvT0dwMjZLSTVTdFJYOUhUb0x3Wlo2OW92N1ZrTFFKRmpiOExuTVRDdUF3L0xHRXRnQkVGV2xERCtlNUNKdStUd0dXZElFS1dDQ2ZwUDZMYytIQm1xOWRFdzNQQ3NqZnI2UjcyRXhaL1FSMHpqRmN6SVUvNlpVWklEUnRydnBsZllDMDNyTGJ5WlVTWHdpSktmVUFyRGg5WWhFN3RKUWpMZnVJaWFwbytjMDhaais1dWYxMEtPUnBzcE04YlFYY0FmczZyUVZzZzZBa216NEpvR0JoSDVzalZrOXhkQVRIRVpBL1dWIiwicyI6IjcxNzdlMDIxYTQ2MTMwODYiLCJpdiI6Ijc5MmZhMDQ5M2UzMWM1MmFiZmZkZTM0ZmUyOGNkM2JmIn0%3D&site=https%3A%2F%2Fwww.roblox.com&userbrowser=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36&data[blob]=GF072PZ1hGIDBSwa.SBW4bqhGsCq4GStOfSumHyt1KLlqJv8o7lukp8tG08PaFNBK7jLW3xrxOwDDgH9%2B8DZ7aPCwwEAvBOhPRQruul5LrJIMJydoRvvplCO%2BLU65R2F%2B2ZMJEDNX89Zv%2FaAraTQq6yz%2FqZCCDFw%2B8gCJVh4uGs89uhtFEhb6u4%2FSmKks54ggfSqTQRuHmelpC852j%2Buzu3jYNC1H2Grz%2Fn46295bCEMwfxWBhQ4QrZ8gdlu%2B7qQg7F4dpYA1GnoxyYKdIFCA19sBfELcnkvOIELXvGmUrljPyRjiGUz1eAPC2WwPEGThfrDC8BLnFOqUgdsrCcFn9J2%2BzyD1o9WjN9GKocMLkdAuRVG4AfVfsox2m%2F8BksGhzIySsXWex2fIOcqq0WZ3ohGJCNA6qp612BQf7w2fIx59uBa9sYNu6ipEK2X8P%2FrW77TdvzjDBZLy4I2NpWFQUg8OtcdcaLn3yAdcRfnR4i6TgRrWFkpVtTyc7PbuMArO9WzdFimmAvRwwYFdhhCGK7PfklgUI4L1vLG578fM720ekb7nERc8aIgfdVXpiw3zV7NvXY3FG5itWQ%3D%3D'

response = requests.post(
    'https://arkoselabs.roblox.com/fc/gt2/public_key/476068BF-9607-4799-B53D-966BE98E2B81',
    cookies=cookies,
    headers=headers,
    data=data,
)


cookies = {
    'ARID': 'hd8TI4vUu2PqwLrDZtLinTmBGE5uoFLoqFNats9oWsr43oFSRNwkTsIUdqjEudK2/jX5QP9NIF0RO0INgw/jal9nPy/c4lzp5oxeqyHidoO6avFY1TK1+uBtUQy0us/eqm5MwKe6XRTL3jHv6UcTXc0UNs95abo=**vbubZcEFDGa+z4jd',
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'ARID=hd8TI4vUu2PqwLrDZtLinTmBGE5uoFLoqFNats9oWsr43oFSRNwkTsIUdqjEudK2/jX5QP9NIF0RO0INgw/jal9nPy/c4lzp5oxeqyHidoO6avFY1TK1+uBtUQy0us/eqm5MwKe6XRTL3jHv6UcTXc0UNs95abo=**vbubZcEFDGa+z4jd; rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'callback': '__jsonp_1755625232682',
    'category': 'loaded',
    'action': 'game loaded',
    'session_token': '687185d3bd9473cb4.3644179604',
    'data[public_key]': '476068BF-9607-4799-B53D-966BE98E2B81',
    'data[site]': 'https%3A%2F%2Fwww.roblox.com',
}

response = requests.get('https://arkoselabs.roblox.com/fc/a/', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'arkoselabs.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 03 Apr 2025 01:20:14 GMT',
    'if-none-match': '"dbebb932424e9f7599691d0ae24897f7"',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://arkoselabs.roblox.com/v2/476068BF-9607-4799-B53D-966BE98E2B81/settings', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Suppressed',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Success',
}

response = requests.options('https://assetgame.roblox.com/game/report-event', params=params, headers=headers)


headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'name': 'ResetPasswordFunCaptcha_SolveTime_Success',
    'value': '1016',
}

response = requests.options('https://assetgame.roblox.com/game/report-stats', params=params, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'hidden',
    'provider': 'FunCaptcha',
    'ucid': '57f1f859-fb1a-4b5d-be9e-641791b78108',
    'session': '687185d3bd9473cb4.3644179604|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=8|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
    'message': '',
    'providerVersion': 'V2',
    'evt': 'captchaInitiated',
    'ctx': 'ResetPassword',
    'url': 'https://www.roblox.com/login/forgot-password-or-username?identifier=Ermomhot',
    'lt': '2025-08-19T17:40:32.676Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'solveDuration': '0',
    'success': 'true',
    'provider': 'FunCaptcha',
    'session': '687185d3bd9473cb4.3644179604|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=8|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
    'ucid': '57f1f859-fb1a-4b5d-be9e-641791b78108',
    'providerVersion': 'V2',
    'evt': 'captcha',
    'ctx': 'ResetPassword',
    'url': 'https://www.roblox.com/login/forgot-password-or-username?identifier=Ermomhot',
    'lt': '2025-08-19T17:40:32.696Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Suppressed',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

params = {
    'name': 'ResetPasswordFunCaptcha_Success',
}

response = requests.post('https://assetgame.roblox.com/game/report-event', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'assetgame.roblox.com',
    'accept': '*/*',
    'accept-language': 'id;q=0.01',
    # 'content-length': '0',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

params = {
    'name': 'ResetPasswordFunCaptcha_SolveTime_Success',
    'value': '1016',
}

response = requests.post('https://assetgame.roblox.com/game/report-stats', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'ResetPassword',
        'event_type': 'FunCaptcha_Suppressed',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '57f1f859-fb1a-4b5d-be9e-641791b78108',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"ResetPassword","event_type":"FunCaptcha_Suppressed","application_type":"unknown","version":"UseLightboxModal"},"identifier":"57f1f859-fb1a-4b5d-be9e-641791b78108"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'name': 'event_captcha',
    'value': 1,
    'labelValues': {
        'action_type': 'ResetPassword',
        'event_type': 'FunCaptcha_Success',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
    'identifier': '57f1f859-fb1a-4b5d-be9e-641791b78108',
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"event_captcha","value":1,"labelValues":{"action_type":"ResetPassword","event_type":"FunCaptcha_Success","application_type":"unknown","version":"UseLightboxModal"},"identifier":"57f1f859-fb1a-4b5d-be9e-641791b78108"}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'name': 'solve_time_captcha',
    'value': 1019,
    'labelValues': {
        'action_type': 'ResetPassword',
        'event_type': 'FunCaptcha_Success',
        'application_type': 'unknown',
        'version': 'UseLightboxModal',
    },
}

response = requests.post(
    'https://apis.roblox.com/account-security-service/v1/metrics/record',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"name":"solve_time_captcha","value":1019,"labelValues":{"action_type":"ResetPassword","event_type":"FunCaptcha_Success","application_type":"unknown","version":"UseLightboxModal"}}'
#response = requests.post(
#    'https://apis.roblox.com/account-security-service/v1/metrics/record',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = {
    'challengeId': '57f1f859-fb1a-4b5d-be9e-641791b78108',
    'challengeType': 'captcha',
    'challengeMetadata': '{"unifiedCaptchaId":"57f1f859-fb1a-4b5d-be9e-641791b78108","captchaToken":"687185d3bd9473cb4.3644179604|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=8|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager","actionType":"ResetPassword"}',
}

response = requests.post('https://apis.roblox.com/challenge/v1/continue', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"challengeId":"57f1f859-fb1a-4b5d-be9e-641791b78108","challengeType":"captcha","challengeMetadata":"{\\"unifiedCaptchaId\\":\\"57f1f859-fb1a-4b5d-be9e-641791b78108\\",\\"captchaToken\\":\\"687185d3bd9473cb4.3644179604|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|maintxtclr=%23b8b8b8|guitextcolor=%23474747|pk=476068BF-9607-4799-B53D-966BE98E2B81|at=40|sup=1|rid=8|ag=101|cdn_url=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc|surl=https%3A%2F%2Farkoselabs.roblox.com|smurl=https%3A%2F%2Farkoselabs.roblox.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager\\",\\"actionType\\":\\"ResetPassword\\"}"}'
#response = requests.post('https://apis.roblox.com/challenge/v1/continue', cookies=cookies, headers=headers, data=data)


headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'rblx-challenge-id': '57f1f859-fb1a-4b5d-be9e-641791b78108',
    'rblx-challenge-metadata': 'eyJ1bmlmaWVkQ2FwdGNoYUlkIjoiNTdmMWY4NTktZmIxYS00YjVkLWJlOWUtNjQxNzkxYjc4MTA4IiwiY2FwdGNoYVRva2VuIjoiNjg3MTg1ZDNiZDk0NzNjYjQuMzY0NDE3OTYwNHxyPWFwLXNvdXRoZWFzdC0xfG1ldGE9M3xtZXRhYmdjbHI9dHJhbnNwYXJlbnR8bWV0YWljb25jbHI9JTIzNzU3NTc1fG1haW50eHRjbHI9JTIzYjhiOGI4fGd1aXRleHRjb2xvcj0lMjM0NzQ3NDd8cGs9NDc2MDY4QkYtOTYwNy00Nzk5LUI1M0QtOTY2QkU5OEUyQjgxfGF0PTQwfHN1cD0xfHJpZD04fGFnPTEwMXxjZG5fdXJsPWh0dHBzJTNBJTJGJTJGYXJrb3NlbGFicy5yb2Jsb3guY29tJTJGY2RuJTJGZmN8c3VybD1odHRwcyUzQSUyRiUyRmFya29zZWxhYnMucm9ibG94LmNvbXxzbXVybD1odHRwcyUzQSUyRiUyRmFya29zZWxhYnMucm9ibG94LmNvbSUyRmNkbiUyRmZjJTJGYXNzZXRzJTJGc3R5bGUtbWFuYWdlciIsImFjdGlvblR5cGUiOiJSZXNldFBhc3N3b3JkIn0=',
    'rblx-challenge-type': 'captcha',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
    'x-retry-attempt': '1',
}

json_data = {
    'identifier': 'Ermomhot',
    'identifierType': 'username',
    'recoverySessionId': '',
}

response = requests.post('https://apis.roblox.com/account-recovery-service/v1/request-recovery', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"identifier":"Ermomhot","identifierType":"username","recoverySessionId":""}'
#response = requests.post('https://apis.roblox.com/account-recovery-service/v1/request-recovery', headers=headers, data=data)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'apis.roblox.com',
    'accept': 'application/json',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'n4LJ0qecHaLZ',
}

json_data = {
    'userIds': [
        3586276342,
    ],
    'fields': [
        'names.combinedName',
        'names.username',
        'names.displayName',
        'names.alias',
    ],
}

response = requests.post(
    'https://apis.roblox.com/user-profile-api/v1/user/profiles/get-profiles',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"userIds":[3586276342],"fields":["names.combinedName","names.username","names.displayName","names.alias"]}'
#response = requests.post(
#    'https://apis.roblox.com/user-profile-api/v1/user/profiles/get-profiles',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'recoverySessionId': 'e8bdf611-5edf-4603-9eb4-5bfcd46bef36',
    'identifierType': 'username',
    'nextComponent': 'sendCode',
    'evt': 'accountSecurityFrontendAccountRecoveryEvent',
    'ctx': 'recoveryInitializedFromAutofill',
    'url': 'https://www.roblox.com/login/forgot-password-or-username',
    'lt': '2025-08-19T17:40:34.354Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'thumbnails.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = [
    {
        'requestId': '3586276342::AvatarHeadshot:60x60:webp:regular:',
        'type': 'AvatarHeadShot',
        'targetId': 3586276342,
        'token': '',
        'format': 'webp',
        'size': '60x60',
        'version': '',
    },
]

response = requests.post('https://thumbnails.roblox.com/v1/batch', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '[{"requestId":"3586276342::AvatarHeadshot:60x60:webp:regular:","type":"AvatarHeadShot","targetId":3586276342,"token":"","format":"webp","size":"60x60","version":""}]'
#response = requests.post('https://thumbnails.roblox.com/v1/batch', cookies=cookies, headers=headers, data=data)


headers = {
    'authority': 'thumbnails.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'content-type,x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options('https://thumbnails.roblox.com/v1/batch', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'pageHeartbeat',
    'ctx': 'heartbeat2',
    'url': 'https://www.roblox.com/login/forgot-password-or-username',
    'lt': '2025-08-19T17:40:35.603Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'tr.rbxcdn.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://tr.rbxcdn.com/30DAY-AvatarHeadshot-56740BAC2377513BA7122FA62B8B674B-Png/60/60/AvatarHeadshot/Webp/noFilter',
    headers=headers,
)


headers = {
    'authority': 'thumbnails.roblox.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'content-type,x-csrf-token',
    'access-control-request-method': 'POST',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

response = requests.options('https://thumbnails.roblox.com/v1/measurements', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'thumbnails.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id;q=0.01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'bcduwkJ7Km8f',
}

json_data = [
    {
        'metricName': 'ThumbnailLoadDurationWebapp',
        'jsonData': '{"Status":"Success","ThumbnailType":"AvatarHeadshot_2d","Value":"1937"}',
    },
    {
        'metricName': 'ThumbnailNoRetrySuccessWebapp',
        'jsonData': '{"ThumbnailType":"AvatarHeadshot_2d"}',
    },
]

response = requests.post('https://thumbnails.roblox.com/v1/measurements', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '[{"metricName":"ThumbnailLoadDurationWebapp","jsonData":"{\\"Status\\":\\"Success\\",\\"ThumbnailType\\":\\"AvatarHeadshot_2d\\",\\"Value\\":\\"1937\\"}"},{"metricName":"ThumbnailNoRetrySuccessWebapp","jsonData":"{\\"ThumbnailType\\":\\"AvatarHeadshot_2d\\"}"}]'
#response = requests.post('https://thumbnails.roblox.com/v1/measurements', cookies=cookies, headers=headers, data=data)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'userInteractions',
    'ctx': 'touch',
    'url': 'https://www.roblox.com/login/forgot-password-or-username',
    'lt': '2025-08-19T17:40:39.330Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


headers = {
    'authority': 'o293668.ingest.us.sentry.io',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_version': '7',
    'sentry_key': '24df60727c94bd0aa14ab1269d104a21',
    'sentry_client': 'sentry.javascript.browser/9.13.0',
}

data = '{}\n{"type":"client_report"}\n{"timestamp":1755625242.948,"discarded_events":[{"reason":"sample_rate","category":"transaction","quantity":1},{"reason":"sample_rate","category":"error","quantity":1}]}'

response = requests.post(
    'https://o293668.ingest.us.sentry.io/api/4509158985826304/envelope/',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/4c743bff28f5258a.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/3ca2abec930f1eb7.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/91232d2e89d6197b.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/575eb3b900ffeaf9.woff2', headers=headers)


headers = {
    'Referer': '',
}

response = requests.get('https://css.rbxcdn.com/da4d20fe0c89fea3.woff2', headers=headers)


cookies = {
    'rbx-ip2': '1',
    'RBXEventTrackerV2': 'CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002',
    'GuestData': 'UserID=-53795620',
    'RBXPaymentsFlowContext': 'd4c47af7-6079-4456-b686-55ef9d8b05b4,',
    'RBXSource': 'rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0',
    '__utma': '200924205.2071042534.1755625228.1755625228.1755625228.1',
    '__utmb': '200924205.0.10.1755625228',
    '__utmc': '200924205',
    '__utmz': '200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'authority': 'ecsv2.roblox.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'rbx-ip2=1; RBXEventTrackerV2=CreateDate=08/19/2025 12:35:48&rbxid=&browserid=1755624948360002; GuestData=UserID=-53795620; RBXPaymentsFlowContext=d4c47af7-6079-4456-b686-55ef9d8b05b4,; RBXSource=rbx_acquisition_time=08/19/2025 17:40:25&rbx_acquisition_referrer=https://www.roblox.com/id/NewLogin&rbx_medium=Social&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; __utma=200924205.2071042534.1755625228.1755625228.1755625228.1; __utmb=200924205.0.10.1755625228; __utmc=200924205; __utmz=200924205.1755625228.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'evt': 'pageHeartbeat',
    'ctx': 'heartbeat3',
    'url': 'https://www.roblox.com/login/forgot-password-or-username',
    'lt': '2025-08-19T17:40:55.699Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'Referer': 'https://www.roblox.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'evt': 'pageHeartbeat',
    'ctx': 'heartbeat4',
    'url': 'https://www.roblox.com/login/forgot-password-or-username',
    'lt': '2025-08-19T17:41:56.692Z',
    'gid': '-53795620',
}

response = requests.get('https://ecsv2.roblox.com/www/e.png', params=params, headers=headers)
