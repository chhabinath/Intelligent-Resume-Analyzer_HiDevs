from file_manager import (
    read_text_file,
    write_text_file,
)


def test_read_write_text(tmp_path):
    file = tmp_path / "sample.txt"

    write_text_file(
        str(file),
        "Hello World",
    )

    text = read_text_file(str(file))

    assert text == "Hello World"