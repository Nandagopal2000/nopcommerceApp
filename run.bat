rem pytest -v -m --html=Reports\report_chrome.html testCases --browser chrome
rem pytest -v -m "regression" --html=Reports\report.html testCases --browser chrome 
rem pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser chrome 
rem pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser chrome 

rem pytest -v -m "sanity" --html=Reports\report_firefox.html testCases --browser firefox
rem pytest -v -m "regression" --html=Reports\report.html testCases --browser firefox
rem pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser firefox 
rem pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser firefox


rem pytest -v -m --html=Reports\report_chrome.html testCases --browser chrome
rem pytest -v -m "Data1" --html=Reports\report_chrome.html testCases --browser chrome
rem pytest -v -m "Data2" --html=Reports\report_chrome.html testCases --browser chrome

pytest -v --html=Reports\newreport.html testCases/test_editCustomer.py --browser chrome
pytest -v --html=Reports\newreport.html testCases/test_deleteCustomer.py --browser chrome




