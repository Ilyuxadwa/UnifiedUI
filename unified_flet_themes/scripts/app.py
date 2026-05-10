import sys
import platform
from pathlib import Path

import flet as ft

sys.path.insert(0, str(Path(__file__).parent))
from theme import get_theme, Theme

DESKTOP_PLATFORMS = {ft.PagePlatform.WINDOWS, ft.PagePlatform.MACOS, ft.PagePlatform.LINUX}
MOBILE_PLATFORMS  = {ft.PagePlatform.ANDROID, ft.PagePlatform.IOS}

LANDSCAPE = [ft.DeviceOrientation.LANDSCAPE_LEFT, ft.DeviceOrientation.LANDSCAPE_RIGHT]
PORTRAIT  = [ft.DeviceOrientation.PORTRAIT_UP,    ft.DeviceOrientation.PORTRAIT_DOWN]


def get_screen_resolution() -> tuple[int, int]:
    try:
        import tkinter
        root = tkinter.Tk()
        root.withdraw()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.destroy()
        return w, h
    except Exception:
        pass

    if platform.system() == "Windows":
        try:
            import ctypes
            user32 = ctypes.windll.user32
            return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        except Exception:
            pass

    return 1920, 1080


class App:

    #=====- Main -=====#

    def __init__(self):
        self.page: ft.Page = None
        self.theme: Theme  = get_theme("Light")
        self.orientation: str = "landscape"
        self.title: str = ""
        self.size: str = "full"

    def run(self, title: str = ""):
        self.title = title
        ft.app(target=self._build)

    async def _build(self, page: ft.Page):
        self.page = page
        self.page.window.disabled = True
        self.page.update()

        self.page.title = self.title
        self.page.bgcolor = self.theme.background
        self.page.padding = 0

        if self.page.platform in MOBILE_PLATFORMS:
            orientations = LANDSCAPE if self.orientation == "landscape" else PORTRAIT
            await self.page.set_allowed_device_orientations(orientations)

        elif self.page.platform in DESKTOP_PLATFORMS:
            screen_w, screen_h = get_screen_resolution()

            if self.size == "full":
                self.page.window.width  = screen_w
                self.page.window.height = screen_h
                self.page.window.left   = 0
                self.page.window.top    = 0
            else:
                divisor = 1.5 if self.size == "1/2" else 2
                self.page.window.width  = int(screen_w / divisor)
                self.page.window.height = int(screen_h / divisor)
                await self.page.window.center()

        self.page.add(self.top_bar())

        self.page.window.disabled = False
        self.page.update()

    def top_bar(self) -> ft.Container:
        s = self.scale
        return ft.Container(
            bgcolor=self.theme.additional_color,
            padding=ft.padding.symmetric(horizontal=int(16 * s), vertical=int(8 * s)),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        self.title,
                        color=self.theme.primary,
                        size=int((self.theme.font_size + 10) * s),
                        weight=ft.FontWeight.BOLD,
                        font_family=self.theme.font_family,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.SETTINGS,
                        icon_color=self.theme.primary,
                        icon_size=int(36 * s),
                        tooltip="Settings",
                        on_click=lambda e: self.open_settings(),
                    ),
                ],
            ),
        )
    
    @property
    def scale(self) -> float:
        return {"full": 1.0, "1/2": 0.75, "1/4": 0.5}[self.size]

    def open_settings(self):
        dialog = ft.AlertDialog(
            title=ft.Text("Settings"),
            content=ft.Column([]),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: self.page.pop_dialog()),
            ],
        )
        self.page.show_dialog(dialog)


    #=====- Configuration -=====#

    def set_theme(self, name: str) -> "App":
        self.theme = get_theme(name)
        return self

    def set_orientation(self, orientation: str) -> "App":
        if orientation not in ("landscape", "portrait"):
            raise ValueError(f"Invalid orientation '{orientation}'. Use 'landscape' or 'portrait'.")
        self.orientation = orientation
        return self

    def set_size(self, size: str) -> "App":
        if size not in ("full", "1/2", "1/4"):
            raise ValueError(f"Invalid size '{size}'. Use 'full', '1/2' or '1/4'.")
        self.size = size
        return self