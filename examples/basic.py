import sys
import os
 
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "unified_ui", "scripts")))
 
from app import App
from settings import Settings
 
settings = Settings()
app = App()
app.set_orientation("landscape")
app.set_size("1/2")
app.custom_settings(settings)
app.run("My App")