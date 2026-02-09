from .creator import create_artifact
from .updater import update_artifact
from .detector import detect_artifacts

class ArtifactService:
    def __init__(self):
        self.artifacts = []

    def add_artifact(self, workspace_id, title, content):
        artifact = create_artifact(workspace_id, title, content)
        self.artifacts.append(artifact)
        return artifact

    def update_artifact(self, artifact, content):
        return update_artifact(artifact, content)

    def detect(self, content):
        return detect_artifacts(content)
