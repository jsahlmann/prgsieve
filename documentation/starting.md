# Preparing DropIt

Start the program DropIt.

In my environment it is installed (unzipped from the downloaded zip-file) in a folder for portable programs:

C:\PortablePgms\DropIt_v8.5.1_Portable\DropIt.exe

Add a new profile. It is called Programm_Sieb in my environment.

Add a new association within this profile. It is called "SAS Programme sieben".

This association filters for files with the extension *.sas and opens them with the batch file main.bat

    REM main.bat expects a path to a filename which is the program file we would like to index
    REM It will be opened in an editor to have a look at it.
    REM Then it will be indexed in the program prgsieve
    echo "Program to be indexed: "
    echo %1
    REM Call editor, but no further processing of batch file before closing the editor
    REM C:\portableapps\PortableApps\Notepad++Portable\Notepad++Portable.exe %1
    C:\WPy64-3870\python-3.8.7.amd64\python.exe E:\ablage\ksfe_2021\prgsieve\prgsieve.py %1
    echo
    REM With the following line you can stop executing before closing for development purposes
    REM set /p Var1 = "Enter for end"

This batchfile opens it with the program ProgSieve.

The parameter %1 provides the path and the file name for the further processing with ProgSieve.

Example: E:\SAS_works\project_1\analysis_1\pgm\main.sas

# Indexing

Drag the file you want to index over the floating DropIt icon. You should have activated the correct profile.

The dialogbox will be opend and you can start the processing with the arrow-button. The program ProgSieve starts.

You can add your flags to the file and close ProgSieve.

The dialogbox will be closed after terminating ProgSieve.




