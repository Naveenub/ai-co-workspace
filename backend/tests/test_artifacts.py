from app.services.artifacts.artifact_service import ArtifactService

def test_artifact_creation():
    service = ArtifactService()
    artifact = service.add_artifact(1, "Title", "Content")
    assert artifact.title == "Title"
