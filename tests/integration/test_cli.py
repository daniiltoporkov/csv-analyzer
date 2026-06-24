import os
import subprocess
import sys
import tempfile


def test_cli_runs():
    data = """id,category,status,created,closed
1,Software,Closed,2026-05-01 10:00:00,2026-05-02 12:00:00
2,Hardware,Open,2026-05-03 09:00:00,
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(data)
        f.flush()
        result = subprocess.run(
            [sys.executable, "-m", "csv_analyzer.cli", f.name],
            capture_output=True,
            text=True,
        )
    os.unlink(f.name)
    assert result.returncode == 0
    assert "Записей обработано: 2" in result.stdout
    assert "Software" in result.stdout
