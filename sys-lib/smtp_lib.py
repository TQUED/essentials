#!/usr/bin/python

import smtplib

s = smtplib.SMTP('websrv.cavisson.com')
s.sendmail('niraj.panda@cavisson.com', 'pradyumnna.satapathy@cavisson.com',
"""To: pradyumnna.satapathy@cavisson.com
   From: niraj.panda@cavisson.com
   My Python Mail Delivery System
""")
s.quit()
