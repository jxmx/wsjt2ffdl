# WSJT2FFDL
This utility listens for multicasted QSO log events from WSJT-X
and publishes them to the [Firefly Field Day Logger](https://github.com/jxmx/ffdl).
This requires WSJT-X to be configured to send to a multicast IP
as described in the "WSJT-X" section of
[this support note from HRD](https://support.hamradiodeluxe.com/support/solutions/articles/51000298966-setup-configuration-hrd-alert-multicasting).
Ignore the part about HRD configuration.

## Installation
This is as simple as installing the package. The application will
automatically start and will listen on the default multicast group
224.0.0.1 port 2237.

## Configuration
For non-standard configurations, the file `/etc/default/wsjt2ffdl`
may be customized as described within the file.

## Logging
Logs go to systemctl journal and/or syslog (if syslog is installed). 
Logging can be reviewed with the command `journalctl -u wsjt2ffdl`.
Note that the logging will also note any QSOs that are not
able to be stored with FFDL (usually due to dups). There is no way
to feed duplicate QSO alerts back to the user of WSJT-X. Duplicate
QSOs will be ignored by FFDL.

## Troubleshooting
There isn't a lot to troubleshoot aside from configuration.
Starting `wsjt2ffdl` with the `--debug` option can be illuminating
but also noisy. For any issue, please include logging output or 
I will simply be asking you to add it as my first response.
