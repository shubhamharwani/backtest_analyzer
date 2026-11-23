import numpy as np
import pandas as pd
from datetime import date, time, datetime
import streamlit as st
import plotly.express as px
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import statistics
import random
from scipy import stats
import calendar
import math
import six
import datetime as dt
import seaborn as sns

# page config
st.set_page_config(page_title='Trade Log Dashboard', page_icon=':bar_chart:', layout='wide')

# instructions video
st.sidebar.subheader('Instructions:')
git_url = 'https://github.com/oyesindhi/backtest_analyzer'
st.sidebar.markdown(f'<a href={git_url}><button style="background-color:#FF4B4B;">Read Documentation</button></a>',unsafe_allow_html=True)

# sidebar header
st.sidebar.header('Filters:')

# setting paths for multiple files to be uploaded and taken into single dataframe

path1 = []
path2 = []
path3 = []
path4 = []
path5 = []
no_of_files = st.sidebar.number_input('How Many Portfolios Do You Want To Analyze ?',0,5,0,
help='''Specify the number of portfolios you want to analyze.

By default it takes 0 and loads the sample journal from our backend.

You can analyze upto 5 portfolios.''')

# if file is 1
try:
    if no_of_files == 1:
        path1 = st.sidebar.file_uploader('Please upload your file 1')
        if path1 is not None:
            file1 = pd.read_excel(path1)

        else:
            pass
        if path1 is not None:
            csv = file1
            csv.sort_values(by='date',inplace=True)
            
        else:
            path = 'Data/default.xlsx'
            csv = pd.read_excel(path)
            csv.sort_values(by='date',inplace=True)

    # if file is 2

    elif no_of_files == 2:
        path1 = st.sidebar.file_uploader('Please upload your file 1')
        if path1 is not None:
            file1 = pd.read_excel(path1)
        else:
            pass
        path2 = st.sidebar.file_uploader('Please upload your file 2')
        if path2 is not None:
            file2 = pd.read_excel(path2)
        else:
            pass
        if path2 is not None:
            frames = [file1,file2]
            csv = pd.concat(frames)
            csv.sort_values(by='date',inplace=True)
        else:
            path = 'Data/default.xlsx'
            csv = pd.read_excel(path)
            csv.sort_values(by='date',inplace=True)

    # if file is 3

    elif no_of_files == 3:
        path1 = st.sidebar.file_uploader('Please upload your file 1')
        if path1 is not None:
            file1 = pd.read_excel(path1)
        else:
            pass
        path2 = st.sidebar.file_uploader('Please upload your file 2')
        if path2 is not None:
            file2 = pd.read_excel(path2)
        else:
            pass
        path3 = st.sidebar.file_uploader('Please upload your file 3')
        if path3 is not None:
            file3 = pd.read_excel(path3)
        else:
            pass
        if path3 is not None:
            frames = [file1,file2,file3]
            csv = pd.concat(frames)
            csv.sort_values(by='date',inplace=True)
        else:
            path = 'Data/default.xlsx'
            csv = pd.read_excel(path)
            csv.sort_values(by='date',inplace=True)

    # if file is 4

    elif no_of_files == 4:
        path1 = st.sidebar.file_uploader('Please upload your file 1')
        if path1 is not None:
            file1 = pd.read_excel(path1)
        else:
            pass
        path2 = st.sidebar.file_uploader('Please upload your file 2')
        if path2 is not None:
            file2 = pd.read_excel(path2)
        else:
            pass
        path3 = st.sidebar.file_uploader('Please upload your file 3')
        if path3 is not None:
            file3 = pd.read_excel(path3)
        else:
            pass
        path4 = st.sidebar.file_uploader('Please upload your file 4')
        if path4 is not None:
            file4 = pd.read_excel(path4)
        else:
            pass
        if path4 is not None:
            frames = [file1,file2,file3,file4]
            csv = pd.concat(frames)
            csv.sort_values(by='date',inplace=True)
        else:
            path = 'Data/default.xlsx'
            csv = pd.read_excel(path)
            csv.sort_values(by='date',inplace=True)

    # if file is 5

    elif no_of_files == 5:
        path1 = st.sidebar.file_uploader('Please upload your file 1')
        if path1 is not None:
            file1 = pd.read_excel(path1)
        else:
            pass
        path2 = st.sidebar.file_uploader('Please upload your file 2')
        if path2 is not None:
            file2 = pd.read_excel(path2)
        else:
            pass
        path3 = st.sidebar.file_uploader('Please upload your file 3')
        if path3 is not None:
            file3 = pd.read_excel(path3)
        else:
            pass
        path4 = st.sidebar.file_uploader('Please upload your file 4')
        if path4 is not None:
            file4 = pd.read_excel(path4)
        else:
            pass
        path5 = st.sidebar.file_uploader('Please upload your file 5')
        if path5 is not None:
            file5 = pd.read_excel(path5)
        else:
            pass
        if path5 is not None:
            frames = [file1,file2,file3,file4,file5]
            csv = pd.concat(frames)
            csv.sort_values(by='date',inplace=True)
        else:
            path = 'Data/default.xlsx'
            csv = pd.read_excel(path)
            csv.sort_values(by='date',inplace=True)

    else:
        path = 'Data/default.xlsx'
        csv = pd.read_excel(path)
        csv.sort_values(by='date',inplace=True)
