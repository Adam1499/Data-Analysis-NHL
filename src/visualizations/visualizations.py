import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
from PIL import Image
import seaborn as sns


def create_scatterplot(df: pd.DataFrame):
    _, ax = plt.subplots(figsize=(50, 30))

    sns.scatterplot(x='goals', y='assists', data=df, ax=ax, color='white')

    img_path = "../../data/team_logos/ANA.png"

    for i, row in df.iterrows():
        _add_image_marker(ax, img_path, row["goals"], row["assists"], img_size_px=100, player_name="test")

    ax.set_title("Goals vs Assists for Players", fontsize=40)
    ax.set_xlabel("Goals", fontsize=30)
    ax.set_ylabel("Assists", fontsize=30)
    ax.tick_params(axis='both', labelsize=25)

    plt.show()


def _add_image_marker(ax, img_path, x, y, img_size_px, player_name):
    img = Image.open(img_path)
    img_width, img_height = img.size

    scale_x = img_size_px / img_width
    scale_y = img_size_px / img_height
    scale_factor = max(scale_x, scale_y)

    imagebox = OffsetImage(img, zoom=scale_factor)
    ab = AnnotationBbox(imagebox, (x, y), frameon=False)
    ax.add_artist(ab)

    ax.text(x, y - img_size_px / 100, player_name, fontsize=25, color='black')

if __name__ == "__main__":
    pass