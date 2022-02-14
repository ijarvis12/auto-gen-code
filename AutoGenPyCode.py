#!/usr/bin/env python3

def func(s):
  try:
    eval(s,None,None)
    print('==============')
    print(s)
    print('==============')
    print('\n\n\n')
  except:
    pass

if __name__ == '__main__':

  from threading import Thread

  words = [chr(i) for i in range(33,127)]
  words += ['\n','False','True','and','break','continue','elif','else:','except:','finally:']
  words += ['for','if','in','is','not','or','pass','try:','while']
  words += ['abs(','dict(','float(','int(','len(','list(','range(','str(','tuple(']

  numList = [0]
  n = len(words)
  
  while True:
    s = ""
    numList[0] += 1
    for k in range(len(numList)):
      if numList[k] == n and k != (len(numList) - 1):
        numList[k+1] += 1
        numList[k] = 0
      elif numList[k] == n and k == (len(numList) - 1):
        numList.append(0)
        numList[k] = 0
    for i,l in enumerate(numList):
      if (i is not 0) and '(' in words[numList[i-1]]:
        s += words[l] + ') '
      elif ':' in words[l]:
        s += ':\n  '
      else:
        s += words[l] + ' '

    job = Thread(target=func, args=(s,))
    job.start()
    job.join(15)