except Exception:
    st.warning('Please upload correct file!')
    st.stop()


#st.sidebar.header('Please Use This Filter:')
capital = st.sidebar.number_input('Capital For This Strategy :',1,1000000000,100000,1,help='''Specify your capital.

All the parameters will be calculated as per the capital you specify.''')

day_name = csv['date'].dt.day_name()                        # find day name
month_name = csv['date'].dt.month_name()                    # find month name
year_name = pd.DatetimeIndex(csv['date']).year              # find year

buy_price = csv['buy_price']
sell_price = csv['sell_price']
qty = csv['qty']

pnl = (sell_price-buy_price)*qty
cum_pnl = pnl.cumsum()                               # calculating TOTAL cumulative PNL
equity = capital + cum_pnl                                  # calculating TOTAL equity

equity_peak = equity.cummax()                               # calcualting TOTAL equity peak

drawdown = equity - equity_peak                             # calculating TOTAL drawdown
mdd = (drawdown / capital)*100                              # TOTAL mdd in % format

csv['pnl'] = pnl
csv['cum_pnl'] = cum_pnl
csv['equity'] = equity
csv['equity_peak'] = equity_peak
csv['drawdown'] = drawdown
csv['mdd'] = mdd
csv['day_name'] = day_name
csv['month_name'] = month_name
csv['year'] = year_name


# side bar filter day and month
day = st.sidebar.multiselect('Select The Day:',options=csv['day_name'].unique(),default=csv['day_name'].unique())
month = st.sidebar.multiselect('Select The Month:',options=csv['month_name'].unique(),default=csv['month_name'].unique())
year_ = st.sidebar.multiselect('Select The Year:',options=csv['year'].unique(),default=csv['year'].unique())

# new and dynamic dataframe for selection
csv_selection = csv.query('day_name == @day & month_name == @month & year == @year_')

# data points as per new dynamic dataframe
month_pnl = csv_selection['pnl']
month_cum_pnl = csv_selection['pnl'].cumsum()
month_equity = capital + month_cum_pnl                                  # calculating equity
month_equity_peak = month_equity.cummax()                               # calcualting equity peak
month_drawdown = month_equity - month_equity_peak                            # calculating drawdown
month_mdd = (month_drawdown/capital)*100                                     # mdd in % format

month_buy_price = csv_selection['buy_price']
month_sell_price = csv_selection['sell_price']
month_qty = csv_selection['qty']

# for splitting win trade and loss trade list

month_xwin = []                               # xwin is a blank list in which all win trades will be added
month_xloss = []                              # xloss is a blank list in which all loss trades will be added

for num in month_pnl:
    if num > 0:
        month_xwin.append(num)
    else:
        month_xloss.append(num)

# for counting winning and losing streaks

month_win_streak = 0
month_loss_streak = 0
month_win_streak_list = []
month_loss_streak_list = []

for num in month_pnl:
    if num > 0:
        month_win_streak += 1
        month_win_streak_list.append(month_win_streak)
        month_loss_streak = 0 
    elif num <=0:
        month_loss_streak += 1
        month_loss_streak_list.append(month_loss_streak)
        month_win_streak = 0
    else:
        pass

# for counting longest time drawdown period

month_mdd_final_days = 0
month_mdd_days = 0

for num in month_drawdown:
    if num < 0:
        month_mdd_days += 1

        if month_mdd_days > month_mdd_final_days:
            month_mdd_final_days = month_mdd_days
    else:
        month_mdd_days = 0

# monthly stats

