# Git Repository Setup Guide for Windows

## Step 1: Install Git for Windows

1. **Download Git**:
   - Go to https://git-scm.com/download/win
   - Download the 64-bit version
   - Run the installer

2. **Installation** (use these exact settings):
   - Click "Next" on all screens EXCEPT:
   - When asked about "Adjusting your PATH environment": Select "Git from the command line and also from 3rd-party software"
   - Continue clicking "Next" and then "Install"

3. **Verify Installation**:
   - Click Windows Start button
   - Type "Git Bash" and open it
   - Type: `git --version`
   - You should see: `git version 2.x.x.windows.x`

## Step 2: Configure Git

Open Git Bash and run these commands (replace with YOUR information):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

## Step 3: Create GitHub Account and Repository

1. Go to https://github.com
2. Sign up for an account (if you don't have one)
3. Sign in to your account
4. Click the **"+"** icon in top right corner
5. Select **"New repository"**
6. Fill in:
   - Repository name: `practice_adk`
   - Keep it **Public**
   - DO NOT check any boxes (no README, no gitignore, no license)
7. Click **"Create repository"**
8. Keep the page open - you'll need it

## Step 4: Create Personal Access Token

1. On GitHub, click your profile picture (top right)
2. Click **Settings**
3. Scroll down, click **Developer settings** (left sidebar)
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token (classic)**
6. Name it: "Git Windows"
7. Check the box for **repo** (it will auto-check sub-items)
8. Scroll down, click **Generate token**
9. **COPY THE TOKEN NOW** (you won't see it again!)
10. Save it in Notepad temporarily

## Step 5: Push Your Project to GitHub

1. **Open your project folder** in File Explorer
   - Example: `C:\Users\YourWindowsUsername\Documents\ai_news_chatbot_adk`

2. **Right-click** in the folder (on empty space)

3. Click **"Git Bash Here"**

4. Run these commands one by one:

```bash
# Initialize Git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit"

# Connect to GitHub (replace YOUR_GITHUB_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/practice_adk.git

# Push to GitHub
git push -u origin main
```

5. **When prompted**:
   - Username: Type your GitHub username
   - Password: Paste your Personal Access Token (NOT your GitHub password)

## Step 6: Clone to Another Location

1. Open File Explorer
2. Navigate to Desktop: `C:\Users\YourWindowsUsername\Desktop`
3. Right-click on empty space
4. Click **"Git Bash Here"**
5. Run this command (replace YOUR_GITHUB_USERNAME):

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/practice_adk.git
```

6. Your project is now cloned to Desktop in a folder called `practice_adk`

## Daily Usage

To work with your repository daily:

1. **Open your project**: Right-click in project folder → "Git Bash Here"

2. **Save and upload changes**:
```bash
git add .
git commit -m "What you changed"
git push
```

3. **Get latest changes**:
```bash
git pull
```

## Troubleshooting

### "git is not recognized"
- Reinstall Git for Windows
- Restart your computer

### "Authentication failed"
- Make sure you're using the Personal Access Token as password, NOT your GitHub password
- Create a new token if needed

### "rejected - non-fast-forward"
```bash
git pull origin main
git push
```

## Important Notes

- **Replace YOUR_GITHUB_USERNAME** with your actual GitHub username
- **Replace YourWindowsUsername** with your Windows username (check in C:\Users\)
- **Use your Personal Access Token** as password, never your GitHub password
- **Always use Git Bash** (not Command Prompt or PowerShell)

## Quick Command Reference

```bash
# Check status
git status

# View history
git log --oneline

# Add and commit
git add .
git commit -m "message"

# Upload changes
git push

# Download changes
git pull
```

---

**That's it!** You now have Git set up on Windows and your project on GitHub.