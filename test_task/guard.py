
hour = int(input('Enter current hour: '))

# if int(hour) > 7 and int(hour) < 17:
#     print('You are in!')
# else:
#     print('Go home!')

if hour in range(7,18):
    print('Come here, darling')
else:
    print('Go home')