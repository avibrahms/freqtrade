from pandas import DataFrame
from typing import Dict


allowed_pairs = ['BTC/USDT', 'BTC/USDT:USDT']

def check_pairs():
    def decorator(func):
        def wrapper(self, dataframe: DataFrame, metadata: Dict, **kwargs):
            if metadata.get("pair") in allowed_pairs:
                return func(self, dataframe, metadata, **kwargs)
            else:
                return dataframe
        return wrapper
    return decorator

def auto_decorate_methods(cls, decorator):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, decorator(attr_value))
    return cls
