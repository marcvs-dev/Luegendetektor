@echo off
set /p vid=Willst du das Video anschauen? Ja/Nein: 

if "%vid%" == "Ja" (

    "Das Tatvideo.mp4"
    main.py

) else if "%vid%" == "Nein" (

    main.py

)