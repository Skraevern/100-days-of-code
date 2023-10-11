from stock_handler import StockHandler
from news_handler import NewsHandler
from message_handler import MessageHandler

stock_handler = StockHandler()
news_handler = NewsHandler()
message_handler = MessageHandler()

new_stock = stock_handler.get_price(day_index=0)
old_stock = stock_handler.get_price(day_index=1)
old_stock = stock_handler.get_price(2) if old_stock == new_stock else old_stock

difference = stock_handler.get_diff_percentage(new_stock, old_stock)

print(old_stock, new_stock, difference)

if difference > 5 or difference < -5:
    text = news_handler.get_3_articles(new_stock, old_stock, percentage=difference)
    message_handler.send_telegram(message=text)
