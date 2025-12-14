import spacy

nlp = spacy.load("en_core_web_md")

def preprocess(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
    return tokens

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in {"PERSON", "ORG", "GPE"}]

def classify_text(text):
    positive_keywords = ["Passionate", "Thrives", "Excited", "Motivated", "Supportive", "Engaging", "Joy", "Eager", "Rewarding", "Inspired"]
    negative_keywords = ["Frustrated", "Lack of team collaboration", "Overwhelmed"]

    sentiment_score = sum([1 for word in positive_keywords if word.lower() in text.lower()]) -\
                      sum([1 for word in negative_keywords if word.lower() in text.lower()])

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"


categories = {
    "Project Manager": ["project management", "scheduling", "risk management", "stakeholders", "milestones"],
    "Graphic Designer": ["photoshop", "illustrator", "creativity", "branding", "typography", "visual design"],
    "HR Specialist": ["recruitment", "onboarding", "employee relations", "hr policies", "talent acquisition"],
    "Cybersecurity Analyst": ["network security", "threat analysis", "firewall", "vulnerability", "incident response"],
    "Sales Representative": ["sales", "negotiation", "client acquisition", "leads", "target", "crm"]
}

def match_category(resume_tokens, categories):
    scores = {}
    for cat, keywords in categories.items():
        score = 0
        for token in resume_tokens:
            for kw in keywords:
                score += nlp(token).similarity(nlp(kw))
        scores[cat] = score
    return max(scores, key=scores.get)

def analyze_resume(text):
    tokens = preprocess(text)
    entities = extract_entities(text)
    sentiment = classify_text(text)
    category = match_category(tokens, categories)

    return {
        "Entities": entities,
        "Sentiment": sentiment,
        "Best Job Category": category
    }

resume1 = "Experienced software engineer proficient in Python and Java development, with a strong understanding of algorithms and data structures. I am passionate about software development and thrive in collaborative team environments. My experience includes leading development projects and implementing rigorous testing procedures."
resume2 = "A data scientist with expertise in machine learning, data analysis, and statistical modeling using Python and R. I am excited about leveraging data to drive insights and have a proven track record in building predictive models and presenting data-driven recommendations."
resume3 = "Project manager with over 7 years of experience in managing software development projects, ensuring timely delivery and stakeholder satisfaction. Skilled in scheduling, risk management, and cross-functional team leadership. Known for delivering complex projects on time and within budget."

result1 = analyze_resume(resume1)
result2 = analyze_resume(resume2)
result3 = analyze_resume(resume3)

print("Result for Resume 1:")
print(result1)
print("\nResult for Resume 2:")
print(result2)
print("\nResult for Resume 3:")
print(result3)
