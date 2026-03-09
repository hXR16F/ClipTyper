@echo off
set SCRIPT="ClipTyper.py"

if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
if exist %SCRIPT:.py=.exe% del %SCRIPT:.py=.exe%

python -m nuitka ^
    --standalone ^
    --onefile ^
    --lto=yes ^
    --windows-console-mode=disable ^
    --windows-icon-from-ico=ClipTyper.ico ^
    --remove-output ^
    --python-flag=-O ^
    --output-dir=dist ^
    --follow-imports ^
    --nofollow-import-to=tkinter ^
    --nofollow-import-to=test ^
    --nofollow-import-to=unittest ^
    --nofollow-import-to=pydoc ^
    --nofollow-import-to=distutils ^
    --nofollow-import-to=idlelib ^
    --nofollow-import-to=wx.richtext ^
    --nofollow-import-to=wx.html ^
    --nofollow-import-to=wx.printout ^
    --nofollow-import-to=wx.aui ^
    --nofollow-import-to=wx.stc ^
    --nofollow-import-to=wx.grid ^
    --nofollow-import-to=wx.media ^
    --nofollow-import-to=mouseinfo ^
    --nofollow-import-to=pyscreeze ^
    --nofollow-import-to=pygetwindow ^
    --nofollow-import-to=pyrect ^
    --nofollow-import-to=pytweening ^
    --nofollow-import-to=PIL.ImageGrab ^
    %SCRIPT%

echo.
echo Build finished!
