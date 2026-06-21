import os
import re
import time
import feedparser
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Constants
FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"
CACHE_FILE = "release_notes_cache.json"
CACHE_DURATION_SECS = 3600  # 1 hour cache duration

# Cache structure in memory
_cache = {
    "data": None,
    "last_updated": 0
}

def clean_html_content(html_str):
    """
    Cleans up HTML string from feed content to make it safer and look better.
    Forces all anchors to open in a new tab.
    """
    if not html_str:
        return ""
    
    soup = BeautifulSoup(html_str, 'html.parser')
    
    # Process links to open in a new tab
    for a in soup.find_all('a'):
        a['target'] = '_blank'
        a['rel'] = 'noopener noreferrer'
        # Add modern CSS class to feed links if needed
        a['class'] = a.get('class', []) + ['feed-link']

    return str(soup)

def parse_feed_source():
    """
    Fetches the XML feed from Google Cloud, parses it using feedparser, 
    and breaks down entries by category headings.
    """
    try:
        feed = feedparser.parse(FEED_URL)
        
        # Check if feedparser encountered parsing errors or fetched empty data
        if not feed.entries and feed.bozo:
            print(f"Feedparser warning/error (bozo): {feed.bozo_exception}")
            
        parsed_items = []
        
        for entry in feed.entries:
            date_str = entry.get('title', 'Unknown Date')
            base_link = entry.get('link', '')
            summary_html = entry.get('summary', '')
            
            # Google release notes often split entries by <h3> headings (e.g., Feature, Announcement, Fix)
            soup = BeautifulSoup(summary_html, 'html.parser')
            h3_elements = soup.find_all('h3')
            
            # If no <h3> categories found, treat the whole entry as one item
            if not h3_elements:
                item_id = entry.get('id', base_link)
                clean_content = clean_html_content(summary_html)
                parsed_items.append({
                    "id": item_id,
                    "date": date_str,
                    "category": "Update",
                    "content": clean_content,
                    "link": base_link
                })
                continue
            
            # Split elements by <h3> headings
            for index, h3 in enumerate(h3_elements):
                category = h3.get_text(strip=True)
                content_parts = []
                
                # Iterate siblings until the next h3
                next_sibling = h3.next_sibling
                while next_sibling and next_sibling.name != 'h3':
                    if next_sibling.name:
                        content_parts.append(str(next_sibling))
                    else:
                        text = str(next_sibling).strip()
                        if text:
                            content_parts.append(text)
                    next_sibling = next_sibling.next_sibling
                
                raw_content = "".join(content_parts).strip()
                clean_content = clean_html_content(raw_content)
                
                # Unique ID per entry update
                entry_id = entry.get('id', base_link)
                item_id = f"{entry_id}#{index}"
                
                parsed_items.append({
                    "id": item_id,
                    "date": date_str,
                    "category": category,
                    "content": clean_content,
                    "link": base_link
                })
                
        return parsed_items, None
    except Exception as e:
        print(f"Error parsing feed: {str(e)}")
        return None, str(e)

def get_release_notes(force_refresh=False):
    """
    Returns release notes from cache or fetches from feed source.
    """
    global _cache
    current_time = time.time()
    
    # Return cache if still valid and force_refresh is False
    if not force_refresh and _cache["data"] is not None and (current_time - _cache["last_updated"] < CACHE_DURATION_SECS):
        return _cache["data"], None
        
    # Attempt to fetch new data
    data, error = parse_feed_source()
    if data is not None:
        _cache["data"] = data
        _cache["last_updated"] = current_time
        return data, None
        
    # If fetch failed but we have stale cache, return stale cache with warning
    if _cache["data"] is not None:
        return _cache["data"], f"Failed to refresh feed ({error}). Serving cached data."
        
    return None, f"Failed to load release notes: {error}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/releases')
def get_releases():
    force_refresh = request.args.get('refresh', 'false').lower() == 'true'
    data, error = get_release_notes(force_refresh)
    
    if data is None:
        return jsonify({"success": False, "error": error}), 500
        
    return jsonify({
        "success": True,
        "releases": data,
        "last_updated": _cache["last_updated"],
        "warning": error
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
