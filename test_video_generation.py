"""
Simple test to verify the video generation functionality.
"""
import sys
import os
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from resource_parser import ResourceGuideParser
from video_generator import VideoGenerator


def test_resource_parser():
    """Test the resource parser functionality."""
    print("Testing ResourceGuideParser...")
    
    parser = ResourceGuideParser('data/inherited_property_guide.json')
    parser.load()
    
    title = parser.get_title()
    assert title == "Inherited Property Resource Guide", f"Expected title not found: {title}"
    print(f"✓ Title: {title}")
    
    sections = parser.get_sections()
    assert len(sections) == 5, f"Expected 5 sections, got {len(sections)}"
    print(f"✓ Sections: {len(sections)}")
    
    scenes = parser.get_scene_texts()
    assert len(scenes) == 6, f"Expected 6 scenes (title + 5 sections), got {len(scenes)}"
    print(f"✓ Scenes: {len(scenes)}")
    
    # Check first section
    first_section = sections[0]
    assert 'heading' in first_section, "Section missing 'heading' field"
    assert 'content' in first_section, "Section missing 'content' field"
    print(f"✓ First section heading: {first_section['heading']}")
    
    print("ResourceGuideParser tests passed!\n")


def test_video_generator():
    """Test the video generator functionality."""
    print("Testing VideoGenerator...")
    
    generator = VideoGenerator(width=640, height=480, fps=10)
    assert generator.width == 640, "Width not set correctly"
    assert generator.height == 480, "Height not set correctly"
    assert generator.fps == 10, "FPS not set correctly"
    print("✓ Generator initialized with correct parameters")
    
    # Test frame creation
    frame = generator.create_text_frame(
        "Test Frame",
        font_size=24,
        font_color=(255, 255, 255),
        background_color=(0, 0, 0)
    )
    assert frame.shape == (480, 640, 3), f"Frame shape incorrect: {frame.shape}"
    print("✓ Frame created with correct dimensions")
    
    print("VideoGenerator tests passed!\n")


def test_full_pipeline():
    """Test the complete pipeline with a small test video."""
    print("Testing full pipeline...")
    
    # Create test data
    test_data = {
        "title": "Test Video",
        "sections": [
            {"heading": "Section 1", "content": "Test content 1"},
            {"heading": "Section 2", "content": "Test content 2"}
        ]
    }
    
    # Write test file
    test_file = Path('data/test_guide.json')
    import json
    with open(test_file, 'w') as f:
        json.dump(test_data, f)
    
    # Parse and generate
    parser = ResourceGuideParser(str(test_file))
    scenes = parser.get_scene_texts()
    
    generator = VideoGenerator(width=320, height=240, fps=5)
    output_file = Path('output/test_video.mp4')
    
    generator.generate_video(
        scenes=scenes,
        output_path=str(output_file),
        duration_per_scene=1,
        font_size=16
    )
    
    assert output_file.exists(), "Test video was not created"
    assert output_file.stat().st_size > 0, "Test video is empty"
    print(f"✓ Test video created: {output_file.stat().st_size} bytes")
    
    # Clean up
    test_file.unlink()
    output_file.unlink()
    print("✓ Cleanup completed")
    
    print("Full pipeline tests passed!\n")


if __name__ == "__main__":
    print("=" * 60)
    print("Running Text-to-Video AI Tests")
    print("=" * 60)
    print()
    
    try:
        test_resource_parser()
        test_video_generator()
        test_full_pipeline()
        
        print("=" * 60)
        print("All tests passed successfully! ✓")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
