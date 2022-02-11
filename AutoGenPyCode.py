#!/usr/bin/env python3

def func(s,noHit):
  try:
    eval(s,None,None)
    print('==============')
    print(s)
    print('==============')
    print('\n\n\n')
    noHit = False
  except:
    pass

if __name__ == '__main__':

  from multiprocessing import Process, Manager

  words = [chr(i) for i in range(33,127)]
  words += ['\n','False','True','and','break','continue','elif','else:','except:','finally:']
  words += ['for','if','in','is','not','or','pass','try:','while']
  words += ['abs(','dict(','float(','int(','len(','list(','pow(','range(','str(','tuple(']

  numList = [0]
  n = len(numList)
  
  noHit = Manager().Value('b',True)
  while noHit:
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
      if '(' in words[numList[i-1]]:
        s += words[l] + ') '
      elif ':' == words[l]:
        s += ':\n  '
      else:
        s += words[l] + ' '

    job = Process(target=func, args=(s,noHit,))
    job.start()
    job.join(15)
