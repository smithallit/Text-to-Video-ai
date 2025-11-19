"""
Resource Guide Parser Module
Parses the inherited property resource guide JSON file and extracts content.
"""
import json
from typing import Dict, List


class ResourceGuideParser:
    """Parser for inherited property resource guide content."""
    
    def __init__(self, file_path: str):
        """
        Initialize the parser with the resource guide file path.
        
        Args:
            file_path: Path to the resource guide JSON file
        """
        self.file_path = file_path
        self.data = None
    
    def load(self) -> Dict:
        """
        Load and parse the resource guide file.
        
        Returns:
            Dictionary containing the parsed resource guide data
        """
        with open(self.file_path, 'r') as f:
            self.data = json.load(f)
        return self.data
    
    def get_title(self) -> str:
        """
        Get the title of the resource guide.
        
        Returns:
            Title string
        """
        if not self.data:
            self.load()
        return self.data.get('title', '')
    
    def get_sections(self) -> List[Dict]:
        """
        Get all sections from the resource guide.
        
        Returns:
            List of section dictionaries with 'heading' and 'content'
        """
        if not self.data:
            self.load()
        return self.data.get('sections', [])
    
    def get_scene_texts(self) -> List[str]:
        """
        Generate text content for each video scene.
        
        Returns:
            List of text strings for each scene
        """
        scenes = []
        title = self.get_title()
        if title:
            scenes.append(title)
        
        for section in self.get_sections():
            heading = section.get('heading', '')
            content = section.get('content', '')
            scene_text = f"{heading}\n\n{content}"
            scenes.append(scene_text)
        
        return scenes
