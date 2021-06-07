import os
import hashlib
import zlib
import pickle

def r_hash(root):
  root = os.path.normpath(root)
  return str(hashlib.md5(root.encode()).hexdigest())[:5]

def has_save(root):
  return os.path.isfile(r_hash(root))
  
def load(root):
  with open(r_hash(root), "rb") as f:
    s = zlib.decompress(f.read())
    return pickle.loads(s)

def save(flist, root):
  with open(r_hash(root), "wb+") as f:
    s = pickle.dumps(flist, pickle.HIGHEST_PROTOCOL)
    f.write(zlib.compress(s))

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