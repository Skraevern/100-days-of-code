from stock_handler import StockHandler
from news_handler import NewsHandler

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
more_than_5_perc_diff = False

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_handler = StockHandler()
new_stock = stock_handler.get_price(day_index=0)
old_stock = stock_handler.get_price(day_index=1)
old_stock = stock_handler.get_price(2) if old_stock == new_stock else old_stock
difference = stock_handler.get_diff_percentage(new_stock, old_stock)
if difference > 5 or difference < -5:
    more_than_5_perc_diff = True

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if more_than_5_perc_diff == False:
    news_handler = NewsHandler()
    text = news_handler.get_3_articles(
        new_stock=new_stock, old_stock=old_stock, percentage=difference
    )
print(text)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
