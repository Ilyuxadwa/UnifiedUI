import sys
import os
 
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "unified_flet_themes", "scripts")))
 
from app import App
 
app = App()
app.set_orientation("landscape")
app.set_size("1/4")
app.run("My App")