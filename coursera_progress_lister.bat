@echo off
Rem Backup current index.html to backup folder
cd "backup"
copy "A:\coursera_course_progress_lister\index.html"
cd
dir
cd ..
Rem Opens folder in Visual Code
code .
pause
