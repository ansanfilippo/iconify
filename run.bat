@echo off

:: Check for input file
if [%1]==[] goto noinput

:: Covert input file
copy %1 "%~dp0\input\%~n1%~x1"
%~dp0png2ico.exe -i %~dp0input -o %~dp1 -s 16 32bpp -s 32 32pp -s 48 32bpp  -s 96 32bpp -s 128 32bpp -s 512 32bpp 
del "%~dp0\input\%~n1%~x1"
pause
exit

:noinput
echo Please provide an input file by dragging and dropping the file onto the application shortcut or executable
echo.
pause
exit