try:
    month_total_pnl = round(month_pnl.sum(),2)

    month_max_drawdown = round(month_drawdown.min(),2)
    month_mdd_perc = round(min(month_mdd),2)

    month_total_trades = len(month_pnl)
    month_win_trades =  len(month_xwin)
    month_loss_trades = len(month_xloss)
    month_win_rate = round((month_win_trades / month_total_trades)*100,2)

    month_avg_pnl = round(month_pnl.mean(),2)
    month_avg_win = round(sum(month_xwin)/month_win_trades,2)
    month_avg_loss = round(sum(month_xloss)/month_loss_trades,2)
    month_avg_rr = round(month_avg_win / - month_avg_loss,2)

    month_gross_wins = (month_avg_win * month_win_trades)
    month_gross_loss = (month_avg_loss * month_loss_trades)
    month_profit_factor = round(month_gross_wins / - month_gross_loss,2)

    month_expectancy = round((((month_avg_rr * month_win_rate) - (100 - month_win_rate)))/100,2)

    no_of_years = len(year_)
    month_calmar = round((month_total_pnl/no_of_years)/-month_max_drawdown,2)

    month_max_win = round(max(month_pnl),2)
    month_max_loss = round(min(month_pnl),2)
    month_max_win_perc = round((month_max_win/capital)*100,2)
    month_max_loss_perc = round((month_max_loss/capital)*100,2)

    month_win_streak_count = max(month_win_streak_list)
    month_loss_streak_count = max(month_loss_streak_list)

    month_pnl_perc = round((month_total_pnl/capital)*100,2)

    final_profit = capital + month_total_pnl
    tenure = 1 / no_of_years
    cagr = round((((final_profit/capital)**tenure)-1)*100,2)

    simple_annul = round((((month_total_pnl/capital)*100)/no_of_years),2)

    risk_adjusted_return = (((month_total_pnl/no_of_years)/capital)*100) - 4
    stddev = (statistics.stdev(month_pnl)/100)
    sharpe = round(risk_adjusted_return / stddev,2)
    sortino = round(risk_adjusted_return / (-1*month_mdd_perc),2)
    
    kelly = round(((month_win_rate/100) - ((1-(month_win_rate/100))/month_avg_rr)) * 100,2)
except Exception:
    st.error('Oops! Something is wrong!')
    st.warning('Possible errros: Please check the filters you have chosen in the sidebar. This error usually occurs when you have not selected any Day / Month / Year in the dropdown box.')
    st.stop()


# /////////////// STATS WITH SLIPPAGES STARTS HERE //////////////////////////////

slippage = st.sidebar.number_input('Insert Slippage',0.0,100.0,0.0,0.25, help='Insert Your Desired Slippages in %.')
slippage_perc = slippage/100

# calculate slippage on buy price & sell price and make 2 list of new buy and sell price including slippages

buy_price_after_slippage = month_buy_price + (month_buy_price * slippage_perc)
sell_price_after_slippage = month_sell_price - (month_sell_price * slippage_perc)

csv_selection['buy_price_after_slippage'] = buy_price_after_slippage
csv_selection['sell_price_after_slippage'] = sell_price_after_slippage

# calculating new pnl after slippage
pnl_after_slippage = (sell_price_after_slippage - buy_price_after_slippage) * qty

# create a new column called pnl after slippage
csv_selection['pnl_after_slippage'] = pnl_after_slippage


month_pnl_after_slippage = csv_selection['pnl_after_slippage']
month_cum_pnl_after_slippage = csv_selection['pnl_after_slippage'].cumsum()
month_equity_after_slippage = capital + month_cum_pnl_after_slippage                          
month_equity_peak_after_slippage = month_equity_after_slippage.cummax()                       
month_drawdown_after_slippage = month_equity_after_slippage - month_equity_peak_after_slippage
month_mdd_after_slippage = (month_drawdown_after_slippage/capital)*100 
month_total_pnl_after_slippage = round(month_pnl_after_slippage.sum(),2)
month_max_drawdown_after_slippage = round(month_drawdown_after_slippage.min(),2)
month_mdd_perc_after_slippage = round(min(month_mdd_after_slippage),2)


month_xwin_after_slippage = []                               # xwin is a blank list in which all win trades will be added
month_xloss_after_slippage = []                              # xloss is a blank list in which all loss trades will be added

for num in csv_selection['pnl_after_slippage']:
    if num > 0:
        month_xwin_after_slippage.append(num)
    else:
        month_xloss_after_slippage.append(num)


try:
    month_total_trades_after_slippage = len(csv_selection['pnl_after_slippage'])
    month_win_trades_after_slippage =  len(month_xwin_after_slippage)
    month_loss_trades_after_slippage = len(month_xloss_after_slippage)                                                    
    month_win_rate_after_slippage = round((month_win_trades_after_slippage / month_total_trades_after_slippage)*100,2)

    month_avg_pnl_after_slippage = round(month_pnl_after_slippage.mean(),2)                                                       
    month_avg_win_after_slippage = round(sum(month_xwin_after_slippage)/month_win_trades_after_slippage,2)                                        
    month_avg_loss_after_slippage = round(sum(month_xloss_after_slippage)/month_loss_trades_after_slippage,2)                                  
    month_avg_rr_after_slippage = round(month_avg_win_after_slippage / - month_avg_loss_after_slippage,2)                                         

    month_gross_wins_after_slippage = (month_avg_win_after_slippage * month_win_trades_after_slippage)
    month_gross_loss_after_slippage = (month_avg_loss_after_slippage * month_loss_trades_after_slippage)
    month_profit_factor_after_slippage = round(month_gross_wins_after_slippage / - month_gross_loss_after_slippage,2)

    month_expectancy_after_slippage = round(((month_avg_rr_after_slippage * month_win_rate_after_slippage) - (100 - month_win_rate_after_slippage))/100,2)

    month_calmar_after_slippage = round((month_total_pnl_after_slippage/no_of_years)/-month_max_drawdown_after_slippage,2)

    month_max_win_after_slippage = round(max(month_pnl_after_slippage),2)
    month_max_loss_after_slippage = round(min(month_pnl_after_slippage),2)
    month_max_win_perc_after_slippage = round((month_max_win_after_slippage/capital)*100,2)
    month_max_loss_perc_after_slippage = round((month_max_loss_after_slippage/capital)*100,2)
