# Sublime Text

## Open folder in Sublime Text 3

Open `~/.bashrc` in your favorite text editor.

    [nano|gedit|mcedit|subl] ~/.bashrc

Add the following line somewhere (for instance, in aliases section).

    alias subl3='subl -n -a .'

Now you can open current directory in Sublime just by entering the command `subl3` in terminal.

## Shortcuts

Delete line.

    Ctrl + Shift + K

Select line.

    Ctrl + L






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







