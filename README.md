# Market News Monitoring Tool - Documentation

## Overview

This is a comprehensive market news monitoring tool designed to automatically scan the internet for negative news on the US regional banking sector. The tool runs daily at 8:00 AM and generates detailed reports with headlines, summaries, and source links.

## Features

- **Automated Daily Monitoring**: Runs automatically at 8:00 AM each day
- **Multiple News Sources**: Aggregates news from NewsAPI, Bing News, and Google News
- **Comprehensive Filtering**: Identifies negative news covering:
  - Rating downgrades and negative outlook revisions
  - Earnings shortfalls and guidance cuts
  - Cybersecurity breaches and data leaks
  - Credit spread widening
  - Financial losses and impairments
  - Liquidity stress and deposit outflows
  - Regulatory enforcement actions and consent orders
  - Capital adequacy concerns
  - Rising non-performing loans (NPLs)
  - Commercial real estate exposure
  - Funding cost pressures
  - Failed capital raises
  - Management turnover
  - Operational disruptions
  - Market confidence shocks
  - And many other adverse developments

- **Detailed Reports**: Generates timestamped reports with:
  - Article headlines
  - Brief summaries
  - Source attribution
  - Publication dates
  - Direct links to original articles

- **Organized Storage**: Saves reports to designated output folder with timestamps

## Installation

### Prerequisites

1. **Python**: Version 3.7 or later
   - Download from: https://www.python.org/downloads/
   - Ensure "Add Python to PATH" is checked during installation

2. **Windows PowerShell**: Available on all modern Windows systems

### Setup Steps

1. **Install Dependencies**:
   ```powershell
   cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
   pip install -r requirements.txt
   ```

2. **Create Scheduled Task** (recommended):
   ```powershell
   PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
   ```

   This will create a Windows Task Scheduler task that runs the monitoring tool daily at 8:00 AM.

3. **Verify Installation**:
   ```powershell
   PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
   ```

   This runs the tool immediately to verify everything works correctly.

## Usage

### Run Immediately
To run the monitoring tool right away instead of waiting for the scheduled 8:00 AM execution:

```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

Or directly:
```powershell
cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
python market_news_monitor.py
```

### View Scheduled Task
To see the scheduled task in Windows Task Scheduler:

1. Press `Windows Key + R`
2. Type `taskschd.msc` and press Enter
3. Look for "MarketNewsMonitor" in the task list
4. Double-click to view or modify settings

### Access Reports
Reports are saved to:
```
C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output\
```

File naming format: `banking_news_YYYY-MM-DD_HH-MM-SS.txt`

Example:
```
banking_news_2026-01-27_08-00-15.txt
```

## Configuration

### Modify Bank List
To add or remove banks from monitoring, edit `market_news_monitor.py`:

```python
self.regional_banks = {
    'JPM': 'JPMorgan Chase',
    'BAC': 'Bank of America',
    # Add more banks here
}
```

### Adjust Negative Keywords
To modify the keywords that identify negative news:

```python
self.negative_keywords = [
    'downgrade', 'downgraded',
    # Add or remove keywords here
]
```

### Change Scheduled Time
To change the daily execution time from 8:00 AM:

1. Open Task Scheduler (`taskschd.msc`)
2. Find "MarketNewsMonitor" task
3. Right-click → Properties
4. Go to "Triggers" tab
5. Edit the trigger and change the time

Or uninstall and reinstall with a modified PowerShell script.

## Optional: Add NewsAPI Support

For enhanced news gathering, you can use NewsAPI.org (requires free registration):

1. Register at https://newsapi.org/
2. Get your API key
3. Set environment variable:
   ```powershell
   [Environment]::SetEnvironmentVariable("NEWS_API_KEY", "your-api-key-here", "User")
   ```
4. Restart PowerShell or the system for the variable to take effect

## Troubleshooting

### Task Won't Run at 8:00 AM

1. **Check Task Scheduler**:
   - Open Task Scheduler (`taskschd.msc`)
   - Verify "MarketNewsMonitor" task exists
   - Check the "History" tab for any errors

2. **Python Path Issue**:
   - Open Task Scheduler
   - Edit the task
   - Check that the Action uses the full path to python.exe
   - Example: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe`

3. **Permissions**:
   - The task needs to run with appropriate permissions
   - Re-run the setup script with Administrator privileges

### No News Articles Found

1. Check internet connection
2. News APIs may have rate limits (especially free tiers)
3. Try running manually to test connectivity:
   ```powershell
   PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
   ```

### Output Folder Issues

1. Verify output folder exists:
   ```powershell
   Test-Path "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output"
   ```

2. Check folder permissions - Windows account needs write access

## File Structure

```
MarketMonitor/
├── market_news_monitor.py      # Main monitoring script
├── setup_scheduler.ps1          # Scheduler setup script
├── run_monitor.bat              # Batch script for running
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── execution_log.txt            # Auto-generated execution log
└── output/                      # Output folder for reports
    ├── banking_news_2026-01-27_08-00-15.txt
    ├── banking_news_2026-01-28_08-00-12.txt
    └── ... (more reports)
```

## Output Report Format

Each report contains:

```
================================================================================
MARKET NEWS MONITORING - US REGIONAL BANKING SECTOR
================================================================================
Report Generated: 2026-01-27 08:00:15
Total Negative News Articles Found: 15
================================================================================

[1] JPMorgan Chase Announces Unexpected Earnings Miss in Q4 2025
--------------------------------------------------------------------------------
Source: Bloomberg News
Published: 2026-01-27T07:30:00Z
URL: https://example.com/article-link

Summary:
JPMorgan Chase reported earnings that fell short of analyst expectations...

[2] Wells Fargo Faces Regulatory Enforcement Action...
...
```

## Uninstall

To remove the scheduled task:

```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Uninstall
```

The script files and output folder will remain for manual deletion if desired.

## Advanced: Manual Task Scheduler Setup

If you prefer to set up the scheduled task manually:

1. Open Task Scheduler (`taskschd.msc`)
2. Click "Create Basic Task" in the right panel
3. Enter:
   - **Name**: MarketNewsMonitor
   - **Description**: Daily US Regional Banking Sector Negative News Monitoring
4. Click "Next", select "Daily", click "Next"
5. Set time to 8:00:00 AM, click "Next"
6. Select "Start a program"
7. Set:
   - **Program/script**: python.exe (full path)
   - **Add arguments**: market_news_monitor.py
   - **Start in**: C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
8. Complete the wizard

## Support

For issues or questions:

1. Check the troubleshooting section above
2. Review error messages in Task Scheduler History
3. Run the tool manually to see detailed output:
   ```powershell
   python C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\market_news_monitor.py
   ```

## License

This tool is provided for market analysis and monitoring purposes.
