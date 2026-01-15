# Deployment Guide for Bhuj Online

## Cloudflare Pages (Recommended)

This website is designed to be hosted on **Cloudflare Pages**.

### Automatic Deployment (Git Integration)
If you have connected your Cloudflare Pages project to your GitHub repository (`https://github.com/nrbhai/bhujonline`):

1.  **Simply Push to GitHub**: Any change pushed to the `main` branch will automatically trigger a new build and deployment on Cloudflare.
2.  **Status**: You can check the build status in your Cloudflare Dashboard > Pages > [Your Project] > Deployments.

**The latest changes (Redesign) have already been pushed to GitHub.** If your site is connected, it should update automatically within a few minutes.

### Manual Upload (Direct Upload)
If you are NOT using Git integration:

1.  Go to your **Cloudflare Dashboard**.
2.  Navigate to **Pages** > **Create a project** > **Direct Upload**.
3.  Upload the entire project folder (`c:\website_project\bhuj-online`).
4.  Cloudflare will deploy the static files immediately.

## Verified Configuration
- **Build Output Directory**: `/` (Root) or leave blank.
- **Framework Preset**: None (Static HTML/CSS).
