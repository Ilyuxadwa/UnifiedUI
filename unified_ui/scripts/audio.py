import flet as ft
import flet_audio as fta


class AudioController:
    def __init__(self, page: ft.Page, volume: float = 1.0, muted: bool = False):
        self.page = page
        self.volume = volume
        self.muted = muted
        self.sounds: dict[str, fta.Audio] = {}


    def add_sound(self, name: str, src: str, volume: float | None = None, loop: bool = False):
        audio = fta.Audio(
            src=src,
            autoplay=False,
            volume=volume if volume is not None else self.volume,
            release_mode=fta.ReleaseMode.LOOP if loop else fta.ReleaseMode.STOP,
        )
        self.sounds[name] = audio

        async def mount():
            self.page.services.append(audio)
            self.page.update()

        self.page.run_task(mount)


    def set_volume(self, value: float):
        self.volume = max(0.0, min(1.0, value))

        async def apply_volume():
            for audio in self.sounds.values():
                audio.volume = self.volume
                audio.update()

        self.page.run_task(apply_volume)


    def get_volume(self) -> float:
        return self.volume


    def set_muted(self, muted: bool):
        self.muted = muted
        if muted:
            self.stop_all()


    def is_muted(self) -> bool:
        return self.muted


    def play(self, name: str):
        if self.muted:
            return

        audio = self.sounds.get(name)
        if audio is None:
            return

        self.page.run_task(audio.play)


    def stop(self, name: str):
        audio = self.sounds.get(name)
        if audio:
            self.page.run_task(audio.stop)


    def stop_all(self):
        for name in self.sounds:
            self.stop(name)
