import os
from moviepy import VideoFileClip
from moviepy.video.tools.drawing import color_gradient
from moviepy import TextClip, CompositeVideoClip, ColorClip

# Define the input and output directories
input_dir = "IN"
output_dir = "OUT"

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define a function to apply filters to a video
def apply_filters(video):
    # Example filters: Increase contrast, add white background, and add text caption

    # Create a white background clip
    white_bg = ColorClip(size=video.size, color=(255, 255, 255)).with_duration(video.duration)

    # Create a text clip
    text = "Sample Caption"

    # Composite the video with the white background and text
    video = CompositeVideoClip([white_bg, video.with_position('center')])

    return video

# Process each video in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):  # Add other video formats if needed
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Load the video
        video = VideoFileClip(input_path)

        # Apply the filters
        filtered_video = apply_filters(video)

        # Save the video with the filters applied
        filtered_video.write_videofile(output_path, codec="libx264")

        # Close the video files to release resources
        video.close()
        filtered_video.close()

print("All videos have been processed and saved in the 'OUT' folder.")
