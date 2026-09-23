import flet as ft
import flet_audio as fta


class AudioController:
    def __init__(self, page: ft.Page, volume: float = 1.0, muted: bool = False):
        self.page = page
        self.volume = volume
        self.muted = muted
        self.audio = fta.Audio(src=None, autoplay=False, volume=volume)
        self.page.services.append(self.audio)
        self.page.update()


    def set_volume(self, value: float):
        self.volume = max(0.0, min(1.0, value))

        async def apply_volume():
            self.audio.volume = self.volume
            self.audio.update()

        self.page.run_task(apply_volume)


    def get_volume(self) -> float:
        return self.volume


    def set_muted(self, muted: bool):
        self.muted = muted
        if muted:
            self.stop()


    def is_muted(self) -> bool:
        return self.muted



    def play(self, src: str, volume: float | None = None, loop: bool = False):
        if self.muted:
            return

        async def start_playing():
            self.audio.src = src
            self.audio.volume = volume if volume is not None else self.volume
            self.audio.release_mode = fta.ReleaseMode.LOOP if loop else fta.ReleaseMode.RELEASE
            self.audio.update()
            await self.audio.play()

        self.page.run_task(start_playing)


    def stop(self):
        self.page.run_task(self.audio.release)