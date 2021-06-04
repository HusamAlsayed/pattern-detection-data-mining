class TreeBasedSequence:

  def __init__(self,min_support,max_level,database):
    self.min_support = min_support
    self.max_level = max_level
    self.database = database

  def dfs(self,ans,data,index,max_level,tpl):
    assert(len(data) <=11)
    if max_level == 0 or index == len(data):
      ans[tpl] = 1
      return
    self.dfs(ans,data,index + 1,max_level,tpl)
    new_tpl = tpl + (data[index],)
    self.dfs(ans,data,index + 1,max_level - 1,new_tpl)
  def build_tree(self):
    pat = {}
    for index , record in enumerate(self.database):
      ans = {}
      self.dfs(ans,record,0,8,())
      for key,value in ans.items():
        pat[key] = pat.get(key,0) + 1
    return pat
