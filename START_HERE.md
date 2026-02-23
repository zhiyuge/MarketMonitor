# Market News Monitoring Tool - START HERE

## Welcome! 👋

This is your **Market News Monitoring Tool** - an automated system that scans the internet for negative news affecting US regional banks every day at 8:00 AM.

---

## ⚡ Quick Start (Choose Your Path)

### Path 1: I Just Want It Working (5 Minutes)

1. Open PowerShell
2. Run these commands:
   ```powershell
   cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
   pip install -r requirements.txt
   PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
   ```
3. **Done!** It runs automatically at 8:00 AM from now on.

**See [QUICKSTART.md](QUICKSTART.md) for the condensed guide.**

---

### Path 2: I Want to Understand Everything

Read the docs in this order:
1. **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - What this tool does and how it works
2. **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)** - Complete setup and troubleshooting
3. **[README.md](README.md)** - Feature details and advanced options

---

### Path 3: I'm Ready to Deploy

See **[DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md)** - Verification checklist and status.

---

## 📁 What's Inside This Folder?

```
MarketMonitor/
├── 📄 START_HERE.md                    ← You are here
│
├── 🚀 GETTING STARTED (Pick One)
│   ├── QUICKSTART.md                   (5-minute guide)
│   ├── INSTALLATION_GUIDE.md            (Detailed setup)
│   └── DEPLOYMENT_SUMMARY.md            (Status & checklist)
│
├── 📚 DOCUMENTATION
│   ├── README.md                        (Full documentation)
│   └── PROJECT_OVERVIEW.md              (Technical details)
│
├── 💻 APPLICATION FILES
│   ├── market_news_monitor.py           (Main tool)
│   ├── setup_scheduler.ps1              (Automatic scheduling)
│   ├── run_monitor.bat                  (Windows batch runner)
│   └── config.ini                       (Configuration)
│
├── 📦 SETUP
│   └── requirements.txt                 (Python packages needed)
│
└── 📊 OUTPUT
    └── output/                          (Daily reports saved here)
        └── banking_news_YYYY-MM-DD_HH-MM-SS.txt
```

---

## 🎯 What This Tool Does

✓ **Scans the Internet** - Multiple news sources (Google, Bing, optional NewsAPI)

✓ **Finds Negative Banking News** - Articles about:
- Rating downgrades
- Earnings misses
- Cybersecurity breaches
- Regulatory enforcement
- Deposit outflows
- Capital concerns
- And 50+ other adverse developments

✓ **Generates Daily Reports** - With headlines, summaries, and links

✓ **Runs Automatically** - Every day at 8:00 AM

✓ **Saves Everything** - To `output/` folder with timestamps

---

## 🔧 Installation (5 Minutes)

### Prerequisites
- Python 3.7+ (download from python.org if needed)
- Windows 10 or later
- Internet connection

### Step 1: Install Dependencies
```powershell
cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
pip install -r requirements.txt
```

### Step 2: Create Scheduled Task
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
```

### Step 3: Verify It Works
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

Done! 🎉

---

## 📊 Check Your Results

**Reports are saved to:**
```
C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output\
```

**To view the latest report:**
```powershell
$latestReport = Get-ChildItem "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Start-Process $latestReport.FullName
```

**File format:** `banking_news_2026-01-27_08-00-15.txt`

---

## ❓ Common Questions

### Q: How do I run it right now instead of waiting for 8 AM?
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

### Q: How do I change the schedule time from 8 AM?
1. Open Task Scheduler (`taskschd.msc`)
2. Find "MarketNewsMonitor"
3. Right-click → Properties
4. Edit the Trigger time

### Q: What banks does it monitor?
JPMorgan Chase, Bank of America, Wells Fargo, Goldman Sachs, Morgan Stanley, Truist, PNC, USB, and more. Edit `market_news_monitor.py` to customize.

### Q: What if something doesn't work?
→ See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md#troubleshooting) for detailed troubleshooting.

### Q: Can I use this without Task Scheduler?
Yes! Just run it manually anytime:
```powershell
python market_news_monitor.py
```

### Q: Where are the reports saved?
```
C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output\
```

---

## 📖 Documentation Files

| File | Purpose | Time |
|------|---------|------|
| **QUICKSTART.md** | Fast 5-minute setup | 5 min |
| **INSTALLATION_GUIDE.md** | Detailed setup + troubleshooting | 15 min |
| **README.md** | Complete feature documentation | 20 min |
| **PROJECT_OVERVIEW.md** | Technical architecture & specs | 15 min |
| **DEPLOYMENT_SUMMARY.md** | Status & verification checklist | 5 min |

---

## 🛠️ Useful Commands

**Run tool now:**
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
```

