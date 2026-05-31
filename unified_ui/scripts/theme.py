import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from importlib.resources import files


THEMES_DIR = files("unified_ui.themes")
 
 
@dataclass
class ThemeColors:
    background: str              = "#ffffff"
    additional_color: str        = "#ffffff"
    button: str                  = "#000000"
    button_additional: str       = "#ffffff"
    entry: str                   = "#ffffff"
    ok_button: str               = "#ffffff"
    cancel_button: str           = "#ffffff"
    primary: str                 = "#ffffff"
    secondary: str               = "#ffffff"
    label_text: str              = "#ffffff"
    outline: str                 = "#ffffff"
 
    @classmethod
    def from_dict(cls, data: dict) -> "ThemeColors":
        known = cls.__dataclass_fields__.keys()
        return cls(**{k: v for k, v in data.items() if k in known})
 
 
@dataclass
class ThemeFont:
    family: str = "Arial"
    size: int = 12
 
    @classmethod
    def from_dict(cls, data: dict) -> "ThemeFont":
        return cls(
            family=data.get("family", "Arial"),
            size=int(data.get("size", 12)),
        )
 
 
@dataclass
class ThemeOthers:
    outline_width: int = 1
 
    @classmethod
    def from_dict(cls, data: dict) -> "ThemeOthers":
        return cls(
            outline_width=int(data.get("outline_width", 1)),
        )
 
 
@dataclass
class ThemeData:
    name: str = "Unnamed"
    colors: ThemeColors = field(default_factory=ThemeColors)
    font: ThemeFont = field(default_factory=ThemeFont)
    others: ThemeOthers = field(default_factory=ThemeOthers)
    source: Optional[str] = field(default=None, repr=False)
 
    @classmethod
    def from_dict(cls, data: dict, source: Optional[str] = None) -> "ThemeData":
        return cls(
            name=data.get("name", "Unnamed"),
            colors=ThemeColors.from_dict(data.get("colors", {})),
            font=ThemeFont.from_dict(data.get("font", {})),
            others=ThemeOthers.from_dict(data.get("others", {})),
            source=source,
        )
 
 
class Theme:
 
    def __init__(self, data: ThemeData) -> None:
        self.name: str                    = data.name
        self.background: str              = data.colors.background
        self.additional_color: str        = data.colors.additional_color
        self.button: str                  = data.colors.button
        self.button_additional: str       = data.colors.button_additional
        self.entry: str                   = data.colors.entry
        self.ok_button: str               = data.colors.ok_button
        self.cancel_button: str           = data.colors.cancel_button
        self.primary: str                 = data.colors.primary
        self.secondary: str               = data.colors.secondary
        self.label_text: str              = data.colors.label_text
        self.outline: str                 = data.colors.outline
        self.font_family: str             = data.font.family
        self.font_size: int               = data.font.size
        self.outline_width: int           = data.others.outline_width
 
    def __repr__(self) -> str:
        return f"<Theme name={self.name!r}>"
 
 
def load_all() -> dict[str, Theme]:
    result: dict[str, Theme] = {}
 
    for path in sorted(THEMES_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            theme_data = ThemeData.from_dict(data, source=str(path))
            result[theme_data.name] = Theme(theme_data)
        except Exception as e:
            print(f"[theme] Skipping '{path.name}': {e}")
 
    return result
 
 
def get_theme(name: str = "Light") -> Theme:
    themes = load_all()
 
    if not themes:
        raise RuntimeError(f"No valid themes found in '{THEMES_DIR}'.")
 
    if name in themes:
        return themes[name]
 
    fallback = next(iter(themes.values()))
    print(f"[theme] '{name}' not found, falling back to '{fallback.name}'.")
    return fallback
 
 
def get_all_themes() -> dict[str, Theme]:
    return load_all()

def available_themes() -> list[str]:
    return list(load_all().keys())