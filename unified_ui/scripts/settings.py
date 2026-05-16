from dataclasses import dataclass, field
from typing import Any, Callable, Literal
import flet as ft


@dataclass
class SettingsField:
    id: str
    label: str
    type: Literal["dropdown", "toggle", "text"]
    value: Any
    options: list[str] = field(default_factory=list)
    on_change: Callable[[Any], None] = None


class Settings:

    def __init__(self):
        self.fields: list[SettingsField] = []

    def add_dropdown(self, id: str, label: str, value: str, options: list[str], on_change: Callable[[str], None] = None):
        self.fields.append(SettingsField(id, label, "dropdown", value, options, on_change))
        return self

    def add_toggle(self, id: str, label: str, value: bool, on_change: Callable[[bool], None] = None):
        self.fields.append(SettingsField(id, label, "toggle", value, on_change=on_change))
        return self

    def add_text(self, id: str, label: str, value: str = "", on_change: Callable[[str], None] = None):
        self.fields.append(SettingsField(id, label, "text", value, on_change=on_change))
        return self

    def get(self, id: str) -> Any:
        for f in self.fields:
            if f.id == id:
                return f.value
        raise KeyError(f"No setting with id '{id}'")

    def build_controls(self, theme, s: float) -> tuple[list[ft.Control], dict]:
        controls = []
        refs = {}

        for f in self.fields:
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

            elif f.type == "switch":
                switch = ft.Switch(
                    value=f.value,
                    active_color=theme.primary,
                    inactive_thumb_color=theme.secondary,
                )
                ctrl = ft.Container(
                    border=ft.border.all(1, theme.secondary),
                    border_radius=8,
                    padding=ft.padding.symmetric(horizontal=12, vertical=8),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(f.label, color=theme.primary,
                                    font_family=theme.font_family,
                                    size=int(theme.font_size * s)),
                            switch,
                        ],
                    ),
                )
                refs[f.id] = (f, switch)   # point directly to switch
                controls.append(ctrl)
                continue

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

            else:
                continue

            refs[f.id] = (f, ctrl)
            controls.append(ctrl)

        return controls, refs

    def apply(self, refs: dict):
        """Read values from controls and fire on_change callbacks."""
        for id, (f, ctrl) in refs.items():
            if f.type == "toggle":
                new_val = ctrl.value
            elif f.type == "dropdown":
                new_val = ctrl.value
            elif f.type == "text":
                new_val = ctrl.value
            else:
                continue

            if new_val != f.value:
                f.value = new_val
                if f.on_change:
                    f.on_change(new_val)