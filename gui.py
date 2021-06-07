import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk
import os

class Handler:
  def __init__(self, builder):
    self.builder = builder
    self.pp = self.builder.get_object("pathPicker")
    self.sp = self.builder.get_object("txt_SearchPattern")
    self.res = self.builder.get_object("ml_Result")
  def onDestroy(self, *args):
    Gtk.main_quit()
  def clear_res(self):
    for child in self.res.get_children():
      self.res.remove(child)
  def onButtonPressed(self, *args):
    from searcher import search_save_and_filter
    self.clear_res()
    path = self.pp.get_file().get_path()
    pattern = self.sp.get_text()
    r = search_save_and_filter(path, pattern)
    to_app = [Gtk.Label(label = res) for res in r]
    for ta in to_app:
      self.res.prepend(ta)
    if not r:
      self.res.prepend(Gtk.Label.new_with_mnemonic("No results"))
    self.res.show_all()
  def startRow(self, lbox, row):
    if hasattr(os, "startfile"):
      os.startfile(row.get_child().get_text())
    else:
      print(row.get_child().get_text())

def gui():
  b = Gtk.Builder()
  b.add_from_file('gui.glade')
  b.connect_signals(Handler(b))
  b.get_object("example_window").show_all()
  Gtk.main()

def main():
  gui()

if __name__ == "__main__":
  main()
