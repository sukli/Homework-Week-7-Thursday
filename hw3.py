#! /usr/bin/python

import pexpect
import glob

def func1(nexus_file, numgen=1000):
	child = pexpect.spawn("mb -i " + nexus_file)
	child.sendline("set nowarn = yes")
	child.sendline("mcmcp ngen = " + str(numgen))
	child.sendline("mcmc")
	child.sendline("no")
	child.sendline("quit")
	child.close()


def func2(nexus_file):
	child = pexpect.spawn("mb -i")
	child.sendline("execute " + nexus_file)
	child.sendline("sumt")
	child.expect("MrBayes >")
	child.sendline("sump")
	child.sendline("quit")
	child.close()


allfiles = glob.glob("*")
otherfiles = glob.glob("*.t")

print "there are " + str(len(allfiles)) + " total files in the current directory and " + str(len(otherfiles)) + " that end in '.t'"

func1("primates2.nex")
func2("primates2.nex")

print "there are " + str(len(allfiles)) + " total files in the current directory and " + str(len(otherfiles)) + " that end in '.t'"
print "these files end in '.t':"
print otherfiles
