# yacy-graphite
Send YaCy metrics to Graphite

# Requirements:
python2.7+

# Usage:
1. Modify the config section of `yacy-graphite.py` to meet your needs
2. Schedule cron job or SystemD task to run this script at your desired interval
  - Example `yacy-graphite.timer` and `yacy-graphite.service` files are included to run every 10 seconds
