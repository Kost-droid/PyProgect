import dns.resolver

ips = dns.resolver.resolve('github.ru', 'A')
for ip in ips:
    print(ip)
