When you see errors like these:

    4294:C 03 Apr 16:58:16.114 * RDB: 221 MB of memory used by copy-on-write
    944:M 03 Apr 16:58:16.213 * Background saving terminated with success
    944:M 03 Apr 17:03:17.024 * 10 changes in 300 seconds. Saving...
    944:M 03 Apr 17:03:17.024 # Can't save in background: fork: Cannot allocate memory
    944:M 03 Apr 17:03:23.037 * 10 changes in 300 seconds. Saving...
    944:M 03 Apr 17:03:23.037 # Can't save in background: fork: Cannot allocate memory
    944:M 03 Apr 17:03:29.048 * 10 changes in 300 seconds. Saving...
    944:M 03 Apr 17:03:29.048 # Can't save in background: fork: Cannot allocate memory
    944:M 03 Apr 17:03:35.061 * 10 changes in 300 seconds. Saving...


Do this:

Modify /etc/sysctl.conf and add

    vm.overcommit_memory=1

Then restart sysctl by:

    $ sudo sysctl -p /etc/sysctl.conf


Reason (from Redis FAQ):

Redis background saving schema relies on the copy-on-write semantic of fork in modern operating systems: Redis forks (creates a child process) that is an exact copy of the parent. The child process dumps the DB on disk and finally exits. In theory the child should use as much memory as the parent being a copy, but actually thanks to the copy-on-write semantic implemented by most modern operating systems the parent and child process will share the common memory pages. A page will be duplicated only when it changes in the child or in the parent. Since in theory all the pages may change while the child process is saving, Linux can't tell in advance how much memory the child will take, so if the overcommit_memory setting is set to zero fork will fail unless there is as much free RAM as required to really duplicate all the parent memory pages, with the result that if you have a Redis dataset of 3 GB and just 2 GB of free memory it will fail.
Setting overcommit_memory to 1 says Linux to relax and perform the fork in a more optimistic allocation fashion, and this is indeed what you want for Redis.
