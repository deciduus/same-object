# check.ps1 - repo verification. Run from the repo root:  powershell -File check.ps1
# Windows PowerShell 5.1 compatible: no '&&', no ternary, no '??'.

$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$vault = Join-Path $root 'vault'
$fail = 0

Write-Host '=== vault lint ==='
Push-Location $vault
python _lint.py
if ($LASTEXITCODE -ne 0) { $fail = 1 }
Pop-Location

Write-Host ''
Write-Host '=== index freshness ==='
python (Join-Path $vault '_idx.py') --check
if ($LASTEXITCODE -ne 0) { $fail = 1 }

Write-Host ''
Write-Host '=== wikilinks ==='
# every [[name]] must resolve to <name>.md somewhere under vault/
# [[name|alias]] and [[name#heading]] resolve on the name part only.
$notes = Get-ChildItem -Path $vault -Filter *.md -Recurse -File | Where-Object {
    $_.FullName -notmatch '\\_templates\\'
}
$stems = @{}
foreach ($n in $notes) { $stems[$n.BaseName] = $true }

$dead = 0
foreach ($n in $notes) {
    $text = Get-Content -LiteralPath $n.FullName -Raw -Encoding UTF8
    if ($null -eq $text) { continue }
    foreach ($m in [regex]::Matches($text, '\[\[([^\]\|#]+)')) {
        $target = $m.Groups[1].Value.Trim()
        if ($target -eq '') { continue }
        if (-not $stems.ContainsKey($target)) {
            $rel = $n.FullName.Substring($root.Length + 1)
            Write-Host ("ERROR  {0}: dead wikilink [[{1}]]" -f $rel, $target)
            $dead = $dead + 1
        }
    }
}
Write-Host ("{0} notes scanned | {1} dead wikilinks" -f $notes.Count, $dead)
if ($dead -gt 0) { $fail = 1 }

Write-Host ''
if ($fail -ne 0) {
    Write-Host 'CHECK FAILED'
} else {
    Write-Host 'CHECK OK'
}
exit $fail
