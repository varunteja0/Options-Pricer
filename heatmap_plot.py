import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from black_scholes import black_scholes_call, black_scholes_put

def generate_option_prices(s_range, v_range, K, T, r):
    call_prices = np.zeros((len(v_range), len(s_range)))
    put_prices = np.zeros((len(v_range), len(s_range)))
    for i, vol in enumerate(v_range):
        for j, s in enumerate(s_range):
            call_prices[i, j] = black_scholes_call(s, K, T, r, vol)
            put_prices[i, j] = black_scholes_put(s, K, T, r, vol)
    return call_prices, put_prices

def plot_heatmap(data, x_labels, y_labels, title, cmap, label):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data, xticklabels=np.round(x_labels, 2), yticklabels=np.round(y_labels, 2),
                cmap=cmap, annot=True, fmt=".2f", ax=ax, cbar_kws={'label': label})
    ax.set_xlabel("Spot Price")
    ax.set_ylabel("Volatility")
    ax.set_title(title, fontsize=15, weight='bold')
    plt.tight_layout()
    return fig
