import random
num_min = input('請輸入最小數: ')
num_min = int(num_min)
num_max = input('請輸入最大數: ')
num_max = int(num_max)
r = random.randint(num_min, num_max)
turn = 0
while True:
	ans = input('請猜數字')
	ans = int(ans)
	turn = turn + 1
	if ans == r:
		print('猜對了。討厭，以後不跟你玩了')
		print('你猜了', turn, '次')
		break
	elif ans > r:
		print('傻瓜，你猜的太大了，哈哈!')
	else:
		print('阿呆，你猜得太小了，ㄎㄎ!')
