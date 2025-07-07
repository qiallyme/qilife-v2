# setup_env.ps1 - PowerShell script to initialize environment, clean __init__.py, and install requirements

<#
  Usage:
    1. Place this file in the root of your project (qilife-main).
    2. In PowerShell:
       Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
       .\setup_env.ps1
#>

# Navigate to project root
Set-Location -Path $PSScriptRoot

# Remove old __init__.py files under src
Get-ChildItem -Path ".\src" -Recurse -Filter "__init__.py" | ForEach-Object {
    Write-Host "Removing old init:" $_.FullName
    Remove-Item $_.FullName -Force
}

# Recreate __init__.py in each folder under src
Get-ChildItem -Path ".\src" -Recurse -Directory | ForEach-Object {
    $initFile = Join-Path $_.FullName "__init__.py"
    if (!(Test-Path $initFile)) {
        Write-Host "Creating init:" $initFile
        New-Item -Path $initFile -ItemType File -Force | Out-Null
    }
}

# Create virtual environment if it doesn't exist
$venvPath = Join-Path $PSScriptRoot ".venv"
if (!(Test-Path $venvPath)) {
    Write-Host "Creating virtual environment at $venvPath..."
    python -m venv .venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
& "$venvPath\\Scripts\\Activate.ps1"

# Upgrade pip
Write-Host "Upgrading pip..."
pip install --upgrade pip

# Install requirements
Write-Host "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

Write-Host "✅ Environment setup complete."