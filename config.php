<?php
$CONFIG = array (
  'htaccess.RewriteBase' => '/',
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'memcache.locking' => '\\OC\\Memcache\\Redis',
  'redis' => 
  array (
    'host' => 'next_redis_1',
    'port' => 6379,
  ),
  'apps_paths' => 
  array (
    0 => 
    array (
      'path' => '/var/www/html/apps',
      'url' => '/apps',
      'writable' => false,
    ),
    1 => 
    array (
      'path' => '/var/www/html/custom_apps',
      'url' => '/custom_apps',
      'writable' => true,
    ),
  ),
  'instanceid' => 'ocxlit4gzeyt',
  'passwordsalt' => 'AcNx7OZAbn05JfB9jgiTOui6Jjq7f2',
  'secret' => 'xujmCf6shneERA6glF24zL5Es6WFnEBv8sOt/iX4+v+iJeF+',
  'trusted_domains' => 
  array (
    0 => <your_trust_domen>,
  ),
  'datadirectory' => '/var/www/html/data',
  'dbtype' => 'mysql',
  'version' => '20.0.2.2',
  'overwrite.cli.url' => 'http://192.168.0.26',
  'dbname' => 'nextcloud',
  'dbhost' => 'next_db_1:3306',
  'dbport' => '',
  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'nextcloud',
  'dbpassword' => 'nextcloud',
  'installed' => true,
  'loglevel' => 0,
  'maintenance' => false,
);
