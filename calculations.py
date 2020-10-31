import random

open_input_file=open("sample_input.txt","r")
next(open_input_file)

data_without_first_line=[]
for line in open_input_file:
	data_without_first_line.append(line.rstrip('\n'))
number_of_employees=random.randrange(1,len(data_without_first_line)+1)
open_input_file.close()

random_lines=[]
for values in range(number_of_employees):
	random_line=random.choice(data_without_first_line)
	print(random_line)
	if random_line not in random_lines:
		random_lines.append(random_line)

price_list=[]
for price in random_lines:
	index_until_colon=price.find(":")
	price_list.append(price[index_until_colon+2:])

print(random_lines)
price_list_of_integers = list(map(int, price_list))
max_price=max(price_list_of_integers)
min_price=min(price_list_of_integers)
diff_price=abs(int(max_price)-int(min_price))

	


open_output_file=open("sample_output.txt","w")
open_output_file.write("Number of Employees: " + str(number_of_employees))
open_output_file.write("\n")
open_output_file.write("\n")
open_output_file.write("Here the goodies are selected for distribution are:")
open_output_file.write("\n")
for line in random_lines:
	open_output_file.write(line+"\n")
open_output_file.write("\n")
open_output_file.write("the difference between the goodie with highest price & the lowest price is "+str(diff_price))

#print(data_without_first_line)
#print(data)
#single_value=random.choice(data_without_first_line)
#print(single_value)
#print(random_lines)
#print(price_list)
#print(max_price)
#print(min_price)
#print(diff_price)