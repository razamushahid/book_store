# import uuid
# import json
# from decimal import Decimal
# from datetime import datetime, timedelta, tzinfo, date, time
#
#
# ZERO = timedelta(0)
#
#
# def is_aware(value):
#     """
#     Determines if a given datetime.datetime is aware.
#
#     The concept is defined in Python's docs:
#     http://docs.python.org/library/datetime.html#datetime.tzinfo
#     Assuming value.tzinfo is either None or a proper datetime.tzinfo,
#     value.utcoffset() implements the appropriate logic.
#     """
#     return value.utcoffset() is not None
#
#
# class CustomJSONEncoder(json.JSONEncoder):
#     """
#     JSONEncoder subclass that knows how to encode date/time, decimal types and UUIDs.
#     """
#     def default(self, o):
#         # See "Date Time String Format" in the ECMA-262 specification.
#         print("Custom Serializer.............")
#         if isinstance(o, datetime):
#             print("DATETIME: {}".format(o))
#             r = o.isoformat()
#             if o.microsecond:
#                 r = r[:23] + r[26:]
#             if r.endswith('+00:00'):
#                 r = r[:-6] + 'Z'
#             return r
#         elif isinstance(o, date):
#             return o.isoformat()
#         elif isinstance(o, time):
#             if is_aware(o):
#                 raise ValueError("JSON can't represent timezone-aware times.")
#             r = o.isoformat()
#             if o.microsecond:
#                 r = r[:12]
#             return r
#         elif isinstance(o, Decimal):
#             return str(o)
#         elif isinstance(o, uuid.UUID):
#             return str(o)
#         else:
#             print("DEFAULT: {}".format(o))
#             return super(CustomJSONEncoder, self).default(o)
#
#
# class UTC(tzinfo):
#     """
#     UTC implementation taken from Python's docs.
#
#     Used only when pytz isn't available.
#     """
#
#     def __repr__(self):
#         return "<UTC>"
#
#     def utcoffset(self, dt):
#         return ZERO
#
#     def tzname(self, dt):
#         return "UTC"
#
#     def dst(self, dt):
#         return ZERO
