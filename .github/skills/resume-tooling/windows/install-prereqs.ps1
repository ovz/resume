$ErrorActionPreference = 'Stop'

function Ensure-Command($name) {
    if (-not (Get-Command $name -ErrorAction SilentlyContinue)) {
        return $false
    }
    return $true
}

Write-Host 'Checking Windows package managers...'
if (Get-Command winget -ErrorAction SilentlyContinue) {
    Write-Host 'Using winget for package installation.'
    winget install --id Git.Git -e
    winget install --id JohnMacFarlane.Pandoc -e
    winget install --id MatthewJ.Contour -e
    exit 0
}

if (Get-Command choco -ErrorAction SilentlyContinue) {
    Write-Host 'Using Chocolatey for package installation.'
    choco install git -y
    choco install pandoc -y
    choco install texlive -y
    exit 0
}

Write-Host 'No supported Windows package manager is available.'
Write-Host 'Follow the manual downloads in .github/skills/resume-tooling/manual-downloads.md' -ForegroundColor Yellow
exit 1
