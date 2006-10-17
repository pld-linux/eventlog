Summary:	EventLog library - a replacement of the simple syslog() API
Summary(pl):	Biblioteka EventLog - zamiennik prostego API syslog()
Name:		eventlog
Version:	0.2.5
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.balabit.com/downloads/syslog-ng/2.0/src/%{name}-%{version}.tar.gz
# Source0-md5:	a6bdba91f88540cc69b398fd138d86cd
URL:		http://www.balabit.com/products/syslog_ng/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The EventLog library aims to be a replacement of the simple syslog()
API provided on UNIX systems. The major difference between EventLog
and syslog is that EventLog tries to add structure to messages.

Where you had a simple non-structrured string in syslog() you have a
combination of description and tag/value pairs.

EventLog provides an interface to build, format and output an event
record. The exact format and output method can be customized by the
administrator via a configuration file.

%description -l pl
Celem biblioteki EventLog jest zast±pienie prostego API syslog()
dostêpnego w systemach uniksowych. G³ówn± ró¿nic± miêdzy EventLogiem a
syslogiem jest to, ¿e EventLog próbuje dodaæ do komunikatów strukturê.

Tam, gdzie w API syslog() by³ prosty ³añcuch bez struktury, mamy
po³±czenie opisu i par znacznik/warto¶æ.

EvengLog udostêpnia interfejs do tworzenia, formatowania i
wyprowadzania rekordu zdarzenia. Dok³adny format i metoda wyj¶ciowa
mo¿e byæ dostosowana przez administratora poprzez plik konfiguracyjny.

%package devel
Summary:	Header files for eventlog
Summary(pl):	Pliki nag³ówkowe biblioteki eventlog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for eventlog.

%description devel -l pl
Pliki nag³ówkowe biblioteki eventlog.

%package static
Summary:	Static eventlog library
Summary(pl):	Biblioteka statyczna eventlog
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static eventlog library.

%description static -l pl
Biblioteka statyczna eventlog.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/configuration.txt AUTHORS COPYING CREDITS NEWS PORTS README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/{API,DESIGN}.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/eventlog
%{_includedir}/eventlog/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
