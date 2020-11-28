# home_nextcloud
docker-compose nextcloud

testTG - testing your TG bot

moniy.py - monitor hdd and send alarm in TG

expt.py - send alarm if TG bot was not ready, when will it be available.

allow big upload file:

correct .htaccess:

<IfModule mod_php7.c>

  php_value upload_max_filesize 16G
  
  php_value post_max_size 16G
  
  php_value max_input_time 3600
  
  php_value max_execution_time 3600
  
<IfModule>

CRONTAB 

*/5 * * * * /usr/bin/docker exec -u www-data $(docker ps -f ancestor=nextcloud -q) php cron.php #Use system cron service to call the cron.php file every 5 minutes. 

0 9-21 * * * <your_path>/monit.py # monitor state

*/20 9-21 * * * <your_path>/expt.py # double monitor state


