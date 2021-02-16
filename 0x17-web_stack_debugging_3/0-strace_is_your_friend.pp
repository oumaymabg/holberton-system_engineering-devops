# Using strace find out  Apache 500 error ;Fixes wordpress config file
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
