$checks = @(
    @{ n = "git";      c = "git --version";      r = "Git >= 2.40" },
    @{ n = "php";      c = "php -v";             r = "PHP >= 8.2" },
    @{ n = "composer"; c = "composer --version"; r = "Composer >= 2.7" },
    @{ n = "mysql";    c = "mysql --version";    r = "MySQL >= 8.0" },
    @{ n = "node";     c = "node -v";            r = "Node >= 20" },
    @{ n = "npm";      c = "npm -v";             r = "npm >= 10" },
    @{ n = "python";   c = "python --version";   r = "Python >= 3.11" },
    @{ n = "docker";   c = "docker --version";   r = "Docker >= 24" }
)

Write-Host "=== Kiem chung moi truong CSE703073 ==="
foreach ($k in $checks) {
    $exe = $k.c.Split(" ")[0]
    if (Get-Command $exe -ErrorAction SilentlyContinue) {
        $v = (Invoke-Expression $k.c 2>&1 | Select-Object -First 1)
        Write-Host " [OK]   $($k.n) - $v" -ForegroundColor Green
    } else {
        Write-Host " [THIEU] $($k.n) - Can $($k.r)" -ForegroundColor Yellow
    }
}
Write-Host "=== Ket thuc ==="
