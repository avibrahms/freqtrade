# Activate virtual environment
source ./.venv/bin/activate

# Run RL strategy
freqtrade trade --freqaimodel ReinforcementLearner --strategy FreqaiRLStrategy --config config_freqai.example.json
freqtrade trade --freqaimodel PGPReinforcementLearner --strategy FreqaiRLStrategy 

# Create user directory
freqtrade create-userdir --userdir user_data

# Create config file
freqtrade new-config --config user_data/config.json

# Download data
freqtrade download-data --pairs ETH/BTC --exchange binance --days 5 -t 1h

# Run backtesting
freqtrade backtesting --config user_data/config.json --strategy SampleStrategy --timerange 20190801-20191001 -i 5m