#!/usr/bin/env python3

# function to evaluate auto gen code string in separate thread
def func(s):
  try:
    eval(s,None,None)
    print('==============')
    print(s)
    print('==============')
    print('\n\n\n')
  except:
    pass
  return

# main function
if __name__ == '__main__':

  from threading import Thread

# list to hold all ASCII, keywords, and basic functions tokens
  words = [chr(i) for i in range(33,127)]
  words += ['\n','False','True','and','break','continue','elif','else:','except:','finally:']
  words += ['for','if','in','is','not','or','pass','try:','while']
  words += ['abs(','dict(','float(','int(','len(','list(','range(','str(','tuple(']

# length of python tokens var
  n = len(words)

# list to hold numeric value of auto gen code string (for iteration)
  numList = [0]

# main loop
  while True:
#   auto gen code string var
    s = ""
#   iterate list of numeric values
    numList[0] += 1
#   carry over iteration if overflow
    for k in range(len(numList)):
      if numList[k] == n and k != (len(numList) - 1):
        numList[k+1] += 1
        numList[k] = 0
      elif numList[k] == n and k == (len(numList) - 1):
        numList.append(0)
        numList[k] = 0
#   concatinate generate code string with some cleanup of syntax
    for i,l in enumerate(numList):
      if (i is not 0) and '(' in words[numList[i-1]]:
        s = s.join(words[l] + ') ')
      elif ':' in words[l]:
        s = s.join(':\n  ')
      else:
        s = s.join(words[l] + ' ')

#   create thread job for eval generated code and run (max 15 seconds)
    job = Thread(target=func, args=(s,))
    job.start()
    job.join(15)
