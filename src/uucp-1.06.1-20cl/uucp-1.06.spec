Summary: GNU uucp
Summary(pt_BR): Uucp da GNU
Summary(es): Uucp de la GNU
Name: uucp
Version: 1.06.1
Release: 20cl
Copyright: GPL
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
#Source0: ftp://prep.ai.mit.edu/pub/gnu/uucp-1.06.1.tar.gz
# recompressed with bzip2
Source0: ftp://prep.ai.mit.edu/pub/gnu/uucp-1.06.1.tar.bz2
Source1: uucp.log
Patch0: uucp-1.06.1-misc.patch
Patch1: uucp-1.06.1-uureroute.patch
Prereq: fileutils
Prereq: info
Buildroot: /var/tmp/uucp-root
Summary(de): GNU-uupc 
Summary(fr): uucp de GNU
Summary(tr): GNU uucp sistemi

%description
UUCP is a Unix to Unix transfer mechanism.  It is used primarily
for remote sites to download and upload email and news files to local
machines. If you didn't already know that, you probably don't need this
package installed.  :-)

%description -l pt_BR
UUCP é um mecanismo de transferência de Unix para Unix. Ele é
usado primeiramente em sites remotos para fazer download e upload
de arquivos de mail e news para máquinas locais. Se você não sabia
disso, você provavelmente não precisa deste pacote instalado. :-)

%description -l es
UUCP es un mecanismo de transferencia de Unix para Unix. Se usa
primeramente en sitios remotos para hacer download y upload de
archivos de mail y news para máquinas locales. Si no lo sabias,
probablemente no necesitas de este paquete instalado. :-)

%description -l de
UUCP ist ein Unix-nach-Unix-Übertragungsprotokoll. Es wird vor allem
verwendet, um E-Mail- und News-Dateien von entfernten auf lokale Rechner
herunter- bzw. umgekehrt hochzuladen. Wie Sie wahrscheinlich wissen,
müssen Sie das Paket wahrscheinlich nicht installieren.  :-)

%description -l fr
UUCP est un mécanisme de transfert d'UNIX à UNIX. Il est principalement
utilisés par les sites de connexion pour télécharger ou envoyer des courriers
èlèctroniques et des nouvelles sur les machines locales. Si vous ne saviez
pas déja cela, vous n'avez probablement pas besoin d'insatller ce package.

%description -l tr
UUCP bir Unix'ten Unix'e iletim mekanizmasýdýr. Uzak sitelerden yerel
sisteme e-posta ve haber öbekleri aktarýmý için kullanýlýr. Bunun ne
olduðunu bilmiyorsanýz, büyük olasýlýkla iþinize de yaramayacaktýr. :-)

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- fixed prereq

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Tue May 05 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild
- added sample config files in /etc/uucp

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- added install-info support
- uses a build root

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- patched uureroute to find perl in /usr/bin instead of /usr/local/bin
- made log files ghosts

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- Brian Candler fixed /usr/lib/uucp/uucico symlink
- Added "create" entries to log file rotation configuration
- Touch log files on install if they don't already exist to allow proper
  rotation

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- symlinked /usr/sbin/uucico into /usr/lib/uucp
- (all of these changes are from Brian Candler <B.Candler@pobox.com>)
- sgid bit added on uucico so it can create lock files
- log files moved to /var/log/uucp/ owned by uucp (so uucico can create them)
- log rotation added
- uses /etc/uucp/oldconfig instead of /usr/lib/uucp for old config files
- package creates /etc/uucp and /etc/uucp/oldconfig directories
- man pages reference the correct locations for spool and config files

%prep
%setup
%patch -p1 -b .config
%patch1 -p1 -b .perlpath

find . -name "*.perlpath" | xargs rm

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make prefix="$RPM_BUILD_ROOT/usr" install install-info

gzip -9nf $RPM_BUILD_ROOT/usr/info/uucp*
mkdir -p $RPM_BUILD_ROOT/var/spool/uucp
mkdir -p $RPM_BUILD_ROOT/var/spool/uucppublic
chown uucp $RPM_BUILD_ROOT/var/spool/uucp
chown uucp $RPM_BUILD_ROOT/var/spool/uucppublic
mkdir -p $RPM_BUILD_ROOT/etc/uucp/oldconfig
chown uucp.uucp $RPM_BUILD_ROOT/etc/uucp $RPM_BUILD_ROOT/etc/uucp/oldconfig
chmod 770 $RPM_BUILD_ROOT/etc/uucp $RPM_BUILD_ROOT/etc/uucp/oldconfig

rm -rf $RPM_BUILD_ROOT/var/log/uucp
mkdir -p $RPM_BUILD_ROOT/var/log/uucp
chown uucp.uucp $RPM_BUILD_ROOT/var/log/uucp
strip $RPM_BUILD_ROOT/usr/sbin/* || :
strip $RPM_BUILD_ROOT/usr/bin/* || :

mkdir -p $RPM_BUILD_ROOT/usr/lib/uucp
ln -sf ../../sbin/uucico $RPM_BUILD_ROOT/usr/lib/uucp/uucico

mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m 644 -o 0 -g 0 $RPM_SOURCE_DIR/uucp.log $RPM_BUILD_ROOT/etc/logrotate.d/uucp

# Create ghost files
for n in Log Stats Debug; do
	touch $RPM_BUILD_ROOT/var/log/uucp/$n
done

chown uucp.uucp $RPM_BUILD_ROOT/var/log/uucp/{Log,Stats,Debug}
chmod 644 $RPM_BUILD_ROOT/var/log/uucp/{Log,Stats}
chmod 600 $RPM_BUILD_ROOT/var/log/uucp/Debug

# the following is kind of gross, but it is effective
for i in dial passwd port dialcode sys call ; do
cat > $RPM_BUILD_ROOT/etc/uucp/$i <<EOF 
# This is an example of a $i file. This file have the syntax compatible
# with Taylor UUCP (not HDB, not anything else). Please check uucp
# documentation if you are not sure how Taylor config files are supposed to 
# look like. Edit it as appropriate for your system.

# Everything after a '#' character is a comment.
EOF
done

# some more documentation
texi2html -monolithic uucp.texi

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Create initial log files so that logrotate doesn't complain
for n in Log Stats Debug; do
	[ -f /var/log/uucp/$n ] || touch /var/log/uucp/$n
done

chown uucp.uucp /var/log/uucp/{Log,Stats,Debug}
chmod 644 /var/log/uucp/{Log,Stats}
chmod 600 /var/log/uucp/Debug

/sbin/install-info /usr/info/uucp.info.gz /usr/info/dir

%preun
/sbin/install-info --del /usr/info/uucp.info.gz /usr/info/dir

%files
%doc README COPYING ChangeLog MANIFEST NEWS
%doc sample contrib uucp.html
%dir /var/spool/uucp
%dir /var/spool/uucppublic
%dir /etc/uucp
%dir /etc/uucp/oldconfig
/usr/info/uucp.info*
/usr/sbin/*
/usr/bin/*
/usr/man/*/*
/usr/lib/uucp/uucico
%dir /var/log/uucp
%config /etc/logrotate.d/uucp
%ghost /var/log/uucp/Log
%ghost /var/log/uucp/Stats
%ghost /var/log/uucp/Debug
%config /etc/uucp/dial
%config /etc/uucp/dialcode
%config /etc/uucp/port
%config /etc/uucp/passwd
%config /etc/uucp/sys
%config /etc/uucp/call
