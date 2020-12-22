import random
answer = random.randint(0,100)
count = 0
while True:
	count +=1
	num = int(input("請輸入猜的號碼: "))
	if num == answer:
		print("終於猜對了!")
		print("這是你猜的第",count,"次")
		break
	elif num < answer:
		print("猜的數字比較小唷")
	elif num > answer:
		print("猜的數字比較大唷")
	print("這是你猜的第",count,"次")