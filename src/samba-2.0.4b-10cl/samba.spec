Summary: Samba SMB client and server
Summary(pt_BR): Cliente e servidor SMB
Summary(es): Cliente y servidor SMB
Name: samba
Version: 2.0.4b
Release: 10cl
Copyright: GNU GPL version 2
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://samba.org/pub/samba/samba-2.0.4b.tar.bz2
Source1: smb.init.i18n
Source2: samba.log
Patch: makefile-path.patch
Patch1: smbw.patch
Patch2: smbwrapper-path.patch
Patch3: samba-glibc21.patch
Patch4: samba-printing.patch
Patch5: samba-no64lock.patch
Patch6: samba-64bits.patch
Requires: pam >= 0.64
Prereq: chkconfig fileutils
BuildRoot: /var/tmp/samba
Serial: 1

%description
Samba provides an SMB server which can be used to provide
network services to SMB (sometimes called "Lan Manager")
clients, including various versions of MS Windows, OS/2,
and other Linux machines. Samba also provides some SMB
clients, which complement the built-in SMB filesystem
in Linux. Samba uses NetBIOS over TCP/IP (NetBT) protocols
and does NOT need NetBEUI (Microsoft Raw NetBIOS frame)
protocol.

Samba-2 features an almost working NT Domain Control
capability and includes the new SWAT (Samba Web Administration
Tool) that allows samba's smb.conf file to be remotely managed
using your favourite web browser. For the time being this is
being enabled on TCP port 901 via inetd.

Please refer to the WHATSNEW.txt document for fixup information.
This binary release includes encrypted password support.
Please read the smb.conf file and ENCRYPTION.txt in the
docs directory for implementation details.

NOTE: Red Hat Linux 5.X Uses PAM which has integrated support
for Shadow passwords. Do NOT recompile with the SHADOW_PWD option
enabled. Red Hat Linux has built in support for quotas in PAM.

%description -l pt_BR
Samba provê um servidor SMB que pode ser usado para oferecer serviços de
rede a clientes SMB (algumas vezes chamado de "Lan Manager"), incluindo
várias versões de MS Windows, OS/2, e outras máquinas Linux. Samba também
fornece alguns clientes SMB, que complementam o sistema de arquivos SMB do
Linux. Samba usa o protocolo NetBIOS sobre TCP/IP (NetBT) e não necessita
do protocolo NetBEUI (Microsoft Raw NetBIOS frame).

O Samba-2 provê a maioria das características de um servidor de Controle
de Domínios NT e inclui o SWAT (Samba Web Administration Tool), que permite
que o arquivo smb.conf seja gerenciador remotamente através de um
navegador.

%description -l es
Samba provee un servidor SMB que se puede usar para ofrecer
servicios de red a clientes SMB (algunas veces se le llama de
"Lan Manager"), incluyendo varias versiones de MS Windows, OS/2,
y otras máquinas Linux. Samba también ofrece algunos clientes SMB,
que complementan el sistema de archivos SMB de Linux. Samba usa el
protocolo NetBIOS sobre TCP/IP (NetBT) y no necesita del protocolo
NetBEUI (Microsoft Raw NetBIOS frame).

%changelog
* Wed Jun 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- %post don't generates message in the inetd restart

* Mon Jun 21 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixed logrotate script
- turn of 64-bit locking on 32-bit platforms
- explicitly uncomment 'printing = bsd' in sample config
- removed smbwrapper and smbsh, fixes libNoVersion dependency
- gziped man pages
- recompressed source
- added --with-pam as pam is no longer used by default

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscript i18n

* Mon Mar  1 1999 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sat Jan 27 1999 Jeremy Allison <jra@samba.org>
 - Removed smbrun binary and tidied up some loose ends

* Sun Oct 25 1998 John H Terpstra <jht@samba.org>
 - Added parameters to /config to ensure smb.conf, lmhosts, 
	and smbusers never gets over-written.

* Sat Oct 24 1998 John H Terpstra <jht@samba.org>
 - removed README.smbsh file from docs area

