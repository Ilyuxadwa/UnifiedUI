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
            size=font_size * s
        ),
        **kwargs
    )
 
def additional_button_style(app, font_size, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.button_additional,
        color=app.theme.secondary,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=font_size * s
        ),
        **kwargs
    )
 
def ok_button_style(app, font_size, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.ok_button,
        color=app.theme.background,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=font_size * s
        ),
        **kwargs
    )
 
def cancel_button_style(app, font_size, **kwargs) -> ft.ButtonStyle:
    s = utils.scale(app.size)
    return ft.ButtonStyle(
        bgcolor=app.theme.cancel_button,
        color=app.theme.background,
        text_style=ft.TextStyle(
            font_family=app.theme.font_family,
            size=font_size * s
        ),
        **kwargs
    )
 
def label_style(app, font_size, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.label_text,
        font_family=app.theme.font_family,
        size=font_size * s
        **kwargs
    )
 
def primary_text_style(app, font_size, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.primary,
        font_family=app.theme.font_family,
        size=font_size * s,
        **kwargs
    )
 
def secondary_text_style(app, font_size, **kwargs) -> ft.TextStyle:
    s = utils.scale(app.size)
    return ft.TextStyle(
        color=app.theme.secondary,
        font_family=app.theme.font_family,
        size=font_size * s,
        **kwargs
    )

def entry(app, font_size, **kwargs) -> ft.TextField:
    s = utils.scale(app.size)
    return ft.TextField(
        bgcolor=app.theme.entry,
        border_color=app.theme.outline,
        focused_border_color=app.theme.outline,
        border_radius=8,
        border_width=app.theme.outline_width,
        color=app.theme.primary,
        cursor_color=app.theme.primary,
        label_style=ft.TextStyle(
            color=app.theme.secondary,
            font_family=app.theme.font_family,
            size=font_size * s
        ),
        text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size * s
        ),
        hint_style=secondary_text_style(app, font_size-int(4*s)),
        **kwargs
    )

def dropdown(app, font_size, **kwargs) -> ft.Dropdown:
    s = utils.scale(app.size)
    return ft.Dropdown(
        bgcolor=app.theme.background,
        color=app.theme.primary,
        fill_color=app.theme.entry,
        border_width=app.theme.outline_width,
        border_color=app.theme.outline,
        filled=True,
        text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size * s
        ),
        label_style=ft.TextStyle(
            color=app.theme.secondary,
            font_family=app.theme.font_family,
            size=font_size * s
        ),
        **kwargs
    )

def doption(app, label: str, key: str = None) -> ft.DropdownOption:
    return ft.DropdownOption(key=key or label, content=ft.Text(label, color=app.theme.secondary))

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
        fill_color=app.theme.entry,
        check_color=app.theme.primary,
        border_side=ft.BorderSide(
            width=app.theme.outline_width,
            color=app.theme.outline,
        ),
        label_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size * s
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
            size=font_size * s
        ),
        **kwargs
    )

def radio_group(app, *radios, **kwargs) -> ft.RadioGroup:
    return ft.RadioGroup(
        content=ft.Column(controls=list(radios)),
        **kwargs
    )

def switch(app, font_size, **kwargs) -> ft.Switch:
    s = utils.scale(app.size)
    return ft.Switch(
        active_color=app.theme.primary,
        active_track_color=app.theme.button_additional,
        inactive_thumb_color=app.theme.secondary,
        inactive_track_color=app.theme.additional_color,
        overlay_color={ft.ControlState.DEFAULT: app.theme.additional_color},
        track_outline_color={ft.ControlState.DEFAULT: app.theme.additional_color, ft.ControlState.SELECTED: app.theme.button_additional},
        track_outline_width={ft.ControlState.DEFAULT: 0, ft.ControlState.SELECTED: 0, ft.ControlState.HOVERED: 0},
        splash_radius=2,
        label_text_style=ft.TextStyle(
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size * s
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
            size=font_size * s + 12 * s,
            weight=ft.FontWeight.BOLD
        ),
        **kwargs
    )

