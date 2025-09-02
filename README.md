# Swim Lessons Website

## Project Overview
**RBC Private Swim Lessons** is a simple, clean, and SEO-optimized website promoting swim instruction services in Ranch at Brushy Creek and Cedar Park, TX. Built with static files and integrated with Square for seamless booking functionality.

## Live Demo
Explore the live site: [RBC Private Swim Lessons](https://sydneyleeatx.github.io/swim_lesson_website/)

Features:
- Service options and pricing
- About section with instructor bio
- Booking link via Square
- Contact information and FAQs

## Purpose & Goals
- Showcase swim lesson offerings clearly to the local community  
- Enhance search engine visibility with SEO optimizations  
- Enable easy lesson registration through Square booking integration  

## Tech Stack & Files
- **HTML**
  - `index.html` — main page structure and content  
  - `google948f9ea7735054ef.html` — Google site verification  
- **CSS**
  - `styles.css` — website styling  
- **Media assets**
  - Photos such as `swim_portrait.jpg` and `coaching_backfloat.jpg`  
- **SEO & indexing tools**
  - `robots.txt` — tells search engines what to crawl  
  - `sitemap.xml` — maps the site's structure for better indexing  
- **Image optimization utilities**
  - `optimize_images.bat`  
  - `optimize_images.py`  
- **Other**
  - `.gitignore` — exclude local/unnecessary files from version control  

## Features & Highlights
- **Booking Integration**: Direct link to Square booking platform for seamless lesson registration  
- **SEO-Focused**: Includes site metadata, sitemap, and robots instructions to improve visibility  
- **Responsive Visuals**: Relevant images enhance engagement  
- **Instructor Bio**: Personal touch with “About Me” section to build trust and connection  

## Getting Started
Although this is a static site, here’s how to modify or extend it:

```bash
# Clone the repository
git clone https://github.com/sydneyleeATX/swim_lesson_website.git

# Review/edit content
index.html   # Update text/content
styles.css   # Adjust styles

# Optimize images before committing
python optimize_images.py

# Push changes
git push origin main
# GitHub Pages will automatically redeploy