except Exception:
    st.error('Oops! Something went wrong!')
    st.warning('Possible errors: This error possibly occurs when you input wrong data in slippage. Please check your input once again.')
    st.stop()

# for counting winning and losing streaks

month_win_streak_after_slippage = 0
month_loss_streak_after_slippage = 0
month_win_streak_list_after_slippage = []
month_loss_streak_list_after_slippage = []

for num in month_pnl_after_slippage:
    if num > 0:
        month_win_streak_after_slippage += 1
        month_win_streak_list_after_slippage.append(month_win_streak_after_slippage)
        month_loss_streak_after_slippage = 0 
    elif num <=0:
        month_loss_streak_after_slippage += 1
        month_loss_streak_list_after_slippage.append(month_loss_streak_after_slippage)
        month_win_streak_after_slippage = 0
    else:
        pass


month_win_streak_count_after_slippage = max(month_win_streak_list_after_slippage)
month_loss_streak_count_after_slippage = max(month_loss_streak_list_after_slippage)

month_pnl_perc_after_slippage = round((month_total_pnl_after_slippage/capital)*100,2)

final_profit_after_slippage = capital + month_total_pnl_after_slippage
tenure = 1 / no_of_years
cagr_after_slippage = round((((final_profit_after_slippage/capital)**tenure)-1)*100,2)

simple_annul_after_slippage = round((((month_total_pnl_after_slippage/capital)*100)/no_of_years),2)

risk_adjusted_return_after_slippage = (((month_total_pnl_after_slippage/no_of_years)/capital)*100) - 4
stddev = (statistics.stdev(month_pnl_after_slippage)/100)
sharpe_after_slippage = round(risk_adjusted_return_after_slippage / stddev,2)
sortino_after_slippage = round(risk_adjusted_return_after_slippage / (-1*month_mdd_perc_after_slippage),2)

kelly_after_slippage = round(((month_win_rate_after_slippage/100) - ((1-(month_win_rate_after_slippage/100))/month_avg_rr_after_slippage)) * 100,2)

# for counting longest time drawdown period

month_mdd_final_days_after_slippage = 0
month_mdd_days_after_slippage = 0

for num in month_drawdown_after_slippage:
    if num < 0:
        month_mdd_days_after_slippage += 1

        if month_mdd_days_after_slippage > month_mdd_final_days_after_slippage:
            month_mdd_final_days_after_slippage = month_mdd_days_after_slippage
    else:
        month_mdd_days_after_slippage = 0



# ///////////////////////// THIS IS CALCULATION FOR COSTS //////////////////////////////


brokerage_per_order = st.sidebar.number_input('Brokerage Per Order:',0,99999,0,1)

buy_side_turnover = buy_price_after_slippage * qty
sell_side_turnover = sell_price_after_slippage * qty
total_turnover = (buy_price_after_slippage + sell_price_after_slippage) * qty

brokerage_per_trade = brokerage_per_order * 2

options_stt = sell_price_after_slippage * (0.05/2)
nse_transaction_charges = (buy_price_after_slippage + sell_price_after_slippage) * (0.053/2)
sebi_charges = total_turnover * 0.000001
gst = (brokerage_per_trade + sebi_charges + nse_transaction_charges) *0.18
stamp_charges = buy_side_turnover * 0.00003
total_costs = (brokerage_per_trade + options_stt + nse_transaction_charges + sebi_charges+gst + stamp_charges)

month_pnl_after_costs = month_pnl_after_slippage - total_costs
    
csv_selection['brokerage_per_trade'] = brokerage_per_trade
csv_selection['nse_transaction_charges'] = nse_transaction_charges
csv_selection['stamp_charges'] = stamp_charges
csv_selection['options_stt'] = options_stt
csv_selection['sebi_charges'] = sebi_charges
csv_selection['gst'] = gst
csv_selection['total_costs'] = total_costs

csv_selection['net_pnl'] = month_pnl_after_costs



#>>>>>>>>>>>>>>>>>>>>>>CALCULATION OF COSTS IS DONE NOW ASSIGNING NEW VARIABLES AGAIN <<<<<<<<<<<<<<<<<<<<<<<<<


month_cum_pnl_after_costs = csv_selection['net_pnl'].cumsum()
month_equity_after_costs = capital + month_cum_pnl_after_costs                          
month_equity_peak_after_costs = month_equity_after_costs.cummax()                       
month_drawdown_after_costs = month_equity_after_costs - month_equity_peak_after_costs
month_mdd_after_costs = (month_drawdown_after_costs/capital)*100 
month_total_pnl_after_costs = round(month_pnl_after_costs.sum(),2)
month_max_drawdown_after_costs = round(month_drawdown_after_costs.min(),2)
month_mdd_perc_after_costs = round(min(month_mdd_after_costs),2)


