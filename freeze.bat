pyinstaller ^
    --add-data "assets/*;assets" ^
    --clean ^
    --noconfirm ^
    --noconsole ^
    --onefile ^
    --name "wat" ^
    --icon=icon.ico ^
    main.py