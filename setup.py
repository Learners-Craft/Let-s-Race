import cx_Freeze

executables = [cx_Freeze.Executable("Let's race.py")]

cx_Freeze.setup(
    name = "Let's Race",
    options = {"build_exe": {"packages": ["pygame"],
                             "include_files":["Images/Car_image/Blue racecar_transparent.png", "Images/Car_image/Red racecar_transparent.png", "Images/Car_image/racecar transparent.png", "Images/Car_image/race_car transparent.png", "music/crash.mp3", "music/music.mp3"]}},
    description = "I made this game using pygame, the game's name is Let's Race",
    executables = executables

    )
