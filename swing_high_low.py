import pandas as pd
import numpy as np

def calculate_swing_points(df, window=2):
    """
    Calculates swing highs and swing lows in a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with 'High' and 'Low' columns.
        window (int): Number of bars to look back and forward for comparison.
                      A window of 2 means 2 bars before and 2 bars after.

    Returns:
        pd.DataFrame: Original DataFrame with 'SwingHigh' and 'SwingLow' columns.
    """
    df['SwingHigh'] = False
    df['SwingLow'] = False

    # Identify Swing Highs
    # A swing high is a high that is higher than 'window' bars before and after it.
    df['SwingHigh'] = np.where(
        (df['high'] == df['high'].rolling(window=2*window+1, center=True).max()) &
        (df['high'].shift(window).notna()) &
        (df['high'].shift(-window).notna()),
        df['high'],
        False
    )

    # Identify Swing Lows
    # A swing low is a low that is lower than 'window' bars before and after it.
    df['SwingLow'] = np.where(
        (df['low'] == df['low'].rolling(window=2*window+1, center=True).min()) &
        (df['low'].shift(window).notna()) &
        (df['low'].shift(-window).notna()),
        df['low'],
        False
    )
    swing_high_list = []
    swing_low_list = []
    for idx in range(len(df["SwingHigh"])):
        print(df["SwingHigh"][idx])
        if df["SwingHigh"][idx] != 0:
            swing_high_list.append((df["date"][idx], df["SwingHigh"][idx]))
        if df["SwingLow"][idx] != 0:
            swing_low_list.append((df["date"][idx], df["SwingLow"][idx]))
        else:
            continue
    return swing_high_list, swing_low_list

# Example Usage:
# Create a sample DataFrame (replace with your actual data)
# ticker_csv = "/media/dell/Works/zaza/Support-Resistance-Fibonacci/supres/src/BTCUSDT.csv"
# candle_count = 250
# df = pd.read_csv(
#             ticker_csv,
#             delimiter=",",
#             encoding="utf-8-sig",
#             index_col=False,
#             nrows=candle_count,
#             keep_default_na=False,
#         )

# # Calculate swing points with a window of 20
# df_with_swings = calculate_swing_points(df.copy(), window=20)
# print(df_with_swings)