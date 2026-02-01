import sys
import subprocess
import random

import Magic8Ball as mb


def test_get_response_monkeypatch(monkeypatch):
    # force random.choice to return a known value
    monkeypatch.setattr(random, "choice", lambda seq: "FORCED-ANSWER")
    assert mb.get_response("anything", answers=["FORCED-ANSWER", "x"]) == "FORCED-ANSWER"


def test_cli_outputs_only_allowed_lines():
    # run the script non-interactively and ensure output includes one of the canonical answers
    proc = subprocess.run([sys.executable, "Magic8Ball.py"], input="Will I pass?\n", text=True, capture_output=True)
    assert proc.returncode == 0
    out = proc.stdout
    # prompt must appear
    assert "Ask a question:" in out
    # one of the canonical answers must appear somewhere in stdout
    assert any(a in out for a in mb.ANSWERS)
    # ensure no stray numeric debug index is printed
    assert not any(line.strip().isdigit() for line in out.splitlines())
