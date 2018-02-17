This is very basic command line app project to download historical weather data from https://english.wunderground.com/ by parsing html files.
This site has also API REST interface, but you need to register to use it and the main purpose of this project was to learn parsing website via Python.
All data are saved into file in JSON format: [year][month][day][param_name][param_subname], please take a look at example json in dist directory.

To use app go to dist directory and in cmd call "main.exe job city_code start_year end_year", for example "main.exe parse EPWR 2008 2008"
Params:
1. job - parse or open
2. city_code - city code, you can get it from website, for example EPWA is city_code for https://english.wunderground.com/history/airport/EPWA/2018/2/16/MonthlyHistory.html
3. start_year - start year (include)
4. end_year - end year (include)

To generate new exe run generate_exe.bat
Project languages: Python 3.6 and cmd (to generate standalone exe)