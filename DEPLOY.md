# Deployment Workflow for Bhuj Online

## Your Deployment Setup

- **Git Repository**: For version control and backup
- **Cloudflare Pages**: For hosting (via Wrangler CLI)
- **Live Site**: https://d48b91ad.bhujonline.pages.dev

---

## Quick Deployment Steps

### 1. Save to Git (Version Control)
```bash
git add .
git commit -m "Your commit message"
git push
```

### 2. Deploy to Cloudflare (Go Live)
```bash
npx wrangler pages deploy . --project-name=bhujonline
```

---

## Complete Workflow Example

```bash
# After making changes to your files:

# 1. Save to Git
git add .
git commit -m "Update pioneer.html with new features"
git push

# 2. Deploy to Cloudflare
npx wrangler pages deploy . --project-name=bhujonline
```

**Done!** Your changes are now live at https://d48b91ad.bhujonline.pages.dev

---

## Tips

- **Git first, deploy second** - Always commit to Git before deploying
- **Deployment time** - Usually takes 10-30 seconds
- **Check your site** - Visit the URL after deployment to verify changes
- **Custom domain** - You can add a custom domain in Cloudflare Dashboard → bhujonline → Custom domains

---

## Troubleshooting

**If deployment fails:**
- Make sure you're in the project directory: `cd c:\website_project\bhujonline`
- Check your internet connection
- Try running the deploy command again

**Need help?** Check the Cloudflare Dashboard → Workers & Pages → bhujonline → Deployments for logs.
