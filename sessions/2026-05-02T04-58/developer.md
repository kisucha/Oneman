# 💻 Developer — 특정 키워드로 과거 세션 로그를 검색하거나 리스트화할 수 있는 인덱싱 자동화 스크립트 및 검색 툴 개발

💻 Developer: 작업 시작합니다.

기존의 파편화된 세션 로그를 효율적으로 관리하기 위해, `sessions/` 폴더 내의 파일들을 스캔하여 **색인(Indexing) 파일을 생성**하고, 특정 키워드로 **검색(Searching)할 수 있는 통합 파이썬 스크립트**를 개발했습니다.

### 🛠️ 로그 인덱싱 및 검색 툴 (`log_manager.py`)

이 스크립트는 두 가지 핵심 기능을 수행합니다.
1. **`index` 모드**: 모든 세션 파일을 읽어 날짜, 세션 ID, 주요 내용을 요약한 `sessions/index.md`를 생성합니다.
2. **`search` 모드**: 특정 키워드가 포함된 로그 파일과 해당 문맥(Context)을 찾아 리스트화합니다.

```python
import os
import re
import argparse
from datetime import datetime

class LogManager:
    def __init__(self, log_dir="sessions/"):
        self.log_dir = log_dir
        self.index_file = os.path.join(log_dir, "index.md")

    def get_all_logs(self):
        """sessions 폴더 내의 모든 .md 파일을 가져옵니다."""
        return [f for f in os.listdir(self.log_dir) if f.endswith('.md') and f != 'index.md']

    def create_index(self):
        """전체 로그를 요약하여 index.md를 생성합니다."""
        logs = self.get_all_logs()
        index_content = [f"# 📑 Session Index ({datetime.now().strftime('%Y-%m-%d')})\n"]
        
        if not logs:
            print("❌ 대상 로그 파일이 없습니다.")
            return

        for log_file in sorted(logs, reverse=True):
            path = os.path.join(self.log_dir, log_file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                # 첫 줄(날짜/세션 정보)과 첫 100자 추출
                first_line = content.split('\n')[0]
                summary = content.replace('\n', ' ').strip()[:100] + "..."
                index_content.append(f"- [{log_file}]({log_file}): {first_line}\n  - *Summary*: {summary}\n")

        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(index_content))
        
        print(f"✅ 인덱싱 완료: {self.index_file}")

    def search_keyword(self, keyword):
        """키워드가 포함된 로그를 검색합니다."""
        logs = self.get_all_logs()
        found_count = 0
        print(f"🔍 '{keyword}' 검색 결과:\n")

        for log_file in logs:
            path = os.path.join(self.log_dir, log_file)
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                matches = []
                for i, line in enumerate(lines):
                    if keyword.lower() in line.lower():
                        # 해당 라인과 전후 1줄을 컨텍스트로 포함
                        start = max(0, i - _context_offset(i)), 
                        end = min(len(lines), i + 2)
                        context = "".join(lines[max(0, i-1):i+2]).strip()
                        matches.append(f"  > [Context] {context}")
                        found_count += 1

                if matches:
                    print(f"📄 파일: {log_file}")
                    for m in matches:
                        print(m)
                    print("-" * 30)

        if found_count == 0:
            print("❌ 검색 결과가 없습니다.")
        else:
            print(f"✅ 총 {found_count}개의 매칭 항목을 찾았습니다.")

def _context_offset(idx):
    return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JAY CORP Log Management Tool")
    parser.add_argument("action", choices=["index", "search"], help="action: index or search")
    parser "keyword", help="keyword to search (for search action)")
    
    # CLI 인자 처리를 위한 간단한 구현 (argparse 확장)
    args = parser.parse_args()
    manager = LogManager()

    if args.action == "index":
        manager.create_index()
    elif args.action == "search":
        if not parser.get_default("keyword"): # 실제 구현 시 argument parsing 로직 보완
            pass 
        # 위 구조를 위해 단순화된 인자 처리 로직 사용
        import sys
        if
