from dbks.runtime import Runtime


def test_runtime_v3():
    assert Runtime.v3("6", "6") == "6.6.x-scala2.12"


def test_runtime_v3_cpu():
    assert Runtime.v3("6", "6", "cpu") == "6.6.x-cpu-ml-scala2.12"
