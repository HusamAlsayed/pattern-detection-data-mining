import copy
class GSP:
  def __init__(self,min_support,max_level,database):
    self.min_support = min_support
    self.max_level = max_level
    self.database = database
    arr = set()
    for i in self.database:
      for j in i:
        arr.add(tuple([j]))
    arr = list(arr)
    self.first_level_patterns = arr

  def generate_patterns(self,patterns):
    new_patterns = []
    for pattern_a in patterns:
      for pattern_b in patterns:
        if pattern_a[1:] == pattern_b[:-1]:
          new_pattern = pattern_a + (pattern_b[-1],)
          new_patterns.append(new_pattern)
    return new_patterns

  def check_current_patterns(self,patterns):
    ans = {}
    for pattern in patterns:
      for record in self.database:
        ok = True
        copy_record = copy.copy(record)
        for sub_pattern in pattern:
          try:
            index = copy_record.index(sub_pattern)
            copy_record = copy_record[index + 1:]
          except:
            ok = False
            break
        ans[pattern] = ans.get(pattern,0) + ok
    ans = {key:value for key ,value in ans.items() if value > self.min_support}
    return ans

  def build_gsp(self):
    ans = {}
    last_patterns = copy.copy(self.first_level_patterns)
    for level in range(self.max_level):
      l = self.check_current_patterns(last_patterns)
      ans.update(l)
      last_patterns = self.generate_patterns(list (l))
    return ans