from string import ascii_uppercase

def comp(a, b):
  print("? "+a, b)
  return input()

def sort5(l):
  a, b, c, d, e = l
  
  if comp(a, b) == ">":
    a, b = b, a
  
  if comp(c, d)== ">":
    c, d = d, c

  if comp(a, c) == ">":
    a, b, c, d = c, d, a, b
  
  if comp(c, e) == "<":
    if comp(d, e) == ">":
      d, e = e, d
    if comp(b, d) == "<":
      if comp(b, c) == "<":
        res = [a, b, c, d, e]
      else:
        res = [a, c, b, d, e]
    else:
      if comp(b, e) == "<":
        res = [a, c, d, b, e] 
      else: 
        res = [a, c, d, e, b] 

  else: 
        if comp(a, e) == "<": 
            if comp(b, c) == "<": 
                if comp(b, e) == "<": 
                    res = [a, b, e, c, d] 
                else: 
                    res = [a, e, b, c, d] 
            else: 
                if comp(b, d) == "<": 
                    res = [a, e, c, b, d] 
                else: 
                    res = [a, e, c, d, b] 
        else: 
            if comp(b, c) == "<": 
                res = [e, a, b, c, d] 
            else: 
                if comp(b, d) == "<": 
                    res = [e, a, c, b, d] 
                else: 
                    res = [e, a, c, d, b] 
  return res
    

def merge_sort(l):
  if len(l)<=1:
    return l
  
  mid = len(l)//2
  left = l[:mid]
  right = l[mid:]
  
  left = merge_sort(left)
  right = merge_sort(right)
  
  return merge(left, right)

def merge(left, right):
  
  merged = []
  lp, rp = 0, 0
  
  while lp < len(left) and rp < len(right):
    print("? "+left[lp], right[rp])
    
    if input() == "<":
      merged.append(left[lp])
      lp = lp + 1
    
    else:
      merged.append(right[rp])
      rp = rp + 1
      
  if lp < len(left): 
    merged.extend(left[lp:]) 
  if rp < len(right): 
    merged.extend(right[rp:]) 
  
  return merged

n, q = map(int, input().split())
ans = list(ascii_uppercase[:n]) 

if n > 5:
  ans = merge_sort(ans)

else:
  ans = sort5(ans)

print("! "+"".join(ans), flush=True)

