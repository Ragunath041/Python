from collections import OrderedDict

def hit_rate(C, page_requests):
    cache = OrderedDict()
    req, hit = 0, 0
    for i in page_requests:
        req += 1
        if i in cache:
            hit += 1
            cache.move_to_end(i)
        else:
            if len(cache) == C:
                cache.popitem(last=False)
            cache[i] = None
    z = (hit / req) * 100
    return round(z)

print(hit_rate(3, [1,2,1,3,4,2]))