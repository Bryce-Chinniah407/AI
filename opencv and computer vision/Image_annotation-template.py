import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
image_path = 'C:\\Users\\User\\Desktop\\AI\\opencv and computer vision\\example.jpg'# User-provided image path
image = cv2.imread(image_path)

# Convert BGR to RGB for correct color display with matplotlib
image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Get image dimensions
height, width, _ = image_RGB.shape
# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rect1_width, rect1_height = 150, 150
topleft1 = (20, 20)  # Fixed 20 pixels padding from top-left
bottomleft1 = (topleft1[0]+rect1_width, topleft1[1]+rect1_height)
cv2.rectangle(image_RGB, topleft1, bottomleft1, (128, 67, 40),3) # Yellow rectangle

# Rectangle 2: Bottom-right corner
rect2_height, rect2_width=200, 150
topleft2 = (width - rect2_width - 20, height - rect2_height - 20)  # 20 pixels padding
bottomleft2 = (topleft2[0]+rect2_width, topleft2[1]+rect2_height)
cv2.rectangle(image_RGB, topleft2, bottomleft2, (64, 57, 98), 3)  # Magenta rectangle

# Step 3: Draw Circles at the Centers of Both Rectangles
   # Filled green circle
    # Filled red circle

# Step 4: Draw Connecting Lines Between Centers of Rectangles


# Step 5: Add Text Labels for Regions and Centers


# Step 6: Add Bi-Directional Arrow Representing Height
  # Start near the top-right
  # End near the bottom-right

# Draw arrows in both directions
  # Downward arrow
 # Upward arrow

# Annotate the height value


# Step 7: Display the Annotated Image
plt.figure(figsize=(12, 8))
plt.imshow(image_RGB)
plt.title("Annotated image with reigion")
plt.axis("off")
plt.show()