"""
Main script to create a video from the inherited property resource guide.
"""
import json
import os
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from resource_parser import ResourceGuideParser
from video_generator import VideoGenerator


def load_config(config_path: str = 'config.json') -> dict:
    """
    Load configuration from JSON file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Configuration dictionary
    """
    with open(config_path, 'r') as f:
        return json.load(f)


def main():
    """Main function to orchestrate video creation."""
    # Get the project root directory
    project_root = Path(__file__).parent
    
    # Load configuration
    config_path = project_root / 'config.json'
    config = load_config(str(config_path))
    
    # Extract configuration values
    video_config = config['video']
    text_config = config['text']
    resource_guide_path = project_root / config['resource_guide']['input_file']
    
    print("=" * 60)
    print("Text-to-Video AI: Inherited Property Resource Guide")
    print("=" * 60)
    print()
    
    # Parse the resource guide
    print(f"Loading resource guide from: {resource_guide_path}")
    parser = ResourceGuideParser(str(resource_guide_path))
    parser.load()
    
    title = parser.get_title()
    sections = parser.get_sections()
    print(f"Title: {title}")
    print(f"Number of sections: {len(sections)}")
    print()
    
    # Get scene texts
    scenes = parser.get_scene_texts()
    print(f"Generated {len(scenes)} scenes for the video")
    print()
    
    # Create output directory if it doesn't exist
    output_dir = project_root / 'output'
    output_dir.mkdir(exist_ok=True)
    
    # Generate video
    output_path = output_dir / f"inherited_property_guide.{video_config['output_format']}"
    print(f"Generating video: {output_path}")
    print(f"Video settings: {video_config['width']}x{video_config['height']} @ {video_config['fps']}fps")
    print(f"Duration per scene: {video_config['duration_per_scene']} seconds")
    print()
    
    generator = VideoGenerator(
        width=video_config['width'],
        height=video_config['height'],
        fps=video_config['fps']
    )
    
    generator.generate_video(
        scenes=scenes,
        output_path=str(output_path),
        duration_per_scene=video_config['duration_per_scene'],
        font_size=text_config['font_size'],
        font_color=tuple(text_config['font_color']),
        background_color=tuple(text_config['background_color'])
    )
    
    print()
    print("=" * 60)
    print("Video generation complete!")
    print(f"Output saved to: {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
