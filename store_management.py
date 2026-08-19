import os

# Lệnh xóa màn hình chuẩn chỉnh
os.system('cls' if os.name == 'nt' else 'clear')

# Thông tin sản phẩm
storage = {"SP01":{"name": "Pork", "price": 29000, 'stock': 14},
"SP02":{"name": "Water", "price": 5000, 'stock': 47},
"SP03":{"name": "Vegetables", "price": 9000, 'stock': 93},
"SP04":{"name": "Beef", "price": 48000, 'stock': 34},
"SP05":{"name": "Toy", "price": 194000, 'stock': 7}}

# Giỏ hàng
gio_hang =[]

# Chọn mục
while True:
	user_choice = input('==================================================\n   				🛒 BELBELMART MANAGEMENT SYSTEM\n 	  ==================================================\n  		[1] 📦 Xem danh sách sản phẩm trong kho\n 		[2] 🛍️  Mua hàng (Thêm vào giỏ)\n 		[3] 💳 Xem giỏ hàng & Thanh toán\n 		[4] 🚪 Thoát chương trình\n  	  ==================================================\n 		👉 Nhập lựa chọn của bạn (1-4):')
	if user_choice == '1':
		for code, item in storage.items():
			print(f"Mã sản phẩm: {code} - Tên sản phẩm: {item['name']}, Giá: {item['price']}, Số lượng tồn kho: {item['stock']}")
		input('\nNhấn Enter để tiếp tục...')
	elif user_choice == '2':
		ma_sp = input('Nhập mã sản phẩm của sản phẩm mà bạn muốn mua: ')
		if ma_sp in storage:
			print(f'Tên sản phẩm:{storage[ma_sp]["name"]} | Giá: {storage[ma_sp]["price"]}| Còn: {storage[ma_sp]["stock"]}' )
			amount = int(input('Số lượng sản phẩm muốn mua: '))
			if amount <= 0:
				print('Số lượng mua hàng phải lớn hơn 0!')
			elif amount > storage[ma_sp]['stock']:
				print(f'Rất tiếc, trong kho chỉ còn{storage[ma_sp]["stock"]}')
			else:
				storage[ma_sp]["stock"] -= amount
				gio_hang.append({'Tên': storage[ma_sp]["name"]
					,'Số mua': amount
					,'Giá': storage[ma_sp]["price"] * amount})
		input('\nNhấn Enter để tiếp tục...')
		else:
			print('Rất tiếc, chúng tôi không thể tìm được sản phẩm nào như vậy.')
			print('\nNhấn enter để tiếp tục...')
	elif user_choice == '3':
		price = 0
		for x, hàng in enumerate(gio_hang, start = 1):
			print(f"{x}. Tên: {hàng['Tên']}, Số mua: {hàng['Số mua']}, Giá: {hàng['Giá']}")
			price += hàng['Giá']
		print("--------------------------------")
		print(f"Tổng tiền thanh toán: {price}")
		print('================================')
		input('\nNhấn Enter để tiếp tục...')
	elif user_choice =='4':
		print('===========#==========')
		print('Cảm ơn đã ghé BelBelMart')
		exit()
