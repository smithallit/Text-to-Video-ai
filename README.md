# Text-to-Video AI

A Python application that creates videos from text content, specifically designed to generate educational videos from an inherited property resource guide.

## Features

- Parse structured JSON resource guides
- Generate video scenes from text content
- Customizable video settings (resolution, FPS, duration)
- Clean, centered text rendering on video frames

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script to generate a video from the inherited property resource guide:

```bash
python create_video.py
```

The script will:
1. Load the resource guide from `data/inherited_property_guide.json`
2. Parse the content into individual scenes
3. Generate a video with text overlays
4. Save the output to `output/inherited_property_guide.mp4`

## Configuration

Edit `config.json` to customize video settings:

```json
{
  "video": {
    "width": 1920,
    "height": 1080,
    "fps": 30,
    "duration_per_scene": 5,
    "output_format": "mp4"
  },
  "text": {
    "font_size": 48,
    "font_color": [255, 255, 255],
    "background_color": [0, 0, 0]
  }
}
```

## Resource Guide Format

The resource guide should be a JSON file with the following structure:

```json
{
  "title": "Guide Title",
  "sections": [
    {
      "heading": "Section Heading",
      "content": "Section content text..."
    }
  ]
}
```

## Project Structure

```
Text-to-Video-ai/
├── create_video.py          # Main script
├── config.json              # Configuration file
├── requirements.txt         # Python dependencies
├── data/                    # Resource guide data
│   └── inherited_property_guide.json
├── src/                     # Source modules
│   ├── resource_parser.py   # Resource guide parser
│   └── video_generator.py   # Video generation logic
└── output/                  # Generated videos
```

## Example

The included sample data (`data/inherited_property_guide.json`) contains information about inherited property, including:

- Understanding inherited property
- Key steps in the process
- Tax implications
- Property management options
- Getting professional help

Running `create_video.py` will create a video that displays each section as a separate scene with centered text on a black background.

## Requirements

- Python 3.7+
- Pillow (PIL)
- NumPy
- OpenCV (cv2)

## License

MIT