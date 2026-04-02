import mplfinance as mpf
import yfinance as yf

df = yf.download("AAPL", start="2025-01-01", end="2026-01-01")

df.columns = df.columns.droplevel(1)

mpf.plot(df, 
         type='candle', 
         volume=True, 
         mav=(20, 50), 
         style='yahoo',
         title='AAPL with Volume & 20/50 MAV',
         tight_layout=True)