# activate virtual environment
source ./.venv/bin/activate

# Run RL strategy
freqtrade trade --freqaimodel ReinforcementLearner --strategy MyRLStrategy --config config.json
