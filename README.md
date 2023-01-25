# Backtesting Journal Analyzing For Options (NSE)

![general video](https://user-images.githubusercontent.com/78555897/214491600-f3303aeb-da50-4711-a3a6-b41b65eb265f.gif)

I initially created this tool for personal use but I think it can benefit a lot of people. 

This tool specifically helps you to show a realistic backtest report / journal by adding slippages and near to real transaction costs (Brokerage, STT Charges, Stamp Duty, SEBI Charges, Exchange Charges, GST, etc). 

All the charges inputs are taken from zerodha’s charges page (https://zerodha.com/charges) and verified with zerodha’s brokerage calculator (https://zerodha.com/brokerage-calculator).

# You can use the tool at https://batjaoptions.streamlit.app/

# Contact me
<a href="https://twitter.com/oyesindhi_?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-count="false">Follow @oyesindhi_</a>

<a href="https://twitter.com/intent/tweet?screen_name=oyesindhi_&ref_src=twsrc%5Etfw" class="twitter-mention-button" data-size="large" data-show-count="false">Give a shoutout to @oyesindhi_</a>

# How to use the tool?

1.	You have to upload your backtesting / trading journal in an Excel (XLSX) format. No other format will work (not even CSV). You can upload up to 5 excel files which means you can analyze data of 5 strategies combined like a portfolio.

![upload file](https://user-images.githubusercontent.com/78555897/214491772-e1a123b5-3f0f-434c-8e50-70e62933cffd.gif)

Note: make sure to write column headers of XLSX file as it is. Highly case sensitive.

![image](https://user-images.githubusercontent.com/78555897/214491922-3c249dea-c7ac-43b6-9f26-4f9e37289841.png)


2.	You need to specify capital for the strategy / set of strategies. Metrics in % will be shown accordingly.

![add capital](https://user-images.githubusercontent.com/78555897/214492397-d32aec1b-617c-4f80-a66c-961543db22ef.gif)


3.	You need to specify slippages in %. Slippages are applied on both entries and exits.

4.	You need to specify brokerage per order in rupees ₹. As of now, I have only made it as per brokerage per order plan and not other plans (fixed monthly brokerage, etc). If you trade with a “free brokerage plan”, just leave the brokerage option 0.

![add slippage  brokerage](https://user-images.githubusercontent.com/78555897/214492463-905cbcb1-9996-40d5-a64f-f37e8aab3f7f.gif)

# Credits

I have created this app using python with streamlit.
The code used for calculation of Monte Carlo Simulation is taken from <a href="https://twitter.com/ankit_quant?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-count="false">@ankit_quant</a> Medium post. Link to post - https://medium.com/@ankit_quant/when-to-stop-trading-a-strategy-28d104bb20b6

# Note

If you think we can make it more better by adding some features, please feel free to DM on twitter.

<a href="https://twitter.com/oyesindhi_?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-count="false">Follow @oyesindhi_</a>
