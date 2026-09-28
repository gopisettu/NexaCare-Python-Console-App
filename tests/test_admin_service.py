from pathlib import Path


def test_export_patient_details(
    monkeypatch,
    tmp_path
):

    def fake_generate_patient_report():

        yield {
            "patient_id": 1,
            "name": "Gopi",
            "age": 25,
            "phone": "9876543210"
        }

    monkeypatch.setattr(
        "services.admin_service.generate_patient_report",
        fake_generate_patient_report
    )

    monkeypatch.chdir(tmp_path)

    from services.admin_service import (
        export_patient_details
    )

    result = export_patient_details()

    assert result == "patient_report.txt"

    file_path = Path(result)

    assert file_path.exists()

    content = file_path.read_text(
        encoding="utf-8"
    )

    assert "Gopi" in content
    assert "9876543210" in content