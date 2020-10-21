from dbks.endpoint import Endpoint


def test_endpoint_str():
    ep = Endpoint("clusters", "create")
    assert ep.string == "/clusters/create"


def test_endpoint_method():
    ep = Endpoint("clusters", "create")
    assert ep.method == "POST"


def test_endpoint_parameters():
    ep = Endpoint("clusters", "create", p_1="p_1", p_2="p_2")
    assert ep.parameters == {"p_1": "p_1", "p_2": "p_2"}
