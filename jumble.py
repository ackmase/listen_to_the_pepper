phone_number = ''.join(map(str, range(10)))

def PrintPhoneNumber(phone_number):
  print '(%s)%s-%s' % (''.join(phone_number[0:3]), 
                       ''.join(phone_number[3:6]),
                       ''.join(phone_number[6:]))
                       
def JumbleNumbers(phone_number):
  return phone_number[1:] + phone_number[0]
  
  
def main():
  for i in range(len(phone_number)):
    PrintPhoneNumber(phone_number)
    phone_number = JumbleNumbers(phone_number)

if __name__ == '__main__':
  main()
