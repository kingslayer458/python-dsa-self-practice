#indexing = accessing elements of a sequence using [] (indexing operator,
#   [start: end : step])

credit_number= "1234-5678-9042-4244"

#print(credit_number[0])
#print(credit_number[8])
#print(credit_number[0:4])
#print(credit_number[:4])
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-5])
#print(credit_number[::2])

#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")
#TO REVERSE A STRING SET A STRING AS  NEGATIVE ONE
last_digits=credit_number[::-1]

print(last_digits)