import os
import pandas as pd
from yahooquery import Ticker as yq
import tkinter as tk
from tkinter import filedialog

# Add tickers in apostrophes, two are added as examples. Search exact ticker at https://finance.yahoo.com/
tickers = ['4300.SR', '4240.SR']

#################################################
## Beyond this point, user inputs not required ##
#################################################

# Global variable(s)
transpose = pd.DataFrame.transpose

# Create GUI window for folder selection
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory()

# Pull data and save to CSV
for ticker in tickers:
    # Create Excel object for each ticker
    xlwriter = pd.ExcelWriter(os.path.join(folder_path, f"{ticker}.xlsx"), engine='xlsxwriter')

    # Pull data
    data_bs = transpose(yq(ticker).balance_sheet(frequency="a", trailing=False))
    data_is = transpose(yq(ticker).income_statement(frequency="a", trailing=False))
    data_cf = transpose(yq(ticker).cash_flow(frequency="a", trailing=False))

    # Additional data
    data_earnings_hist = transpose(yq(ticker).earning_history)
    data_rec_trend = transpose(yq(ticker).recommendation_trend)
    data_valuation = transpose(yq(ticker).valuation_measures)

    # Push data frame to Excel and save
    data_bs.to_excel(xlwriter, sheet_name='Balance Sheet')
    data_is.to_excel(xlwriter, sheet_name='Income Statement')
    data_cf.to_excel(xlwriter, sheet_name='Cash Flow')
    data_earnings_hist.to_excel(xlwriter, sheet_name='Earning History')
    data_rec_trend.to_excel(xlwriter, sheet_name='Recommendations Trend')
    data_valuation.to_excel(xlwriter, sheet_name='Valuation')

    # Close XLS to save changes
    xlwriter.close()

print("Done. Closing.")
