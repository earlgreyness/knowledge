
# MENUFORYOU

    ssh m4u@taun.menuforyou.ru

    ssh kirill@moff.menuforyou.ru


MySQL Databases on `moff.menuforyou.ru`:

* `data_collector`
* `django`
* `m4u_customer_area`
* `m4ubilling`
* `rmsmanage`



# MySQL

MySQL Database management software: https://www.adminer.org.


# Git

Create new branch and switch to it immediately:

    git checkout -b BRANCH_NAME

The first time pushing that branch:

    git push [-u|--set-upstream] origin BRANCH_NAME

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
