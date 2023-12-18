import random
from typing import Any
import polars as pl
import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets


class DataExtractor:
    def load_df(self, **kwargs) -> pl.DataFrame:
        return pl.from_pandas(
            pd.read_table(
                "data/ml-1m/ratings.dat",
                header=None,
                sep="::",
                names=["user_id", "movie_id", "rating", "timestamp"],
                nrows=100,
            )
        )

    def __call__(self, df: pl.DataFrame, *args: Any, **kwds: Any) -> Any:
        df = self.load_df(df)
        return df


class DataCleaner:
    def sort_df(self, df: pl.DataFrame | pd.DataFrame) -> pl.DataFrame:
        return df.sort(["user_id", "timestamp"])

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        df = self.sort_df(df)
        return df


class FeatureEngineer:
    def __init__(self) -> None:
        pass


class DataSpliter:
    def split_df(
        self, df: pl.Dataframe, method: str = "leave-k-out", k=1
    ) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        if method == "leave-k-out":
            df_eval_test = df.group_by(["user_id"], maintain_order=True).tail(n=2 * k)
            df_train = df.join(df_eval_test, on=self.df.columns, how="anti")
            df_test = df_eval_test.group_by(["user_id"], maintain_order=True).tail(n=k)
            df_eval = df_eval_test.group_by(["user_id"], maintain_order=True).head(n=k)
        return df_train, df_eval, df_test

    def neg_sampling(self, df: pl.DataFrame, ratio: int = 4) -> pl.DataFrame:
        pass


class DataPrep:
    def __init__(self) -> None:
        self.extracter = DataExtractor()
        self.cleaner = DataCleaner()
        self.featurizer = FeatureEngineer()
        self.spliter = DataSpliter()

    def call_extracter(self):
        self.df = self.extracter()

    def call_components(self):
        self._uniq_users = self.df["user_id"].unique()
        self._uniq_items = self.df["movie_id"].unique()
        self._

    @property
    def uniq_items(self):
        return self._uniq_items


class MovieLensDataset(Dataset):
    def __init__(self):
        pass

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx: int):
        if self.label is None:
            return self.data[idx]
        else:
            return self.data[idx], self.label[idx]
