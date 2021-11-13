﻿param(  
    [string]$TargetFolder="C:/Windows/System32/drivers/",
    [string]$ResultFile="baseline.txt"
)


Get-ChildItem $TargetFolder | Get-FileHash | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders | Out-File $ResultFile -Encoding ascii

