import flet as ft
from . import utils

def adapt_dimensions(app, dim: str, size: int):
    w, h = app.get_work_area()
    if dim == "w":
        return int(w * (size / 100) - (32 * utils.scale(app.size)))
    elif dim == "h":
        return int(h * (size / 100) - (24 * utils.scale(app.size)))
    else:
        raise ValueError("Invalid dimension. Use 'w' for width or 'h' for height.")



def column_align_start(app, *controls, **kwargs) -> ft.Column:
    """Controls aligned to the top."""
    return ft.Column(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def column_align_center(app, *controls, **kwargs) -> ft.Column:
    """Controls centered vertically."""
    return ft.Column(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def column_align_end(app, *controls, **kwargs) -> ft.Column:
    """Controls aligned to the bottom."""
    return ft.Column(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.END,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def column_align_space_between(app, *controls, **kwargs) -> ft.Column:
    """Controls spread vertically with space between."""
    return ft.Column(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def column_align_space_around(app, *controls, **kwargs) -> ft.Column:
    """Controls spread vertically with space around."""
    return ft.Column(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def column_align_space_evenly(app, *controls, **kwargs) -> ft.Column:
    """Controls spread vertically with equal spacing."""
    return ft.Column(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )


def row_align_start(app, *controls, **kwargs) -> ft.Row:
    """Controls aligned to the top."""
    return ft.Row(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def row_align_center(app, *controls, **kwargs) -> ft.Row:
    """Controls centered horizontally."""
    return ft.Row(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def row_align_end(app, *controls, **kwargs) -> ft.Row:
    """Controls aligned to the bottom."""
    return ft.Row(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.END,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def row_align_space_between(app, *controls, **kwargs) -> ft.Row:
    """Controls spread horizontally with space between."""
    return ft.Row(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def row_align_space_around(app, *controls, **kwargs) -> ft.Row:
    """Controls spread horizontally with space around."""
    return ft.Row(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
 
def row_align_space_evenly(app, *controls, **kwargs) -> ft.Row:
    """Controls spread horizontally with equal spacing."""
    return ft.Row(
        controls=list(controls),
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        **kwargs,
    )
    


def main_button_style(app, font_size, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.button,
        color=app.theme.primary,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=font_size
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def additional_button_style(app, font_size, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.button_additional,
        color=app.theme.secondary,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=font_size
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def ok_button_style(app, font_size, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.ok_button,
        color=app.theme.background,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=font_size
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def cancel_button_style(app, font_size, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.cancel_button,
        color=app.theme.background,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=font_size
        ),
        shape=ft.StadiumBorder(),
        **kwargs
    )
 
def label_style(app, font_size, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.label_text,
        font_family=app.theme.font_family,
        size=font_size
        **kwargs
    )
 
def primary_text_style(app, font_size, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.primary,
        font_family=app.theme.font_family,
        size=font_size,
        **kwargs
    )
 
def secondary_text_style(app, font_size, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.secondary,
        font_family=app.theme.font_family,
        size=font_size,
        **kwargs
    )

def entry(app, font_size, **kwargs) -> ft.TextField:
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
            size=font_size
        ),
        text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size
        ),
        **kwargs
    )

def dropdown(app, font_size, **kwargs) -> ft.Dropdown:
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
            size=font_size
        ),
        label_style=ft.TextStyle(
            color=app.theme.secondary,
            font_family=app.theme.font_family,
            size=font_size
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

def checkbox(app, font_size, **kwargs) -> ft.Checkbox:
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
            size=font_size
        ),
        **kwargs
    )

def radio(app, font_size, **kwargs) -> ft.Radio:
    s = utils.scale(app.size)
    return ft.Radio(
        fill_color=app.theme.primary,
        label_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size
        ),
        **kwargs
    )

def switch(app, font_size, **kwargs) -> ft.Switch:
    s = utils.scale(app.size)
    return ft.Switch(
        active_color=app.theme.primary,
        active_track_color=app.theme.button_additional,
        inactive_thumb_color=app.theme.secondary,
        inactive_track_color=app.theme.additional_color,
        label_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size
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

def dialog(app, font_size, **kwargs) -> ft.AlertDialog:
    s = utils.scale(app.size)
    return ft.AlertDialog(
        bgcolor=app.theme.background,
        title_text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size + 12 * s,
            weight=ft.FontWeight.BOLD
        ),
        **kwargs
    )

def data_table(app, font_size, **kwargs) -> ft.DataTable:
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
            size=font_size,
            weight=ft.FontWeight.BOLD,
        ),
        data_text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size
        ),
        **kwargs
    )