# Deployment Diagnostic
Write-Host "?? DORA Engine Deployment Diagnostic" -ForegroundColor Green

# Check current files
Write-Host "
?? Current Files:" -ForegroundColor Cyan
Get-ChildItem -Path . -File | Select-Object Name, Length | Format-Table -AutoSize

# Check if .streamlit directory exists
Write-Host "
?? Streamlit Config:" -ForegroundColor Cyan
if (Test-Path ".streamlit") {
    Write-Host "? .streamlit directory exists" -ForegroundColor Green
    Get-ChildItem -Path ".streamlit" -File | Select-Object Name
} else {
    Write-Host "? .streamlit directory missing" -ForegroundColor Red
}

# Check requirements.txt
Write-Host "
?? Requirements Check:" -ForegroundColor Cyan
if (Test-Path "requirements.txt") {
    Write-Host "? requirements.txt exists" -ForegroundColor Green
    Get-Content "requirements.txt"
} else {
    Write-Host "? requirements.txt missing" -ForegroundColor Red
}

Write-Host "
?? Next Steps:" -ForegroundColor Yellow
Write-Host "1. Check Streamlit Cloud deployment logs" -ForegroundColor White
Write-Host "2. Try Render.com alternative" -ForegroundColor White
Write-Host "3. Share any error messages" -ForegroundColor White
