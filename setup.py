from cx_Freeze import setup, Executable

setup(
    name="beeper",
    version="0.1",
    description="beep with custom frequency",
    executables=[Executable("main.py")]
)
