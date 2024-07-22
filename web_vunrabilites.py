import requests
from bs4 import BeautifulSoup

# Vulnerability scanner class
class VulnerabilityScanner:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def check_sql_injection(self):
        # List of common SQL injection payloads
        payloads = ["'", '"', "1=1", "' OR '1'='1", '" OR "1"="1']
        vulnerable = False

        for payload in payloads:
            # Test URL with payload
            test_url = self.url + payload
            response = self.session.get(test_url)

            # Check if SQL error message is in response (simple check)
            if "sql" in response.text.lower() or "syntax" in response.text.lower():
                print(f"Possible SQL Injection vulnerability detected with payload: {payload}")
                vulnerable = True

        if not vulnerable:
            print("No SQL Injection vulnerabilities detected.")

    def check_xss(self):
        # List of common XSS payloads
        payloads = ['<script>alert(1)</script>', '" onmouseover="alert(1)"']
        vulnerable = False

        for payload in payloads:
            # Test URL with payload
            test_url = self.url + payload
            response = self.session.get(test_url)

            # Check if payload is in the response
            if payload in response.text:
                print(f"Possible XSS vulnerability detected with payload: {payload}")
                vulnerable = True

        if not vulnerable:
            print("No XSS vulnerabilities detected.")

    def check_security_headers(self):
        response = self.session.get(self.url)
        headers = response.headers

        # List of important security headers
        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]

        for header in security_headers:
            if header not in headers:
                print(f"Missing security header: {header}")

        print("Security headers check complete.")

    def check_directory_traversal(self):
        # List of common directory traversal payloads
        payloads = ["../", "..%2F", "..%c0%af", "..%5c"]
        vulnerable = False

        for payload in payloads:
            # Test URL with payload
            test_url = self.url + payload
            response = self.session.get(test_url)

            # Check if directory traversal is successful
            if response.status_code == 200 and "root" in response.text.lower():
                print(f"Possible Directory Traversal vulnerability detected with payload: {payload}")
                vulnerable = True

        if not vulnerable:
            print("No Directory Traversal vulnerabilities detected.")

    def run_scanner(self):
        print(f"Scanning {self.url} for vulnerabilities...")
        self.check_sql_injection()
        self.check_xss()
        self.check_security_headers()
        self.check_directory_traversal()
        print("Scanning complete.")

# Example usage
if __name__ == "__main__":
    target_url = "http://hkrb.hackxor.net/login"
    scanner = VulnerabilityScanner(target_url)
    scanner.run_scanner()
