import pytest

from todo import add_task, complete_task, remove_task, format_task


def test_add_task_assigns_incrementing_ids():
    tasks = []
    first = add_task(tasks, "Buy milk")
    second = add_task(tasks, "Walk dog")
    assert first["id"] == 1
    assert second["id"] == 2
    assert tasks == [first, second]


def test_add_task_defaults_to_not_done():
    tasks = []
    task = add_task(tasks, "Buy milk")
    assert task["done"] is False


def test_complete_task_marks_done():
    tasks = []
    task = add_task(tasks, "Buy milk")
    completed = complete_task(tasks, task["id"])
    assert completed["done"] is True
    assert tasks[0]["done"] is True


def test_complete_task_missing_id_raises():
    tasks = []
    add_task(tasks, "Buy milk")
    with pytest.raises(ValueError):
        complete_task(tasks, 999)


def test_remove_task_removes_from_list():
    tasks = []
    task = add_task(tasks, "Buy milk")
    removed = remove_task(tasks, task["id"])
    assert removed == task
    assert tasks == []


def test_remove_task_missing_id_raises():
    tasks = []
    with pytest.raises(ValueError):
        remove_task(tasks, 999)


def test_format_task_shows_checkbox_state():
    tasks = []
    task = add_task(tasks, "Buy milk")
    assert format_task(task) == "[ ] 1: Buy milk"
    complete_task(tasks, task["id"])
    assert format_task(task) == "[x] 1: Buy milk"
