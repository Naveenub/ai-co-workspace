class ContextBuilder:
    def build(self, workspace_id: int, messages: list[str]) -> str:
        # Combine messages + metadata for context
        return f"Workspace {workspace_id} Context:\n" + "\n".join(messages)