month_xwin_after_costs = []                               # xwin is a blank list in which all win trades will be added
month_xloss_after_costs = []                              # xloss is a blank list in which all loss trades will be added

for num in csv_selection['net_pnl']:
    if num > 0:
        month_xwin_after_costs.append(num)
    else:
        month_xloss_after_costs.append(num)


try:
    month_total_trades_after_costs = len(csv_selection['net_pnl'])
    month_win_trades_after_costs =  len(month_xwin_after_costs)
    month_loss_trades_after_costs = len(month_xloss_after_costs)                                                    
    month_win_rate_after_costs = round((month_win_trades_after_costs / month_total_trades_after_costs)*100,2)

    month_avg_pnl_after_costs = round(month_pnl_after_costs.mean(),2)                                                       
    month_avg_win_after_costs = round(sum(month_xwin_after_costs)/month_win_trades_after_costs,2)                                        
    month_avg_loss_after_costs = round(sum(month_xloss_after_costs)/month_loss_trades_after_costs,2)                                  
    month_avg_rr_after_costs = round(month_avg_win_after_costs / - month_avg_loss_after_costs,2)                                         

    month_gross_wins_after_costs = (month_avg_win_after_costs * month_win_trades_after_costs)
    month_gross_loss_after_costs = (month_avg_loss_after_costs * month_loss_trades_after_costs)
    month_profit_factor_after_costs = round(month_gross_wins_after_costs / - month_gross_loss_after_costs,2)

    month_expectancy_after_costs = round(((month_avg_rr_after_costs * month_win_rate_after_costs) - (100 - month_win_rate_after_costs))/100,2)

    month_calmar_after_costs = round((month_total_pnl_after_costs/no_of_years)/-month_max_drawdown_after_costs,2)

    month_max_win_after_costs = round(max(csv_selection['net_pnl']),2)
    month_max_loss_after_costs = round(min(csv_selection['net_pnl']),2)
    month_max_win_perc_after_costs = round((month_max_win_after_costs/capital)*100,2)
    month_max_loss_perc_after_costs = round((month_max_loss_after_costs/capital)*100,2)


    # for counting winning and losing streaks

    month_win_streak_after_costs = 0
    month_loss_streak_after_costs = 0
    month_win_streak_list_after_costs = []
    month_loss_streak_list_after_costs = []

    for num in month_pnl_after_costs:
        if num > 0:
            month_win_streak_after_costs += 1
            month_win_streak_list_after_costs.append(month_win_streak_after_costs)
            month_loss_streak_after_costs = 0 
        elif num <=0:
            month_loss_streak_after_costs += 1
            month_loss_streak_list_after_costs.append(month_loss_streak_after_costs)
            month_win_streak_after_costs = 0
        else:
            pass


    month_win_streak_count_after_costs = max(month_win_streak_list_after_costs)
    month_loss_streak_count_after_costs = max(month_loss_streak_list_after_costs)

    month_pnl_perc_after_costs = round((month_total_pnl_after_costs/capital)*100,2)

    final_profit_after_costs = capital + month_total_pnl_after_costs
    tenure = 1 / no_of_years
    cagr_after_costs = round((((final_profit_after_costs/capital)**tenure)-1)*100,2)

    simple_annul_after_costs = round((((month_total_pnl_after_costs/capital)*100)/no_of_years),2)

    risk_adjusted_return_after_costs = (((month_total_pnl_after_costs/no_of_years)/capital)*100) - 4
    stddev = (statistics.stdev(csv_selection['net_pnl'])/100)
    sharpe_after_costs = round(risk_adjusted_return_after_costs / stddev,2)
    sortino_after_costs = round(risk_adjusted_return_after_costs / (-1*month_mdd_perc_after_costs),2)
    
    kelly_after_costs = round(((month_win_rate_after_costs/100) - ((1-(month_win_rate_after_costs/100))/month_avg_rr_after_costs)) * 100,2)

    # for counting longest time drawdown period

    month_mdd_final_days_after_costs = 0
    month_mdd_days_after_costs = 0

    for num in month_drawdown_after_costs:
        if num < 0:
            month_mdd_days_after_costs += 1

            if month_mdd_days_after_costs > month_mdd_final_days_after_costs:
                month_mdd_final_days_after_costs = month_mdd_days_after_costs
        else:
            month_mdd_days_after_costs = 0
except Exception:
    st.error('Oops! Something went wrong!')
    st.warning('Possible errors: This error possible occurs when you input wrong data in the brokerage. Please check your input once again')
    st.stop()






#//////////////// DESIGN STARTS FROM HERE /////////////////

st.subheader('Backtest / Trading Journal Analyzer')

# create 3 colums and post

