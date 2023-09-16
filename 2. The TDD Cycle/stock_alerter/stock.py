class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []
        # Add by me.
        self.timestamp_history = []
        
    @property
    def price(self):
        return self.price_history[-1] \
            if self.price_history else None
            
    # Add by me.
    @property
    def timestamp(self):
        return self.timestamp_history[-1] \
            if self.timestamp_history else None
        
    def update(self, timestamp, price):
        if price < 0:
            raise ValueError('price should not be negative')
        # Add by me.
        if self.timestamp:
            if self.timestamp > timestamp:
                raise ValueError('timestamp should not be older than the last')
        self.price_history.append(price)
        # Add by me.
        self.timestamp_history.append(timestamp)
        
    def is_increasing_trend(self):
        return self.price_history[-3] < \
            self.price_history[-2] < self.price_history[-1]
