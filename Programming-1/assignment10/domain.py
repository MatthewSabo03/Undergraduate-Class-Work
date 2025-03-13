import stdio
import sys


url = 'http://introcs.cs.princeton.edu/python'

splitUrl = url.split('http://')[1].split('/')[0]
fullDomainName = splitUrl.split('.')[-2] + '.' + splitUrl.split('.')[-1]
domainType = fullDomainName.split('.')[1]


stdio.writeln(domainType)