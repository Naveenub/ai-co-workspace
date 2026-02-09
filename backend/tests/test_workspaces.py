from app.services.workspaces.context_builder import ContextBuilder
from app.services.workspaces.permissions import check_permission

def test_context_builder():
    builder = ContextBuilder()
    ctx = builder.build(1, ["Hello", "World"])
    assert "Workspace 1 Context" in ctx

def test_permissions():
    assert check_permission(1, 1) is True
