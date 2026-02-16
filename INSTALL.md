# Installation & Setup Guide for Signify

This guide will help you run the Signify project on your local machine or in VS Code.

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser (Chrome, Firefox, Edge, Safari)

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/Pratikn2003/signify.git
cd signify
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or if using pip3:
```bash
pip3 install -r requirements.txt
```

### Step 3: Configure Email Settings (Optional)

If you want the contact form to send emails:

1. Open the `.env` file
2. Update the following settings:
   ```
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password-here
   RECEIVER_EMAIL=support@signify.com
   ```

**Note:** For Gmail, you'll need to:
- Enable 2-factor authentication
- Generate an "App Password" from your Google Account settings
- Use the app password in the `EMAIL_PASSWORD` field

### Step 4: Run the Project

You have two options:

#### Option A: Static Website Only (No Backend)

Simply open `index.html` in your web browser, or use a simple HTTP server:

```bash
# Using Python
python -m http.server 8000
# Then visit: http://localhost:8000

# Using Python 3
python3 -m http.server 8000
# Then visit: http://localhost:8000
```

**Note:** The contact form won't work without the backend server.

#### Option B: Full Application (With Backend)

1. **Start the Backend Server:**
   ```bash
   python server.py
   # Or
   python3 server.py
   ```
   
   You should see:
   ```
   🚀 Signify Backend Server starting...
   ✅ Server running on http://localhost:5000
   ```

2. **In a new terminal, start the Frontend:**
   ```bash
   python -m http.server 8000
   # Or
   python3 -m http.server 8000
   ```

3. **Open your browser:**
   - Visit: http://localhost:8000
   - The contact form will now work and send emails!

## 💻 Running in VS Code

### Method 1: Live Server Extension

1. Install the "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"
4. The website will open in your default browser

### Method 2: Integrated Terminal

1. Open VS Code terminal (View → Terminal or Ctrl+`)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend (if needed):
   ```bash
   python server.py
   ```
4. Open a new terminal and start HTTP server:
   ```bash
   python -m http.server 8000
   ```
5. Open http://localhost:8000 in your browser

### Method 3: Python Extension

1. Install the "Python" extension in VS Code
2. Open `server.py`
3. Click the "Run" button (▶️) in the top right
4. In another terminal, run:
   ```bash
   python -m http.server 8000
   ```

## 🔧 Troubleshooting

### Issue: "pip not found" or "python not found"

**Solution:**
- Make sure Python is installed: https://www.python.org/downloads/
- Try using `python3` and `pip3` instead of `python` and `pip`
- Add Python to your system PATH

### Issue: Port 5000 or 8000 already in use

**Solution:**
- Use a different port:
  ```bash
  python -m http.server 9000  # For frontend
  ```
- Or modify `server.py` to use a different port:
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)
  ```

### Issue: Contact form doesn't work

**Solution:**
1. Make sure the backend server (`server.py`) is running
2. Check the browser console (F12) for errors
3. Verify email settings in `.env` file
4. Ensure Flask and Flask-CORS are installed

### Issue: Images not loading

**Solution:**
- Check that the `assets/img/` directory exists
- Make sure you're accessing via HTTP server (http://localhost:8000), not file:// protocol
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)

### Issue: CSS/JS not loading

**Solution:**
- Verify files exist in:
  - `assets/css/home.css`
  - `assets/js/home.js`
  - `assets/js/animation.js`
- Check browser console (F12) for 404 errors
- Make sure you're using an HTTP server, not opening the file directly

## 📁 Project Structure

```
signify/
├── assets/
│   ├── css/
│   │   └── home.css          # Main stylesheet
│   ├── js/
│   │   ├── home.js           # Main JavaScript
│   │   └── animation.js      # Animation effects
│   └── img/
│       ├── Signify_logo.png  # Logo image
│       ├── About.png         # About section image
│       └── Joachim_Gaucks_signature.svg  # Signature image
├── index.html                # Main HTML file
├── server.py                 # Flask backend server
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
├── README.md                 # Project documentation
├── SETUP.md                  # Contact form setup
└── INSTALL.md               # This file
```

## 🌐 Deploying to Production

### GitHub Pages (Static Only)

1. Go to repository Settings → Pages
2. Select main branch
3. Your site will be at: https://pratikn2003.github.io/signify/

**Note:** Backend features (contact form) won't work on GitHub Pages.

### Deploying with Backend

For full functionality, deploy to:
- **Heroku**: https://www.heroku.com/
- **Railway**: https://railway.app/
- **Render**: https://render.com/
- **PythonAnywhere**: https://www.pythonanywhere.com/

## 📝 Additional Notes

- The `.env` file contains sensitive information. Never commit it to version control with real credentials.
- For production use, replace the development server with a production WSGI server like Gunicorn.
- Update email addresses and phone numbers in `index.html` to your actual contact information.

## 🆘 Need More Help?

If you encounter issues not covered here:
1. Check the browser console (F12) for error messages
2. Review Python terminal output for backend errors
3. Ensure all dependencies are installed correctly
4. Verify file paths are correct

## ✅ Verification Checklist

After setup, verify:
- [ ] HTML page loads at http://localhost:8000
- [ ] Navigation menu works
- [ ] Smooth scrolling functions
- [ ] Dark mode toggle works
- [ ] Images display correctly
- [ ] Backend server runs without errors (if using contact form)
- [ ] Contact form submits successfully (if backend is running)

---

**Happy coding! 🚀**
