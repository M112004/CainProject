<#
.SYNOPSIS
    Refreshes the AST and Document Knowledge Graph for CAIN using Graphify and updates the Obsidian vault.
.DESCRIPTION
    Scans the CAIN knowledge base and rules, extracts semantic nodes and wikilinks,
    updates graphify-out/graph.json, GRAPH_REPORT.md, graph.html, and exports the Obsidian vault.
#>

$projectRoot = $PSScriptRoot
Set-Location $projectRoot

Write-Host "Refreshing Knowledge Graph and Obsidian Vault for CAIN Project..." -ForegroundColor Cyan

$sourceFiles = Get-ChildItem -Path (Join-Path $projectRoot "knowledge"), (Join-Path $projectRoot "Pecados"), (Join-Path $projectRoot "Exorcistas") -Recurse -File -Include *.md,*.json,*.py -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch '[\\/](graphify-out|node_modules)[\\/]' }

if (-not $sourceFiles -or $sourceFiles.Count -eq 0) {
    Write-Host "No knowledge or sin files found in $projectRoot." -ForegroundColor Yellow
    exit 0
}

Write-Host "Extracting graph nodes across $($sourceFiles.Count) files..." -ForegroundColor Gray
graphify extract . --allow-partial

if ($LASTEXITCODE -ne 0) {
    Write-Host "Graphify extraction encountered an issue (exit code $LASTEXITCODE)." -ForegroundColor Yellow
}

Write-Host "Clustering and labeling communities..." -ForegroundColor Gray
graphify cluster-only .

Write-Host "Exporting updated Obsidian vault..." -ForegroundColor Gray
graphify export obsidian

if ($LASTEXITCODE -eq 0) {
    Write-Host "Knowledge graph and Obsidian vault successfully updated in graphify-out/" -ForegroundColor Green
    Write-Host "Obsidian vault path: graphify-out/obsidian/" -ForegroundColor Green
} else {
    Write-Host "Graphify finished with exit code $LASTEXITCODE." -ForegroundColor Yellow
}
