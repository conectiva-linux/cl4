Summary: The Webalizer - A web server log file analysis thingie
Summary(pt_BR): Um software para análise de arquivos de log de servidores WWW
Summary(es): The Webalizer - A web server log file analysis thingie
Name:      webalizer
Version:   1.2203
Release:   1cl
URL:       http://www.mrunix.net/webalizer/
Source:    ftp://ftp.mrunix.net/pub/webalizer/pre-release/%{name}-1.22-03-src.tar.bz2
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
BuildRoot: /tmp/%{name}-%{version}-root

%description
The Webalizer is a web server log file analysis program which produces
usage statistics in HTML format for viewing with a browser.  The results
are presented in both columnar and graphical format, which facilitates
interpretation.  Yearly, monthly, daily and hourly usage statistics are
presented, along with the ability to display usage by site, URL, referrer,
user agent (browser) and country (user agent and referrer are only
available if your web server produces combined log format files).

%description -l pt_BR
Um analisador de arquivos de log de servidores WWW

%description -l es
The Webalizer is a web server log file analysis program which produces
usage statistics in HTML format for viewing with a browser.  The results
are presented in both columnar and graphical format, which facilitates
interpretation.  Yearly, monthly, daily and hourly usage statistics are
presented, along with the ability to display usage by site, URL, referrer,
user agent (browser) and country (user agent and referrer are only
available if your web server produces combined log format files).

%prep
%setup -q %{name}-%{version} -n  webalizer-1.22-03

%build
make CFLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/man/man1
install -m644 sample.conf $RPM_BUILD_ROOT/etc/webalizer.conf
install -m755 webalizer $RPM_BUILD_ROOT/usr/bin
strip $RPM_BUILD_ROOT/usr/bin/webalizer
install -m644 webalizer.1 $RPM_BUILD_ROOT/usr/man/man1/webalizer.1

#install -d $RPM_BUILD_ROOT/home/httpd/html/usage
#install -m644 msfree.gif $RPM_BUILD_ROOT/home/httpd/html/usage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README country-codes.txt
%config /etc/webalizer.conf
/usr/bin/webalizer
/usr/man/man1/webalizer.1
#/home/httpd/html/usage

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 16 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- new package
