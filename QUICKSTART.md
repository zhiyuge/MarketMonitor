# Quick Start Guide

## 5-Minute Setup

### Step 1: Install Python Dependencies
Open PowerShell and run:
```powershell
cd [Your Work Folder]\MarketMonitor
pip install -r requirements.txt
```

### Step 2: Create the Scheduled Task
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
```

### Step 3: Test It Works
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

Done! The tool will now run automatically every day at 8:00 AM.

---

## Common Commands

**Run the tool right now:**
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

**View the scheduled task:**
Press `Windows + R`, type `taskschd.msc`, press Enter. Look for "MarketNewsMonitor"

**Check output reports:**
Open: `[Your Work Folder]\MarketMonitor\output`

**Uninstall the scheduled task:**
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Uninstall
```

---

## What It Does

- Scans the internet for negative news on US regional banks
- Identifies articles about earnings misses, breaches, regulatory issues, etc.
- Creates a detailed report with headlines, summaries, and source links
- Saves the report as a text file with timestamp
- Runs automatically at 8:00 AM every day

---

## Where to Find Results

Reports are saved in:
```
[Your Work Folder]\MarketMonitor\output\
```

Each report is named: `banking_news_YYYY-MM-DD_HH-MM-SS.txt`
