import random
answer = random.randint(0,100)
while True:
	num = int(input("請輸入猜的號碼: "))
	if num == answer:
		print("終於猜對了!")
		break
	elif num < answer:
		print("猜的數字比較小唷")
	elif num > answer:
		print("猜的數字比較大唷")