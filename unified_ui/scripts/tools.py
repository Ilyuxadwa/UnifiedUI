import flet as ft
import utils

def adaptive_size(self, dim: str, size: int):
    w, h = utils.get_screen_resolution()
    if dim == "w":
        return int((size / 100) * w)
    elif dim == "h":
        return int((size / 100) * h)
    else:
        raise ValueError("Invalid dimension. Use 'w' for width or 'h' for height.")
    
def main_button_style(self, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=self.theme.button,
        color=self.theme.primary,
        **kwargs
    )
    
def secondary_button_style(self, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=self.theme.button_additional,
        color=self.theme.secondary,
        **kwargs
    )
    
def ok_button_style(self, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=self.theme.ok_button,
        color=self.theme.background,
        **kwargs
    )
 
def cancel_button_style(self, **kwargs) -> ft.ButtonStyle:
    return ft.ButtonStyle(
        bgcolor=self.theme.cancel_button,
        color=self.theme.background,
        **kwargs
    )
 
def main_text_style(self, **kwargs) -> ft.TextStyle:
    return ft.TextStyle(
        color=self.theme.primary,
        font_family=self.theme.font_family,
        **kwargs
    )
 
def secondary_text_style(self, **kwargs) -> ft.TextStyle:
    return ft.TextStyle(
        color=self.theme.secondary,
        font_family=self.theme.font_family,
         **kwargs
    )

def label_text_style(self, **kwargs) -> ft.TextStyle:
    return ft.TextStyle(
        color=self.theme.label_text,
        font_family=self.theme.font_family,
         **kwargs
    )