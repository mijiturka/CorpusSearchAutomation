REM Corpus Search automatisation for all files in psd directory

SETLOCAL

FOR /r icepahc-v0.9\psd %%X IN (*.psd) DO (
    java -cp CS_2.003.04.jar csearch.CorpusSearch icepahc-v0.9\queries\rel_ice.c icepahc-v0.9\psd\%%~nX.psd
    java -cp CS_2.003.04.jar csearch.CorpusSearch icepahc-v0.9\queries\output_ice.q icepahc-v0.9\queries\rel_ice.cod
	cd icepahc-v0.9\queries
    REN "rel_ice.cod" "%%~nX.cod"
    REN "rel_ice.cod.ooo" "%%~nX.cod.ooo"
	cd ..
	cd ..
)

IF %ERRORLEVEL% NEQ 0 (
  ECHO %ERRORLEVEL%
)

ENDLOCAL
