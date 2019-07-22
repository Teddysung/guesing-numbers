import random
r = random.randint(1, 100)
while True:
	ans = input('請猜數字')
	ans = int(ans)
	if ans == r:
		print('猜對了。討厭，以後不跟你玩了')
		break
	elif ans > r:
		print('傻瓜，你猜的太大了，哈哈!')
	else:
		print('阿呆，你猜得太小了，ㄎㄎ!')
