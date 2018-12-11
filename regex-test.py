import re
import time
import datetime
import pickle
import redis

# how to install SERVER:
# ### CentOS/RHEL 7
# yum install epel-release
# ### CentOS/RHEL 6
# rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
# yum install redis
# cat /etc/redis/redis.conf
# edit bing to 0.0.0.0
### CentOS/RHEL 7 
# systemctl enable redis
# systemctl start redis
### CentOS/RHEL 6 
# chkconfig redis on
# service redis restart

# how to install CLIENT:
# pip install redis

redis_server = '10.2.21.169'
redis_port = 6379
regex = r'(\S+)\s*=\s*([\']|[\"])([\W\w]*?)\2'
text = 'attr="a" attr="b" attr="c" attr="d" attr="e"'

prog = re.compile(regex)
r = redis.Redis(host=redis_server, port=redis_port, db=0)
r.set('myreg', pickle.dumps(prog))

# - NORMAL ----------------------------------
start1 = datetime.datetime.now().timestamp()
for i in range(0,10000):
    prog = re.compile(regex)
    match = prog.search(text)

    end1 = datetime.datetime.now().timestamp()
print(end1-start1)

# - PICKLE FILE ----------------------------------
start2 = datetime.datetime.now().timestamp()
# prog = re.compile(regex)
# pickle.dump( prog, open( "./_regex.xxx", "wb" ) )

for i in range(0,10000):
    prog = pickle.load(open("./_regex.xxx", "rb"))
    # prog = re.compile(regex)
    match = prog.search(text)
end2 = datetime.datetime.now().timestamp()
print(end2-start2)

# - REDIS FILE ----------------------------------
start3 = datetime.datetime.now().timestamp()
# prog = re.compile(regex)
# pickle.dump( prog, open( "./_regex.xxx", "wb" ) )

for i in range(0,10000):
    prog = pickle.load(open("./_regex.xxx", "rb"))
    # prog = re.compile(regex)
    match = r.get('myreg')
end3 = datetime.datetime.now().timestamp()
print(end3-start3)