**View scheduled task:**
```powershell
Get-ScheduledTask -TaskName "MarketNewsMonitor"
```

**List all reports:**
```powershell
Get-ChildItem "C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output" | Sort-Object LastWriteTime -Descending
```

**Uninstall scheduler:**
```powershell
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Uninstall
```

**Run directly without scheduler:**
```powershell
cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
python market_news_monitor.py
```

---

## ✅ Status

**Project Status:** ✓ COMPLETE AND READY TO USE

- ✓ Application built and tested
- ✓ Task scheduling configured
- ✓ Documentation completed
- ✓ Sample reports generated
- ✓ All systems operational

---

## 🚀 Next Steps

### Right Now (5 min):
1. Run the installation commands above
2. Verify with the test command
3. Check output folder for first report

### Tomorrow Morning:
- Check if report was generated at 8:00 AM
- Open and review the report

### Ongoing:
- Reports automatically generate daily
- No action needed from you
- Optional: Archive old reports monthly

---

## 📞 Need Help?

**Check the right documentation:**

- **"How do I install it?"** → [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)
- **"How does it work?"** → [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
- **"What features does it have?"** → [README.md](README.md)
- **"Something's broken"** → [INSTALLATION_GUIDE.md#troubleshooting](INSTALLATION_GUIDE.md#troubleshooting)
- **"Is it working?"** → [DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md)

---

## 📋 File Inventory

| File | Size | Purpose |
|------|------|---------|
| `market_news_monitor.py` | 14.6 KB | Main application |
| `setup_scheduler.ps1` | 5.1 KB | Task scheduling |
| `requirements.txt` | <1 KB | Python dependencies |
| `config.ini` | 2.6 KB | Configuration |
| `README.md` | 8.1 KB | Features & config |
| `QUICKSTART.md` | 1.6 KB | Quick setup |
| `INSTALLATION_GUIDE.md` | 9.4 KB | Detailed guide |
| `PROJECT_OVERVIEW.md` | 12.6 KB | Architecture |
| `DEPLOYMENT_SUMMARY.md` | 11.0 KB | Status & checklist |
| `run_monitor.bat` | 0.5 KB | Batch runner |

---

## 🎓 Learning Path

**New to this? Read in order:**

1. **This file (START_HERE.md)** - Overview and quick start
2. **QUICKSTART.md** - 5-minute install
3. **PROJECT_OVERVIEW.md** - How it works
4. **README.md** - All features
5. **INSTALLATION_GUIDE.md** - Troubleshooting reference

**Experienced? Jump to:**
- **DEPLOYMENT_SUMMARY.md** - Status check
- **config.ini** - Customization
- **market_news_monitor.py** - Code review

---

## 🎉 Ready to Begin?

**Fastest path to success:**

```powershell
# 1. Install dependencies (1 minute)
cd C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor
pip install -r requirements.txt

# 2. Create scheduler (1 minute)
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install

# 3. Test it (1 minute)
PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run

# 4. Check results
# Open: C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output
```

**Total time: 5 minutes**

---

## ⚡ Key Features at a Glance

| Feature | Status |
|---------|--------|
| Automated daily execution | ✓ Active |
| Multi-source news aggregation | ✓ Enabled |
| Negative banking news detection | ✓ 40+ keywords |
| Headlines and summaries | ✓ Included |
| Source attribution | ✓ Included |
| Direct article links | ✓ Included |
| Daily timestamped reports | ✓ Enabled |
| Organized output folder | ✓ C:\Users\zhiyu\Documents\Innovation\Programming\VSCodeProjects\MarketMonitor\output |
| Customizable banks | ✓ 16+ available |
| Customizable keywords | ✓ Fully editable |
| No API keys required | ✓ Works with free sources |
| Easy installation | ✓ 2 commands |

---

## 📞 Contact

For issues beyond basic troubleshooting, refer to the detailed documentation files included in this folder.

---

**Welcome to the Market News Monitoring Tool!** 

Start with the installation command above and you'll have daily banking sector monitoring in 5 minutes.

🚀 **Let's get started!**
