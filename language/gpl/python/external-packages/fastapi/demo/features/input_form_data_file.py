from typing import Annotated
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import HTMLResponse

# 'Content-Type: multipart/form-data'

router = APIRouter(
    prefix="/formdatafile",
    tags=["Form Data File"],
)

# Define files to be uploaded by the client

# --- File

# The file is received in bytes and the content is stored in memory (works well for small files)


@router.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


# --- UploadFile
# It uses a "spooled" file: A file stored in memory up to a maximum size limit, and after passing this limit it will be stored in disk.
# Works well for large files like images, videos, large binaries, etc. without consuming all the memory.
# You can get metadata from the uploaded file.
# It has a file-like async interface.
# It exposes an actual Python SpooledTemporaryFile object that you can pass directly to other libraries that expect a file-like object.


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(file.file)  # The actual file uploaded (SpooledTemporaryFile instance)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_content": str(await file.read()),
    }


## --- Multiple FileUpload


@router.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


# --- Test
@router.get("/")
async def html_response():
    content = """
<body>
    <h1> Multiple Files</h1>
    <form action="/formdatafile/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)


## --  Files and Form


@router.post("/files/")
async def form_and_files(
    file_a: Annotated[bytes, File()],
    file_b: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file_a),
        "token": token,
        "fileb_content_type": file_b.content_type,
    }


# curl -X 'POST' \
#   'http://localhost:8000/formdatafile/files/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'file_a=@my document.pdf;type=application/pdf' \
#   -F 'file_b=@my document.pdf;type=application/pdf' \
#   -F 'token=string'
