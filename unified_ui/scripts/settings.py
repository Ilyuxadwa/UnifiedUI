from dataclasses import dataclass, field
from typing import Any, Callable, Literal
import flet as ft


@dataclass
class SettingsField:
    id: str
    label: str
    type: Literal["dropdown", "toggle", "text", "slider", "directory"]
    value: Any
    options: list[str] = field(default_factory=list)
    on_change: Callable[[Any], None] = None
    min_value: float = 0.0
    max_value: float = 1.0
    divisions: int | None = None


@dataclass
class SettingsCategory:
    id: str
    label: str
    fields: list[SettingsField] = field(default_factory=list)

    def add_dropdown(self, id, label, value, options, on_change=None):
        self.fields.append(SettingsField(id, label, "dropdown", value, options, on_change))
        return self

    def add_toggle(self, id, label, value, on_change=None):
        self.fields.append(SettingsField(id, label, "toggle", value, on_change=on_change))
        return self

    def add_text(self, id, label, value="", on_change=None):
        self.fields.append(SettingsField(id, label, "text", value, on_change=on_change))
        return self

    def add_slider(self, id, label, value=0.0, min_value=0.0, max_value=1.0, divisions=None, on_change=None):
        f = SettingsField(id, label, "slider", value, on_change=on_change,
                          min_value=min_value, max_value=max_value, divisions=divisions)
        self.fields.append(f)
        return self

    def add_directory(self, id, label, value="", on_change=None):
        self.fields.append(SettingsField(id, label, "directory", value, on_change=on_change))
        return self



