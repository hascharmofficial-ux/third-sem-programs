# Repository Automation & Sync Guidelines

When the user says **upload** (or asks to sync/upload newly created/modified programs), follow this exact workflow:

## Step 1: Read the Last Sync Timestamp
- Check `D:\Programs\last_sync_time.txt`.
- If the file exists, read and parse the timestamp (format: `yyyy-MM-dd HH:mm:ss`). If it does not exist, use `[datetime]::MinValue`.

## Step 2: Identify New or Modified Programs
- Run PowerShell to find programs in `D:\Python` modified after the timestamp:
  ```powershell
  $lastSync = if (Test-Path "D:\Programs\last_sync_time.txt") { [datetime](Get-Content "D:\Programs\last_sync_time.txt").Trim() } else { [datetime]::MinValue }
  Get-ChildItem -Path "D:\Python" -Recurse -File -Include *.py | Where-Object { $_.LastWriteTime -gt $lastSync } | Select-Object FullName, Name, Directory
  ```
- If no files are returned, inform the user that everything is up to date and end turn.

## Step 3: Generate Documentation (Folder README Updates)
- For each new or modified program:
  - Read its source code using `view_file`.
  - Analyze the logic.
  - Formulate a 1-line description formatted as: `*ProgramName* : A short, descriptive summary of what the program does.`
  - Append this line to `D:\Programs\Python\README.md` (or update existing entry).

## Step 4: Copy Files to the Git Repository
- Copy modified/new programs to `D:\Programs\Python\`:
  ```powershell
  Copy-Item -Path $file.FullName -Destination "D:\Programs\Python\" -Force
  ```
- Do NOT delete any existing files from `D:\Programs`.

## Step 5: Update Total Program Counts (Root README)
- Dynamically count total programs:
  ```powershell
  (Get-ChildItem -Path "D:\Programs\Python" -File -Include *.py -Recurse).Count
  ```
- Update the table in `D:\Programs\README.md` to reflect the updated count.

## Step 6: Commit and Push to GitHub
- Navigate to `D:\Programs` and push:
  ```powershell
  git add .
  git commit -m "Auto-sync: Uploaded new programs and updated READMEs"
  git push origin main
  ```

## Step 7: Update Timestamp Tracker
- Record current timestamp in `last_sync_time.txt`:
  ```powershell
  Get-Date -Format "yyyy-MM-dd HH:mm:ss" | Out-File -FilePath "D:\Programs\last_sync_time.txt" -Encoding utf8
  ```
