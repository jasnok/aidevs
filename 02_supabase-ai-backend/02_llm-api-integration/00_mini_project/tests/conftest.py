"""미니 프로젝트 테스트의 공통 pytest 설정."""

import sys
from pathlib import Path


# pytest를 어느 폴더에서 실행하더라도 `from app...` import가 가능하게 한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
project_root = str(PROJECT_ROOT)

if project_root not in sys.path:
    sys.path.insert(0, project_root)
