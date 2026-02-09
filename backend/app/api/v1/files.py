from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    content = file.file.read()
    # Process and store as artifact
    return {"filename": file.filename, "size": len(content)}
