if [ -z "`ps -Af | grep conky | grep -v grep | grep -v auto`" ]; then
sudo blueman-applet | \
sudo wicd-client | \
volumeicon | \
conky | \
sudo cpufreq-set -g powersave | \
xset m 1/50 1/50
fi
