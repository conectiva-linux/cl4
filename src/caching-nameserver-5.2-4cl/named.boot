;
; Uma configuração de servidor de nomes somente para cache
;
directory                              /var/named
cache           .                      named.ca
primary         0.0.127.in-addr.arpa   named.local