month1, month2, month3 = st.columns(3)
with month1:
    st.text_area('Raw Analysis','''Total PNL : {}
Total PNL % : {} %

Total Trades : {}
Win Trades : {}
Loss Trades : {}
Win Rate : {} %

Average PNL Per Trade : {} 
Average Win PNL : {}
Average Loss PNL : {}
Average Risk to Reward Ratio : {}

Max Drawdown : {}
MDD% : {} %
Time Drawdown : {} Trades

Longest Winning Streak : {}
Longest Losing Streak : {}

Biggest Profit in Single Trade : {}  ({} %)
Biggest Loss in Single Trade : {}  ({}%)

Profit Factor : {}
Expectancy : {}
Calmar/RMDD : {}

Sharpe : {}
Sortino : {}

Kelly % : {}

CAGR : {} %
Simple Yearly : {} %'''
.format(month_total_pnl,month_pnl_perc,month_total_trades,month_win_trades,month_loss_trades,month_win_rate,month_avg_pnl,
month_avg_win,month_avg_loss,month_avg_rr,month_max_drawdown,month_mdd_perc,month_mdd_final_days,month_win_streak_count,month_loss_streak_count,month_max_win,month_max_win_perc,month_max_loss,
month_max_loss_perc,month_profit_factor,month_expectancy,month_calmar,sharpe,sortino,kelly,cagr,simple_annul),height=800)


with month2:
    st.text_area('After Slippages','''Total PNL : {}
Total PNL % : {} %

Total Trades : {}
Win Trades : {}
Loss Trades : {}
Win Rate : {} %

Average PNL Per Trade : {} 
Average Win PNL : {}
Average Loss PNL : {}
Average Risk to Reward Ratio : {}

Max Drawdown : {}
MDD% : {} %
Time Drawdown : {} Trades

Longest Winning Streak : {}
Longest Losing Streak : {}

Biggest Profit in Single Trade : {}  ({} %)
Biggest Loss in Single Trade : {}  ({}%)

Profit Factor : {}
Expectancy : {}
Calmar/RMDD : {}

Sharpe : {}
Sortino : {}

Kelly % : {}

CAGR : {} %
Simple Yearly : {} %'''
.format(month_total_pnl_after_slippage,month_pnl_perc_after_slippage,month_total_trades_after_slippage,month_win_trades_after_slippage,
month_loss_trades_after_slippage,month_win_rate_after_slippage,month_avg_pnl_after_slippage,month_avg_win_after_slippage,month_avg_loss_after_slippage,
month_avg_rr_after_slippage,month_max_drawdown_after_slippage,month_mdd_perc_after_slippage,month_mdd_final_days_after_slippage,
month_win_streak_count_after_slippage,month_loss_streak_count_after_slippage,
month_max_win_after_slippage,month_max_win_perc_after_slippage,month_max_loss_after_slippage,
month_max_loss_perc_after_slippage,month_profit_factor_after_slippage,month_expectancy_after_slippage,month_calmar_after_slippage,
sharpe_after_slippage,sortino_after_slippage,kelly_after_slippage,cagr_after_slippage,simple_annul_after_slippage),height=800)


with month3:
    st.text_area('After Costs','''Total PNL : {}
Total PNL % : {} %

Total Trades : {}
Win Trades : {}
Loss Trades : {}
Win Rate : {} %

Average PNL Per Trade : {} 
Average Win PNL : {}
Average Loss PNL : {}
Average Risk to Reward Ratio : {}

Max Drawdown : {}
MDD% : {} %
Time Drawdown : {} Trades

Longest Winning Streak : {}
Longest Losing Streak : {}

Biggest Profit in Single Trade : {}  ({} %)
Biggest Loss in Single Trade : {}  ({}%)

Profit Factor : {}
Expectancy : {}
Calmar/RMDD : {}

Sharpe : {}
Sortino : {}

Kelly % : {}

CAGR : {} %
Simple Yearly : {} %'''
.format(month_total_pnl_after_costs,month_pnl_perc_after_costs,month_total_trades_after_slippage,month_win_trades_after_costs,
month_loss_trades_after_costs,month_win_rate_after_costs,month_avg_pnl_after_costs,month_avg_win_after_costs,month_avg_loss_after_costs,
month_avg_rr_after_costs,month_max_drawdown_after_costs,month_mdd_perc_after_costs,month_mdd_final_days_after_costs,
month_win_streak_count_after_costs,month_loss_streak_count_after_costs,
month_max_win_after_costs,month_max_win_perc_after_costs,month_max_loss_after_costs,
month_max_loss_perc_after_costs,month_profit_factor_after_costs,month_expectancy_after_costs,month_calmar_after_costs,
sharpe_after_costs,sortino_after_costs,kelly_after_costs,cagr_after_costs,simple_annul_after_costs),height=800)

pie1, pie2, pie3 = st.columns(3)

with pie1:
    st.write('Win Rate : Raw File')
    fig = go.Figure(data=[go.Pie(labels=['Wins','Losses'], values=[month_win_trades,month_loss_trades])])
    fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)

