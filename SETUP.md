# Quick Setup Guide for Signify

## 🚀 Getting Messages from Your Contact Form

Your website now has a fully functional contact form! Here's how to start receiving messages:

### Option 1: Formspree (Recommended - Free & Easy)

1. **Sign up for Formspree** (free):
   - Visit https://formspree.io
   - Create an account with your email

2. **Create a form**:
   - Click "New Form" after logging in
   - Name it "Signify Contact Form"
   - Copy your form ID (looks like: `abc123xyz`)

3. **Update your website**:
   - Open `index.html`
   - Find line ~157: `action="https://formspree.io/f/xyzypqgz"`
   - Replace `xyzypqgz` with your form ID
   - Save the file

4. **You're done!** 
   - Messages will now be sent to your email
   - Formspree will forward all form submissions to you

### Option 2: EmailJS (Alternative)

1. Visit https://www.emailjs.com/
2. Create a free account
3. Follow their setup guide
4. Update the JavaScript in `index.html` to use EmailJS

### Option 3: Direct Email (Simple)

Replace the form with a simple mailto link:
```html
<a href="mailto:your-email@example.com?subject=Signify Contact">Email Us</a>
```

## 📧 What Happens When Someone Sends a Message?

1. Visitor fills out the form with their name, email, and message
2. They click "Send Message"
3. The form submits to Formspree (or your chosen service)
4. You receive an email with their message
5. You can reply directly to their email address

## 🎨 Customization

### Change Contact Information

Edit the contact details in `index.html`:
- Line ~136: Phone number
- Line ~144: Email address
- Lines 189-190: Footer contact info

### Modify the Website Content

- **Home section**: Lines 39-69
- **About section**: Lines 72-93
- **How to Use section**: Lines 96-162
- **Contact section**: Lines 165-223

## 🌐 Publishing Your Website

### GitHub Pages (Free Hosting)

1. Go to your repository settings
2. Navigate to "Pages"
3. Select your main branch
4. Your site will be live at: `https://pratikn2003.github.io/signify/`

### Other Hosting Options

- **Netlify**: Drag and drop your folder
- **Vercel**: Connect your GitHub repo
- **Surge**: Use command line `surge`

## 💡 Tips

- Test your contact form after setting up Formspree
- Check your spam folder for test messages
- Customize the email address shown on the site
- Keep your Formspree form ID private (it's okay to share, but best practice)

## ❓ Need Help?

If you encounter any issues:
1. Check that your Formspree form ID is correct
2. Ensure you're using the correct email format in the form
3. Check Formspree's dashboard for submission logs
4. Read the full documentation in README.md

---

**Ready to go?** Just set up your Formspree account and you'll start receiving messages immediately!
