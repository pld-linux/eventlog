Summary:	EventLog library - a replacement of the simple syslog() API
Name:		eventlog
Version:	0.2.4
Release:	0.1
License:	BSD-like
Group:		Libraries
Source0:	http://www.balabit.com/downloads/syslog-ng/1.9/src/%{name}-%{version}.tar.gz
# Source0-md5:	d4f6137da17212c69d6ab9cd35926a0a
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

%package devel
Summary:	Header files for eventlog
Summary(pl):	Pliki nag³ówkowe do eventlog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for eventlog.

%description devel -l pl
Pliki nag³ówkowe do eventlog.

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

#%post
#aaa

#%postun
#aaa

%files
%defattr(644,root,root,755)
%doc doc/configuration.txt AUTHORS COPYING CREDITS NEWS PORTS README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/{API,DESIGN}.txt
%{_pkgconfigdir}/*
%dir %{_includedir}/eventlog
%{_includedir}/eventlog/*
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