with pie2:
    st.write('Win Rate : After Slippages')
    fig = go.Figure(data=[go.Pie(labels=['Wins','Losses'], values=[month_win_trades_after_slippage,month_loss_trades_after_slippage])])
    fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)

with pie3:
    st.write('Win Rate : After Costs')
    fig = go.Figure(data=[go.Pie(labels=['Wins','Losses'], values=[month_win_trades_after_costs,month_loss_trades_after_costs])])
    fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)


#printing cumulative pnl chart and max drawdown chart

col1, col2 = st.columns(2)

with col1:
    fig = px.line(csv_selection, x='date', y=[month_cum_pnl,month_cum_pnl_after_slippage,month_cum_pnl_after_costs],title='Cumulative PNL')
    st.plotly_chart(fig,theme=None,use_container_width=True)


with col2:
    fig = px.line(csv_selection, x='date', y=[month_drawdown,month_drawdown_after_slippage,month_drawdown_after_costs],title='Drawdown Chart')
    st.plotly_chart(fig,theme=None,use_container_width=True)


st.write('Tradewise PNL')
#st.bar_chart(csv_selection['pnl'])                       # printing daily pnl bar chart
fig = go.Figure(data=[
    go.Bar(name='PNL', x=csv_selection['date'], y=csv_selection['pnl']),
    go.Bar(name='PNL After Slippages', x=csv_selection['date'], y=csv_selection['pnl_after_slippage']),
    go.Bar(name='PNL After Costs', x=csv_selection['date'], y=csv_selection['net_pnl'])
])
# Change the bar mode
fig.update_layout(barmode='group')
st.plotly_chart(fig,theme=None,use_container_width=True)


col1, col2, col3 = st.columns(3)

with col1:
    daywise = csv_selection.groupby(['day_name']).sum()
    st.write('Daywise PNL')
    st.bar_chart(daywise['pnl'])
    st.write('Daywise PNL After Slippage')
    st.bar_chart(daywise['pnl_after_slippage'])
    st.write('Daywise PNL After Costs')
    st.bar_chart(daywise['net_pnl'])

with col2:
    monthwise = csv_selection.groupby(['month_name']).sum()
    st.write('Monthwise PNL')
    st.bar_chart(monthwise['pnl'])
    st.write('Monthwise PNL After Slippage')
    st.bar_chart(monthwise['pnl_after_slippage'])
    st.write('Monthwise PNL After Costs')
    st.bar_chart(monthwise['net_pnl'])

with col3:
    yearwise = csv_selection.groupby(['year']).sum()
    st.write('Yearwise PNL')
    st.bar_chart(yearwise['pnl'])
    st.write('Yearwise PNL After Slippage')
    st.bar_chart(yearwise['pnl_after_slippage'])
    st.write('Yearwise PNL After Costs')
    st.bar_chart(yearwise['net_pnl'])




# returns in histogram
hist1, hist2, hist3 = st.columns(3)
with hist1:
    fig1 = px.histogram(month_pnl, x='pnl',title='Histogram of Daily PNL Distribution (Maximize Chart To See Better)',
    labels={'pnl' : 'PNL'},text_auto=True,histnorm='percent',color_discrete_sequence=['green'])
    st.plotly_chart(fig1,theme=None,use_container_width=True)

