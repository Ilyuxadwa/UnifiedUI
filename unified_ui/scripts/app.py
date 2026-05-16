import platform
import flet as ft

from theme import get_theme, Theme
from settings import Settings
import utils



DESKTOP_PLATFORMS = {ft.PagePlatform.WINDOWS, ft.PagePlatform.MACOS, ft.PagePlatform.LINUX}
MOBILE_PLATFORMS  = {ft.PagePlatform.ANDROID, ft.PagePlatform.IOS}

LANDSCAPE = [ft.DeviceOrientation.LANDSCAPE_LEFT, ft.DeviceOrientation.LANDSCAPE_RIGHT]
PORTRAIT  = [ft.DeviceOrientation.PORTRAIT_UP,    ft.DeviceOrientation.PORTRAIT_DOWN]


def get_screen_resolution() -> tuple[int, int]:
    if platform.system() == "Windows":
        try:
            import ctypes, ctypes.wintypes
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.SystemParametersInfoW(48, 0, ctypes.byref(rect), 0)  # SPI_GETWORKAREA = 48
            return rect.right - rect.left, rect.bottom - rect.top
        except Exception:
            pass

    try:
        import tkinter
        root = tkinter.Tk()
        root.withdraw()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.destroy()
        return w, h
    except Exception:
        pass

    return 1920, 1080



class App:

    #=====- Main -=====#

    def __init__(self):
        self.page: ft.Page = None
        self.settings: Settings | None = None
        self.theme: Theme = get_theme("Light")
        self.orientation: str = "landscape"
        self.title: str = ""
        self.size: str = "full"

    def run(self, title: str = ""):
        self.title = title
        ft.app(target=self.build)

    async def build(self, page: ft.Page):
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
                self.page.window.width = screen_w
                self.page.window.height = screen_h
                self.page.window.left = 0
                self.page.window.top = 0
                self.page.window.title_bar_hidden = True
                self.page.window.maximized = True
            else:
                if self.size == "1/2": divisor = 1.5
                else: divisor = 2.0
                print (int(screen_w / divisor), int(screen_h / divisor))
                self.page.window.width = int(screen_w / divisor)
                self.page.window.height = int(screen_h / divisor) + 40 
                self.page.update()
                await self.page.window.center()
            self.page.window.resizable = False
            self.page.window.maximizable = False

        self.page.add(self.top_bar())

        self.page.window.disabled = False
        self.page.update()

    def top_bar(self):
        s = utils.scale(self.size)

        right_controls = [
            ft.IconButton(
                icon=ft.Icons.SETTINGS,
                icon_color=self.theme.secondary,
                icon_size=int(36 * s),
                tooltip="Settings",
                on_click=lambda e: self.open_settings()
            )
        ]

        if self.size == "full" and self.page.platform in DESKTOP_PLATFORMS:
            right_controls.append(
                ft.IconButton(
                    icon=ft.Icons.CLOSE_ROUNDED,
                    icon_color=self.theme.cancel_button,
                    icon_size=int(36 * s),
                    tooltip="Close",
                    on_click=lambda e: self.page.run_task(self.page.window.close)
                )
            )

        return ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    bgcolor=self.theme.background,
                    padding=16 * s,
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
                            ft.Row(spacing=0, controls=right_controls)
                        ]
                    )
                ),
                ft.Container(
                    height=5 * s,
                    border_radius=999,
                    bgcolor=self.theme.additional_color,
                    margin=20 * s
                )
            ]
        )

    def open_settings(self):
        s = utils.scale(self.size)

        if self.settings is None:
            controls, refs = [], {}
        else:
            controls, refs = self.settings.build_controls(self.theme, s)

        def close(e):
            self.page.pop_dialog()

        def apply(e):
            if self.settings:
                self.settings.apply(refs)
            self.page.pop_dialog()

        dialog = ft.AlertDialog(
            bgcolor=self.theme.background,
            title=ft.Text(
                "Settings",
                color=self.theme.primary,
                weight=ft.FontWeight.BOLD,
                font_family=self.theme.font_family,
                size=int((self.theme.font_size + 12) * s),
            ),
            content=ft.Container(
                width=self.page.window.width - 100 * s,
                height=self.page.window.height - 100 * s,
                content=ft.Column(
                    tight=True,
                    spacing=int(16 * s),
                    controls=controls,
                ),
            ),
            actions=[
                ft.FilledButton(
                    "Close",
                    style=ft.ButtonStyle(bgcolor=self.theme.cancel_button,
                                        color=self.theme.background),
                    on_click=close,
                ),
                ft.FilledButton(
                    "Apply",
                    style=ft.ButtonStyle(bgcolor=self.theme.ok_button,
                                        color=self.theme.background),
                    on_click=apply,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.show_dialog(dialog)

    def change_theme(self, name: str):
        self.theme = get_theme(name)
        return self

    #=====- Configuration -=====#

    def set_orientation(self, orientation: str):
        if orientation not in ("landscape", "portrait"):
            raise ValueError(f"Invalid orientation '{orientation}'. Use 'landscape' or 'portrait'.")
        self.orientation = orientation
        return self

    def set_size(self, size: str):
        if size not in ("full", "1/2", "1/4"):
            raise ValueError(f"Invalid size '{size}'. Use 'full', '1/2' or '1/4'.")
        self.size = size
        return self
    
    def custom_settings(self, settings: "Settings"):
        self.settings = settings
        return self
    