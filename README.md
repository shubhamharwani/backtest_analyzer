# 📊 Backtest & Trading Journal Analyzer

A quantitative trade-analytics and stress-testing dashboard built with **Python**, **Streamlit**, and **Plotly**. Upload up to 5 Excel trading journals to evaluate raw strategy performance side-by-side against **slippage-adjusted** and **Indian market transaction-cost-adjusted** returns—complete with equity curves, time-based breakdowns, and a **10,000-run Monte Carlo drawdown simulation**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-brightgreen)](https://batjaoptions.streamlit.app)

---

## 📌 Overview

Backtests often look profitable on paper until real-world execution friction—slippage, brokerage, taxes, and adverse trade sequencing—erodes the edge. **Backtest & Trading Journal Analyzer** bridges the gap between raw trade logs and realistic live performance:

1. **Multi-Portfolio Ingestion:** Merge and analyze up to 5 Excel trade logs simultaneously (or explore immediately using the built-in sample dataset).
2. **3-Tier Reality Check:** Compares **Raw P&L**, **After-Slippage P&L**, and **Net P&L (After Indian Market Costs)** side-by-side across 25+ institutional performance metrics.
3. **Statistical Stress Testing:** Runs a 10,000-iteration Monte Carlo simulation to estimate worst-case drawdown percentiles beyond what the historical sequence alone shows.

---

## ✨ Key Features

- **Multi-Portfolio Consolidation:** Upload and concatenate 1 to 5 `.xlsx` trade journals sorted chronologically, with a fallback sample dataset (`Data/default.xlsx`) for instant demoing.
- **Dynamic Filtering:** Slice performance by **Day of Week**, **Month**, and **Year**, alongside configurable **Starting Capital**, **Slippage (%)**, and **Brokerage per Order**.
- **Indian Options Cost Engine:** Automatically models brokerage, Options STT, NSE transaction charges, SEBI turnover fees, Stamp Duty, and 18% GST per trade.
- **25+ Performance & Risk Metrics:** Computes Total P&L, Win Rate, Avg Risk-to-Reward, Max Drawdown (`₹` & `%`), Time Drawdown (in trades), Longest Win/Loss Streaks, Profit Factor, Expectancy, Calmar Ratio, Sharpe Ratio, Sortino Ratio, Kelly Criterion (`%`), and CAGR across all three cost tiers.
- **Interactive Visualizations:**
  - Win/Loss breakdown pie charts (Raw vs. Slippage vs. Net)
  - Overlaid Cumulative Equity Curve & Drawdown charts
  - Grouped Trade-wise P&L bar chart
  - Day-wise, Month-wise, and Year-wise P&L attribution charts
  - Daily P&L percentage distribution histogram
- **10,000-Run Monte Carlo Simulation:** Randomly reshuffles trade returns to plot an empirical cumulative distribution (ECDF) of drawdowns and outputs 10th–95th percentile drawdown benchmarks against the historical backtest drawdown.
- **One-Click CSV Export:** Download the enriched dataset (including computed slippages, itemized taxes/charges, and net P&L) as `data.csv`.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python |
| **Frontend / UI** | Streamlit |
| **Data Processing** | Pandas, NumPy, SciPy |
| **Visualizations** | Plotly, Matplotlib, Seaborn |
| **Excel Parsing** | `openpyxl` (via Pandas) |

---

## 📂 Expected Input Format

Upload `.xlsx` files containing the following columns:

| `date` | `buy_price` | `sell_price` | `qty` |
| :--- | :--- | :--- | :--- |
| `2024-01-02` | `120.50` | `135.00` | `50` |
| `2024-01-03` | `98.00` | `91.25` | `50` |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/shubhamharwani/](https://github.com/shubhamharwani/)<repo-name>.git
   cd <repo-name>
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas numpy plotly matplotlib seaborn scipy openpyxl
   ```
   *(Or if using a `requirements.txt` file: `pip install -r requirements.txt`)*

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🗺️ Roadmap & Planned Enhancements

- [ ] **Modularize Metric Calculations:** Refactor the Raw, Slippage, and Net P&L blocks into a reusable helper function to eliminate code duplication.
- [ ] **Configurable Cost Presets:** Add toggleable statutory charge profiles for Equity Intraday, Equity Delivery, and Futures alongside Options.
- [ ] **Caching for Monte Carlo:** Cache simulation results with `@st.cache_data` and allow users to customize the number of simulation runs (e.g., 1,000 to 25,000).
- [ ] **CSV Upload Support:** Accept both `.csv` and `.xlsx` trade logs.

---

## 🙏 Acknowledgments

- Monte Carlo drawdown simulation methodology adapted from [Ankit Garg (@Ankit_Quant)](https://medium.com/@ankit_quant/when-to-stop-trading-a-strategy-28d104bb20b6).

---

## ⚠️ Disclaimer

This tool is built for educational and research purposes only and does not constitute financial or investment advice.

---

## 👤 Author

**Shubham Harwani**  
- GitHub: [@shubhamharwani](https://github.com/shubhamharwani)  
- Twitter/X: [@oyesindhi_](https://twitter.com/oyesindhi_)
