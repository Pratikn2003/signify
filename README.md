# Signify - Secure Digital Signature Verification

Welcome to **Signify**, a modern web application for secure digital signature verification and authentication.

## 📋 Table of Contents
- [Quick Start](#-quick-start)
- [About the Project](#about-the-project)
- [Features](#features)
- [How to Run This Project](#-how-to-run-this-project)
- [Contact & Messaging](#contact--messaging)
- [Quick Setup for Repository Owner](#quick-setup-for-repository-owner)
- [Contributing](#contributing)

## ⚡ Quick Start

Get Signify running in 3 simple steps:

```bash
# 1. Clone the repository
git clone https://github.com/Pratikn2003/signify.git
cd signify

# 2. Open the website (choose one method)
# Method A: Open index.html directly in your browser
# Method B: Use Python's built-in server (Python 3)
python3 -m http.server 8000
# Or just 'python' if it points to Python 3 on your system

# 3. Visit http://localhost:8000 in your browser
```

**That's it!** The website will run without any installation.

For full functionality with the contact form, see [How to Run This Project](#-how-to-run-this-project) below.

## 🔍 About the Project

Signify is a digital signature verification platform that delivers intelligent authentication systems to ensure document integrity and eliminate fraudulent signature risks. Our platform modernizes digital authentication processes and strengthens trust in secure document verification systems.

## ✨ Features

- **Advanced Signature Validation**: State-of-the-art algorithms for signature verification
- **Fraud Detection Intelligence**: AI-powered fraud detection systems
- **Secure Cloud-Based Verification**: Enterprise-grade security for all verifications
- **Enterprise-Grade Reliability**: Built for mission-critical applications
- **User-Friendly Interface**: Clean, modern design for easy navigation

## 🚀 How to Run This Project

Signify can run in two modes: **Static Website** (no setup required) or **Full Application** (with backend for contact form).

### Prerequisites

- **For Static Website**: Any modern web browser (Chrome, Firefox, Safari, Edge)
- **For Full Application**: 
  - Python 3.7 or higher
  - pip (Python package manager)

### Option 1: Static Website (Recommended for Quick View)

No installation required! Just open the website:

```bash
# Clone the repository
git clone https://github.com/Pratikn2003/signify.git
cd signify

# Method A: Open directly in browser
# Double-click index.html or right-click → Open with → Your Browser

# Method B: Use Python's HTTP server (recommended)
python3 -m http.server 8000
# Then visit: http://localhost:8000

# Method C: Use Node.js http-server
npx http-server
# Then visit: http://localhost:8080
```

**What works in static mode:**
- ✅ Browse all website sections (Home, About, Contact)
- ✅ View all content and images
- ✅ Navigation and smooth scrolling
- ✅ Dark mode toggle
- ✅ Responsive design
- ❌ Contact form (requires backend)

### Option 2: Full Application (With Contact Form)

To enable the contact form functionality:

```bash
# 1. Clone the repository
git clone https://github.com/Pratikn2003/signify.git
cd signify

# 2. Install Python dependencies
pip3 install -r requirements.txt

# 3. Configure email settings (edit .env file)
# Update EMAIL_USER, EMAIL_PASSWORD, and RECEIVER_EMAIL

# 4. Start the backend server
python3 server.py
# You should see: ✅ Server running on http://localhost:5000

# 5. In a new terminal, start the frontend
python3 -m http.server 8000

# 6. Visit http://localhost:8000 in your browser
```

**What works in full mode:**
- ✅ Everything from static mode
- ✅ Fully functional contact form
- ✅ Email notifications to support team
- ✅ Auto-reply emails to users

### Using the Website

Once running, you can:
- **Browse sections**: Navigate between Home, About, and Contact Us
- **Add Signature**: Click the "Add Signature" button to add a digital signature to your document
- **Verify Signature**: Click the "Verify Signature" button to verify an existing digital signature
- **Contact Us**: Fill out the contact form to send messages (backend required)

### Detailed Setup Instructions

For more detailed instructions including:
- VS Code setup
- Troubleshooting
- Deployment options
- Email configuration

See [INSTALL.md](INSTALL.md) for complete documentation.

## 💬 Contact & Messaging

### How to Send Us a Message

We've made it easy for anyone to contact us! Here's how:

1. **Visit the Contact Section**:
   - Scroll down to the "Contact Us" section on the homepage
   - Or click "Contact Us" in the navigation menu

2. **Fill Out the Contact Form**:
   - **Your Name**: Enter your full name
   - **Your Email**: Provide your email address so we can respond
   - **Your Message**: Tell us how we can help you

3. **Submit Your Message**:
   - Click the "Send Message" button
   - You'll receive a confirmation that your message was sent
   - We'll respond to your email address as soon as possible

### Setting Up the Contact Form (For Repository Owner)

The contact form is currently configured to use **Formspree**, a free email service for static websites. To receive messages:

1. **Create a free Formspree account**:
   - Visit [formspree.io](https://formspree.io)
   - Sign up with your email address

2. **Create a new form**:
   - After logging in, click "New Form"
   - Give it a name (e.g., "Signify Contact Form")
   - You'll receive a unique form endpoint URL

3. **Update the form action**:
   - Open `index.html`
   - Find the line: `<form class="contact-form" id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID_HERE" method="POST">`
   - Replace `YOUR_FORM_ID_HERE` with your actual Formspree form ID
   - Example: `action="https://formspree.io/f/abc123xyz"`

4. **Alternative: Use EmailJS or other services**:
   - [EmailJS](https://www.emailjs.com/) - Free email service
   - [Form-Data](https://form-data.com/) - Simple form backend
   - [Getform](https://getform.io/) - Form backend service

### Alternative Contact Methods

- **Email**: [support@signify.com](mailto:support@signify.com)
- **Phone**: +91 012 345 6789

### What You Can Message Us About

- Questions about using the Signify platform
- Technical support and troubleshooting
- Business inquiries and partnerships
- Integration support for your organization
- Feature requests and suggestions
- Reporting issues or bugs

## 🔧 Quick Setup for Repository Owner

**Want to start receiving messages right away?** See [SETUP.md](SETUP.md) for a quick 5-minute setup guide!

The contact form is ready to use - you just need to:
1. Create a free Formspree account
2. Get your form ID
3. Update one line in `index.html`

That's it! Full instructions in [SETUP.md](SETUP.md).

## 🤝 Contributing

We welcome contributions to make Signify better! If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

## 📄 License

This project is available for use and modification.

## 👨‍💻 Project Maintainer

- **GitHub**: [@Pratikn2003](https://github.com/Pratikn2003)

---

**Need help?** Don't hesitate to reach out through our [contact form](#contact--messaging) or email us at support@signify.com!