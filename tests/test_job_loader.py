import json

from job_loader import load_job


def test_load_job(tmp_path):
    job = {
        "title": "Python Developer",
        "required_skills": ["Python", "SQL"],
        "min_experience": 2,
        "education": "B.Tech Computer Science",
    }

    file = tmp_path / "job.json"

    file.write_text(json.dumps(job))

    loaded = load_job(str(file))

    assert loaded.title == "Python Developer"
    assert loaded.min_experience == 2