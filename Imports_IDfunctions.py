import random
import csv
import colorsys
import pandas as pd
import numpy as np  # For array operations
import matplotlib_inline
import matplotlib.pyplot as plt


def generate_random_cmyk():
    """Returns a tuple of four random CMYK values in the range [0, 1]."""
    return (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))


def cmyk_to_rgb(c, m, y, k):
    """Converts CMYK (0-1) to RGB (0-1)."""
    r = (1 - c) * (1 - k)
    g = (1 - m) * (1 - k)
    b = (1 - y) * (1 - k)
    return r, g, b


def rgb_to_hsv(r, g, b):
    """Converts RGB (0-1) to HSV (0-1)."""
    return colorsys.rgb_to_hsv(r, g, b)


def get_hex_code(r, g, b):
    """Converts RGB (0-1) to HEX code."""
    r_int = int(r * 255)
    g_int = int(g * 255)
    b_int = int(b * 255)
    return '#{:02x}{:02x}{:02x}'.format(r_int, g_int, b_int)


def classify_warm_cool(h, s):
    """Classifies color as warm, cool, or neutral based on HSV."""
    if s < 0.2:
        return "neutral"
    elif 0.0 <= h < 0.15 or 0.85 <= h <= 1.0:
        return "warm"  # Reds and pinks
    elif 0.15 <= h < 0.4:
        return "warm"  # Oranges and yellows
    elif 0.4 <= h < 0.65:
        return "cool"  # Greens and cyans
    elif 0.65 <= h < 0.85:
        return "cool"  # Blues and purples
    else:
        return "neutral"  # Catch any outliers


def classify_color_category(h, s, v):
    """Classifies color into categories with semantic associations."""
    if s < 0.2:
        return "Neutral"
    elif 0.0 <= h < 0.1 or 0.95 <= h <= 1.0:
        return "Fire"  # Red/Pink
    elif 0.1 <= h < 0.25:
        return "Energy"  # Orange/Yellow
    elif 0.25 <= h < 0.4:
        return "Energy"  # Yellow
    elif 0.4 <= h < 0.55:
        return "Nature"  # Green
    elif 0.55 <= h < 0.7:
        return "Water"  # Cyan
    elif 0.7 <= h < 0.85:
        return "Water"  # Blue
    elif 0.85 <= h < 0.95:
        return "Calm"  # Purple
    else:
        return "Other"


def generate_pixel_swatch(hex_code):
    """Generates a 3x3 pixel swatch string from a HEX code."""
    return hex_code * 9


def calculate_rgb_ratios(r, g, b):
    """Calculates the proportion of each RGB component."""
    total = r + g + b + 1e-7  # Avoid division by zero
    red_ratio = r / total
    green_ratio = g / total
    blue_ratio = b / total
    return red_ratio, green_ratio, blue_ratio


def is_dominant(value, threshold):
    """Checks if a value is dominant based on a threshold."""
    return 1 if value > threshold else 0


def is_saturated(s, high_threshold, low_threshold):
    """Checks if a color is highly or lowly saturated."""
    if s > high_threshold:
        return "High"
    elif s < low_threshold:
        return "Low"
    else:
        return "Normal"


def is_bright(v, high_threshold, low_threshold):
    """Checks if a color is bright or dark."""
    if v > high_threshold:
        return "High"
    elif v < low_threshold:
        return "Low"
    else:
        return "Normal"


def is_close_to_complementary(h, threshold=0.1):
    """Simplified check if a color is close to its complementary color."""
    complementary_hue = (h + 0.5) % 1.0  # Hue of the complementary color
    # Check if the hue is in a range around its complementary hue
    return 1 if (complementary_hue - threshold <= h <= complementary_hue + threshold) else 0


def generate_color_data(num_samples, output_filename="color_data.csv"):
    """Generates color data with warmth/coolness, categories, and RGB ratios."""
    data = []
    for i in range(num_samples):
        c, m, y, k = generate_random_cmyk()
        r, g, b = cmyk_to_rgb(c, m, y, k)
        h, s, v = rgb_to_hsv(r, g, b)
        hex_code = get_hex_code(r, g, b)
        warmth = classify_warm_cool(h, s)
        color_category = classify_color_category(h, s, v)
        pixel_swatch = generate_pixel_swatch(hex_code)
        red_ratio, green_ratio, blue_ratio = calculate_rgb_ratios(r, g, b)

        is_dom_cyan = is_dominant(c, 0.7)
        is_dom_magenta = is_dominant(m, 0.7)
        is_dom_yellow = is_dominant(y, 0.7)
        saturation_level = is_saturated(s, 0.7, 0.3)
        brightness_level = is_bright(v, 0.7, 0.3)
        is_complementary = is_close_to_complementary(h)

        data.append([i + 1, hex_code, h, s, v, c, m, y, k,
                     warmth, color_category, pixel_swatch,
                     red_ratio, green_ratio, blue_ratio,
                     is_dom_cyan, is_dom_magenta, is_dom_yellow,
                     saturation_level, brightness_level, is_complementary,
                     None])  # None for Color Associations

    header = ['Color_ID', 'Hex_code', 'HSV_Hue', 'HSV_Saturation', 'HSV_Value',
              'CMYK_Cyan', 'CMYK_Magenta', 'CMYK_Yellow', 'CMYK_Key_Black',
              'Warmth_Label', 'Color_Category', 'Pixel_Swatch',
              'RGB_Red_Ratio', 'RGB_Green_Ratio', 'RGB_Blue_Ratio',
              'Is_Dominant_Cyan', 'Is_Dominant_Magenta', 'Is_Dominant_Yellow',
              'Saturation_Level', 'Brightness_Level', 'Is_Complementary',
              'Color_Associations']

    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)
        print(f"Generated and saved {
              num_samples} color data points to '{output_filename}'.")


# %%
# Dataset configuring


num_samples_to_generate = 1000
output_file = "color_data.csv"
generate_color_data(num_samples_to_generate, output_file)

try:
    df = pd.read_csv(output_file)
    print("\nFirst 5 rows of the generated data:")
    print(df.head())
except FileNotFoundError:
    print(f"\nError: The file '{
          output_file}' was not found. There might have been an issue during data generation.")
except Exception as e:
    print(f"\nAn error occurred while trying to read the CSV file: {e}")

compile("Imports_IDfunctions.py")
