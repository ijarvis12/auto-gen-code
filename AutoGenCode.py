#!/usr/bin/env python3

# function to evaluate auto gen code string in separate thread
def evalCode(code):
  try:
    eval(code,None,None)
    print('==============')
    print(code)
    print('==============')
    print('\n\n\n')
  except:
    pass
  return

# main function
if __name__ == '__main__':

  from threading import Thread

# list to hold all ASCII, keywords, and basic functions tokens
  tokens = [chr(i) for i in range(33,127)]
  tokens += ['\n','False','True','and','break','continue','elif','else:','except:','finally:']
  tokens += ['for','if','in','is','not','or','pass','try:','while']
  tokens += ['abs(','dict(','float(','int(','len(','list(','range(','str(','tuple(']

# length of python tokens var
  lenTokens = len(tokens)

# list to hold numeric value of auto gen code string (for iteration)
  numList = [0]

# main loop
  while True:
#   auto gen code string var
    code = ""
#   iterate list of numeric values
    numList[0] += 1
    lenNumList = len(numList)
#   carry over iteration if overflow
    for idx in range(lenNumList)):
      if (numList[idx] == lenTokens) and (idx != (lenNumList - 1)):
        numList[idx+1] += 1
        numList[idx] = 0
      elif (numList[idx] == lenTokens) and (idx == (lenNumList - 1)):
        numList.append(0)
        numList[idx] = 0
#   concatinate generate code string with some cleanup of syntax
    for i,num in enumerate(numList):
      token = tokens[num]
      if (i != 0) and ('(' in tokens[numList[i-1]]):
        code += token + ') '
      elif ':' in token:
        code += token + '\n  '
      else:
        code += token + ' '

#   create thread job for eval generated code and run (max 15 seconds)
    job = Thread(target=evalCode, args=(code,))
    job.start()
    job.join(15)
