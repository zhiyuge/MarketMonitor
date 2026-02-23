# Installation and Execution Guide

## System Requirements

- **Windows 10 or later**
- **Python 3.7+** (installed and added to PATH)
- **Internet connection** (for fetching news articles)
- **Administrator privileges** (for Task Scheduler setup)

## Quick Installation (2 steps)

### Step 1: Install Python Dependencies
```powershell
cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
pip install -r requirements.txt
```

### Step 2: Create Scheduled Task
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
```

That's it! The tool will now run every day at 8:00 AM automatically.

---

## Detailed Installation Guide

### 1. Verify Python Installation

```powershell
python --version
```

If you see a version number (3.7 or higher), Python is installed correctly.

If Python is not found:
- Download from https://www.python.org/downloads/
- During installation, **check "Add Python to PATH"**
- Restart your computer

### 2. Install Python Dependencies

Navigate to the project directory and install required packages:

```powershell
cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
pip install -r requirements.txt
```

Expected output:
```
Successfully installed requests-2.31.0 python-dateutil-2.8.2
```

### 3. Set Up Automated Daily Execution

The tool includes a PowerShell script to automatically create a Windows Task Scheduler task:

```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
```

This will:
- ✓ Check Python installation
- ✓ Verify project files exist
- ✓ Create a scheduled task named "MarketNewsMonitor"
- ✓ Configure it to run every day at 8:00 AM
- ✓ Set appropriate permissions

### 4. Test the Installation

Run the tool immediately to verify everything works:

```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

Expected output:
```
Checking prerequisites...
✓ Python found: Python 3.12.7
✓ Project directory exists: C:\Users\zhiyu\Documents\Innovation\...
✓ requirements.txt found
  Installing dependencies...
  Dependencies installed

Running Market News Monitor...
Project Directory: C:\Users\zhiyu\Documents\Innovation\...
Output Directory: C:\Users\zhiyu\Documents\Innovation\...

Starting market news monitoring...
Fetching news articles...
Total articles fetched: 378
Recent articles (last 24h): 378
Negative banking articles: 101
Report saved to: C:\Users\zhiyu\Documents\Innovation\...output\banking_news_2026-01-27_08-00-15.txt
Monitoring complete!

✓ Monitoring complete. Check the output folder for results.
```

### 5. Verify Scheduled Task

To confirm the task was created correctly:

1. **Method 1: Using PowerShell**
   ```powershell
   Get-ScheduledTask -TaskName "MarketNewsMonitor" | Select-Object State, TaskPath
   ```

2. **Method 2: Using Task Scheduler GUI**
   - Press `Windows Key + R`
   - Type `taskschd.msc` and press Enter
   - Look for "MarketNewsMonitor" in the task list
   - Double-click to view details
   - Check the "Triggers" tab - should show "Daily at 8:00 AM"

---

## Daily Operations

### Automatic Execution
Once installed, the tool runs automatically at 8:00 AM every day. No manual action required.

### Manual Execution
To run the tool on-demand (useful for testing):

```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

Or directly:
```powershell
python market_news_monitor.py
```

### Accessing Reports
All reports are saved to:
```
C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output\
```

**File naming format:** `banking_news_YYYY-MM-DD_HH-MM-SS.txt`

**Example reports:**
- `banking_news_2026-01-27_08-00-15.txt`
- `banking_news_2026-01-28_08-00-12.txt`

To open the most recent report:
```powershell
$latestReport = Get-ChildItem "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Start-Process $latestReport.FullName
```

---

## Configuration

### Change Scheduled Time

If you want to change from 8:00 AM to a different time:

**Option 1: Using Task Scheduler GUI**
1. Open Task Scheduler (`taskschd.msc`)
2. Right-click "MarketNewsMonitor"
3. Click "Properties"
4. Go to "Triggers" tab
5. Double-click the trigger
6. Change the time and click OK

**Option 2: Using PowerShell (Uninstall and Reinstall)**
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Uninstall

# Then edit setup_scheduler.ps1 and change the time
# Then reinstall:
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
```

