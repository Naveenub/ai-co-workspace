from app.db.models.artifact import Artifact

def create_artifact(workspace_id: int, title: str, content: str, type_: str = "text"):
    return Artifact(workspace_id=workspace_id, title=title, content=content, type=type_)
