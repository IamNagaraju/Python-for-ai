from pydantic import BaseModel


class ResumeAnalysis(BaseModel):
    summary: str
    skills: list[str]
    experience: str
    strengths: list[str]
    skill_gaps: list[str]
    recommended_roles: list[str]

class JobMatchAnalysis(BaseModel):
    match_score: int
    matching_skills: list[str]
    missing_skills: list[str]
    recommendation: str