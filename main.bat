REM main.bat expects a path to a filename which is the program file we would like to index
REM It will be opened in an editor to have a look at it.
REM Then it will be indexed in the program prgsieve
echo "Program to be indexed: "
echo %1
C:\portableapps\PortableApps\Notepad++Portable\Notepad++Portable.exe %1
C:\WPy64-3870\python-3.8.7.amd64\python.exe E:\ablage\ksfe_2021\prgsieve\prgsieve.py %1
echo
set /p Var1 = "Enter for end"
