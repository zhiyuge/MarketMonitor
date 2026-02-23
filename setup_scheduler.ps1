# Market News Monitor - Setup and Execution Script
# This script sets up the Windows Task Scheduler to run the monitoring tool daily at 8am

param(
    [switch]$Install,
    [switch]$Uninstall,
    [switch]$Run,
    [switch]$Help
)

$ProjectDir = "[Your Work Folder]\MarketMonitor"
$TaskName = "MarketNewsMonitor"
$TaskDescription = "Daily US Regional Banking Sector Negative News Monitoring"
$ScriptPath = Join-Path $ProjectDir "market_news_monitor.py"
$OutputDir = Join-Path $ProjectDir "output"

function Show-Help {
    Write-Host @"
Market News Monitor - Scheduler Setup

Usage: PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 [options]

Options:
  -Install    Create a scheduled task to run at 8am daily
  -Uninstall  Remove the scheduled task
  -Run        Execute the monitoring script immediately
  -Help       Show this help message

Examples:
  # Install daily 8am task
  PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Install
  
  # Run immediately
  PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Run
  
  # Uninstall task
  PowerShell -ExecutionPolicy Bypass -File setup_scheduler.ps1 -Uninstall
"@
}

function Install-ScheduledTask {
    Write-Host "Installing Market News Monitor scheduled task..."
    
    # Check if task already exists
    $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($task) {
        Write-Host "Task already exists. Removing and recreating..."
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    }
    
    # Create trigger for 8am daily
    $trigger = New-ScheduledTaskTrigger -Daily -At 8am
    
    # Create action to run Python script
    $action = New-ScheduledTaskAction `
        -Execute "python.exe" `
        -Argument "`"$ScriptPath`"" `
        -WorkingDirectory $ProjectDir
    
    # Create task settings
    $settings = New-ScheduledTaskSettingsSet `
        -AllowStartIfOnBatteries `
        -DontStopIfGoingOnBatteries `
        -StartWhenAvailable
    
    # Register the task
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -RunLevel Highest
    
    Register-ScheduledTask `
        -TaskName $TaskName `
        -Description $TaskDescription `
        -Trigger $trigger `
        -Action $action `
        -Settings $settings `
        -Principal $principal `
        -Force
    
    Write-Host "✓ Scheduled task created successfully!"
    Write-Host "  Task Name: $TaskName"
    Write-Host "  Schedule: Daily at 8:00 AM"
    Write-Host "  Output Location: $OutputDir"
    Write-Host ""
    Write-Host "To view the task in Task Scheduler:"
    Write-Host "  Open Task Scheduler and navigate to: Task Scheduler Library"
    Write-Host ""
}

function Uninstall-ScheduledTask {
    Write-Host "Uninstalling Market News Monitor scheduled task..."
    
    $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($task) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Host "✓ Scheduled task removed successfully!"
    } else {
        Write-Host "Task not found. Nothing to uninstall."
    }
}

function Run-Monitor {
    Write-Host "Running Market News Monitor..."
    Write-Host "Project Directory: $ProjectDir"
    Write-Host "Output Directory: $OutputDir"
    Write-Host ""
    
    # Check if output directory exists
    if (-not (Test-Path $OutputDir)) {
        New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
        Write-Host "Created output directory: $OutputDir"
    }
    
    # Run the Python script
    try {
        Set-Location $ProjectDir
        python market_news_monitor.py
        Write-Host ""
        Write-Host "✓ Monitoring complete. Check the output folder for results."
    } catch {
        Write-Host "Error running monitor: $_"
        exit 1
    }
}

function Check-Prerequisites {
    Write-Host "Checking prerequisites..."
    
    # Check Python installation
    try {
        $pythonVersion = python --version 2>&1
        Write-Host "✓ Python found: $pythonVersion"
    } catch {
        Write-Host "✗ Python not found. Please install Python 3.7 or later."
        exit 1
    }
    
    # Check if project directory exists
    if (Test-Path $ProjectDir) {
        Write-Host "✓ Project directory exists: $ProjectDir"
    } else {
        Write-Host "✗ Project directory not found: $ProjectDir"
        exit 1
    }
    
    # Check requirements
    if (Test-Path (Join-Path $ProjectDir "requirements.txt")) {
        Write-Host "✓ requirements.txt found"
        Write-Host "  Installing dependencies..."
        pip install -r (Join-Path $ProjectDir "requirements.txt") | Out-Null
        Write-Host "  Dependencies installed"
    }
    
    Write-Host ""
}

# Main execution
if ($Help -or ($PSBoundParameters.Count -eq 0)) {
    Show-Help
} elseif ($Install) {
    Check-Prerequisites
    Install-ScheduledTask
} elseif ($Uninstall) {
    Uninstall-ScheduledTask
} elseif ($Run) {
    Check-Prerequisites
    Run-Monitor
} else {
    Show-Help
}
