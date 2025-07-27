from flask import render_template,Flask, request
from .utils.semantic_search import get_similar_occupations
from app import app

@app.route('/',methods=['GET','POST'])
@app.route('/home')
def index():
    results=[]
    status=""
    if request.method=='POST':
        query=request.form.get('query')
        results=get_similar_occupations(query)
        status=f"Showing top {len(results)} results for: {query}"
    return render_template('index.html',results=results,status=status)