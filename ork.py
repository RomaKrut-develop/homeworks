print('1. Addition 2. Subtraction 3. Multiplication 4. Division 0. Exit')
calc_choose = int(input('Wait for input '))
if calc_choose == 1:
		first_num = int(input('Wait for input: First number: '))
		sec_num = int(input('Wait for input: Second number: '))
		result = first_num + sec_num
		print(result)
elif calc_choose == 2:
		first_num = int(input('Wait for input: First number: '))
		sec_num = int(input('Wait for input: Second number: '))
		result = first_num - sec_num
		print(result)
elif calc_choose == 3:
			first_num = int(input('Wait for input: First number: '))
			sec_num = int(input('Wait for input: Second number: '))
			result = first_num * sec_num
			print(result)
elif calc_choose == 4:
			first_num = int(input('Wait for input: First number: '))
			sec_num = int(input('Wait for input: Second number: '))
			result = first_num / sec_num
			print(result)
elif calc_choose == 0:
		pass
else:
	print('Critical Error: Unknown Function')