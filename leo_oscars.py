number = int(input())

message = ''

if number == 88:
    message = 'Leo finally won the Oscar! Leo is happy'
elif number == 86:
    message = 'Not even for Wolf of Wall Street?!'
elif message != 88 and message != 86 and number < 88:
    message = 'When will you give Leo an Oscar?'
else:
    message = 'Leo got one already!'

print(message)