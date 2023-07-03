pytest -v -m --html=Reports\report_chrome.html testCases --browser chrome
rem pytest -v -m "regression" --html=Reports\report.html testCases --browser chrome 
rem pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser chrome 
rem pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser chrome 

rem pytest -v -m "sanity" --html=Reports\report_firefox.html testCases --browser firefox
rem pytest -v -m "regression" --html=Reports\report.html testCases --browser firefox
rem pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser firefox 
rem pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser firefox

pytest -v -m "Data" --html=Reports\report.html testcases --browser chrome
