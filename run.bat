pytest -v -s --html=./Reports/report.html Test_cases/
REM pytest -v -s -m "sanity" --html=./Reports/report.html Test_cases/ --browser chrome
REM pytest -v -s -m "regression" --html=./Reports/report.html Test_cases/ --browser chrome
REM pytest -v -s --html=./Reports/report.html Test_cases/ --browser firefox
REM pytest -v -s -m "sanity" --html=./Reports/report.html Test_cases/ --browser firefox
REM pytest -v -s -m "regression" --html=./Reports/report.html Test_cases/ --browser firefox