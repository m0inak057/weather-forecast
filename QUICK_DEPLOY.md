# Quick Deployment Commands

## 1. Generate SECRET_KEY
```python
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## 2. Push to GitHub
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin master
```

## 3. Render Configuration

**Build Command:**
```bash
./build.sh
```

**Start Command:**
```bash
gunicorn weatherproject.weatherproject.wsgi:application
```

## 4. Environment Variables to Set on Render

```
SECRET_KEY=<generate-a-long-random-string>
OPENWEATHER_API_KEY=c2b044b9195153769145eb89b91fda3a
DEBUG=False
PYTHON_VERSION=3.12.2
```

## 5. Your App Will Be Live At
```
https://your-app-name.onrender.com
```
