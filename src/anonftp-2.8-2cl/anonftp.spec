Summary: A program which enables anonymous FTP access.
Summary(pt_BR): Habilita acesso via ftp anônimo
Summary(es): Habilita acceso vía ftp anónimo
Name: anonftp
Version: 2.8
Release: 2cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Prefix: /home/ftp
BuildRoot: /var/tmp/anonftp-root
AutoReqProv: 0
Requires: ftpserver

%description
The anonftp package contains the files you need in order to
allow anonymous FTP access to your machine. Anonymous FTP access allows
anyone to download files from your machine without having a user account. 
Anonymous FTP is a popular way of making programs available via the
Internet.

You should install anonftp if you would like to enable anonymous FTP
downloads from your machine.

%description -l pt_BR
Contém os arquivos necessários para permitir acesso ftp anônimo
a sua máquina.  Isso deixa qualquer usuário pegar arquivos de
sua máquina sem ter uma conta, o que é um meio popular de tornar
programas disponíveis na Internet.

%description -l es
Contiene los archivos necesarios para permitir acceso ftp anónimo
a tu máquina. Esto deja cualquier usuario coger archivos de tu
máquina sin tener una cuenta, esto es un medio popular de poner a
disposición programas en Internet.

%prep
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/home/ftp
mkdir -p $RPM_BUILD_ROOT/home/ftp/pub
mkdir -p $RPM_BUILD_ROOT/home/ftp/etc
mkdir -p $RPM_BUILD_ROOT/home/ftp/bin
mkdir -p $RPM_BUILD_ROOT/home/ftp/lib

cat > $RPM_BUILD_ROOT/home/ftp/etc/passwd <<EOF
root:*:0:0:::
bin:*:1:1:::
operator:*:11:0:::
ftp:*:14:50:::
nobody:*:99:99:::
EOF

cat > $RPM_BUILD_ROOT/home/ftp/etc/group <<EOF
root::0:
bin::1:
daemon::2:
sys::3:
adm::4:
ftp::50:
EOF

%define LDSOVER 2
%define LIBCVER 2.1.1
%define LIBNSSVER 2

%ifarch i386 sparc armv4l
%define LIBCSOVER 6
%define LIBNSLVER 1
%endif

%ifarch alpha
%define LIBCSOVER 6.1
%define LIBNSLVER 1.1
%endif

%define ROOT $RPM_BUILD_ROOT/home/ftp/lib

cp -fd /etc/ld.so.cache $RPM_BUILD_ROOT/home/ftp/etc
cp -fd /lib/libc.so.%{LIBCSOVER} /lib/libc-%{LIBCVER}.so %{ROOT}
cp -fd /lib/ld-linux.so.%{LDSOVER} /lib/ld-%{LIBCVER}.so %{ROOT}
cp -fd /lib/libnss_files-%{LIBCVER}.so \
	/lib/libnss_files.so.%{LIBNSSVER}	%{ROOT}
cp -fd /lib/libnsl-%{LIBCVER}.so /lib/libnsl.so.%{LIBNSLVER} %{ROOT}

%ifnarch armv4l
cp -fd	/lib/libnss1_files-%{LIBCVER}.so %{ROOT}
%endif

cp -fd /bin/ls /bin/cpio /bin/gzip /bin/tar $RPM_BUILD_ROOT/home/ftp/bin
cp -fd /bin/ash $RPM_BUILD_ROOT/home/ftp/bin/sh
ln -sf gzip $RPM_BUILD_ROOT/home/ftp/bin/zcat
cp -fd /usr/bin/compress $RPM_BUILD_ROOT/home/ftp/bin

strip $RPM_BUILD_ROOT/home/ftp/lib/*
cd $RPM_BUILD_ROOT/home/ftp/bin/
strip ls cpio gzip tar 
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%attr(0444,root,root) %config /home/ftp/etc/passwd
%attr(0444,root,root) %config /home/ftp/etc/group

/home/ftp/etc/ld.so.cache
/home/ftp/lib/libc.so.%{LIBCSOVER}
/home/ftp/lib/libc-%{LIBCVER}.so
/home/ftp/lib/ld-linux.so.%{LDSOVER}
/home/ftp/lib/ld-%{LIBCVER}.so
/home/ftp/lib/libnss_files-%{LIBCVER}.so
/home/ftp/lib/libnss_files.so.%{LIBNSSVER}
/home/ftp/lib/libnsl-%{LIBCVER}.so
/home/ftp/lib/libnsl.so.%{LIBNSLVER}

%attr(0755,root,root) %dir /home/ftp
%attr(0111,root,root) %dir /home/ftp/bin
%attr(0111,root,root) %dir /home/ftp/etc
%attr(2755,root,ftp) %dir /home/ftp/pub
%dir /home/ftp/lib
%attr(0111,root,root) /home/ftp/bin/ls
%attr(0111,root,root) /home/ftp/bin/compress
%attr(0111,root,root) /home/ftp/bin/cpio
%attr(0111,root,root) /home/ftp/bin/gzip
%attr(0111,root,root) /home/ftp/bin/sh
%attr(0111,root,root) /home/ftp/bin/tar
%attr(0111,root,root) /home/ftp/bin/zcat

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)
- glibc version 2.1.1

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- add sparc

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- fix defattr typo (#784)
- newer libc

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- abuse the %attr settings instead of massive chown
- avoid cp-av because it breaks on symlinks (the wonders of lchown/chown
- rebuild for glibc 2.1

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- newer libc

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- updated for the newer glibc libs

* Thu Nov 06 1997 Donnie Barnes <djb@redhat.com>
- Built with glibc for the first time
- moved BuildRoot to /var/tmp
- mega-reworking of the spec file

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Requires ftpserver virtual package now (which wu-ftpd provides).

