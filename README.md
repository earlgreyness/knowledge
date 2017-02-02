# SSH without password.

    cd ~
    ssh-keygen -t rsa
    ssh root@jurist-rus.ru mkdir -p .ssh
    cat .ssh/id_rsa.pub | ssh root@jurist-rus.ru 'cat >> .ssh/authorized_keys'
    ls ~

Issue the command `ls ~/.ssh` and study contained files.

    ~/.ssh/id_rsa
    ~/.ssh/id_rsa.pub
    ~/.ssh/known_hosts


# MySQL

MySQL Database management software: https://www.adminer.org.


# Git

Create new branch and switch to it immediately:

    git checkout -b BRANCH_NAME

The first time pushing that branch:

    git push [-u|--set-upstream] origin BRANCH_NAME

Resets the index and working tree. Any changes to tracked files in the working tree since <commit> are discarded.

    git reset --hard HEAD

# Django

This is equivalent to `GROUP BY` in raw SQL.

```python
AggregatedOrders.objects
                .filter(date__in=dates, restaurant_id=restaurant_id)
                .values('date')
                .annotate(count=Sum(F('count_total') - F('count_deleted')))
                .order_by('count')
```

# Tools

* Genymotion (https://www.genimotion.com) for testing Android on desktop.

Genymotion requires Oracle VirtualBox (https://www.virtualbox.org/wiki/Linux_Downloads)

After that we can run `*.apk` files on it -- like Apps from Google Market

My account on genimotion: `earlgreyness`.
