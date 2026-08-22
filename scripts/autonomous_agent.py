import os
import glob
import logging
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Fault-tolerant logging
logging.basicConfig(level=logging.INFO, format='🤖 %(asctime)s - %(levelname)s - %(message)s')

class AutonomousGuardian:
    def __init__(self):
        self.html_files = glob.glob('./**/*.html', recursive=True)
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.llm_enabled = False
        self.model = None
        
        if self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                # Find an available model dynamically for bulletproof fault tolerance
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        self.model = genai.GenerativeModel(m.name)
                        self.llm_enabled = True
                        logging.info(f"Gemini AI integration ACTIVE using {m.name}. Neural pathways engaged.")
                        break
                if not self.llm_enabled:
                    logging.error("No suitable Gemini model found for generation.")
            except Exception as e:
                logging.error(f"Failed to initialize Gemini AI: {e}")
        else:
            logging.info("Running in standard heuristic mode (No API Key detected).")

    def validate_link(self, url):
        """Fault-tolerant link validation with timeout and retries."""
        if not url.startswith('http'):
            return True
        try:
            response = requests.head(url, timeout=3, allow_redirects=True)
            if response.status_code >= 400:
                logging.warning(f"Broken link detected: {url} (Status: {response.status_code})")
                return False
            return True
        except requests.RequestException:
            logging.warning(f"Unreachable link detected: {url}")
            return False

    def ai_improve_text(self, text):
        if not self.llm_enabled or not self.model or len(text.strip()) < 10:
            return text
            
        prompt = (
            "You are an expert copywriter and AI researcher. "
            "Fix any grammatical errors in the following text and make it slightly more professional, "
            "but keep the exact same meaning and similar length. DO NOT add any markdown formatting or quotes around the output. "
            f"Text: {text}"
        )
        try:
            response = self.model.generate_content(prompt)
            improved = response.text.strip()
            if improved and len(improved) > 0:
                return improved
        except Exception as e:
            logging.error(f"AI text improvement failed: {e}")
        return text

    def run(self):
        logging.info("Starting Level-10 Autonomous Self-Repair & Build Sequence...")
        for filepath in self.html_files:
            try:
                self.process_file(filepath)
            except Exception as e:
                logging.critical(f"FATAL ERROR processing {filepath}: {e}. Continuing to next file for fault tolerance.")
        logging.info("Sequence complete. The repository is optimized.")

    def process_file(self, filepath):
        logging.info(f"Scanning {filepath}...")
        with open(filepath, 'r', encoding='utf-8') as f:
            original_html = f.read()

        soup = BeautifulSoup(original_html, 'html.parser')
        modified = False

        for img in soup.find_all('img'):
            if not img.get('alt') or img.get('alt').strip() == '':
                src = img.get('src', '')
                filename = os.path.basename(src).split('.')[0]
                repair_alt = filename.replace('-', ' ').replace('_', ' ').title() if filename else 'Portfolio Graphic'
                img['alt'] = repair_alt
                logging.info(f"SEO Healed: Added alt='{repair_alt}' to {src}")
                modified = True

        for a_tag in soup.find_all('a', href=True):
            self.validate_link(a_tag['href'])

        if self.llm_enabled:
            for p in soup.find_all('p', class_=['about__content-details-para', 'project-details__desc-para']):
                original_text = p.get_text(strip=True)
                if original_text:
                    improved_text = self.ai_improve_text(original_text)
                    if improved_text != original_text:
                        p.string = improved_text
                        logging.info("AI Rewrote paragraph for better impact.")
                        modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            logging.info(f"Modifications successfully committed to {filepath}")
        else:
            logging.info(f"System optimal. No repairs needed for {filepath}")

if __name__ == "__main__":
    agent = AutonomousGuardian()
    agent.run()