### Modify Banks to Monitor

Edit `market_news_monitor.py` and find the `self.regional_banks` dictionary:

```python
self.regional_banks = {
    'JPM': 'JPMorgan Chase',
    'BAC': 'Bank of America',
    # Add/remove banks here
}
```

### Add Custom Keywords

Edit `market_news_monitor.py` and find the `self.negative_keywords` list:

```python
self.negative_keywords = [
    'downgrade', 'downgraded',
    # Add/remove keywords here
]
```

---

## Troubleshooting

### Task Not Running at 8:00 AM

**Check 1: Verify task exists**
```powershell
Get-ScheduledTask -TaskName "MarketNewsMonitor"
```

**Check 2: View task history**
1. Open Task Scheduler (`taskschd.msc`)
2. Right-click "MarketNewsMonitor"
3. Click "View History"
4. Look for errors in the Event column

**Check 3: Verify Python path**
1. Open Task Scheduler
2. Right-click "MarketNewsMonitor"
3. Click "Properties"
4. Click "Actions" tab
5. Verify the python.exe path is correct

**Check 4: Computer may be sleeping**
- Ensure your computer is not in sleep mode at 8:00 AM
- Or use "Start When Available" feature in Task Scheduler

### No News Articles Found

1. Check your internet connection
2. Try running manually to see detailed output:
   ```powershell
   python C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\market_news_monitor.py
   ```
3. News APIs have rate limits on free tiers
4. Try again after waiting a few minutes

### Python Not Found

If you get "python: The term 'python' is not recognized":

1. Check Python is installed: https://www.python.org/downloads/
2. **During installation, check "Add Python to PATH"**
3. Restart your computer after installation
4. Open a new PowerShell window and try again

### Permission Denied

If you get permission errors:

1. Run PowerShell as Administrator
2. Run the setup script again:
   ```powershell
   PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
   ```

### Output Folder Not Writable

If reports aren't being saved:

1. Check the output folder exists:
   ```powershell
   Test-Path "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output"
   ```

2. If it doesn't exist, create it:
   ```powershell
   mkdir "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output"
   ```

3. Verify permissions on the folder:
   - Right-click folder → Properties
   - Security tab → Edit
   - Select your username
   - Check "Full Control"
   - Click Apply and OK

---

## Maintenance

### Regular Tasks

**Weekly:** Check that output files are being created
```powershell
Get-ChildItem "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output" | Sort-Object LastWriteTime -Descending | Select-Object Name, LastWriteTime
```

**Monthly:** Archive old reports (older than 30 days)
```powershell
$archiveDir = "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output\Archive"
mkdir $archiveDir -Force
Get-ChildItem "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output" -Filter "*.txt" | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-30)} | Move-Item -Destination $archiveDir
```

### Updating Dependencies

To update to the latest versions of dependencies:
```powershell
pip install --upgrade -r requirements.txt
```

### Uninstalling

To completely remove the scheduled task:

```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Uninstall
```

The script files will remain if you want to reinstall later.

---

## Advanced Features

### Email Notifications (Optional Enhancement)

To add email notifications when reports are generated, modify the `generate_report()` function to call an email script.

### Database Integration (Optional Enhancement)

To store results in a database instead of text files, modify the `save_report()` function.

### Slack Integration (Optional Enhancement)

To send Slack notifications with daily summaries, add Slack webhook integration.

---

## Support Resources

- **Python Official Documentation:** https://www.python.org/doc/
- **PowerShell Documentation:** https://docs.microsoft.com/en-us/powershell/
- **Windows Task Scheduler Documentation:** https://docs.microsoft.com/en-us/windows/win32/taskschd/
- **News API Services:**
  - NewsAPI.org: https://newsapi.org/
  - Google News: https://news.google.com/
  - Bing News: https://www.bing.com/news/

---

## Next Steps

1. ✓ Install dependencies
2. ✓ Create scheduled task
3. ✓ Test the tool
4. ✓ Check output reports
5. Monitor daily for negative banking news!
