import os
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# Lấy các giá trị API Key
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY", "")

# Cấu hình Ollama local
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")

# Kiểm tra nhanh khi chạy trực tiếp file config.py
if __name__ == "__main__":
    print("--- KIỂM TRA CẤU HÌNH BẢO MẬT ---")
    print(f"VirusTotal Key: {'Đã cấu hình' if VIRUSTOTAL_API_KEY else 'Chưa có (Trống)'}")
    print(f"AbuseIPDB Key:  {'Đã cấu hình' if ABUSEIPDB_API_KEY else 'Chưa có (Trống)'}")
    print(f"Ollama Server:  {OLLAMA_HOST} (Model: {OLLAMA_MODEL})")