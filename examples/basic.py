import sys
import os
 
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "unified_ui", "scripts")))
 
from unified_ui import App, Settings
 
settings = Settings()
example_settings_category = settings.add_category("example", "Example Settings")
example_settings_category.add_dropdown("dropdown", "Example Dropdown", "option1", ["option1", "option2", "option3"],
                        on_change=lambda value: print(f"Dropdown changed to: {value}"))
example_settings_category.add_toggle("toggle", "Example Toggle", True, on_change=lambda value: print(f"Toggle changed to: {value}"))
example_settings_category.add_text("text", "Example Text", "Hello, World!", on_change=lambda value
                    : print(f"Text changed to: {value}"))
example_settings_category.add_slider("slider", "Example Slider", 0.5, min_value=0.0, max_value=1.0, on_change=lambda value: print(f"Slider changed to: {value}"))
example_settings_category.add_directory("directory", "Example Directory", on_change=lambda value: print(f"Directory changed to: {value}"))

app = App()
app.set_orientation("landscape")
app.set_size("1/2")
app.custom_settings(settings)
app.set_version("1.0.0")
app.run("My App")