#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# NOTE: take care to keep the syntax bash compatible
#

# webserver port
port=8080

# log files
web_logfile="var/access.log"
app_logfile="var/application.log"
sql_logfile="var/sql.log"

# session defaults
session_salt="87525f4c-af0e-47bd-81c2-144bbd2bca0b"
session_timeout=86400 #24 * 60 * 60, # 24 hours   in seconds
session_dir='var'
session_name="framework"
session_cookie_domain=None
session_ignore_expiry=True
session_ignore_change_ip=False
session_expired_message='Session expired'

