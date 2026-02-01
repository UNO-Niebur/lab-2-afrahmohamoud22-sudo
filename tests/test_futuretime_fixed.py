import datetime

import FutureTime as ft


class FixedDT(datetime.datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2020, 1, 1, 23, 50)


def _mock_inputs(monkeypatch, responses):
    it = iter(responses)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(it))


def test_futuretime_rollover_and_padding(monkeypatch, capsys):
    monkeypatch.setattr(ft.datetime, "datetime", FixedDT)
    _mock_inputs(monkeypatch, ["1", "15"])  # hours, minutes

    ft.main()
    out = capsys.readouterr().out.strip()
    assert out == "01:05"


def test_futuretime_minute_only(monkeypatch, capsys):
    class D2(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2020, 1, 1, 10, 20)

    monkeypatch.setattr(ft.datetime, "datetime", D2)
    _mock_inputs(monkeypatch, ["0", "50"])  # hours, minutes

    ft.main()
    out = capsys.readouterr().out.strip()
    assert out == "11:10"