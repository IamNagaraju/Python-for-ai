from google import genai

from app.config.settings import GEMINI_API_KEY, GEMINI_MODEL
from app.schemas.resume import ResumeAnalysis, JobMatchAnalysis


client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_resume(resume_text: str) -> ResumeAnalysis:
    prompt = f"""
You are an expert technical recruiter.

Analyze the following resume.

Provide:
1. Candidate summary
2. Technical skills
3. Years of experience
4. Key strengths
5. Missing or weak skills
6. Suitable job roles

Resume:
{resume_text}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": ResumeAnalysis,
        },
    )

    return response.parsed

def match_resume_with_job(
    resume_text: str,
    job_description: str
) -> JobMatchAnalysis:

    prompt = f"""
You are an expert technical recruiter.

Compare the candidate's resume against the job description.

Evaluate:

1. Overall match score from 0 to 100.
2. Skills that match the job requirements.
3. Important skills required by the job but missing from the resume.
4. A concise recommendation for the candidate.

Rules:

- match_score must be between 0 and 100.
- Only identify skills that are actually supported by the resume.
- Do not invent experience.
- Focus on technical skills and relevant experience.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": JobMatchAnalysis,
        },
    )

    return response.parsed