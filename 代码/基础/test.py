# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta
# 测试:
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
def to_timestamp(dt_str,tz_str):
        cody = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')



# to_timestamp('2015-6-1 08:10:30')
