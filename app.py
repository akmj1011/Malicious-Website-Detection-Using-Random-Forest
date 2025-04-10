import re
import tldextract
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

app = Flask(__name__)

# Expanded list of suspicious keywords for better detection
suspicious_keywords = [
    'login', 'secure', 'account', 'update', 'banking', 
    'verification', 'pay', 'confirm', 'purchase', 'invoice',
    'mod', 'apk', 'free', 'download', 'torrent', 'click', 'offer', 'promo', 'win', 'prize',
    'paypal', 'giftcard', 'password', 'hacked', 'reward'
]

# Additional heuristic checks: Length of URL, presence of HTTPS, query parameters, and file extensions
def url_length(url):
    return len(url)

def is_https(url):
    return 1 if url.startswith("https") else 0

def has_suspicious_extension(url):
    suspicious_extensions = ['.exe', '.apk', '.zip', '.torrent', '.rar', '.cc']
    return any(url.endswith(ext) for ext in suspicious_extensions)

def has_suspicious_parameters(url):
    """Check if the URL contains suspicious query parameters."""
    suspicious_params = ['token', 'id=', 'session', 'key=', 'ref=']
    return any(param in url for param in suspicious_params)

# Expanded dataset (safe and malicious URLs)
safe_urls = [
    "https://www.google.com", "https://www.amazon.com", "https://www.microsoft.com", 
    "https://www.reddit.com", "https://www.facebook.com", "https://www.github.com", 
    "https://www.apple.com", "https://www.youtube.com", "https://www.twitter.com", 
    "https://www.linkedin.com", "https://www.instagram.com", "https://www.netflix.com", 
    "https://www.github.com", "https://www.wikipedia.org", "https://www.stackoverflow.com"
]

malicious_urls = [
    "http://192.168.1.1/login", "http://phishing-example.com/account-update", 
    "http://malicious-example.com/login", "http://banking-phishing.com/verify", 
    "http://modapk-download.com/free", "http://betflixapk.net/en/", "http://happymod.com/",
    "http://phishing-attacks.com/fake-login", "http://get-rich-fast.com/win-prize-now", 
    "http://fakebanking-login.com/secure-login", "http://scam-offer.com/claim-your-prize", 
    "http://dangerous-site.com/install-malware", "http://download-virus.com/fake-update", 
    "http://phishing-example.com/login?session=1234", "http://fake-payment.com/offer?token=abcd1234"
]

# Prepare URLs and labels
urls = safe_urls + malicious_urls
labels = [0] * len(safe_urls) + [1] * len(malicious_urls)  # 0 = safe, 1 = malicious

# Vectorize URLs (use bigger n-grams to capture more context)
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 6))
X = vectorizer.fit_transform(urls)

# Add new features: URL length, HTTPS presence, suspicious file extensions, and parameters
lengths = [url_length(url) for url in urls]
https_flags = [is_https(url) for url in urls]
extensions = [has_suspicious_extension(url) for url in urls]
params = [has_suspicious_parameters(url) for url in urls]
X = np.hstack((X.toarray(), np.array(lengths).reshape(-1, 1), 
               np.array(https_flags).reshape(-1, 1), 
               np.array(extensions).reshape(-1, 1), 
               np.array(params).reshape(-1, 1)))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Train a RandomForest model (with more estimators and a max depth)
model = RandomForestClassifier(n_estimators=500, max_depth=25, random_state=42)
model.fit(X_train, y_train)

# Functions for URL detection
def contains_ip_address(url):
    """Check if the URL contains an IP address."""
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    return bool(ip_pattern.search(url))

def contains_suspicious_keyword(url):
    """Check if the URL contains suspicious keywords.""" 
    return any(keyword in url for keyword in suspicious_keywords)

def check_domain_reputation(url):
    """Placeholder for domain reputation check."""
    domain = tldextract.extract(url).registered_domain
    # Example: using a predefined list or third-party service
    bad_domains = ["phishing-example.com", "malicious-site.net", "banking-phishing.com"]
    return domain in bad_domains

def predict_malicious(url):
    """Predict if the URL is malicious using a trained ML model."""
    url_vector = vectorizer.transform([url])
    length = url_length(url)
    https = is_https(url)
    extension = has_suspicious_extension(url)
    param = has_suspicious_parameters(url)
    feature_vector = np.hstack((url_vector.toarray(), np.array([[length, https, extension, param]])))
    return model.predict(feature_vector)[0]

def calculate_trust_score(url):
    """Calculate a trust score for the URL based on various checks."""
    score = 100  # Start with a high trust score

    # Deduct points for IP address presence
    if contains_ip_address(url):
        score -= 40

    # Deduct points for suspicious keywords
    if contains_suspicious_keyword(url):
        score -= 30

    # Deduct points for poor domain reputation
    if check_domain_reputation(url):
        score -= 20

    # Deduct points for machine learning model prediction of malicious
    if predict_malicious(url) == 1:
        score -= 50

    # Add a bonus for HTTPS (more secure URLs)
    if is_https(url):
        score += 10

    # Deduct points for suspicious extensions (e.g., `.exe`, `.apk`, `.cc`)
    if has_suspicious_extension(url):
        score -= 15

    # Deduct points for suspicious parameters
    if has_suspicious_parameters(url):
        score -= 10

    # Ensure the trust score stays within the range of 0 to 100
    score = max(0, min(100, score))

    return score

def is_malicious(url):
    """Combine all methods to assess whether a URL is malicious."""
    trust_score = calculate_trust_score(url)
    return trust_score, trust_score < 50  # Trust score less than 50 is considered malicious

# Routes for the Flask Application

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_url', methods=['POST'])
def check_url():
    url = request.form['url']
    trust_score, malicious = is_malicious(url)
    
    if malicious:
        return render_template('result.html', status='Malicious', trust_score=trust_score, message="This URL is potentially malicious.")
    else:
        return render_template('result.html', status='Safe', trust_score=trust_score, message="This URL seems safe.")

if __name__ == "__main__":
    app.run(debug=True)