class Settings:

    def __init__(self):
        self.categories: list[SettingsCategory] = []

    def add_category(self, id: str, label: str) -> SettingsCategory:
        cat = SettingsCategory(id=id, label=label)
        self.categories.append(cat)
        return cat

    def get_or_create_category(self, id: str, label: str) -> SettingsCategory:
        for cat in self.categories:
            if cat.id == id:
                return cat
        return self.add_category(id, label)


    def add_dropdown(self, category_id: str, id: str, label: str,
                     value: str, options: list[str],
                     on_change: Callable[[str], None] = None):
        self.category(category_id).add_dropdown(id, label, value, options, on_change)
        return self

    def add_toggle(self, category_id: str, id: str, label: str,
                   value: bool, on_change: Callable[[bool], None] = None):
        self.category(category_id).add_toggle(id, label, value, on_change)
        return self

    def add_text(self, category_id: str, id: str, label: str,
                 value: str = "", on_change: Callable[[str], None] = None):
        self.category(category_id).add_text(id, label, value, on_change)
        return self

    def add_slider(self, category_id: str, id: str, label: str,
                   value: float = 0.0, min_value: float = 0.0, max_value: float = 1.0,
                   divisions: int | None = None, on_change: Callable[[float], None] = None):
        self.category(category_id).add_slider(id, label, value, min_value, max_value, divisions, on_change)
        return self

    def add_directory(self, category_id: str, id: str, label: str,
                      value: str = "", on_change: Callable[[str], None] = None):
        self.category(category_id).add_directory(id, label, value, on_change)
        return self

    def category(self, category_id: str) -> SettingsCategory:
        for cat in self.categories:
            if cat.id == category_id:
                return cat
        raise KeyError(f"No category with id '{category_id}'")
    


    @property
    def fields(self) -> list[SettingsField]:
        """Flat view of every field across all categories."""
        return [f for cat in self.categories for f in cat.fields]

    def get(self, id: str) -> Any:
        for f in self.fields:
            if f.id == id:
                return f.value
        raise KeyError(f"No setting with id '{id}'")



    def build_controls(self, theme, s: float) -> tuple[list[ft.Control], dict]:
        controls = []
        refs = {}

        for cat in self.categories:
            if not cat.fields:
                continue

            controls.append(
                ft.Container(
                    padding=int(8 * s),
                    content=ft.Column(
                        spacing=int(4 * s),
                        controls=[
                            ft.Text(
                                cat.label.upper(),
                                color=theme.secondary,
                                size=int(14 * s),
                                weight=ft.FontWeight.BOLD,
                                font_family=theme.font_family
                            ),
                            ft.Divider(color=theme.secondary, height=1, thickness=1),
                        ]
                    )
                )
            )

            for f in cat.fields:
                ctrl = self.build_category(f, theme, s, refs)
                if ctrl is not None:
                    controls.append(ctrl)

        return controls, refs

    def build_category(self, f: SettingsField, theme, s: float, refs: dict):
        if f.type == "dropdown":
            ctrl = ft.Dropdown(
                label=f.label,
                value=f.value,
                options=[ft.dropdown.Option(o) for o in f.options],
                color=theme.primary,
                border_color=theme.secondary,
                focused_border_color=theme.primary,
                label_style=ft.TextStyle(color=theme.secondary),
                text_style=ft.TextStyle(color=theme.primary),
            )

        elif f.type == "toggle":
            switch = ft.Switch(
                value=f.value,
                active_color=theme.primary,
                active_track_color=theme.button_additional,
                inactive_thumb_color=theme.secondary,
                inactive_track_color=theme.additional_color
            )
            ctrl = ft.Container(
                border=ft.Border(
                    top=ft.BorderSide(theme.outline_width+1, theme.secondary),
                    bottom=ft.BorderSide(theme.outline_width+1, theme.secondary),
                    left=ft.BorderSide(theme.outline_width+1, theme.secondary),
                    right=ft.BorderSide(theme.outline_width+1, theme.secondary)
                ),
                border_radius=8,
                padding=12 * s,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(f.label, color=theme.primary,
                                font_family=theme.font_family,
                                size=int(12 * s)),
                        switch,
                    ],
                ),
            )
            refs[f.id] = (f, switch)
            return ctrl

        elif f.type == "text":
            ctrl = ft.TextField(
                label=f.label,
                value=str(f.value) if f.value is not None else "",
                color=theme.primary,
                border_color=theme.secondary,
                focused_border_color=theme.primary,
                label_style=ft.TextStyle(color=theme.secondary),
                text_style=ft.TextStyle(color=theme.primary),
            )

        elif f.type == "slider":
            slider = ft.Slider(
                value=float(f.value),
                min=f.min_value,
                max=f.max_value,
                divisions=f.divisions,
                active_color=theme.primary,
                inactive_color=theme.button_additional,
                thumb_color=theme.secondary,
                label="{value}",
            )
            ctrl = ft.Container(
                border=ft.Border(
                    top=ft.BorderSide(theme.outline_width+1, theme.secondary),
                    bottom=ft.BorderSide(theme.outline_width+1, theme.secondary),
                    left=ft.BorderSide(theme.outline_width+1, theme.secondary),
                    right=ft.BorderSide(theme.outline_width+1, theme.secondary)
                ),
                border_radius=8,
                padding=12 * s,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.Text(f.label, color=theme.primary,
                                font_family=theme.font_family,
                                size=int(12 * s)),
                        slider,
                    ],
                ),
            )
            refs[f.id] = (f, slider)
            return ctrl

        elif f.type == "directory":
            ctrl = ft.TextField(
                label=f.label,
                value=str(f.value) if f.value is not None else "",
                hint_text="Enter folder path...",
                prefix_icon=ft.Icons.FOLDER_OUTLINED,
                color=theme.primary,
                border_color=theme.secondary,
                focused_border_color=theme.primary,
                label_style=ft.TextStyle(color=theme.secondary),
                text_style=ft.TextStyle(color=theme.primary),
            )

        else:
            return None

        refs[f.id] = (f, ctrl)
        return ctrl

    def apply(self, refs: dict):
        for id, (f, ctrl) in refs.items():
            new_val = ctrl.value
            if new_val != f.value:
                f.value = new_val
                if f.on_change:
                    f.on_change(new_val)