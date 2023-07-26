"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import image_lib
import ctypes
import inspect

# Get the script and images directory
script_name =inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
    os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry('600x600')
root.minsize(500,600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TODO: Set the icon
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap(os.path.join(script_dir, 'poke_ball.ico'))

# TODO: Create frames
frame_main = ttk.Frame(root)
frame_main.columnconfigure(0, weight=1)
frame_main.rowconfigure(0, weight=1)
frame_main.grid(sticky=NSEW)

#create a button to get 
def handle_set_desktop():

 """
 Event handler called when user clicks the "Set as desktop image" button.
 Sets the desktop image to the currnet pokemon display image. 
 """
image_lib.set_desktop_background_image(image_path)

btn_et_desktop = ttk.Button(frame_main, text='Set as Desktop Image', command=handle_set_desktop)
btn_et_desktop.state("Disabled")
btn_et_desktop.grid(row=1, column=0, padx=0, pady=(10,20))

#Create a list of pokemon
pokemon_list = poke_api.get_pokemon_info
pokemon_list.sort()
cbox_poke_sel = ttk.Combobox(frame_main, value=pokemon_list, state = 'readonly')
cbox_poke_sel.set("Select a Pokemon")

def handle_poke_sel(event):
   global image_path

   current_sel = cbox_poke_sel.get()
   image_path = poke_api.download_pokemon_artwork(current_sel, images_dir)
   if image_path:
      lbl_image['text'] = None
      photo['file'] = image_path
      #
      #
      #
      #
      #
      #
      else

# TODO: Populate frames with widgets and define event handler functions


root.mainloop()