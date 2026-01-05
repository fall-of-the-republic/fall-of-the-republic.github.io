#!/usr/bin/env python3
"""Align obverse and reverse coin images side-by-side"""

import argparse
from PIL import Image
import os
import sys


def align_images(obverse_path, reverse_path, output_path, spacing=0, bg_color=(0, 0, 0)):
    """
    Align two images side-by-side with specified spacing and background color.
    
    Args:
        obverse_path: Path to obverse (front) image
        reverse_path: Path to reverse (back) image
        output_path: Path to save aligned image
        spacing: Pixels between images (default: 0)
        bg_color: Background color as RGB tuple (default: black)
    """
    # Load images
    obverse = Image.open(obverse_path)
    reverse = Image.open(reverse_path)
    
    print(f"Loaded obverse: {obverse.size}")
    print(f"Loaded reverse: {reverse.size}")
    
    # Convert to RGBA if needed
    if obverse.mode != 'RGBA':
        obverse = obverse.convert('RGBA')
    if reverse.mode != 'RGBA':
        reverse = reverse.convert('RGBA')
    
    # Resize to same height
    target_height = min(obverse.height, reverse.height)
    obverse_ratio = target_height / obverse.height
    reverse_ratio = target_height / reverse.height
    
    obverse_new_size = (int(obverse.width * obverse_ratio), target_height)
    reverse_new_size = (int(reverse.width * reverse_ratio), target_height)
    
    obverse_resized = obverse.resize(obverse_new_size, Image.Resampling.LANCZOS)
    reverse_resized = reverse.resize(reverse_new_size, Image.Resampling.LANCZOS)
    
    print(f"Resized obverse: {obverse_resized.size}")
    print(f"Resized reverse: {reverse_resized.size}")
    
    # Create combined image with background color
    combined_width = obverse_resized.width + reverse_resized.width + spacing
    combined_height = target_height
    
    combined = Image.new('RGB', (combined_width, combined_height), bg_color)
    
    # Paste images
    combined.paste(obverse_resized, (0, 0), obverse_resized if obverse_resized.mode == 'RGBA' else None)
    combined.paste(reverse_resized, (obverse_resized.width + spacing, 0), reverse_resized if reverse_resized.mode == 'RGBA' else None)
    
    # Save
    combined.save(output_path, 'PNG')
    print(f"\nAligned image saved to: {output_path}")
    print(f"Dimensions: {combined_width}x{combined_height}")


def main():
    parser = argparse.ArgumentParser(
        description='Align obverse and reverse coin images side-by-side',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s obverse.png reverse.png output.png
  %(prog)s obverse.png reverse.png output.png --spacing 20
  %(prog)s obverse.png reverse.png output.png --bg-color white
        """
    )
    
    parser.add_argument('obverse', help='Path to obverse (front) image')
    parser.add_argument('reverse', help='Path to reverse (back) image')
    parser.add_argument('output', help='Path to save aligned image')
    parser.add_argument('--spacing', type=int, default=0,
                       help='Spacing between images in pixels (default: 0)')
    parser.add_argument('--bg-color', default='black',
                       choices=['black', 'white', 'gray'],
                       help='Background color (default: black)')
    
    args = parser.parse_args()
    
    # Validate input files exist
    if not os.path.exists(args.obverse):
        print(f"Error: Obverse image not found: {args.obverse}", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.exists(args.reverse):
        print(f"Error: Reverse image not found: {args.reverse}", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory if needed
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Map color names to RGB
    bg_colors = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'gray': (128, 128, 128)
    }
    bg_color = bg_colors[args.bg_color]
    
    # Align the images
    align_images(args.obverse, args.reverse, args.output, args.spacing, bg_color)


if __name__ == '__main__':
    main()
