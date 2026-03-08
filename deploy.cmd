@echo off
"C:\Program Files\Git\cmd\git.exe" config --global user.name "Harshal"
"C:\Program Files\Git\cmd\git.exe" config --global user.email "harshal959@users.noreply.github.com"
"C:\Program Files\Git\cmd\git.exe" init
"C:\Program Files\Git\cmd\git.exe" add .
"C:\Program Files\Git\cmd\git.exe" commit -m "Initialize project and Vercel/Firebase configuration"
"C:\Program Files\Git\cmd\git.exe" branch -M main
"C:\Program Files\Git\cmd\git.exe" remote add origin https://github.com/harshal959/price_comparison-system.git
"C:\Program Files\Git\cmd\git.exe" push -u origin main
