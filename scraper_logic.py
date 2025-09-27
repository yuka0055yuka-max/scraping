# scraper_logic.py
import os, json, re, urllib.robotparser
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from getpass import getpass
from dotenv import load_dotenv

load_dotenv()
SCRAPE_PASSWORD = os.getenv("SCRAPE_PASSWORD")

def is_scraping_allowed(url, ua="*"):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url.rstrip("/") + "/robots.txt")
    try:
        rp.read()
        return rp.can_fetch(ua, url)
    except:
        return False

def expand_keywords(keywords):
    syn = { "AI":["AI","人工知能","機械学習"],
            "Python":["Python","パイソン","py"],
            "ニュース":["ニュース","速報","報道"] }
    expanded = []
    for kw in keywords:
        expanded += syn.get(kw, [kw])
    return list(set(expanded))

def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    parts = list(soup.stripped_strings)
    for tag in soup.find_all("script"):
        if tag.string: parts.append(tag.string.strip())
    for meta in soup.find_all("meta"):
        c = meta.get("content")
        if c: parts.append(c.strip())
    if soup.title and soup.title.string:
        parts.append(soup.title.string.strip())
    return "\n".join(parts)

def filter_text(text, keywords):
    kx = expand_keywords(keywords)
    hits = []
    for line in text.splitlines():
        s = line.strip()
        if len(s) < 5: continue
        for kw in kx:
            if re.search(re.escape(kw), s, re.IGNORECASE):
                hits.append(s)
                break
    return hits

def scrape_url(url):
    with sync_playwright() as p:
        br = p.chromium.launch(headless=True)
        pg = br.new_page()
        pg.goto(url, timeout=60000)
        html = pg.content()
        br.close()
    return html

def perform_scrape(url, keywords, password=None):
    allowed = is_scraping_allowed(url)
    if not allowed:
        if password != SCRAPE_PASSWORD:
            return { "error":"robots.txt 禁止。パスワード認証失敗" }
    html = scrape_url(url)
    text = extract_text(html)
    hits = filter_text(text, keywords)
    return { "allowed":allowed, "hits":hits, "count":len(hits) }
