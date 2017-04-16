phone_number = range(10)

def PrintPhoneNumber(phone_number):
  print '(%s)%s-%s' % (phone_number[0:3], 
                       phone_number[3:6],
                       phone_number[6:])
                       
def JumbleNumbers(phone_number):
  return [phone_number.pop(0)] + phone_number
  
  
def main():
  for i in range(len(phone_number)):
    PrintPhoneNumber(phone_number)
    phone_number = JumbleNumbers(phone_number)

if __name__ == '__main__':
  main()
