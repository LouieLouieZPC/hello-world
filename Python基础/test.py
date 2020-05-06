age=-1
while age<=0:
  try:
    age=int(input('Enter your age in years:'))
    if age<=0:
      print('your age must be positive!')
  except ValueError:
    print('This is an invaild age specification!')
  except EOFError:
    print('There was an unexceted error reading input!')
    raise
  finally:
    print('Your age is:',age)
  