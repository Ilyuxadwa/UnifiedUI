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

    table = tools.Table(app, 12).cols("Column 1", "Column 2", "Column 3").add_row("Some 1", "Information 1", "Here 1").add_row("Some 2", "Information 2", "Here 2")
    table.size(w=80, h=16)
    
    app.add_element(app.alignment("rcenter", 
                        ft.Button("Main Button", width = tools.adapt_dimensions(app, "w", 16), height = tools.adapt_dimensions(app, "h", 8), style=tools.main_button_style(app, 12, padding = 5), icon=ft.Icons.SETTINGS_ROUNDED, on_click=lambda _: print("Button clicked!")),
                        ft.Button("Additional Button", width = tools.adapt_dimensions(app, "w", 14), height = tools.adapt_dimensions(app, "h", 10), style=tools.additional_button_style(app, 12, padding = 5), icon=ft.Icons.SETTINGS_ROUNDED, on_click=lambda _: print("Button clicked!")),
                        ft.Button("Okay", width = tools.adapt_dimensions(app, "w", 12), height = tools.adapt_dimensions(app, "h", 6), style=tools.ok_button_style(app, 12, padding = 5)),
                        ft.Button("Cancel", width = tools.adapt_dimensions(app, "w", 12), height = tools.adapt_dimensions(app, "h", 6), style=tools.cancel_button_style(app, 12, padding = 5)),
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
    app.add_element(app.alignment("rspace_evenly",
                        tools.radio_group(app, tools.radio(app, 12, label="Radio 1", value="option1", width=tools.adapt_dimensions(app, "w", 10)), tools.radio(app, 12, label="Radio 2", value="option2", width=tools.adapt_dimensions(app, "w", 10))),
                        tools.checkbox(app, 12, label="Checkbox", width=tools.adapt_dimensions(app, "w", 10)),
                        tools.switch(app, 12, label="Switch", width=tools.adapt_dimensions(app, "w", 12)),
                    expand=True))
    app.add_element(app.alignment("rspace_evenly",
                        tools.progress_bar(app, width=tools.adapt_dimensions(app, "w", 32), height=tools.adapt_dimensions(app, "h", 4), value=0.7),
                        tools.progress_ring(app, width=tools.adapt_dimensions(app, "w", 8), height=tools.adapt_dimensions(app, "w", 8), value=0.4),
                    expand=True))
    app.add_element(app.alignment("rcenter",
                        table.build(),
                    expand=True, height=tools.adapt_dimensions(app, "h", 50)))
    
    
app = App()
app.set_orientation("landscape")
app.set_size("1/2")
app.custom_settings(settings)
app.set_version("1.0.0")
app.set_ui(ui)
app.run("My App")