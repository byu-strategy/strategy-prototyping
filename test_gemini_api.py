import os
from google import genai
import pandas as pd

# Initialize the client (reads GEMINI_API_KEY from environment)
client = genai.Client(api_key='AIzaSyAMZgXi_HrAnmfRcVNsC5MCptjm5YPLuDY')

# Example 1: Competitive Analysis Loop
# Analyze multiple competitors with the same questions
competitors = ['Slack', 'Microsoft Teams', 'Discord', 'Zoom']

results = []
for competitor in competitors:
    # Dynamic prompt - changes for each competitor
    prompt = f"""
    Analyze {competitor} as a business collaboration tool:
    1. What is their primary value proposition?
    2. What is their pricing strategy?
    3. What are their top 3 competitive advantages?
    4. What market segment do they target?

    Provide a concise summary in bullet points.
    """

    response = client.models.generate_content(
        model='gemini-2.0-flash-exp',
        contents=prompt
    )

    results.append({
        'competitor': competitor,
        'analysis': response.text
    })
    print(f"Completed analysis for {competitor}")

# Save results to CSV
df = pd.DataFrame(results)
df.to_csv('competitor_analysis.csv', index=False)
print(f"\nAnalyzed {len(competitors)} competitors and saved to CSV")
