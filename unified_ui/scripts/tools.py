import flet as ft
import utils

def adaptive_size(dim: str, size: int):
    w, h = utils.get_screen_resolution()
    if dim == "w":
        return int((size / 100) * w)
    elif dim == "h":
        return int((size / 100) * h)
    else:
        raise ValueError("Invalid dimension. Use 'w' for width or 'h' for height.")

def adaptive_position(dim: str, position: int):
    w, h = utils.get_screen_resolution()
    if dim == "x":
        return int((position / 100) * w)
    elif dim == "y":
        return int((position / 100) * h)
    else:
        raise ValueError("Invalid dimension. Use 'x' for x-coordinate or 'y' for y-coordinate.")
    
def main_button_style(app, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=app.theme.button,
        color=app.theme.primary,
        **kwargs
    )
    
def secondary_button_style(app, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=app.theme.button_additional,
        color=app.theme.secondary,
        **kwargs
    )
    
def ok_button_style(app, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=app.theme.ok_button,
        color=app.theme.background,
        **kwargs
    )
 
def cancel_button_style(app, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=app.theme.cancel_button,
        color=app.theme.background,
        **kwargs
    )
 
def main_text_style(app, **kwargs) -> ft.TextStyle:
    return ft.TextStyle(
        color=app.theme.primary,
        font_family=app.theme.font_family,
        **kwargs
    )
 
def secondary_text_style(app, **kwargs) -> ft.TextStyle:
    return ft.TextStyle(
        color=app.theme.secondary,
        font_family=app.theme.font_family,
         **kwargs
    )

def label_text_style(app, **kwargs) -> ft.TextStyle:
    return ft.TextStyle(
        color=app.theme.label_text,
        font_family=app.theme.font_family,
         **kwargs
    )