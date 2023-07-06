pytest -v -m "sanity" --html=Reports\report.html testCases --browser chrome
pytest -v -m "regression" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Data1" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Data2" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Edit" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Delete" --html=Reports\report.html testCases --browser chrome












