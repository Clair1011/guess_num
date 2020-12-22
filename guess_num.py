import random
start = int(input("請輸入隨機數字的開始值: "))
end = int(input("請輸入隨機數字的結束值: "))
answer = random.randint(start , end)
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