import flet as ft

from typing import Any

from .theme import get_theme, available_themes, Theme
from .settings import Settings, SettingsField
from .settings import Settings
from . import utils
from . import tools



DESKTOP_PLATFORMS = {ft.PagePlatform.WINDOWS, ft.PagePlatform.MACOS, ft.PagePlatform.LINUX}
MOBILE_PLATFORMS  = {ft.PagePlatform.ANDROID, ft.PagePlatform.IOS}

LANDSCAPE = [ft.DeviceOrientation.LANDSCAPE_LEFT, ft.DeviceOrientation.LANDSCAPE_RIGHT]
PORTRAIT  = [ft.DeviceOrientation.PORTRAIT_UP,    ft.DeviceOrientation.PORTRAIT_DOWN]



class App:

    #=====- Main -=====#

    def __init__(self):
        self.page: ft.Page = None
        self.settings: Settings | None = None
        self.body: ft.ListView = ft.ListView(expand=True, spacing=0, padding=ft.Padding(left=16, right=16, top=12, bottom=12))
        self.version: str = "0.99"
        self.theme: Theme = get_theme("Light")
        self.orientation: str = "landscape"
        self.title: str = ""
        self.size: str = "full"
        self.fixed_size: bool = False
        self.initialized: bool = False
        self.icon: str | None = None
        self.ui_builder = None
        self.pages: dict = {}
        self.current_page: str | None = None
        self.on_ready = None
        self.on_ready_async = None

    def run(self, title: str = ""):
        self.title = title
        ft.app(target=self.build)

    async def build(self, page: ft.Page):
        self.page = page
        self.page.window.disabled = True
        self.page.update()

        if not self.initialized:

            if self.settings is None:
                self.settings = Settings()

            system = self.settings.get_or_create_category("system", "System")
            system.fields.insert(0, SettingsField(
                id="theme",
                label="Theme",
                type="dropdown",
                value=self.theme.name,
                options=available_themes(),
                on_change=lambda val: self.change_theme(val)
            ))

            if not self.fixed_size and self.page.platform in DESKTOP_PLATFORMS:
                system.fields.insert(0, SettingsField(
                    id="size",
                    label="Size",
                    type="dropdown",
                    value=self.size,
                    options=["full", "1/2", "1/4"],
                    on_change=lambda val: self.set_size(val)
                ))

            self.settings.categories.remove(system)
            self.settings.categories.insert(0, system)

        

        self.page.title = self.title
        self.page.padding = 0

        if self.icon:
            self.page.window.icon = self.icon

        await self.load_settings()

        self.page.bgcolor = self.theme.background

        if self.page.platform in MOBILE_PLATFORMS:
            if not self._initialized:
                orientations = LANDSCAPE if self.orientation == "landscape" else PORTRAIT
                await self.page.set_allowed_device_orientations(orientations)

        elif self.page.platform in DESKTOP_PLATFORMS:
            screen_w, screen_h = utils.get_screen_resolution()

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
                self.page.window.title_bar_hidden = False
                self.page.window.maximized = False
                self.page.window.width = int(screen_w / divisor)
                self.page.window.height = int(screen_h / divisor) + 40
                self.page.update()
                await self.page.window.center()

            self.page.window.resizable = False
            self.page.window.maximizable = False

        self.initialized = True

        self.app_ui()

        self.page.window.disabled = False
        self.page.update()

        if self.on_ready:
            self.on_ready(self)

        if self.on_ready_async:
            self.page.run_task(self.on_ready_async(), self)

    def app_ui(self):
        s = utils.scale(self.size)

        if self.ui_builder:
            self.body = ft.ListView(expand=True, spacing=0, padding=ft.Padding(left=16, right=16, top=12, bottom=12))
            self.ui_builder(self)

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

        return self.page.add(ft.Column(
            expand=True,
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
                                size=int(22 * s),
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
                ),
                self.body,
                ft.Container(
                    padding=ft.Padding(left=0, top=0, right=16 * s, bottom=12 * s),
                    alignment=ft.Alignment(1, 1),
                    content=ft.Text(
                        f"v{self.version}",
                        color=self.theme.additional_color,
                        size=int(24 * s),
                        font_family=self.theme.font_family,
                    )
                )
            ]
        ))

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
                self.page.run_task(self.save_settings)
            self.page.pop_dialog()

        dialog = ft.AlertDialog(
            bgcolor=self.theme.background,
            title=ft.Text(
                "Settings",
                color=self.theme.primary,
                weight=ft.FontWeight.BOLD,
                font_family=self.theme.font_family,
                size=int(24 * s)
            ),
            content=ft.Container(
                width=self.page.window.width - 100 * s,
                height=self.page.window.height - 100 * s,
                content=ft.Column(
                    tight=True,
                    spacing=int(16 * s),
                    scroll=ft.ScrollMode.AUTO,
                    controls=controls
                )
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
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.show_dialog(dialog)

    async def save_settings(self):
        if self.settings:
            for f in self.settings.fields:
                await self.save(f.id, f.value)
            self.page.controls.clear()
            self.page.update()
            await self.build(self.page)

    async def load_settings(self):
        if self.settings:
            for f in self.settings.fields:
                val = await self.load(f.id)
                if val is not None:
                    f.value = val
                    if f.on_change:
                        f.on_change(val)

    def change_theme(self, name: str):
        self.theme = get_theme(name)
        return self
    
    async def save(self, key: str, value: Any):
        await self.page.shared_preferences.set(f"{self.title}.{key}", value)

    async def load(self, key: str, default: Any = None) -> Any:
        val = await self.page.shared_preferences.get(f"{self.title}.{key}")
        return val if val is not None else default

    async def delete(self, key: str):
        await self.page.shared_preferences.remove(f"{self.title}.{key}")


    #=====- Configuration -=====#

    def set_icon(self, path: str):
        self.icon = path
        return self

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
    
    def is_fixed_size(self, fixed: bool):
        self.fixed_size = fixed
        return self
    
    def custom_settings(self, settings: "Settings"):
        self.settings = settings
        return self
    
    def set_version(self, version: str):
        self.version = version
        return self
    
    def set_next(self, callback):
        self.on_ready = callback
        return self
    
    def set_async_next(self, callback):
        self.on_ready_async = callback
        return self
    

    #=====- UI Building -=====#

    def add_element(self, *controls: ft.Control):
        for control in controls:
            self.body.controls.append(control)
        if self.page:
            self.page.update()
        return self

    def update(self):
        self.body.controls.clear()
        if self.ui_builder:
            self.ui_builder(self)
        if self.page:
            self.page.update()
        return self

    def add_page(self, name: str, builder):
        self.pages[name] = builder
        if self.current_page is None:
            self.current_page = name
            self.ui_builder = builder
        return self

    def navigate(self, name: str):
        if name not in self.pages:
            raise ValueError(f"Page '{name}' not found. Register it with add_page() first.")
        self.current_page = name
        self.ui_builder = self.pages[name]
        self.update()
        return self

    def alignment(self, align_type, *controls, **kwargs):
        match align_type:
            case "cstart": return tools.column_align_start(self, *controls, **kwargs)
            case "ccenter": return tools.column_align_center(self, *controls, **kwargs)
            case "cend": return tools.column_align_end(self, *controls, **kwargs)
            case "cspace_between": return tools.column_align_space_between(self, *controls, **kwargs)
            case "cspace_around": return tools.column_align_space_around(self, *controls, **kwargs)
            case "cspace_evenly": return tools.column_align_space_evenly(self, *controls, **kwargs)
            case "rstart": return tools.row_align_start(self, *controls, **kwargs)
            case "rcenter": return tools.row_align_center(self, *controls, **kwargs)
            case "rend": return tools.row_align_end(self, *controls, **kwargs)
            case "rspace_between": return tools.row_align_space_between(self, *controls, **kwargs)
            case "rspace_around": return tools.row_align_space_around(self, *controls, **kwargs)
            case "rspace_evenly": return tools.row_align_space_evenly(self, *controls, **kwargs)

    def set_ui(self, builder):
        self.ui_builder = builder
        return self
    
    def get_work_area(self) -> tuple[int, int]:
        s = self.scale = utils.scale(self.size)
        if self.page:
            return self.page.window.width - int(32*s), self.page.window.height - int(24*s)
        else:
            return utils.get_screen_resolution()