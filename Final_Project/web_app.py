import csv
import pandas as pd
import numpy as np
import gradio as gr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

yoga_data = pd.read_csv(r"C:\Users\Dell\Desktop\PYTHON ML INTERNSHIP\Yoga_asanas - Sheet1.csv")
benefit_poses = dict()
asana_desc = dict()
csvfile = open(r'C:\Users\Dell\Desktop\PYTHON ML INTERNSHIP\Yoga_asanas - Sheet1.csv', newline='\n')
reader = csv.reader(csvfile)
for row in reader :
    pose = row[0]
    desc = row[2].split('\n')
    asana_desc[pose] = desc
del asana_desc['Asanas']

csvfile = open(r'C:\Users\Dell\Desktop\PYTHON ML INTERNSHIP\Yoga_asanas - Sheet1.csv', newline='\n')
reader = csv.reader(csvfile)
for row in reader:
    pose = row[0]
    b_list = row[1].split(',')   #list of benefits
    for benefit in b_list:
        if benefit.strip() in benefit_poses :
            benefit_poses[benefit.strip()].append(pose)
        else:
            benefit_poses[benefit.strip()] = [pose]
del benefit_poses['Benefits']

benefits = list(benefit_poses.keys())

tfidf = TfidfVectorizer()
benefit_vectors = tfidf.fit_transform(benefits)

def recommend_yoga_asanas(user_input):
    # Transform user input using TF-IDF vectorizer
    user_vector = tfidf.transform([user_input])
    
    
    # Calculate cosine similarity with the benefits in the dataset
    similarity_scores = cosine_similarity(user_vector, benefit_vectors)
    
    # Get the top similar benefit
    recommended_index = np.argsort(similarity_scores[0])[::-1][:1]
    
    # Get the related asanas
    recommended_asanas = benefit_poses[benefits[recommended_index[0]]]
    
    # If the user wants descriptions, return those too
    descriptions = [asana_desc[asana] for asana in recommended_asanas]
    
    return recommended_asanas, descriptions

def yoga_recommender(user_problem, show_descriptions):
    asanas, descriptions = recommend_yoga_asanas(user_problem)
    asanas_str = "\n".join(f"{i+1}. {asana}" for i, asana in enumerate(asanas))
    
    if show_descriptions:
        descriptions_str = "\n\n".join(
            f"{i+1}. {asana}\n   " + "\n   ".join(f"- {desc}" for desc in description_list)
            for i, (asana, description_list) in enumerate(zip(asanas, descriptions)))
        return asanas_str, descriptions_str
    else:
        return asanas_str, ""

iface = gr.Interface(
    fn=yoga_recommender,
    inputs=[
        gr.Textbox(label="Describe for what purpose do you want yoga asanas recommendation "),
        gr.Checkbox(label="Show descriptions?", value=False)
    ],
    outputs=[
        gr.Textbox(label="Recommended Asanas"),
        gr.Textbox(label="Asana Descriptions")
    ],
    title="Yoga Recommendation System",
    description="Get personalized yoga asana recommendations based on your health concerns."
)

iface.launch(share=True)
