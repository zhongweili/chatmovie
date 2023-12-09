# chatmovie

## Development
1. install dependencies
```
pip install -r requirements
```

2. setup environment variables
```
export OPENAI_KEY=
export OPENAI_URL=
export TMDB_API_KEY=
export TMDB_SESSON_ID=
export TMDB_LANGUAGE=
```

3. run the app
```
cd app
uvicorn main:app --reload
```

4. go to `localhost:8000` and have fun
