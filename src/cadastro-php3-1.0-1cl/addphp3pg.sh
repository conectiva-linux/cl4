# script para adicionar exemplos ao banco de dados "cadastro" rodando em PostgreSQL
#!/bin/bash

/etc/rc.d/init.d/postgresql stop
su - postgres -c "/usr/bin/postmaster -i -S -D/var/lib/pgsql"
su - postgres -c "createuser nobody << EOF

y
n
EOF"
su - postgres -c "createdb cadastro"
su - postgres -c "psql cadastro -f /usr/doc/cadastro-php3-1.0/cadastro.sql"
echo postgresql > /etc/cadastro.conf

