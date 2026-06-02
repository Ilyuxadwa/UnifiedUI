import sys
import os
import flet as ft
 
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "unified_ui", "scripts")))
 
from unified_ui import App, Settings, tools
 
settings = Settings()
example_settings_category = settings.add_category("example", "Example Settings")
example_settings_category.add_dropdown("dropdown", "Example Dropdown", "option1", ["option1", "option2", "option3"],
                        on_change=lambda value: print(f"Dropdown changed to: {value}"))
example_settings_category.add_toggle("toggle", "Example Toggle", True, on_change=lambda value: print(f"Toggle changed to: {value}"))
example_settings_category.add_text("text", "Example Text", "Hello, World!", on_change=lambda value
                    : print(f"Text changed to: {value}"))
example_settings_category.add_slider("slider", "Example Slider", 0.5, min_value=0.0, max_value=1.0, on_change=lambda value: print(f"Slider changed to: {value}"))
example_settings_category.add_directory("directory", "Example Directory", on_change=lambda value: print(f"Directory changed to: {value}"))

def ui(app):
    app.add_element(app.alignment("rcenter", 
                        ft.Button("Main Button", width = tools.adapt_dimensions(app, "w", 16), height = tools.adapt_dimensions(app, "h", 8), style=tools.main_button_style(app, 12, padding = 5), icon=ft.Icons.SETTINGS_ROUNDED, on_click=lambda _: print("Button clicked!")),
                        ft.Button("Additional Button", width = tools.adapt_dimensions(app, "w", 14), height = tools.adapt_dimensions(app, "h", 10), style=tools.additional_button_style(app, 12, padding = 5), icon=ft.Icons.SETTINGS_ROUNDED, on_click=lambda _: print("Button clicked!")),
                    expand=True))
    app.add_element(app.alignment("rspace_around",
                        ft.Text("Primary Text", style=tools.primary_text_style(app, 18)),
                        ft.Text("Secondary Text", style=tools.secondary_text_style(app, 18)),
                    expand=True))
    app.add_element(app.alignment("rspace_evenly",
                        tools.entry(app, 12, label="Entry 1", hint_text="Text", width=tools.adapt_dimensions(app, "w", 32), height=tools.adapt_dimensions(app, "h", 16)),
                        tools.dropdown(app, 12, label="Dropdown 1", options=[ft.DropdownOption("Option 1", "option1"), ft.DropdownOption("Option 2", "option2"), ft.DropdownOption("Option 3", "option3")], width=tools.adapt_dimensions(app, "w", 16), height=tools.adapt_dimensions(app, "h", 16)),
                        tools.slider(app),
                    expand=True))
    app.add_element(app.alignment("rcenter",
                        tools.radio(app, 12, label="Radio 1", width=tools.adapt_dimensions(app, "w", 16), height=tools.adapt_dimensions(app, "h", 16)),
                        tools.checkbox(app, 12, label="Checkbox 1", width=tools.adapt_dimensions(app, "w", 16), height=tools.adapt_dimensions(app, "h", 16)),
                        tools.switch(app, 12, label="Switch 1", width=tools.adapt_dimensions(app, "w", 16), height=tools.adapt_dimensions(app, "h", 16)),
                    expand=True))
    
app = App()
app.set_orientation("landscape")
app.set_size("1/2")
app.custom_settings(settings)
app.set_version("1.0.0")
app.set_ui(ui)
app.run("My App")