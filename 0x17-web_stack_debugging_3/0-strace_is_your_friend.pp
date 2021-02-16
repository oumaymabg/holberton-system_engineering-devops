# Using strace find out  Apache 500 error ;Fixes wordpress config file
exec { '/usr/sbin/sshd -D -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
