#! /usr/bin/python

import pexpect

# homework 1

newprimates = open("primates2.nex", "w")
oldprimates = open("primates.nex").read() #reads entire contents of primates.nex as a string

corrected = oldprimates.replace("mcmc", "mcmcp")
newprimates.write(corrected)
newprimates.close()

child = pexpect.spawn("mb -i primates2.nex") #-i tells mrbayes to run in interactive mode
#send the string "mcmc" to the process. This tells mrbayes to start running. The \r is carriage return
child.sendline("mcmc")
# tells mrbayes to stop the analysis (do not continue)
child.sendline("no")
child.expect("MrBayes >") # wait for the mrbayes prompt.
print child.before # child.before shows all of the screen output
#now add a line to tell mrbayes to quit ("quit")
child.sendline("quit")
child.close()

# homework 2

#spawn an interactive mrbayes process
child = pexpect.spawn("mb -i")
#send the command "execute primates2.nex" to mrbayes
child.sendline("execute primates2.nex")
#send the sumt command to mrbayes
child.sendline("sumt")
#check to see that the mrbayes command prompt is returned
child.expect("MrBayes >")
#print everything before the mrbayes prompt
print child.before
#send the sump command
child.sendline("sump")
#quit mrbayes
child.sendline("quit")
child.close()
