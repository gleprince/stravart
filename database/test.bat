@echo off

:: Ici on spécifie le path
forfiles /P "C:\Users\Guilhem Leprince\repo\data\%1\activities" /C "cmd /c echo @ext"