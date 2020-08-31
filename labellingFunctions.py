x = str(x)
  pattern = '[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
  match = re.findall(pattern, x)
  if(len(match) > 0):
    return POSITIVE
    print(x)
  else:
    return NEGATIVE
