"""
Video Generator Module
Creates video frames from text content using PIL and OpenCV.
"""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from typing import List, Tuple
import textwrap


class VideoGenerator:
    """Generates video from text content."""
    
    def __init__(self, width: int = 1920, height: int = 1080, fps: int = 30):
        """
        Initialize the video generator.
        
        Args:
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
        """
        self.width = width
        self.height = height
        self.fps = fps
    
    def create_text_frame(
        self,
        text: str,
        font_size: int = 48,
        font_color: Tuple[int, int, int] = (255, 255, 255),
        background_color: Tuple[int, int, int] = (0, 0, 0),
    ) -> np.ndarray:
        """
        Create a single frame with text content.
        
        Args:
            text: Text to display on the frame
            font_size: Font size in points
            font_color: RGB tuple for text color
            background_color: RGB tuple for background color
            
        Returns:
            Numpy array representing the frame
        """
        # Create a PIL image with background color
        img = Image.new('RGB', (self.width, self.height), background_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a default font, fallback to basic font
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        # Wrap text to fit within frame
        max_width = self.width - 200  # Padding
        wrapped_lines = []
        for line in text.split('\n'):
            if line.strip():
                wrapped = textwrap.wrap(line, width=40)
                wrapped_lines.extend(wrapped)
            else:
                wrapped_lines.append('')
        
        # Calculate text position to center vertically
        line_height = font_size + 10
        total_height = len(wrapped_lines) * line_height
        y_start = (self.height - total_height) // 2
        
        # Draw each line of text
        y = y_start
        for line in wrapped_lines:
            # Get text bounding box for centering horizontally
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            x = (self.width - text_width) // 2
            
            draw.text((x, y), line, font=font, fill=font_color)
            y += line_height
        
        # Convert PIL image to OpenCV format (BGR)
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        return frame
    
    def generate_video(
        self,
        scenes: List[str],
        output_path: str,
        duration_per_scene: int = 5,
        font_size: int = 48,
        font_color: Tuple[int, int, int] = (255, 255, 255),
        background_color: Tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        """
        Generate a complete video from multiple text scenes.
        
        Args:
            scenes: List of text strings for each scene
            output_path: Path where the output video will be saved
            duration_per_scene: Duration in seconds for each scene
            font_size: Font size for text
            font_color: RGB tuple for text color
            background_color: RGB tuple for background color
        """
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, self.fps, (self.width, self.height))
        
        frames_per_scene = self.fps * duration_per_scene
        
        for scene_text in scenes:
            # Create frame for this scene
            frame = self.create_text_frame(
                scene_text,
                font_size=font_size,
                font_color=font_color,
                background_color=background_color
            )
            
            # Write the same frame multiple times for the duration
            for _ in range(frames_per_scene):
                out.write(frame)
        
        # Release the video writer
        out.release()
        print(f"Video successfully created: {output_path}")
