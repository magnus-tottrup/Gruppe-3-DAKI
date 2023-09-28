import cv2 as cv
import numpy as np
import os

# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100])
    return tiles

# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.median(hsv_tile, axis=(0,1)) # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}") #Change value <= (less or equal to)
    if 20 <= hue <= 29 and 219 <= saturation <= 255 and 100 <= value <= 210:
        return "Field"
    if 29 <= hue <= 77 and 65 <= saturation <= 223 and 25 <= value <= 78:
        return "Forest"
    if 100 <= hue <= 110 and 220 <= saturation <= 260 and 108 <= value <= 205:
        return "Lake"
    if 21.5 <= hue <= 51 and 156 <= saturation <= 248 and 74 <= value <= 170:
        return "Grassland"
    if 17 <= hue <= 26 and 23 <= saturation <= 181 and 73 <= value <= 144:
        return "Swamp"
    if 19 <= hue <= 30 and 34 <= saturation <= 140 and 24 <= value <= 110:
        return "Mine"
    if 16 <= hue <= 40 and 41 <= saturation <= 193 and 45 <= value <= 150:
        return "Home"
    return "Unknown"

# Define main-function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"C:\Users\Admin\Skrivebord\King Domino dataset\73.jpg"
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image)
    print(len(tiles))

    # Create a copy of the original image for overlaying text
    image_with_text = image.copy()

    # Make terrain_count variables
    field_count = 0
    forest_count = 0
    lake_count = 0
    grassland_count = 0
    swamp_count = 0
    mine_count = 0
    home_count = 0

    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            # Declare new variable, terrain
            terrain = get_terrain(tile)
            print(terrain)
            print("=====")

            # Updating the terrain_count
            if terrain == "Field":
                field_count += 1
            if terrain == "Forest":
                forest_count += 1
            if terrain == "Lake":
                lake_count += 1
            if terrain == "Grassland":
                grassland_count += 1
            if terrain == "Swamp":
                swamp_count += 1
            if terrain == "Mine":
                mine_count += 1
            if terrain == "Home":
                home_count += 1

            # Overlay the HSV values on the image with separate lines
            x1, y1, x2, y2 = x * 100, y * 100, (x + 1) * 100, (y + 1) * 100
            hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
            hue, saturation, value = np.median(hsv_tile, axis=(0, 1))
            text = f"H: {hue:.2f}\nS: {saturation:.2f}\nV: {value:.2f}"
            cv.putText(image_with_text, f"H: {hue:.2f}", (x1 + 10, y1 + 20), 
                       cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
            cv.putText(image_with_text, f"S: {saturation:.2f}", (x1 + 10, y1 + 40),
                       cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
            cv.putText(image_with_text, f"V: {value:.2f}", (x1 + 10, y1 + 60), 
                       cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
   
    # Resize the image
    cv.namedWindow("Image with HSV Values", cv.WINDOW_NORMAL)
    resized_image = cv.resize(image_with_text, (1000, 1000))

    # Display the image with HSV values in a popup window
    cv.imshow("Image with HSV Values", image_with_text)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Print the terrain counts and scores
    print("Scoren er derfor:")
    print(f"'Field': \t{field_count}")
    print(f"'Forest': \t{forest_count}")
    print(f"'Lake': \t{lake_count}")
    print(f"'Grassland': \t{grassland_count}")
    print(f"'Swamp': \t{swamp_count}")
    print(f"'Mine': \t{mine_count}")
    print(f"'Home': \t{home_count}")

    

if __name__ == "__main__":
    main()