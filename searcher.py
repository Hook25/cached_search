import os
import fnmatch

from utils import has_save, load, save

def get_all_leafs(root):
  res = []
  to_visit = [root]
  while to_visit:
    now = to_visit.pop()
    try:
      with os.scandir(now) as sdn:
        ls = [(p.path, p.is_dir()) for p in sdn if not p.is_symlink()]
        to_visit += [p for (p, is_dir) in ls if is_dir]
        res += [p for (p, is_dir) in ls if not is_dir]
    except PermissionError:
      pass
  return res

def search_save_and_filter(root, pattern):
  if has_save(root):
    res = load(root)
  else:
    res = get_all_leafs(root)
    save(res, root)
  r = fnmatch.filter(res, pattern)
  return r