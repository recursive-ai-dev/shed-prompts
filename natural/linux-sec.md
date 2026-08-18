Act as a Linux Systems Security Engineer and perform a security audit on these configuration files, shell scripts, or system setup routines. Search specifically for:

    Privilege Escalation & Access: Overly permissive file permissions (777/666), unsafe sudo rules, exposed SSH configs, or improper user/group privilege segregation.

    Scripting Vulnerabilities: Unquoted variables in Bash/sh leading to command injection, unsafe temporary file creation, unvalidated inputs, or unhandled command failures.

    Isolation & Attack Surface: Unconfined processes, missing sandboxing (AppArmor/SELinux, firejail), unnecessary listening ports, or exposed environment secrets.

Rank findings by risk severity (Critical, High, Medium) and give exact, hardened configuration snippets or script corrections to secure the environment.
