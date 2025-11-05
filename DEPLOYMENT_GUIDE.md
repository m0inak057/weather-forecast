# 🚀 Deploy Weather Forecast App to Render

## Prerequisites Checklist
- [ ] GitHub account
- [ ] Render account (sign up at https://render.com)
- [ ] Code pushed to GitHub repository
- [ ] OpenWeather API key (you already have: c2b044b9195153769145eb89b91fda3a)

---

## Step 1: Prepare Your Code for Deployment

### 1.1 Verify Your Files
Make sure these files exist in your project root:
- ✅ `build.sh` - Build script for Render
- ✅ `requirements.txt` - Python dependencies
- ✅ `.gitignore` - Excludes .env and sensitive files
- ✅ `manage.py` - Django management script

### 1.2 Push to GitHub
If you haven't already, push your code to GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Prepare for Render deployment"

# Add your GitHub repository as remote
git remote add origin https://github.com/m0inak057/reg-form.git

# Push to GitHub
git push -u origin master
```

---

## Step 2: Create Web Service on Render

### 2.1 Login to Render
1. Go to https://dashboard.render.com
2. Click **"New +"** button in the top right
3. Select **"Web Service"**

### 2.2 Connect Your Repository
1. Choose **"Build and deploy from a Git repository"**
2. Click **"Connect account"** to connect your GitHub
3. Search for `reg-form` repository
4. Click **"Connect"**

### 2.3 Configure Web Service

Fill in the following settings:

**Basic Settings:**
- **Name:** `weather-forecast-app` (or any name you prefer)
- **Region:** Choose closest to you (e.g., `Ohio (US East)`)
- **Branch:** `master`
- **Root Directory:** Leave empty (blank)
- **Runtime:** `Python 3`

**Build & Deploy Settings:**
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn weatherproject.weatherproject.wsgi:application`

**Instance Type:**
- Select **"Free"** (or paid if you prefer)

---

## Step 3: Configure Environment Variables

**CRITICAL:** Before deploying, click **"Advanced"** and add these environment variables:

| Key | Value | Notes |
|-----|-------|-------|
| `SECRET_KEY` | `your-production-secret-key-here-make-it-long-and-random` | Generate a secure key* |
| `OPENWEATHER_API_KEY` | `c2b044b9195153769145eb89b91fda3a` | Your existing API key |
| `DEBUG` | `False` | **IMPORTANT:** Must be False in production |
| `PYTHON_VERSION` | `3.12.2` | Match your local version |

**How to generate a secure SECRET_KEY:*
```python
# Run this in Python to generate a secure key:
import secrets
print(secrets.token_urlsafe(50))
```

Or use online generator: https://djecrety.ir/

---

## Step 4: Deploy Your Application

1. **Review all settings** to make sure everything is correct
2. Click **"Create Web Service"** button at the bottom
3. Render will now:
   - Clone your repository
   - Run `build.sh` to install dependencies and collect static files
   - Start your application with gunicorn
   - This takes 2-5 minutes ⏱️

### Monitor the Build
You'll see a live log showing:
```
==> Cloning from https://github.com/m0inak057/reg-form...
==> Running build command './build.sh'...
==> Installing dependencies from requirements.txt
==> Collecting static files
==> Running migrations
==> Build successful!
==> Starting service with gunicorn...
```

---

## Step 5: Access Your Deployed App

Once deployment is complete:

1. **Your app URL** will be shown at the top:
   - Format: `https://weather-forecast-app-xxxx.onrender.com`
   - The "xxxx" will be a unique identifier

2. **Click the URL** to open your live app! 🎉

3. **Test the app:**
   - Search for a city (e.g., "London", "New York")
   - Verify weather data loads correctly
   - Check that all features work

---

## Step 6: Custom Domain (Optional)

### Add Your Own Domain
1. Go to your service dashboard
2. Click **"Settings"** tab
3. Scroll to **"Custom Domains"**
4. Click **"Add Custom Domain"**
5. Follow the instructions to add DNS records

---

## Common Issues & Troubleshooting

### Issue 1: Build Failed
**Solution:** Check the build logs for errors. Common fixes:
- Verify `build.sh` has Unix line endings (not Windows CRLF)
- Make sure all dependencies are in `requirements.txt`

### Issue 2: Application Error
**Solution:** 
- Check if environment variables are set correctly
- View logs: Dashboard → Logs tab
- Verify `DEBUG=False` is set

### Issue 3: Static Files Not Loading
**Solution:**
- Check that `whitenoise` is in `requirements.txt` ✅
- Verify `build.sh` runs `collectstatic` ✅
- Check STATIC settings in `settings.py` ✅

### Issue 4: Weather Data Not Loading
**Solution:**
- Verify `OPENWEATHER_API_KEY` environment variable is set
- Test API key at: https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY

---

## Post-Deployment Checklist

After successful deployment:
- [ ] Test the app with multiple cities
- [ ] Check 5-day forecast works
- [ ] Verify temperature history chart displays
- [ ] Test on mobile devices
- [ ] Share your app URL with friends! 🎊

---

## Updating Your App

When you make changes:

1. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Update UI and features"
   git push origin master
   ```

2. **Render auto-deploys:**
   - Render automatically detects changes
   - Rebuilds and redeploys your app
   - Takes 2-3 minutes

3. **Manual Deploy (if auto-deploy is off):**
   - Go to Render dashboard
   - Click **"Manual Deploy"** → **"Deploy latest commit"**

---

## Monitoring & Maintenance

### View Logs
- Dashboard → Your Service → **"Logs"** tab
- See real-time application logs
- Debug errors and monitor traffic

### View Metrics
- Dashboard → Your Service → **"Metrics"** tab
- Monitor CPU, memory, and bandwidth usage
- Track response times

### Free Tier Limitations
- Your app spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- 750 hours/month free (enough for most personal projects)

---

## 🎉 Success!

Your Weather Forecast App is now live on Render!

**Share your app:**
- Your URL: `https://weather-forecast-app-xxxx.onrender.com`
- Add to your portfolio
- Share on social media
- Show it to potential employers!

---

## Need Help?

- **Render Docs:** https://render.com/docs
- **Django Deployment:** https://docs.djangoproject.com/en/stable/howto/deployment/
- **Community Support:** https://community.render.com

Good luck with your deployment! 🚀
