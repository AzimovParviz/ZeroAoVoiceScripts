@echo off

set curp=%~dp0
set toolsp=%curp%\..\tools
set PYTHONPATH=%toolsp%\EDDecompiler\Decompiler;%toolsp%\PyLibs

set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a

set input=%curp%\tmp\py.%curd%
set output=%curp%\tmp\psp.py.%curd%

md "%output%"

copy /Y "%input%\*.py" "%output%\"
del /Q "%output%\a*.py"