with hist2:    
    #options = st.selectbox('Enable Monte Carlo Simulation ?',options=('Yes','No'),index=1)
    options = st.checkbox('Enable Monte Carlo Simulation ?')
    #if options == 'Yes':
    if options:
        raw=csv_selection
        raw['date']=pd.to_datetime(raw['date'])
        raw['ret']=100*csv_selection['pnl']/capital
        raw.drop(['pnl'],inplace=True,axis=1)

        df_ret=raw.copy()
        df_ret.columns = map(str.lower, df_ret.columns)
        df_ret['date']=pd.to_datetime(df_ret['date'])
        df_ret['ret']=df_ret['ret']
        df_ret.head()

        def calc_max_dd(data_series):
            cumm_ret=data_series.cumsum()
            hwm=cumm_ret.cummax()
            dd=cumm_ret-hwm
            return round(min(dd),2)


        def monte_carlo(simulations,df):
            mdd_list=[]
            for s in range(simulations):
                mdd=0
                reshuffle=df['ret'].sample(frac=1).reset_index(drop=True)
                plt.plot(reshuffle.cumsum())
                mdd=calc_max_dd(reshuffle)
                mdd_list.append(mdd)
            plt.plot(df['ret'].cumsum(),linewidth=3,color='black')
            plt.xlabel('Trade No.')
            plt.ylabel('Cummulative Returns')
            plt.title('Monte Carlo Simulation for {} Simulations'.format(simulations))
            plt.show()
            return mdd_list   
        
        simulations=10000
        plt.figure(figsize=(8,6))
        mdd_list=monte_carlo(simulations,df_ret)
        #print(mdd_list)

        df_mdd=pd.DataFrame(mdd_list,columns=['Max DD'])

        n_tile=0.95 # Cut-Off Percentile to plot 
        n_tile_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile),2)

        n_tile90=0.90 # Cut-Off Percentile to plot 
        n_tile90_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile90),2)

        n_tile80=0.80 # Cut-Off Percentile to plot 
        n_tile80_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile80),2)

        n_tile75=0.75 # Cut-Off Percentile to plot 
        n_tile75_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile75),2)

        n_tile60=0.60 # Cut-Off Percentile to plot 
        n_tile60_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile60),2)

        n_tile50=0.50 # Cut-Off Percentile to plot 
        n_tile50_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile50),2)

        n_tile40=0.40 # Cut-Off Percentile to plot 
        n_tile40_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile40),2)

        n_tile30=0.30 # Cut-Off Percentile to plot 
        n_tile30_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile30),2)

        n_tile20=0.20 # Cut-Off Percentile to plot 
        n_tile20_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile20),2)

        n_tile10=0.10 # Cut-Off Percentile to plot 
        n_tile10_value=np.round(df_mdd['Max DD'].quantile(q=1-n_tile10),2)


        bt_dd=calc_max_dd(df_ret['ret'])
        fig2,ax=plt.subplots(1,1,figsize=(8,6))
        sns.histplot(ax=ax,x=-1*df_mdd['Max DD'],stat='percent')#,cumulative=True)
        ax.set_title('Cumulative Distribution of DD(%) from Monte Carlo Analysis')
        ax.set_xlabel('Max DD(%) during Simulation')
        ax.axvline(-bt_dd,ymax=1,color='purple',linestyle='dashed',linewidth=0.75)
        ax.axvline(-2*bt_dd,ymax=1,color='brown',linestyle='dashed',linewidth=0.75)
        ax.legend(labels=['bt_dd','2*bt_dd','Max DD Bins'])
        ax2 = ax.twinx()
        sns.ecdfplot(ax=ax2,x=-1*df_mdd['Max DD'],color='green',linewidth=1.25)
        sns.scatterplot(x=[-1*n_tile_value],y=[n_tile],ax=ax2,color='red')
        ax2.axvline(-1*n_tile_value,ymax=n_tile,color='red',linestyle='dashed',linewidth=2.8)
        ax2.set_ylabel('Proportion of DDs under X-axis DD%')
        ax.text(x=1,y=1,s='''Taken from code 
created by @Ankit_Quant''')
        #plt.show()

        fig3,ax=plt.subplots(1,1,figsize=(8,6))
        #new = sns.load_dataset(mdd_list)
        sns.lineplot(data=mdd_list)
        
        st.pyplot(fig2)
    
    else:
        #st.write('You have chosen NO. Please select YES to see results')
        st.write('Please select the checkbox to see results. Have patience, loading will take some time depending on the size of data.')
    
with hist3:
    #options = st.selectbox('Enable Monte Carlo Simulation ?',options=('Yes','No'),index=1)
    #if options == 'Yes':
    if options:
        st.text_area('Drawdown percentile based on Monte Carlo Simulation:','''95 percentile : {} %
90 percentile : {} %
80 percentile : {} %
75 percentile : {} %
60 percentile : {} %
50 percentile : {} %
40 percentile : {} %
30 percentile : {} %
20 percentile : {} %
10 percentile : {} %

Backtest Drawdown : {} %'''
    .format(n_tile_value,n_tile90_value,n_tile80_value,n_tile75_value,n_tile60_value,n_tile50_value,
    n_tile40_value,n_tile30_value,n_tile20_value,n_tile10_value,bt_dd),height=330)
        st.write('Code of calculation for Monte Carlo Simulation has been taken from [Ankit Garg\'s](https://twitter.com/Ankit_Quant) Medium.com [post](https://medium.com/@ankit_quant/when-to-stop-trading-a-strategy-28d104bb20b6).')
    else:
        st.write('-')


# function to convert and download the uploaded data as a csv file

st.sidebar.subheader('Download Detailed Report')

def convert_df(df):
    return df.to_csv().encode('utf-8')
    

file = convert_df(csv_selection)
st.sidebar.download_button('Download CSV Report',file,'data.csv',
help='''Download detailed report''')

st.markdown('###')

import streamlit.components.v1 as components

tw1, tw2 = st.columns(2)
with tw1:
    st.subheader('Follow me on Twitter')
    components.html('<a href="https://twitter.com/oyesindhi_?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-count="false">Follow @oyesindhi_</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>')
with tw2:
    st.subheader('Share on Twitter')
    components.html('<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-size="large" data-text="Checkout this Backtesting Analyzer by @oyesindhi_" data-url="https://batjaoptions.streamlit.app"data-show-count="false">"Share on Twitter</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>')

#this is the css code to hide main menu button, stream logo at the bottom, top header colored ribbon

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
