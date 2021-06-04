import os
import sys
import fnmatch
import hashlib
import pickle

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

def r_hash(root):
  root = os.path.normpath(root)
  return str(hashlib.md5(root.encode()).hexdigest())[:5]

def has_save(root):
  return os.path.isfile(r_hash(root))
  
def load(root):
  with open(r_hash(root), "rb") as f:
    return pickle.load(f)

def save(flist, root):
  with open(r_hash(root), "wb+") as f:
    pickle.dump(flist, f, pickle.HIGHEST_PROTOCOL)

def skip_scan():
  print("You already searched in this directory")
  print("the save file might not contain some results")
  print()
  i = input("Do you want to try there first? [Y/n]")
  if i and i in "nN":
    return False
  return True

def interactive_args():
  root = input("Location to search: ")
  pattern = input("Pattern to search: ")
  return [root, pattern]
  
def compress(res):
  new_r = [res[0]]
  
  
def main():
  args = sys.argv[1:]
  if len(args) != 2:
    args = interactive_args()
    #print("Usage: name.py root pattern")
  if has_save(args[0]) and skip_scan():
    print("loading...")
    res = load(args[0])
    print("done")
  else:
    print("searching...")
    res = get_all_leafs(args[0])
    print("done")
  print()
  r = fnmatch.filter(res, args[1])
  if r:
    print("\n".join(r))
  else:
    print("No results")
  save(res, args[0])
  input("Press return to close")

if __name__ == "__main__":
    main()

