# Example: Creating Custom Resource Guides

This guide shows how to create your own resource guide for video generation.

## Basic Format

Create a JSON file in the `data/` directory with this structure:

```json
{
  "title": "Your Guide Title",
  "sections": [
    {
      "heading": "Section 1 Title",
      "content": "Detailed content for section 1..."
    },
    {
      "heading": "Section 2 Title",
      "content": "Detailed content for section 2..."
    }
  ]
}
```

## Example: Real Estate Investment Guide

```json
{
  "title": "Real Estate Investment Guide",
  "sections": [
    {
      "heading": "Getting Started",
      "content": "Real estate investment can be a powerful wealth-building strategy. Start by understanding your financial goals and risk tolerance."
    },
    {
      "heading": "Types of Properties",
      "content": "Consider residential, commercial, industrial, or mixed-use properties. Each has different risk profiles and return potentials."
    },
    {
      "heading": "Financing Options",
      "content": "Explore conventional mortgages, hard money loans, or partnership arrangements. Each has different terms and requirements."
    },
    {
      "heading": "Due Diligence",
      "content": "Always conduct thorough inspections, title searches, and market analysis before purchasing. Knowledge prevents costly mistakes."
    }
  ]
}
```

## Generating Your Video

1. Save your JSON file to `data/your_guide_name.json`
2. Update `config.json` to point to your file:
   ```json
   "resource_guide": {
     "input_file": "data/your_guide_name.json"
   }
   ```
3. Run: `python create_video.py`

## Tips for Good Content

1. **Keep sections focused**: Each section should cover one main topic
2. **Use clear headings**: Headings should be concise and descriptive
3. **Reasonable length**: Content should be readable in 5 seconds (configurable)
4. **Logical flow**: Order sections in a way that makes sense for learning

## Customizing Video Settings

Edit `config.json` to change:

- **Video resolution**: Adjust `width` and `height`
- **Frame rate**: Change `fps` (frames per second)
- **Scene duration**: Modify `duration_per_scene` (seconds)
- **Text appearance**: Update `font_size`, `font_color`, and `background_color`

Example configuration for shorter scenes with different colors:

```json
{
  "video": {
    "width": 1920,
    "height": 1080,
    "fps": 30,
    "duration_per_scene": 3,
    "output_format": "mp4"
  },
  "text": {
    "font_size": 56,
    "font_color": [255, 255, 0],
    "background_color": [0, 0, 128]
  }
}
```

This creates yellow text on a dark blue background with 3-second scenes.
