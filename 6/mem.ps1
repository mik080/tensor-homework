$mem=((Get-WmiObject win32_operatingsystem).TotalVisibleMemorySize-(Get-WmiObject win32_operatingsystem).FreePhysicalMemory) * 1000

$DateTime = Get-Date #or any other command to get DateTime object
$meas_time=([DateTimeOffset]$DateTime).ToUnixTimeMilliseconds()
$meas_time=$meas_time*1000000
$mem_meas="memory_ps,host=$env:computername,contur=prod memory_used=$mem $meas_time"
Write-Output $mem_meas