def data_cell(app, content: ft.Control, **kwargs) -> ft.DataCell:
    return ft.DataCell(content=content, **kwargs)
 
def data_column(app, font_size, label: str, **kwargs) -> ft.DataColumn:
    s = utils.scale(app.size)
    return ft.DataColumn(
        label=ft.Text(
            label,
            color=app.theme.primary,
            font_family=app.theme.font_family,
            size=font_size * s,
            weight=ft.FontWeight.BOLD,
        ),
        **kwargs
    )
 
 
class Table:
 
    def __init__(self, app, font_size: int):
        self.app = app
        self.font_size = font_size
        self.columns = []
        self.rows = []
        self.extra = {}
        self.table: ft.DataTable | None = None
        self._heading_height: int | None = None
        self._row_height: int | None = None
 
    def cols(self, *labels: str):
        s = utils.scale(self.app.size)
        for label in labels:
            self.columns.append(ft.DataColumn(
                label=ft.Text(
                    label,
                    color=self.app.theme.primary,
                    font_family=self.app.theme.font_family,
                    size=self.font_size * s,
                    weight=ft.FontWeight.BOLD,
                )
            ))
        return self
 
    def add_row(self, *values, color: str = None):
        s = utils.scale(self.app.size)
        if color is None:
            index = len(self.rows)
            color = self.app.theme.additional_color if index % 2 == 0 else self.app.theme.entry
        self.rows.append(ft.DataRow(
            color=color,
            cells=[
                ft.DataCell(ft.Text(
                    str(v),
                    color=self.app.theme.primary,
                    font_family=self.app.theme.font_family,
                    size=self.font_size * s,
                ))
                for v in values
            ]
        ))
        return self
 
    def heading_height(self, height: int):
        self._heading_height = height
        return self
 
    def row_height(self, height: int):
        self._row_height = height
        return self
 
    def size(self, w: int = None, h: int = None):
        if w is not None:
            self.extra["width"] = adapt_dimensions(self.app, "w", w)
        if h is not None:
            self.extra["height"] = adapt_dimensions(self.app, "h", h)
        return self
 
    def build(self, **kwargs) -> ft.Control:
        s = utils.scale(self.app.size)
 
        table_kwargs = {}
        if self._heading_height is not None:
            table_kwargs["heading_row_height"] = self._heading_height
        if self._row_height is not None:
            table_kwargs["data_row_min_height"] = self._row_height
            table_kwargs["data_row_max_height"] = self._row_height
 
        self.table = ft.DataTable(
            columns=self.columns,
            rows=self.rows,
            bgcolor=self.app.theme.background,
            border_radius=8,
            border=ft.Border.all(2, self.app.theme.outline),
            divider_thickness=self.app.theme.outline_width,
            heading_row_color=self.app.theme.background,
            heading_text_style=ft.TextStyle(
                color=self.app.theme.primary,
                font_family=self.app.theme.font_family,
                size=self.font_size * s,
                weight=ft.FontWeight.BOLD,
            ),
            data_text_style=ft.TextStyle(
                color=self.app.theme.primary,
                font_family=self.app.theme.font_family,
                size=self.font_size * s,
            ),
            **table_kwargs,
            **kwargs,
        )
 
        if "height" in self.extra:
            return ft.Container(
                width=self.extra.get("width"),
                height=self.extra["height"],
                bgcolor=self.app.theme.background,
                content=ft.ListView(
                    controls=[self.table],
                    expand=True,
                )
            )
 
        return ft.Container(
            width=self.extra.get("width"),
            bgcolor=self.app.theme.background,
            content=self.table,
        )
 
    def clear(self):
        self.rows.clear()
        if self.table is not None:
            self.table.rows.clear()
        return self
 
    def update(self):
        if self.table is not None:
            self.table.rows = self.rows
            self.table.update()
        return self