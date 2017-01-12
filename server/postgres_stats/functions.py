from django.db.models import Aggregate, Func


class DateTrunc(Func):
    """
    Accepts a single timestamp field or expression and returns that timestamp
    truncated to the specified *precision*. This is useful for investigating
    time series.

    The *precision* named parameter can take:

    * microseconds
    * milliseconds
    * second
    * minute
    * hour
    * day
    * week
    * month
    * quarter
    * year
    * decade
    * century
    * millennium

    Usage example::

        checkin = Checkin.objects.
            annotate(day=DateTrunc('logged_at', 'day'),
                     hour=DateTrunc('logged_at', 'hour')).
            get(pk=1)

        assert checkin.logged_at == datetime(2015, 11, 1, 10, 45, 0)
        assert checkin.day == datetime(2015, 11, 1, 0, 0, 0)
        assert checkin.hour == datetime(2015, 11, 1, 10, 0, 0)
    """

    function = "DATE_TRUNC"
    template = "%(function)s('%(precision)s', %(expressions)s)"

    def __init__(self, expression, precision, **extra):
        super().__init__(expression, precision=precision, **extra)


class Extract(Func):
    """
    Accepts a single timestamp or interval field or expression and returns
    the specified *subfield* of that expression. This is useful for grouping
    data.

    The *subfield* named parameter can take:

    * century
    * day
    * decade
    * dow (day of week)
    * doy (day of year)
    * epoch (seconds since 1970-01-01 00:00:00 UTC)
    * hour
    * isodow
    * isodoy
    * isoyear
    * microseconds
    * millennium
    * milliseconds
    * minute
    * month
    * quarter
    * second
    * timezone
    * timezone_hour
    * timezone_minute
    * week
    * year

    See `the Postgres documentation`_ for details about the subfields.

    Usage example::

        checkin = Checkin.objects.
            annotate(day=Extract('logged_at', 'day'),
                     minute=Extract('logged_at', 'minute'),
                     quarter=Extract('logged_at', 'quarter')).
            get(pk=1)

        assert checkin.logged_at == datetime(2015, 11, 1, 10, 45, 0)
        assert checkin.day == 1
        assert checkin.minute == 45
        assert checkin.quarter == 4

    .. _the Postgres documentation: http://www.postgresql.org/docs/current/static/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT

    """
    function = 'EXTRACT'
    name = 'extract'
    template = "%(function)s(%(subfield)s FROM %(expressions)s)"

    def __init__(self, expression, subfield, **extra):
        super().__init__(expression, subfield=subfield, **extra)


