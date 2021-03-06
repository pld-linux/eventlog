Summary:	EventLog library - a replacement of the simple syslog() API
Summary(pl.UTF-8):	Biblioteka EventLog - zamiennik prostego API syslog()
Name:		eventlog
Version:	0.2.14
Release:	1
License:	BSD-like
Group:		Libraries
#Source0:	https://my.balabit.com/downloads/eventlog/0.2/%{name}_%{version}.tar.gz
Source0:	https://my.balabit.com/downloads/syslog-ng/open-source-edition/3.5.0beta1/source/%{name}_%{version}.tar.gz
# Source0-md5:	c4b0dca3f3d558d41b67d7e6ad663584
URL:		https://github.com/balabit/eventlog
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

%description -l pl.UTF-8
Celem biblioteki EventLog jest zastąpienie prostego API syslog()
dostępnego w systemach uniksowych. Główną różnicą między EventLogiem a
syslogiem jest to, że EventLog próbuje dodać do komunikatów strukturę.

Tam, gdzie w API syslog() był prosty łańcuch bez struktury, mamy
połączenie opisu i par znacznik/wartość.

EvengLog udostępnia interfejs do tworzenia, formatowania i
wyprowadzania rekordu zdarzenia. Dokładny format i metoda wyjściowa
może być dostosowana przez administratora poprzez plik konfiguracyjny.

%package devel
Summary:	Header files for eventlog
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki eventlog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for eventlog.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki eventlog.

%package static
Summary:	Static eventlog library
Summary(pl.UTF-8):	Biblioteka statyczna eventlog
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static eventlog library.

%description static -l pl.UTF-8
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

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libevtlog.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/configuration.txt AUTHORS COPYING CREDITS NEWS PORTS README ChangeLog
%attr(755,root,root) %{_libdir}/libevtlog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevtlog.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/{API,DESIGN}.txt
%attr(755,root,root) %{_libdir}/libevtlog.so
%{_includedir}/eventlog
%{_pkgconfigdir}/eventlog.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libevtlog.a
