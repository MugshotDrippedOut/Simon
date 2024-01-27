@ECHO off
REM Vytvorenie zlozky



IF[%1]==[](SET /P folder="Zvolte nazev zlozky: ")ELSE (SET folder=%1

MKDIR %folder%
cd %folder%
PING utb.cz > log.log

EXIT /B 0s