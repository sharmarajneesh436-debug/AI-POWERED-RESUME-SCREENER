import streamlit as st

from candidate import Candidate

from parser import ResumeParser

from skill_extractor import SkillExtractor

from ats_scorer import AtSScorer

from db import Database

from heap_ranking import HeapRanking



st.title(
    "AI Powered Resume Screener"
)

jd = st.text_area(
    "Enter Job Description"
)

files = st.file_uploader(
    "Upload Resumes",
    
    type=["pdf"],
    accept_multiple_files=True
)

if files:
    st.write(f"{len(files)} resume(s) uploaded")


if st.button("Analyze"):
    
    parser = ResumeParser()
    
    extractor = SkillExtractor()
    
    scorer = AtSScorer()
    
    db = Database()
    
    candidates =[]
    
    for file in files:
        
        text = parser.extract_text(file)
        
        skills = extractor.extract_skills(text)
        
        score = scorer.calculate_score(
            jd,
            text
        )
        
        candidate = Candidate(
            file.name,
            file.name,
            skills
        )
        st.write("Score Calculated:", score)
        
        candidate.set_score(score)
        st.write(candidate.get_data())
        
        candidates.append(candidate)
        
        candidates_id = db.save_candidate(
            candidate
        )
        db.save_skills(
            candidates_id,
            skills
        )
    
    top_candidates = HeapRanking.top_candidates(
        candidates,
        10
    )
    
    st.subheader(
        "Top Ranked Candidates"
    )
    
    rank =1
    
    for candidates in top_candidates:
        
        st.write(
        f"""
        Rank : {rank}
        
        Name : {candidates.name}
        
        Score: {candidates.score}
        
        Skills: {candidates.skills}"""    
            
        )
        
        rank +=1
        