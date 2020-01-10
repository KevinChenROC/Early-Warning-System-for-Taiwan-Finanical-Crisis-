def make_url_stock_ai(symbol, data_start_date, data_end_date, r_key):
    return "https://stock-ai.com/ddl?s=" + symbol+"&r=" + \
        r_key + "&d1=" + data_start_date + "&d2=" + data_end_date
