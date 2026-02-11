"""
Manager 1: Ingestion Engine.
Captures DOM render via Playwright to bypass API limits.
Strictly extracts text, discarding binary objects.
"""
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

class IngestionManager:
    def __init__(self, whitelist: list):
        # Whitelist logic for authoritative sources
        self.whitelist = whitelist

    async def fetch_rendered_text(self, url: str) -> str:
        """Captures full browser render and strips multimedia tags."""
        if not any(domain in url for domain in self.whitelist):
            raise ValueError("Source not in authoritative whitelist.")

        async with async_playwright() as p:
            # Headless mode to save RAM
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle")
            
            # Capture full DOM render
            html_content = await page.content()
            await browser.close()
            
            return self._clean_html(html_content)

    def _clean_html(self, html: str) -> str:
        """Removes img, video, and audio tags."""
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup(["script", "style", "img", "video", "audio", "source"]):
            tag.decompose()
        
        # Extract text and normalize spacing
        text = soup.get_text(separator=' ')
        return " ".join(text.split())

# Example usage for USA-Iran Geopolitics focus
if __name__ == "__main__":
    manager = IngestionManager(whitelist=["reuters.com", "apnews.com"])
    # loop = asyncio.get_event_loop()
    # text = loop.run_until_complete(manager.fetch_rendered_text("https://example.com"))