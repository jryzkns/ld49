pyinstaller ^
    --add-data "assets/*;assets" ^
    --clean ^
    --noconfirm ^
    --noconsole ^
    --onefile ^
    --name "TWR" ^
    --icon=icon.ico ^
    main.py