"""
Market News Monitoring Tool for US Regional Banking Sector
Scans for negative news and generates daily reports
"""

import requests
import json
from datetime import datetime, timedelta, timezone
from urllib.parse import quote
import os
from pathlib import Path

class BankingNewsMonitor:
    """Monitor and collect negative news on US regional banks"""
    
    def __init__(self):
        self.output_dir = r"[Your Work Folder]\MarketMonitor\output"
        self.ensure_output_dir()
        
        # Regional bank tickers and names to monitor
        self.regional_banks = {
            'JPM': 'JPMorgan Chase',
            'BAC': 'Bank of America',
            'WFC': 'Wells Fargo',
            'GS': 'Goldman Sachs',
            'MS': 'Morgan Stanley',
            'BLK': 'BlackRock',
            'SCHW': 'Charles Schwab',
            'TFC': 'Truist Financial',
            'PNC': 'PNC Financial',
            'USB': 'U.S. Bancorp',
            'FITB': 'Fifth Third Bancorp',
            'RF': 'Regions Financial',
            'KEY': 'KeyCorp',
            'MTB': 'M&T Bank',
            'ZION': 'Zions Bancorporation',
            'CFG': 'Citizens Financial Group',
            'STL': 'Sterling Bancorp',
            'FRC': 'First Republic Bank',
            'SBNY': 'Signature Bank',
            'UVSP': 'UVB (UV Bank)',
        }
        
        # Negative keywords to identify adverse news
        self.negative_keywords = [
            'downgrade', 'downgraded', 'negative outlook',
            'earnings miss', 'earnings shortfall', 'guidance cut',
            'cybersecurity breach', 'data breach', 'hacked',
            'credit spread', 'widening spreads',
            'financial loss', 'loss', 'impairment',
            'liquidity stress', 'liquidity crisis',
            'deposit outflow', 'deposit flight',
            'regulatory enforcement', 'consent order', 'settlement',
            'capital ratio decline', 'capital deficiency',
            'non-performing loan', 'NPL', 'charge-off',
            'commercial real estate exposure', 'office loan',
            'funding cost', 'net interest margin decline',
            'failed capital raise', 'bond issuance cancelled',
            'management turnover', 'ceo resignation',
            'operational disruption', 'technology outage',
            'emergency funding', 'fed lending',
            'equity decline', 'share price drop',
            'short interest', 'bankruptcy', 'restructuring',
            'stress test failure', 'asset quality', 'loan loss',
            'covenant breach', 'default', 'fail',
            'investigation', 'lawsuit', 'litigation',
            'scandal', 'fraud', 'misconduct',
            'weakness', 'weakness in', 'troubled',
            'crisis', 'emergency', 'critical',
            'fined', 'penalty', 'violated'
        ]
        
        # Try multiple news sources
        self.news_sources = [
            self._fetch_from_newsapi,
            self._fetch_from_bing,
            self._fetch_from_google_news
        ]
    
    def ensure_output_dir(self):
        """Ensure output directory exists"""
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def _fetch_from_newsapi(self):
        """Fetch news from NewsAPI (requires API key)"""
        try:
            # Using NewsAPI free tier - you may need to register for an API key at https://newsapi.org
            api_key = os.environ.get('NEWS_API_KEY', '')
            if not api_key:
                return []
            
            articles = []
            search_terms = [
                'US regional banks negative',
                'US banking crisis',
                'bank earnings miss',
                'bank regulatory action',
                'bank cybersecurity breach',
                'regional bank stress',
            ]
            
            for term in search_terms:
                url = f"https://newsapi.org/v2/everything?q={quote(term)}&sortBy=publishedAt&language=en&pageSize=100"
                headers = {'Authorization': api_key}
                
                try:
                    response = requests.get(url, headers=headers, timeout=10)
                    if response.status_code == 200:
                        data = response.json()
                        articles.extend(data.get('articles', []))
                except requests.exceptions.RequestException:
                    pass
            
            return articles
        except Exception as e:
            print(f"Error fetching from NewsAPI: {e}")
            return []
    
    def _fetch_from_bing(self):
        """Fetch news from Bing News Search"""
        try:
            articles = []
            search_queries = [
                'US regional banks negative news',
                'bank earnings miss 2026',
                'US banking sector crisis',
                'regional bank failures',
                'bank regulatory enforcement',
                'banking cybersecurity',
            ]
            
            for query in search_queries:
                url = "https://www.bing.com/news/search"
                params = {
                    'q': query,
                    'format': 'rss'
                }
                
                try:
                    response = requests.get(url, params=params, timeout=10)
                    if response.status_code == 200:
                        # Parse RSS feed
                        import xml.etree.ElementTree as ET
                        root = ET.fromstring(response.content)
                        
                        for item in root.findall('.//item'):
                            title = item.find('title')
                            description = item.find('description')
                            link = item.find('link')
                            pubDate = item.find('pubDate')
                            
                            if title is not None:
                                articles.append({
                                    'title': title.text or '',
                                    'description': description.text if description is not None else '',
                                    'url': link.text if link is not None else '',
                                    'publishedAt': pubDate.text if pubDate is not None else datetime.now().isoformat(),
                                    'source': {'name': 'Bing News'}
                                })
                except Exception:
                    pass
            
            return articles
        except Exception as e:
            print(f"Error fetching from Bing: {e}")
            return []
    
    def _fetch_from_google_news(self):
        """Fetch news using Google News RSS feeds"""
        try:
            articles = []
            search_queries = [
                'regional+banks+negative',
                'US+bank+earnings',
                'bank+crisis',
                'banking+regulation',
            ]
            
            for query in search_queries:
                url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
                
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        import xml.etree.ElementTree as ET
                        root = ET.fromstring(response.content)
                        
                        for item in root.findall('.//item'):
                            title = item.find('title')
                            description = item.find('description')
                            link = item.find('link')
                            pubDate = item.find('pubDate')
                            
                            if title is not None:
                                articles.append({
                                    'title': title.text or '',
                                    'description': description.text if description is not None else '',
                                    'url': link.text if link is not None else '',
                                    'publishedAt': pubDate.text if pubDate is not None else datetime.now().isoformat(),
                                    'source': {'name': 'Google News'}
                                })
                except Exception:
                    pass
            
            return articles
        except Exception as e:
            print(f"Error fetching from Google News: {e}")
            return []
    
    def fetch_news(self):
        """Fetch news from all available sources"""
        all_articles = []
        
        for fetch_function in self.news_sources:
            articles = fetch_function()
            all_articles.extend(articles)
        
        # Remove duplicates based on title
        seen = set()
        unique_articles = []
        for article in all_articles:
            title = article.get('title', '').lower()
            if title and title not in seen:
                seen.add(title)
                unique_articles.append(article)
        
        return unique_articles
    
    def is_negative_news(self, article):
        """Check if article contains negative banking news"""
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()
        full_text = f"{title} {description}".lower()
        
        # Check for banking sector relevance
        banking_keywords = ['bank', 'banking', 'financial', 'credit', 'lending', 'deposit']
        has_banking_context = any(keyword in full_text for keyword in banking_keywords)
        
        # Check for US regional bank mentions
        us_banks_mentioned = any(
            bank_name.lower() in full_text or ticker.lower() in full_text 
            for ticker, bank_name in self.regional_banks.items()
        )
        
        # Check for negative keywords
        has_negative = any(
            keyword in full_text for keyword in self.negative_keywords
        )
        
        # Must be about banking and contain negative indicators
        return has_banking_context and has_negative
    
    def filter_by_date(self, articles):
        """Filter articles from the last 24 hours - STRICT filtering"""
        cutoff_time = datetime.now(timezone.utc) - timedelta(days=1)
        filtered = []
        
        for article in articles:
            try:
                # Parse various date formats
                pub_date_str = article.get('publishedAt', '')
                if not pub_date_str:
                    continue
                
                # Try ISO format first
                if 'T' in pub_date_str:
                    pub_date = datetime.fromisoformat(pub_date_str.replace('Z', '+00:00'))
                else:
                    # Try RFC 2822 format (from email.utils)
                    from email.utils import parsedate_to_datetime
                    pub_date = parsedate_to_datetime(pub_date_str)
                
                # Make sure we're comparing timezone-aware datetimes
                if pub_date.tzinfo is None:
                    pub_date = pub_date.replace(tzinfo=timezone.utc)
                
                # Only include articles from the last 24 hours
                if pub_date >= cutoff_time:
                    filtered.append(article)
            except (ValueError, TypeError, AttributeError):
                # Skip articles with unparseable dates - strict filtering
                continue
        
        return filtered
    
    def generate_report(self, articles):
        """Generate a formatted report of negative news"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = []
        report.append("=" * 80)
        report.append("MARKET NEWS MONITORING - US REGIONAL BANKING SECTOR")
        report.append("=" * 80)
        report.append(f"Report Generated: {timestamp}")
        report.append(f"Total Negative News Articles Found: {len(articles)}")
        report.append("=" * 80)
        report.append("")
        
        if not articles:
            report.append("No significant negative news found in the monitoring period.")
            report.append("")
        else:
            for idx, article in enumerate(articles, 1):
                report.append(f"[{idx}] {article.get('title', 'Untitled')}")
                report.append("-" * 80)
                report.append(f"Source: {article.get('source', {}).get('name', 'Unknown')}")
                report.append(f"Published: {article.get('publishedAt', 'Unknown')}")
                report.append(f"URL: {article.get('url', 'No URL provided')}")
                report.append("")
                report.append("Summary:")
                report.append(article.get('description', 'No summary available'))
                report.append("")
                report.append("")
        
        report.append("=" * 80)
        report.append("End of Report")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def save_report(self, report):
        """Save report to output file"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        time_str = datetime.now().strftime("%H-%M-%S")
        filename = f"banking_news_{date_str}_{time_str}.txt"
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Report saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"Error saving report: {e}")
            return None
    
    def run(self):
        """Execute the monitoring process"""
        print("Starting market news monitoring...")
        print("Fetching news articles...")
        
        articles = self.fetch_news()
        print(f"Total articles fetched: {len(articles)}")
        
        # Filter by date
        recent_articles = self.filter_by_date(articles)
        print(f"Recent articles (last 24h): {len(recent_articles)}")
        
        # Filter by negative sentiment
        negative_articles = [a for a in recent_articles if self.is_negative_news(a)]
        print(f"Negative banking articles: {len(negative_articles)}")
        
        # Sort by date (newest first)
        negative_articles.sort(
            key=lambda x: x.get('publishedAt', ''),
            reverse=True
        )
        
        # Generate and save report
        report = self.generate_report(negative_articles)
        filepath = self.save_report(report)
        
        print("Monitoring complete!")
        return filepath


def main():
    """Main entry point"""
    monitor = BankingNewsMonitor()
    monitor.run()


if __name__ == "__main__":
    main()
