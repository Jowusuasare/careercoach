from django import forms

class CareerInputForm(forms.Form):
    linkedin_url = forms.URLField(label='LinkedIn Profile URL', required=True)
    job_description = forms.CharField(widget=forms.Textarea, label='Sample Job Description', required=True)
    career_goals = forms.CharField(widget=forms.Textarea, label='Career Goals', required=True)
    skills_experience = forms.CharField(widget=forms.Textarea, label='Skills and Experience', required=True)
    # submit = forms.Input