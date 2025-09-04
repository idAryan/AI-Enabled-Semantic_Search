# Semantic Search using Sentence Transformers
## How i made flask app
Simply create the semantic_search.py in which i linked it **app/__init__py**  
To ensure that my application run on **flask run** i installed python-dotenv and in .flaskenv i set FLASK_APP=semantic_search.py and FLASK_DEBUG=1  
Now in app folder I created **routes.py** in which I just render the templates.  
In **utils/semantic_search.py** I wrote the main logic of search which I will explain later.  
data folder have NCO-2015 data which I imported it in semantic_search.py  
And now my application is ready!!  
Be sure to install flask,dotenv,SentenceTransformer   
<img width="1919" height="912" alt="image" src="https://github.com/user-attachments/assets/6c00e8df-38a2-48a0-8a70-44102e8e192d" />

# Semantic Search  
I have selected **all-MiniLM-L6-v2** model  
Now created data corpus with title and description  
Created corpus embeddings using model.encode()  
Now to get similar occupations and get top_k=5 results  
First user type query which i encode it to the same embedding used to encode corpus  
Then I find cosine similarities between corpus embeddings and query embedding  
top_hits will store the top top_k numbers of similar corpus embeddings  
Now top hits similarities have format in which there is values and indices  
now item in selected by idx  
result is appended in which code, title, description and score is appended by score.item()  
Return the result which will be stored in results in route.py and then passed along render_template.

