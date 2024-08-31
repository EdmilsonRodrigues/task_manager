import simple_task


def test_add():
    simple_task.add("test")
    assert simple_task.tasks[-1]["description"] == "test"


def test_update():
    simple_task.update(1, "updated")
    assert simple_task.tasks[-1]["description"] == "updated"


def test_mark_in_progress():
    simple_task.mark_in_progress(1)
    assert simple_task.tasks[-1]["status"] == "in-progress"


def test_mark_done():
    simple_task.mark_done(1)
    assert simple_task.tasks[-1]["status"] == "done"


def test_list():
    assert simple_task.list() == simple_task.tasks


def test_list_mark_todo():
    simple_task.mark_todo(1)
    assert simple_task.list("todo") == simple_task.tasks


def test_delete():
    simple_task.delete(1)
    assert not simple_task.tasks


def test_argparser():
    simple_task.argv = ["simple_task.py", "add", "test"]
    assert simple_task.argparser() == ("add", ["test"])


def test_argparser_wrong_arguments():
    simple_task.argv = ["simple_task.py"]
    try:
        simple_task.argparser()
    except simple_task.WrongArguments:
        assert True
    else:
        assert False


def test_argparser_wrong_function_arguments():
    simple_task.argv = ["simple_task.py", "add", "test", "wrong"]
    try:
        simple_task.main()
    except simple_task.WrongFunctionArguments:
        assert True
    else:
        assert False
