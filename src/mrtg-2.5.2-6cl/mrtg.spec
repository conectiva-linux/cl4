Summary:Multi Router Traffic Grapher
Summary(pt_BR): Ferramenta para fazer gráficos do uso da rede.
Summary(es): Multi Router Traffic Grapher
Name:mrtg
Version: 2.5.2
Release: 6cl
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Copyright: distributable
Source0: http://www.ee.ethz.ch/~oetiker/webtools/mrtg/pub/mrtg-2.5.2.tar.gz
Url:http://www.ee.ethz.ch/~oetiker/webtools/mrtg/mrtg.html
Source1: mrtg.cfg
Patch0: mrtg-2.2-make.patch
Patch1: mrtg.path.patch
Requires: perl >= 5.003
Buildroot: /var/tmp/mrtg-root

%description
The Multi Router Traffic Grapher (MRTG) is a tool to monitor the traffic
load on network-links. MRTG generates HTML pages containing GIF
images which provide a LIVE visual representation of this traffic. 

%description -l pt_BR
O MRTG é uma ferramenta parar monitorar o tráfego de links de rede.
Ele gera páginas HTML contendo imagens GIF que provêm uma sensação
realística deste gráfico.


The Multi Router Traffic Grapher (MRTG) is a tool to monitor the traffic
load on network-links. MRTG generates HTML pages containing GIF
images which provide a LIVE visual representation of this traffic. 


%description -l es
E MRTG es una herramienta para monitorar el uso de la red.

%prep
%setup -q
%patch0 -p1 -b .make
%patch1 -p1 -b .path

echo "Removing..."
find . -name "*.orig" -print -exec rm -f {} \;

%build
rm -rf contrib/*/*.path
make rateup
make substitute

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/home/httpd/html/mrtg
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/mrtg
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/

cp  mrtg*.gif $RPM_BUILD_ROOT/home/httpd/html/mrtg/
cp  readme.html $RPM_BUILD_ROOT/home/httpd/html/mrtg/
cp  $RPM_SOURCE_DIR/mrtg.cfg $RPM_BUILD_ROOT/home/httpd/html/mrtg/
cp  mrtg-conf.html $RPM_BUILD_ROOT/home/httpd/html/mrtg

for i in  mrtg rateup; do
  install -m 755 -c $i $RPM_BUILD_ROOT/usr/bin/$i
done

for i in BER.pm SNMP_Session.pm; do
  install -m 755 -c $i $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/
done

find contrib | cpio -pdmv $RPM_BUILD_ROOT/usr/lib/mrtg/
cp -p cfgmaker convert indexmaker $RPM_BUILD_ROOT/usr/lib/mrtg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc readme.txt readme.html mibhelp.txt
%doc COPYING COPYRIGHT Changes Contributors INSTALL Todo
%dir /home/httpd/html/mrtg
%config /home/httpd/html/mrtg/mrtg.cfg
/home/httpd/html/mrtg/mrtg*gif
/home/httpd/html/mrtg/readme.html
/home/httpd/html/mrtg/mrtg-conf.html
/usr/lib/perl5/site_perl/BER.pm
/usr/lib/perl5/site_perl/SNMP_Session.pm
/usr/lib/mrtg
/usr/bin/mrtg
/usr/bin/rateup

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Modified Group

* Sun Apr 18 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Removed %post and %postun sections from spec file

* Fri Oct 08 1998 Michael Maher <mike@redhat.com>
- built package for 5.2 powertools.

* Fri Jun 02 1998 Michael Maher <mike@redhat.com>
- fixed bugs found in package. 

* Fri May 22 1998 Michael Maher <mike@redhat.com>
- updated package
- checked package looks ok

* Sun Dec  7 1997 Otto Hammersmith <otto@redhat.com>
- added WorkDir to mrtg.cfg

* Tue Nov 25 1997 Otto Hammersmith <otto@redhat.com>
- addeed patch to clean up paths to perl in the contrib directory.  ugh

* Mon Nov 17 1997 Otto Hammersmith <otto@redhat.com>
- updated version to 2.5.1
- change buildroot to /var/tmp from /tmp

* Mon Apr 28 1997 Michael Fulbright <msf@redhat.com>
- Updated to 2.2 and changed to build with a Buildroot.
