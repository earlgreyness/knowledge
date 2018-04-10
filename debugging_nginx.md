If you see error

    2018/04/09 12:42:22 [emerg] 27914#27914: bind() to 0.0.0.0:80 failed (98: Address already in use)

try this:

    https://stackoverflow.com/questions/14972792/nginx-nginx-emerg-bind-to-80-failed-98-address-already-in-use/15101745

    https://chrisjean.com/fix-nginx-emerg-bind-to-80-failed-98-address-already-in-use/


Command to see what ports are used:

    netstat -tulpn | grep 80

kill everything on port 80:

    fuser -k 80/tcp


