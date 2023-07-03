<<<<<<< HEAD
rem pytest -v -m "sanity" --html=Reports\report_chrome.html testCases --browser chrome
=======
rem pytest -v -m --html=Reports\report_chrome.html testCases --browser chrome
>>>>>>> 502ed7cc86876ac921e30ef97f20df6a2c5ba3f7
rem pytest -v -m "regression" --html=Reports\report.html testCases --browser chrome 
rem pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser chrome 
rem pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser chrome 

rem pytest -v -m "sanity" --html=Reports\report_firefox.html testCases --browser firefox
rem pytest -v -m "regression" --html=Reports\report.html testCases --browser firefox
rem pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser firefox 
rem pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser firefox

<<<<<<< HEAD
rem pytest -v -m --html=Reports\report_chrome.html testCases --browser chrome
pytest -v -m "Data1" --html=Reports\report_chrome.html testCases --browser chrome
pytest -v -m "Data2" --html=Reports\report_chrome.html testCases --browser chrome
=======
pytest -v -m "Data" --html=Reports\report.html testCases --browser chrome
>>>>>>> 502ed7cc86876ac921e30ef97f20df6a2c5ba3f7
