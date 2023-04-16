# Financial statements downloader
This Python script downloads financial statements (balance sheet, income statement, 
and cash flow statement) and other publicly available information via Yahoo! Finance  for 
listed companies.

### How to use?
1. Install Python3 using Microsoft Store or any other IDE of choice.


2. Download the zip https://github.com/voidbydefault/financial-statements/archive/refs/heads/master.zip


3. Unzip the code and open the folder, right click then select 'open in terminal'.


4. `copy/paste` following commands in 'cmd' or 'terminal' to get started:
      
   * `pip install -r requirements.txt`
   * `python3 main.py`


5. Enter tickers/symbols in code.country format [e.g., 4300.SR] in 'main.py'
   (browse https://finance.yahoo.com/ to find ticker(s) of interest)
   
    `tickers = ['4300.SR', '4240.SR', '####.XY']`


6. Select a folder to save financial statements in Excel format:

   ![img_1.png](help/save-location.png)

That's it.