* Mon Oct 05 1998 John H Terpstra <jht@samba.org>
 - Added rpcclient to binaries list
 - Added smbwrapper stuff

* Fri Aug 21 1998 John H Terpstra <jht@samba.org>
 - Updated for Samba version 2.0 building

* Tue Jul 07 1998 Erik Troan <ewt@redhat.com>
  - updated postun triggerscript to check $0
  - clear /etc/codepages from %preun instead of %postun

* Sat Jul 04 1998 John H Terpstra <jht@samba.org>
 - fixed codepage preservation during update via -Uvh

* Mon Jun 08 1998 Erik Troan <ewt@redhat.com>
  - made the %postun script a tad less agressive; no reason to remove
    the logs or lock file 
  - the %postun and %preun should only exectute if this is the final
    removal
  - migrated %triggerpostun from Red Hat's samba package to work around
    packaging problems in some Red Hat samba releases

* Sun Apr 26 1998 John H Terpstra <jht@samba.org>
 - Tidy up for early alpha releases
 - added findsmb from SGI packaging

* Thu Apr 09 1998 John H Terpstra <jht@samba.org>
 - Updated spec file
 - Included new codepage.936

* Sat Mar 20 1998 John H Terpstra <jht@samba.org>
 - Added swat facility

* Sat Jan 24 1998 John H Terpstra <jht@samba.org>
 - Many optimisations (some suggested by Manoj Kasichainula <manojk@io.com>
  - Use of chkconfig in place of individual symlinks to /etc/rc.d/init/smb
  - Compounded make line
  - Updated smb.init restart mechanism
  - Use compound mkdir -p line instead of individual calls to mkdir
  - Fixed smb.conf file path for log files
  - Fixed smb.conf file path for incoming smb print spool directory
  - Added a number of options to smb.conf file
  - Added smbadduser command (missed from all previous RPMs) - Doooh!
  - Added smbuser file and smb.conf file updates for username map

%prep
%setup
%patch -p1  -b .paths
%patch1 -p1 -b smbw
%patch2 -p0 -b smbwrapper
%patch3 -p1 -b .glibc21
%patch4 -p1 -b .printing
#%patch5 is in build
%patch6 -p1 -b .64bit


%build
cd source
./configure --prefix=/usr --libdir=/etc --with-lockdir=/var/lock/samba --with-privatedir=/etc --with-swatdir=/usr/share/swat --with-automount --with-quotas --with-smbmount --with-pam
%ifnarch alpha
patch -p2 -b --suffix .no64lock < $RPM_SOURCE_DIR/samba-no64lock.patch
%endif
make CFLAGS="$RPM_OPT_FLAGS" all
make bin/smbrun

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/codepages/src
mkdir -p $RPM_BUILD_ROOT/etc/{logrotate.d,pam.d}
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/{init.d,rc0.d,rc1.d,rc2.d,rc3.d,rc5.d,rc6.d}
mkdir -p $RPM_BUILD_ROOT/home/samba
mkdir -p $RPM_BUILD_ROOT/usr/{bin,sbin}
mkdir -p $RPM_BUILD_ROOT/usr/share/swat/{images,help,include}
mkdir -p $RPM_BUILD_ROOT/usr/man/{man1,man5,man7,man8}
mkdir -p $RPM_BUILD_ROOT/var/lock/samba
mkdir -p $RPM_BUILD_ROOT/var/log/samba
mkdir -p $RPM_BUILD_ROOT/var/spool/samba

# Install standard binary files
for i in nmblookup smbclient smbpasswd smbrun smbstatus testparm testprns \
    smbmount smbmnt smbumount make_smbcodepage make_printerdef rpcclient
do
  install -m755 -s source/bin/$i $RPM_BUILD_ROOT/usr/bin
done
for i in addtosmbpass mksmbpasswd.sh smbtar convert_smbpasswd
do
  install -m755 source/script/$i $RPM_BUILD_ROOT/usr/bin
done
#install -m755 -s source/bin/smbwrapper.so $RPM_BUILD_ROOT/usr/lib

# Install secure binary files
for i in smbd nmbd swat
do
  install -m755 -s source/bin/$i $RPM_BUILD_ROOT/usr/sbin
done

# Compress all man pages
gzip -9f docs/manpages/*

# Install level 1 man pages
for i in smbclient.1 smbrun.1 smbstatus.1 smbtar.1 testparm.1 testprns.1 make_smbcodepage.1 nmblookup.1
do
install -m644 docs/manpages/$i.gz $RPM_BUILD_ROOT/usr/man/man1
done

# Install codepage source files
for i in 437 737 850 852 861 866 932 936 949 950
do
install -m644 source/codepages/codepage_def.$i $RPM_BUILD_ROOT/etc/codepages/src
done

# Install SWAT helper files
for i in swat/help/*.html docs/htmldocs/*.html
do
install -m644 $i $RPM_BUILD_ROOT/usr/share/swat/help
done
for i in swat/images/*.gif
do
install -m644 $i $RPM_BUILD_ROOT/usr/share/swat/images
done
for i in swat/include/*.html
do
install -m644 $i $RPM_BUILD_ROOT/usr/share/swat/include
done

# Install the miscellany
install -m644 swat/README $RPM_BUILD_ROOT/usr/share/swat
install -m644 docs/manpages/smb.conf.5.gz $RPM_BUILD_ROOT/usr/man/man5
install -m644 docs/manpages/lmhosts.5.gz $RPM_BUILD_ROOT/usr/man/man5
install -m644 docs/manpages/smbpasswd.5.gz $RPM_BUILD_ROOT/usr/man/man5
install -m644 docs/manpages/samba.7.gz $RPM_BUILD_ROOT/usr/man/man7
install -m644 docs/manpages/smbd.8.gz $RPM_BUILD_ROOT/usr/man/man8
install -m644 docs/manpages/nmbd.8.gz $RPM_BUILD_ROOT/usr/man/man8
install -m644 docs/manpages/swat.8.gz $RPM_BUILD_ROOT/usr/man/man8
install -m644 docs/manpages/smbpasswd.8.gz $RPM_BUILD_ROOT/usr/man/man8
install -m644 docs/manpages/smbmnt.8.gz $RPM_BUILD_ROOT/usr/man/man8
install -m644 docs/manpages/smbmount.8.gz $RPM_BUILD_ROOT/usr/man/man8
install -m644 docs/manpages/smbumount.8.gz $RPM_BUILD_ROOT/usr/man/man8
install -m644 packaging/RedHat/smb.conf $RPM_BUILD_ROOT/etc/smb.conf
install -m644 packaging/RedHat/smbusers $RPM_BUILD_ROOT/etc/smbusers
install -m755 packaging/RedHat/smbprint $RPM_BUILD_ROOT/usr/bin
install -m755 packaging/RedHat/findsmb $RPM_BUILD_ROOT/usr/bin
install -m755 packaging/RedHat/smbadduser $RPM_BUILD_ROOT/usr/bin
install -m644 packaging/RedHat/samba.pamd $RPM_BUILD_ROOT/etc/pam.d/samba
install -m644 $RPM_SOURCE_DIR/samba.log $RPM_BUILD_ROOT/etc/logrotate.d/samba
echo 127.0.0.1 localhost > $RPM_BUILD_ROOT/etc/lmhosts

install -m755 $RPM_SOURCE_DIR/smb.init.i18n $RPM_BUILD_ROOT/usr/sbin/samba
ln -sf /usr/sbin/samba $RPM_BUILD_ROOT/etc/rc.d/init.d/smb

# to not enter in %files docs
rm -rf docs/manpages

%clean
rm -rf $RPM_BUILD_ROOT

%post
#/sbin/chkconfig --add smb

# Build codepage load files
for i in 437 737 850 852 861 866 932 936 949 950
do
/usr/bin/make_smbcodepage c $i /etc/codepages/src/codepage_def.$i /etc/codepages/codepage.$i
done

# Add swat entry to /etc/services if not already there
if !( grep ^[:space:]*swat /etc/services > /dev/null ) then
	echo 'swat		901/tcp				# Add swat service used via inetd' >> /etc/services
fi

# Add swat entry to /etc/inetd.conf if needed
if !( grep '^#*[:space:]*swat' /etc/inetd.conf > /dev/null ) then
	echo '#swat	stream	tcp	nowait.400	root	/usr/sbin/swat swat' >> /etc/inetd.conf
killall -1 inetd 2> /dev/null || :
fi

%preun
if [ $1 = 0 ] ; then
    /sbin/chkconfig --del smb

    for n in /etc/codepages/*; do
	if [ "$n" != "/etc/codepages/src" ]; then
	    rm -rf $n
	fi
    done
    # We want to remove the browse.dat and wins.dat files so they can not interfer with a new version of samba!
    if [ -e /var/lock/samba/browse.dat ]; then
	    rm -f /var/lock/samba/browse.dat
    fi
    if [ -e /var/lock/samba/wins.dat ]; then
	    rm -f /var/lock/samba/wins.dat
    fi
fi

%postun
# Only delete remnants of samba if this is the final deletion.
if [ $1 != 0 ] ; then
    if [ -x /etc/pam.d/samba ]; then
      rm -f /etc/pam.d/samba
    fi
    if [ -e /var/log/samba ]; then
      rm -rf /var/log/samba
    fi
    if [ -e /var/lock/samba ]; then
      rm -rf /var/lock/samba
    fi

    # Remove swat entries from /etc/inetd.conf and /etc/services
    cd /etc
    tmpfile=/etc/tmp.$$
    sed -e '/^#*[:space:]*swat.*$/d' /etc/inetd.conf > $tmpfile
    mv $tmpfile inetd.conf
    sed -e '/^[:space:]*swat.*$/d' /etc/services > $tmpfile
    mv $tmpfile services
fi

%triggerpostun -- samba < samba-2.0.0
if [ $0 != 0 ]; then
    /sbin/chkconfig --add smb
fi


%files
%defattr(-,root,root)
%doc README COPYING Manifest Read-Manifest-Now
%doc WHATSNEW.txt Roadmap
%doc docs
%doc examples
/usr/sbin/smbd
/usr/sbin/nmbd
/usr/sbin/swat
/usr/bin/addtosmbpass
/usr/bin/mksmbpasswd.sh
/usr/bin/smbclient
/usr/bin/rpcclient
/usr/bin/testparm
/usr/bin/testprns
/usr/bin/findsmb
/usr/bin/smbstatus
/usr/bin/smbmount
/usr/bin/smbumount
/usr/bin/smbmnt
/usr/bin/nmblookup
/usr/bin/make_smbcodepage
/usr/bin/make_printerdef
/usr/bin/smbpasswd
/usr/bin/smbtar
/usr/bin/smbprint
/usr/bin/smbadduser
/usr/bin/smbrun
/usr/share/swat
%attr(0750,root,root) /usr/sbin/samba
%config(noreplace) /etc/lmhosts
%config(noreplace) /etc/smb.conf
%config(noreplace) /etc/smbusers
%config /etc/rc.d/init.d/smb
%config /etc/logrotate.d/samba
%config /etc/pam.d/samba
%config /etc/codepages/src/codepage_def.437
%config /etc/codepages/src/codepage_def.737
%config /etc/codepages/src/codepage_def.850
%config /etc/codepages/src/codepage_def.852
%config /etc/codepages/src/codepage_def.861
%config /etc/codepages/src/codepage_def.866
%config /etc/codepages/src/codepage_def.932
%config /etc/codepages/src/codepage_def.936
%config /etc/codepages/src/codepage_def.949
%config /etc/codepages/src/codepage_def.950
%attr(-,root,nobody) %dir /home/samba
%dir /etc/codepages
%dir /etc/codepages/src
%dir /var/lock/samba
%dir /var/log/samba
%attr(1777,root,root) %dir /var/spool/samba
/usr/man/man*/*
