import requests
from bs4 import BeautifulSoup

def scan_sql_injection(url):
    payload = "' OR '1'='1"
    try:
        response = requests.get(url + payload)
        if "sql" in response.text.lower() or "syntax" in response.text.lower():
            return True
    except:
        pass
    return False

def scan_xss(url):
    xss_payload = "<script>alert(1)</script>"
    try:
        response = requests.get(url + xss_payload)
        if xss_payload in response.text:
            return True
    except:
        pass
    return False

def run_scan(target_url):
    results = {
        "sql_injection": scan_sql_injection(target_url),
        "xss": scan_xss(target_url),
    }
    return results

