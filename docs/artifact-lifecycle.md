## Artifact Lifecycle

Artifacts represent structured outputs, documents, or insights generated in workspaces.

## Lifecycle

1. **Creation**  
   - New artifacts can be created manually or automatically from chat insights  

2. **Update**  
   - Artifacts can be updated via API or UI  

3. **Retrieval**  
   - Access artifact content and metadata  
   - Supports filtering by workspace, type, or date  

4. **Detection**  
   - Artifact detector identifies important messages or events  
   - Automates artifact creation

## Flow

[Chat / Task] 
│
▼ 
[Artifact Detector] 
│
▼ 
[Artifact Service] 
│
▼ 
[Database / Memory]
