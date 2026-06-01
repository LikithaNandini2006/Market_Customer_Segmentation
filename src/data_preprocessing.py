import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Dict


def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data from `filepath` into a DataFrame."""
    return pd.read_csv(filepath)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the DataFrame and encode the `Gender` column to integers.

    Behavior:
    - Requires a `Gender` column; raises `KeyError` if missing.
    - Fills missing `Gender` values with the mode.
    - Normalizes common values case-insensitively (e.g. 'Male', 'male', 'M').
    - Uses an explicit mapping for common genders; unknown values are encoded
      with `LabelEncoder` (offset to avoid colliding with the explicit mapping).

    Returns the modified DataFrame (same object, encoded `Gender`).
    """

    if 'Gender' not in df.columns:
        raise KeyError("DataFrame must contain a 'Gender' column")

    original = df['Gender'].astype(str).str.strip()

    if df['Gender'].isnull().any():
        try:
            mode_val = df['Gender'].mode().iloc[0]
            original = original.fillna(mode_val)
        except Exception:
            original = original.fillna('')

    lowered = original.str.lower()

    explicit_map: Dict[str, int] = {
        'male': 1,
        'm': 1,
        'female': 0,
        'f': 0,
    }

    mapped = lowered.map(explicit_map)

    unknown_mask = mapped.isna()
    if unknown_mask.any():
        le = LabelEncoder()
        encoded_unknowns = le.fit_transform(original[unknown_mask])
        offset = max(explicit_map.values()) + 1
        mapped.loc[unknown_mask] = encoded_unknowns + offset

    df['Gender'] = mapped.astype(int)
    return df
