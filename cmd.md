# activate virtual environment
source ./.venv/bin/activate

# Run RL strategy
freqtrade trade --freqaimodel ReinforcementLearner --strategy FreqaiRLStrategy --config config_freqai.example.json
