# ChatMovie

## Development
1. install dependencies
```
pip install -r requirements
```

2. setup the environment variables
```
export OPENAI_KEY=
export OPENAI_URL=
export TMDB_API_KEY=
export TMDB_SESSION_ID=
export TMDB_LANGUAGE=
```

3. run the app
```
cd app
uvicorn main:app --reload
```

3. go to `localhost:8000` and have fun


## Deploy
```
modal deploy main.py
```
