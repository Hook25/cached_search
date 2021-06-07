import os
import sys
import fnmatch
import hashlib
import pickle
import zlib

from gui import gui
from utils import interactive_args, save, load, skip_scan, has_save
from searcher import get_all_leafs

def interactive(): 
  if len(args) != 2:
    args = interactive_args()
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

def not_interactive(args):
  root, pattern = args
  if has_save(root):
    res = load(root)
    loaded = True
  else:
    res = get_all_leafs(root)
    loaded = False
  r = fnmatch.filter(res, pattern)
  if r:
    print("\n".join(r))
  else:
    print("No result")
  if not loaded:
    save(res, root)

def main():
  args = sys.argv[1:]
  if len(args) == 0:
    gui()
  elif "-int" in args:
    interactive()
  elif len(args) == 2:
    not_interactive(args)
  else:
    print("Usage: name.py root pattern")


if __name__ == "__main__":
    main()

