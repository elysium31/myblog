from math import ceil


class Paginator(object):

    def __init__(self, query, page, per_page):
        self.query = query
        self.page = page
        self.per_page = per_page
        offset = (page - 1) * per_page
        self.count = self.query.order_by(None).count()
        self.items = query.limit(per_page).offset(offset).all()

    @property
    def pages(self):
        return int(ceil(self.count / float(self.per_page)))

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2, right_current=5,
                   right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if (
                num <= left_edge or
                    (
                        num > self.page - left_current - 1 and
                        num < self.page + right_current
                    ) or
                num > self.pages - right_edge
            ):
                if last + 1 != num:
                    yield None
                yield num
                last = num
