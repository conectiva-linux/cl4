Summary: Rotates, compresses, removes and mails system log files.
Summary(pt_BR): Rotaciona, comprime e envia mail de logs do sistema
Summary(es): Hace el rutado, comprime y envía mail de logs del sistema
Name: logrotate
Version: 3.2
Release: 2cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.redhat.com/pub/redhat/code/logrotate/logrotate-%{PACKAGE_VERSION}.tar.gz
BuildRoot: /var/tmp/logrotate.root

%description
The logrotate utility is designed to simplify the administration of
log files on a system which generates a lot of log files.  Logrotate
allows for the automatic rotation compression, removal and mailing of
log files.  Logrotate can be set to handle a log file daily, weekly,
monthly or when the log file gets to a certain size.  Normally, logrotate
runs as a daily cron job.

Install the logrotate package if you need a utility to deal with the log
files on your system.

%description -l pt_BR
Logrotate foi projetado para facilitar a administração de sistemas
que geram grande número de arquivos de log. Permite automatização
na rotação, compressão, remoção e envio de mail de arquivos de
logs. Cada arquivo de log pode ser tratado diariamente, semanalmente,
mensalmente ou quanto crescer demais.

%description -l es
Logrotate fue proyectado para facilitar la administración de sistemas
que generan gran número de archivos de log. Permite automatización
en la rotación, compresión, remoción y envío de mail de archivos
de logs. Cada archivo de log puede ser tratado diariamente,
semanalmente, mensualmente o cuanto crezca demasiado.

%prep
%setup

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make PREFIX=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
mkdir -p $RPM_BUILD_ROOT/etc/cron.daily

install -m 644 examples/logrotate-default $RPM_BUILD_ROOT/etc/logrotate.conf
install -m 755 examples/logrotate.cron $RPM_BUILD_ROOT/etc/cron.daily/logrotate

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755, root, root) /usr/sbin/logrotate
%attr(0644, root, root) /usr/man/man8/logrotate.8
%attr(0755, root, root) /etc/cron.daily/logrotate
%attr(0644, root, root) %config /etc/logrotate.conf
%attr(0755, root, root) %dir /etc/logrotate.d

%changelog
* Tue May 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
