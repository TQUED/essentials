#!/usr/bin/python

import pexpect
import getpass
import time
import os
import sys
import commands
import shutil
import getopt

prompt = '.*[\$#]'

#This is a function to Login to the remote machine Using the pexpect
def cli_login(user, host, password):
    print 'Login to the machine %s'% host 
    ssh_newkey = 'Are you sure you want to continue connecting'
    child = pexpect.spawn('ssh -l %s %s'%(user, host))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'assword:'])
    if i == 0: # Timeout
        print 'SSH could not login:'
        print child.before, child.after
        return None
    if i == 1: # SSH public key prompt, just accept it
        child.sendline ('yes')
        i = child.expect([pexpect.TIMEOUT, 'assword:'])
        if i == 0: # Timeout
            print "SSH timeout"
            print child.before, child.after
            return None
    child.sendline(password)
    child.sendline('1')
    print child.before, child.after
    i = child.expect([pexpect.TIMEOUT, prompt])    # Expect CLI prompt
    if i == 0: # Timeout
        return None
    print child.before, child.after
    return child

def main ():
    hostname = sys.argv[1]
    #hostname = 10.10.30.13
    #type = sys.argv[2]
    print '%s'% type
    username = 'root'
    password = 'abeona'
    child = cli_login(username, hostname, password)#Call for login to remote machin
    #child.sendline('rm -f /var/www/hpd/conf/hpd.conf')
    #child.expect(prompt)
    #child.sendline('cp /var/www/hpd/conf/hpd_%s.conf /var/www/hpd/conf/hpd.conf'%(type))
    #child.expect(prompt)
    #print child.before, child.after
    child.sendline('/etc/init.d/hpd_QA_Niraj stop')
    child.expect(prompt, timeout=120)
    print child.before, child.after
    time.sleep(20)
    child.sendline('ps -ef|grep QA_Niraj')
    child.expect(prompt, timeout=120)
    print child.before, child.after
    time.sleep(20)
    sys.exit(1)
    return 0

if __name__ == '__main__':
    main()
