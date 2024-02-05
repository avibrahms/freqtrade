import logging
from functools import reduce
from typing import Dict

# import talib.abstract as ta
from pandas import DataFrame
# from technical import qtpylib

from freqtrade.strategy import IStrategy
from freqtrade.util.vis import save_data_with_metadata

logger = logging.getLogger(__name__)


class FreqaiRLStrategy(IStrategy):

    def feature_engineering_standard(self, dataframe: DataFrame, metadata: Dict, **kwargs) -> DataFrame:  # noqa: E501
        # The following features are necessary for RL models
        dataframe["%-raw_close"] = dataframe["close"]
        dataframe["%-raw_open"] = dataframe["open"]
        dataframe["%-raw_high"] = dataframe["high"]
        dataframe["%-raw_low"] = dataframe["low"]
        save_data_with_metadata(dataframe, metadata["pair"])
        return dataframe

    def set_freqai_targets(self, dataframe, metadata: Dict, **kwargs) -> DataFrame:
        # For RL, there are no direct targets to set. This is filler (neutral)
        # until the agent sends an action.
        dataframe["&-action"] = 0
        save_data_with_metadata(dataframe, metadata["pair"])
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe = self.freqai.start(dataframe, metadata, self)
        save_data_with_metadata(dataframe, metadata["pair"])
        return dataframe

    def populate_entry_trend(self, df: DataFrame, metadata: dict) -> DataFrame:
        enter_long_conditions = [df["do_predict"] == 1, df["&-action"] == 1]
        if enter_long_conditions:
            df.loc[reduce(lambda x, y: x & y, enter_long_conditions), ["enter_long", "enter_tag"]] = (1, "long")  # noqa: E501
        enter_short_conditions = [df["do_predict"] == 1, df["&-action"] == 3]
        if enter_short_conditions:
            df.loc[reduce(lambda x, y: x & y, enter_short_conditions), ["enter_short", "enter_tag"]] = (1, "short")  # noqa: E501
        save_data_with_metadata(df, metadata["pair"])
        return df

    def populate_exit_trend(self, df: DataFrame, metadata: dict) -> DataFrame:
        exit_long_conditions = [df["do_predict"] == 1, df["&-action"] == 2]
        if exit_long_conditions:
            df.loc[reduce(lambda x, y: x & y, exit_long_conditions), "exit_long"] = 1

        exit_short_conditions = [df["do_predict"] == 1, df["&-action"] == 4]
        if exit_short_conditions:
            df.loc[reduce(lambda x, y: x & y, exit_short_conditions), "exit_short"] = 1
        save_data_with_metadata(df, metadata["pair"])
        return df
