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
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.button,
        color=app.theme.primary,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def additional_button_style(app, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.button_additional_color,
        color=app.theme.secondary,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def ok_button_style(app, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.ok_button,
        color=app.theme.background,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def cancel_button_style(app, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.cancel_button,
        color=app.theme.background,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def label_style(app, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.label_text,
        font_family=app.theme.font_family,
        size=int(app.theme.font_size * s),
        **kwargs
    )
 
def primary_text_style(app, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.primary,
        font_family=app.theme.font_family,
        size=int(app.theme.font_size * s),
        **kwargs
    )
 
def secondary_text_style(app, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.secondary,
        font_family=app.theme.font_family,
        size=int(app.theme.font_size * s),
        **kwargs
    )

def entry(app, **kwargs) -> ft.TextField:
    s = utils.scale(app.size)
    return ft.TextField(
        bgcolor=app.theme.entry,
        border_color=app.theme.outline,
        focused_border_color=app.theme.primary,
        border_radius=8,
        border_width=app.theme.outline_width,
        color=app.theme.primary,
        cursor_color=app.theme.primary,
        label_style=ft.TextStyle(
            color=app.theme.secondary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        **kwargs
    )

def dropdown(app, **kwargs) -> ft.Dropdown:
    s = utils.scale(app.size)
    return ft.Dropdown(
        bgcolor=app.theme.entry,
        border_color=app.theme.outline,
        focused_border_color=app.theme.primary,
        border_radius=8,
        border_width=app.theme.outline_width,
        color=app.theme.primary,
        text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        label_style=ft.TextStyle(
            color=app.theme.secondary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        **kwargs
    )

def slider(app, **kwargs) -> ft.Slider:
    return ft.Slider(
        active_color=app.theme.primary,
        inactive_color=app.theme.button_additional,
        thumb_color=app.theme.secondary,
        **kwargs
    )

def checkbox(app, **kwargs) -> ft.Checkbox:
    s = utils.scale(app.size)
    return ft.Checkbox(
        fill_color=app.theme.button_additional,
        check_color=app.theme.primary,
        border_side=ft.BorderSide(
            width=app.theme.outline_width,
            color=app.theme.outline,
        ),
        label_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        **kwargs
    )

def radio(app, **kwargs) -> ft.Radio:
    s = utils.scale(app.size)
    return ft.Radio(
        fill_color=app.theme.primary,
        label_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        **kwargs
    )

def switch(app, **kwargs) -> ft.Switch:
    s = utils.scale(app.size)
    return ft.Switch(
        active_color=app.theme.primary,
        active_track_color=app.theme.button_additional,
        inactive_thumb_color=app.theme.secondary,
        inactive_track_color=app.theme.additional_color,
        label_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        **kwargs
    )

def progress_bar(app, **kwargs) -> ft.ProgressBar:
    return ft.ProgressBar(
        color=app.theme.primary,
        bgcolor=app.theme.additional_color,
        border_radius=8,
        **kwargs,
    )
 
def progress_ring(app, **kwargs) -> ft.ProgressRing:
    return ft.ProgressRing(
        color=app.theme.primary,
        bgcolor=app.theme.additional_color,
        **kwargs
    )

def dialog(app, **kwargs) -> ft.AlertDialog:
    s = utils.scale(app.size)
    return ft.AlertDialog(
        bgcolor=app.theme.background,
        title_text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int((app.theme.font_size + 4) * s),
            weight=ft.FontWeight.BOLD,
        ),
        **kwargs
    )

def data_table(app, **kwargs) -> ft.DataTable:
    s = utils.scale(app.size)
    return ft.DataTable(
        bgcolor=app.theme.additional_color,
        border=ft.Border.all(
            width=app.theme.outline_width,
            color=app.theme.outline,
        ),
        border_radius=8,
        divider_thickness=app.theme.outline_width,
        heading_row_color=app.theme.secondary,
        heading_text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
            weight=ft.FontWeight.BOLD,
        ),
        data_text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=int(app.theme.font_size * s),
        ),
        **kwargs,
    )