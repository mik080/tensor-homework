$cpu_ut=(Get-WmiObject win32_processor).LoadPercentage

$meas_time=[Math]::Round([decimal]((New-TimeSpan -Start (Get-Date "01/01/1970") -End (Get-Date)).TotalMilliseconds))




$DateTime = Get-Date #or any other command to get DateTime object
$meas_time=([DateTimeOffset]$DateTime).ToUnixTimeMilliseconds()
$meas_time=$meas_time*1000000

$cpu_meas="cpu_ut_ps,host=$env:computername,contur=prod cpu_util=$cpu_ut $meas_time"
Write-Output $cpu_meas



