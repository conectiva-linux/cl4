Summary: Benchmark to test TCP and UDP performance
Summary(pt_BR): Teste de performance TCP e UDP
Summary(es): Prueba de desempeño para TCP y UDP
Name: ttcp
Version: 1.4
Release: 3cl
Source: ftp://ftp.cdrom.com/pub/unix-c/benchmarks/ttcp.shar
Copyright: distributable
Group: Applications/Benchmarks
Group(pt_BR): Aplicações/Teste de Performance
Group(es): Aplicaciones/Teste de Performance

%description
Ttcp is a benchmark that times the transmission and reception of data
between two systems using the UDP or TCP protocols. 

%description -l pt_BR
Teste de performance TCP e UDP

%description -l es
Prueba de desempeño para TCP y UDP

%prep
cd $RPM_BUILD_DIR
rm -rf ttcp
mkdir ttcp
cd ttcp
unshar $RPM_SOURCE_DIR/ttcp.shar

%build
cd ttcp
gcc -O2 -o ttcp ttcp.c

%install
cd ttcp
install -o root -g root -s -m 0744 ttcp /usr/bin/ttcp
install -o root -g root -m 0644 ttcp.1m /usr/man/man1/ttcp.1

%files
/usr/bin/ttcp
/usr/man/man1/ttcp.1
