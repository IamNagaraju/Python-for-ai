from fastapi import APIRouter, UploadFile, File, Form

from app.services.pdf_service import extract_text_from_pdf

from app.services.resume_service import (
    analyze_resume,
    match_resume_with_job
)

from app.services.pdf_service import extract_text_from_pdf


router = APIRouter()


@router.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = f"/tmp/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "text": text
    }


@router.post("/resume/analyze")
async def analyze_resume_api(file: UploadFile = File(...)):
    file_path = f"/tmp/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    resume_text = extract_text_from_pdf(file_path)

    analysis = analyze_resume(resume_text)

    return {
        "filename": file.filename,
        "analysis": analysis
    }

@router.post("/resume/match-job")
async def match_resume_with_job_api(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    file_path = f"/tmp/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    resume_text = extract_text_from_pdf(file_path)

    analysis = match_resume_with_job(
        resume_text,
        job_description
    )

    return {
        "filename": file.filename,
        "analysis": analysis
    }