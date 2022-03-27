#!/usr/bin/env lua

--[[ This program auto generates lua code --]]

-- lua tokens for gen code
tokens = {'"','#','%','*','+','-','..','/','0','1','2','3','4','5','6','7','8','9','<','=','>',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
          'W','X','Y','Z','^','a','b','c','d','e','f','g','h','i','j','h','i','j','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z','and','break','do','else','elseif','end',
          'false','for','if','in','not','or','repeat','then','true','until','while'}

-- length of token table
lenTokens = #tokens

-- table to hold numeric value of auto gen code string (for iteration)
numList = {0}

-- main loop
while true do
-- var to hold code string
  code = ""
-- iterate numeric table
  numList[1] = numList[1] + 1
-- get length of numeric table
  lenNumList = #numList
-- carry over iteration if overflow
  for idx=1,lenNumList,1 do
    if(numList[idx] == (lenTokens + 1)) and (idx ~= lenNumList) then
      numList[idx+1] = numList[idx+1] + 1
      numList[idx] = 1
    elseif (numList[idx] == (lenTokens + 1)) and (idx == lenNumList) then
      table.insert(numList,1)
      numList[idx] = 1
    end
  end
-- create code string from numeric table
  for _,num in ipairs(numList) do
    code = code..tokens[num]..' '
  end
-- try code, if valid print
  status,errormsg = load(code)
  if status then
    print('============')
    print(code)
    print('============')
    print('\n\n')
  end

end
